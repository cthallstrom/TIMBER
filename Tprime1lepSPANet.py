from TIMBER.Analyzer import *
from TIMBER.Tools.Common import *

import ROOT
from ROOT import TFile, TRandom3
import sys, os
import gc
from rates import to_cpp_vec2d, pnet_loose, upart_med

gc.disable()

from TIMBER.Tools.RestFramesHandler import load_restframes
import correctionlib
correctionlib.register_pyroot_binding()

sys.path.append('../../')
sys.path.append('../../../')

# ------------------ Command Line Arguments and Parsing -------------------
inputFiles = sys.argv[1] #fileList
testNum1 = sys.argv[2]   #first file in the list to use 
testNum2 = sys.argv[3]   #last file in the list to use
year = sys.argv[4]       #2022, 2022EE, 2023, 2023BPix, 2024, 2025

# Make the New .txt file from line testNum1 to testNum2 because TIMBER can handle .txt of .root's files   
print(f"Input File Path: {inputFiles}")
with open(inputFiles) as fp:
  lines = fp.readlines()

start = int(testNum1)
end = int(testNum2)

print(f"TestNum 1: {start} and TestNum 2: {end}")

#print("Adding files to trimmed_input.txt")
#file_name = 'trimmed_input_'+inputFiles.replace('.txt','')+'_'+str(testNum1)+'.txt'
#listFiles = open(file_name, 'w')
  #if (listFiles.is_open())

filelist = []
for i, line in enumerate(lines): #, start=1):
  if i in range(start, end+1):
    #listFiles.write(line)    
    #print(line)
    filelist.append(line.strip())
#listFiles.close()

print("Number of Entries:",len(filelist))
print("list contents:",filelist)
#sampleName = lines[start]
sampleName = filelist[0]
print(f"Sample Name: {sampleName}")

# Parse the incoming file names to assign labels  
isSig = ("prime" in sampleName)
isTpTp = ("Tprime" in sampleName)
isMadgraphBkg = (("QCD" in sampleName) or ("madgraphMLM" in sampleName))
isTOP = (("Mtt" in sampleName) or ("ST" in sampleName) or ("ttZ" in sampleName) or ("ttW" in sampleName) or ("ttH" in sampleName) or ("TTTo" in sampleName))
isTT = (("TT_Tune" in sampleName) or ("Mtt" in sampleName) or ("TTTo" in sampleName))
isVV = (("WW_" in sampleName) or ("WZ_" in sampleName) or ("ZZ_" in sampleName))
isSM = ("Muon" in sampleName)
isSE = (("SingleElectron" in sampleName) or ("EGamma" in sampleName))
isMC = not (("Single" in sampleName) or ("Muon" in sampleName) or ("EGamma" in sampleName))
#NOTE: BB has lines below:
#dataset = int(-1)
#if "MuonEG" in sampleName: dataset = 2
#elif ("Muon" in sampleName) or ("Muon0" in sampleName) or ("Muon1" in sampleName): dataset = 1
#elif ("EGamma" in sampleName) or ("EGamma0" in sampleName) or ("EGamma1" in sampleName): dataset = 3
#elif "Tau/" in sampleName: dataset = 4

#'root://cms-xrd-global.cern.ch//store/data/Run2018A/SingleMuon/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v2/2550000/28FF17A8-95EB-FD41-A55B-2EFAF2D6AF91.root' 
tokens = sampleName.split("/")
sample = tokens[7] # was 5
era = ''
ver = ''
if not isMC:
  runera = tokens[6] # was 4
  process = tokens[9] # was 7
  era = runera[-1] # last char
  print(process)
  ver = process[process.find('_')+1:process.find('_')+3] 
  #ver = process[process.find('_'):process.find('_')+2]
del tokens

jecera = ''
if not isMC:
  jecera = era
  if year == '2022':
    jecera = 'CD'
  elif year == '2023':
    if(ver != 'v4'):
      jecera = 'Cv123'
    else:
      jecera = 'Cv4'
     
if isMC:
  if (("_ext1" in sampleName)): era = "ext1"
  if (("_ext2" in sampleName)): era = "ext2"
  if (("_ext3" in sampleName)): era = "ext3"

region = "Signal"
if isTT:
  region = "TTbar" # TPrimeTPrime or BPrimeBPrime
elif not isSig:
  region = "DataBkg"

print('============== RUN SETTINGS ===============')
print('isMC = ',isMC)
print('isSig = ',isSig)
print('sample = ',sample)
print('era = ',era)
print('jecera = ',jecera)
print('ver = ',ver)
print('region = ',region)
  
# ------------------ TIMBER Analyzer inputs ------------------

num_threads = 1

# Import the C++
CompileCpp('TIMBER/Framework/include/common.h') # Compile (via gInterpreter) commonly used c++ code
CompileCpp('TIMBER/Framework/Tprime1lep/cleanjet.cc') # Compile Our vlq c++ code
CompileCpp('TIMBER/Framework/Tprime1lep/utilities.cc') # Compile Our vlq c++ code
CompileCpp('TIMBER/Framework/Tprime1lep/lumiMask.cc')
CompileCpp('TIMBER/Framework/Tprime1lep/selfDerived_corrs.cc')
CompileCpp('TIMBER/Framework/Tprime1lep/corr_funcs.cc')
CompileCpp('TIMBER/Framework/Tprime1lep/topographInput.cc') 
CompileCpp('TIMBER/Framework/Tprime1lep/manualreco.cc') 
CompileCpp('TIMBER/Framework/Tprime1lep/StandardTT_fatjet_matching.cc')
CompileCpp('TIMBER/Framework/Tprime1lep/StandardTTBB_decayModeFinder.cc')
CompileCpp('TIMBER/Framework/Tprime1lep/eventReco.cc')
CompileCpp('TIMBER/Framework/Tprime1lep/truthComparing.cc')
CompileCpp('TIMBER/Framework/Tprime1lep/SPANet_functions.cc')
ROOT.gInterpreter.ProcessLine('#include "TString.h"')

# Enable using 4 threads
ROOT.ROOT.EnableImplicitMT(num_threads)

# handler_name1 = 'Tprime_handler_W.cc'
# handler_name2 = 'Tprime_handler_t.cc'
# class_name1 = 'Tprime_RestFrames_Container_W'
# class_name2 = 'Tprime_RestFrames_Container_t'

# Enable using 4 threads
ROOT.ROOT.EnableImplicitMT(num_threads)

# load rest frames handlers
# load_restframes(num_threads, handler_name1, class_name1, 'W_rfc')
# load_restframes(num_threads, handler_name2, class_name2, 't_rfc')

#CompileCpp('bin/restframes/helper.cc')

# load rest frames handler NEED TO UPDATE FOR CURRENT
#handler_name = 'Tprime_handler_W.cc'
#class_name = 'Tprime_RestFrames_Container_W'
#load_restframes(num_threads, handler_name, class_name, 'rfc')

# ------------------ Important Variables ------------------
debug = False

ROOT.gInterpreter.Declare("""
  string year = \"""" + year + """\"; 
  string sample = \"""" + sample + """\";
  string jecera = \"""" + jecera + """\";
  string region = \"""" + region + """\";
  string ver = \"""" + ver + """\";

  bool isMC = """+str(isMC).lower()+"""; 
  bool debug = """+str(debug).lower()+""";
  bool isSig = """+str(isSig).lower()+""";
""")

def analyze(jesvar):
  ROOT.gInterpreter.ProcessLine('string jesvar = "' + jesvar + '"; ')

  # Create analyzer instance
  a = analyzer(filelist)
  
  print('==========================INITIALIZED ANALYZER========================')
  
  # ------------------ Golden JSON Data ------------------
  # change the jsonfile path to somewhere they have it in TIMBER
  jsonfile = "./TIMBER/data/LumiJSON/"
  if '2022' in year:
    jsonfile = jsonfile + "Cert_Collisions2022_355100_362760_Golden.json"
  elif '2023' in year:
    jsonfile = jsonfile + "Cert_Collisions2023_366442_370790_Golden.json"
  elif '2024' in year:
      jsonfile = jsonfile + "Cert_Collisions2024_378981_386951_Golden.json"
  elif '2025' in year:
      jsonfile = jsonfile + "Cert_Collisions2025_391658_398903_Golden.json"
  else:
    print(f'ERROR: Can\'t parse the year to assign a golden json file. Expected 2022(EE) or 2023(BPix). Got: {year}\n')
    
  ROOT.gInterpreter.Declare("""
    const auto myLumiMask = lumiMask::fromJSON(\"""" + jsonfile + """\");
  """)

  print('========= loaded lumimask ============')
  
  # ------------------ Self-derived corrections ------------------

  #TODO when we determine what Run 3 scale factors need to be computed by us, load them up here

  ROOT.gInterpreter.ProcessLine('initialize(year);')


  # ------------------ correctionsLib corrections ------------------

  BTagM = {'2022':0.245,'2022EE':0.2605,'2023':0.1917,'2023BPix':0.1919, '2024':0.1272, '2025':0.1272} #PNet for 22-23BPix, UParT for 2024-2025 should seperate in the future
  yrstr = {'2022':"Run3-22CDSep23-Summer22-NanoAODv12",'2022EE':"Run3-22EFGSep23-Summer22EE-NanoAODv12",'2023':"Run3-23CSep23-Summer23-NanoAODv12",'2023BPix':"Run3-23DSep23-Summer23BPix-NanoAODv12",'2024':"Run3-24CDEReprocessingFGHIPrompt-Summer24-NanoAODv15",'2025':"Run3-25Prompt-Summer24-NanoAODv15"}
  jmetags = {'2022':'2026-06-05','2022EE':'2026-06-05','2023':'2026-06-05','2023BPix':'2026-06-05','2024':'2026-06-05','2025':'2026-06-05'} 
  btvtags = {'2022':'2025-08-20','2022EE':'2025-08-20','2023':'2025-08-20','2023BPix':'2025-08-20','2024':'2026-03-10','2025':'2026-05-27'}
  egmtags = {'2022':'2025-12-15','2022EE':'2025-12-15','2023':'2025-12-15','2023BPix':'2025-12-15','2024':'2025-12-15','2025':'2026-05-06'}
  muotags = {'2022':'2026-04-28','2022EE':'2026-04-28','2023':'2026-04-28','2023BPix':'2026-04-28','2024':'2026-04-28','2025':'2026-04-28'}
  lumtags = {'2022':'2024-01-31','2022EE':'2024-01-31','2023':'2024-01-31','2023BPix':'2024-01-31','2024':'2026-04-15','2025':'latest'}      

  jmeyrstr = {'2022':yrstr['2022'],'2022EE':yrstr['2022EE'],'2023':yrstr['2023'],'2023BPix':yrstr['2023BPix'],'2024':yrstr['2024'],'2025':yrstr['2024']} # yes, really use 24 for 25
  jecyr = {'2022':"Summer22_22Sep2023",'2022EE':"Summer22EE_22Sep2023",'2023':"Summer23Prompt23",'2023BPix':"Summer23BPixPrompt23",'2024':"Summer24Prompt24", '2025':"Summer24Prompt24"}
  jeryr = {'2022':"Summer22_22Sep2023_JRV2",'2022EE':"Summer22EE_22Sep2023_JRV2",'2023':"Summer23Prompt23_RunCv1234_JRV2",'2023BPix':"Summer23BPixPrompt23_RunD_JRV2",'2024':"Summer24Prompt24_JRV1",'2025':"Summer24Prompt24_JRV1"}
  jetvetoname = {'2022':"Summer22_23Sep2023_RunCD_V1",'2022EE':"Summer22EE_23Sep2023_RunEFG_V1",'2023':"Summer23Prompt23_RunC_V1",'2023BPix':"Summer23BPixPrompt23_RunD_V1",'2024':"Summer24Prompt24_RunBCDEFGHI_V1",'2025':"Summer24Prompt24_RunBCDEFGHI_V1"}      
  if not isMC: #is DATA
    jmeyrstr['2025'] = 'Run3-25Prompt-Winter25-NanoAODv15'
    jecyr['2025'] = "Winter25Prompt25"
    jeryr['2025'] = "Summer24Prompt25_JRV1"
    jetvetoname['2025'] = "Winter25Prompt25_RunCDEFG_V1" 

  jecver = {'2022':"V4",'2022EE':"V4",'2023':"V4",'2023BPix':"V4",'2024':"V3",'2025':"V3"}   
  puname = {'2022':"Collisions2022_355100_357900_eraBCD_GoldenJson",'2022EE':"Collisions2022_359022_362760_eraEFG_GoldenJson",'2023':"Collisions2023_366403_369802_eraBC_GoldenJson",'2023BPix':"Collisions2023_369803_370790_eraD_GoldenJson",'2024':"Collisions24_BCDEFGHI_goldenJSON",'2025':"Collisions25_goldenJSON"}  
  puweights = {'2022':"puWeights",'2022EE':'puWeights','2023':'puWeights','2023BPix':'puWeights','2024':"puWeights_BCDEFGHI",'2025':"puWeights_2025pp_Golden_Summer24_25ns_69200ub"}  
  elecyr = {'2022':"2022Re-recoBCD",'2022EE':"2022Re-recoE+PromptFG",'2023':"2023PromptC",'2023BPix':"2023PromptD",'2024':"2024Prompt",'2025':"2025Prompt"}
  muonisoname = {'2022':'NUM_TightPFIso_DEN_MediumID','2022EE':'NUM_TightPFIso_DEN_MediumID','2023':'NUM_TightPFIso_DEN_MediumID','2023BPix':'NUM_TightPFIso_DEN_MediumID','2024':'NUM_TightMiniIso_DEN_MediumID','2025':'NUM_TightMiniIso_DEN_MediumID'} # CHECKME WHICH EXIST IN 22 AND 23??????
  METyr = {'2022':"2022",'2022EE':"2022EE",'2023':"2023",'2023BPix':"2023BPix",'2024':"2024",'2025':"2025"}                            
  METsimpleyr = {'2022':"2022",'2022EE':"2022",'2023':"2023",'2023BPix':"2023",'2024':"2024",'2025':"2025"} 
  btagname = {'2022':"particleNet_comb",'2022EE':"particleNet_comb",'2023':"deepJet_comb",'2023BPix':"deepJet_comb",'2024':"UParTAK4_comb",'2025':"UParTAK4_comb"}
  lightwps = {'2022':"particleNet_light", '2022EE':"particleNet_light",'2023':"particleNet_light",'2023BPix':"particleNet_light",'2024':"UParTAK4_light",'2025':"UParTAK4_light"}

  if year == '2024' or year == '2025':
    btageffsdict = upart_med
  else:
    btageffsdict = pnet_loose # this is wrong, but not for long
  
  year_hack='2023'
  ROOT.gInterpreter.Declare("""
  float BTagM = """+str(BTagM[year])+""";
  string yrstr = \""""+yrstr[year]+"""\";
  string jmeyrstr = \""""+jmeyrstr[year]+"""\";
  string jecyr = \""""+jecyr[year]+"""\";
  string jecver = \""""+jecver[year]+"""\";
  string jmetag = \""""+jmetags[year]+"""\";
  string btvtag = \""""+btvtags[year]+"""\";
  string egmtag = \""""+egmtags[year]+"""\";
  string muotag = \""""+muotags[year]+"""\";
  string muonisoname = \""""+muonisoname[year]+"""\";
  string lumtag = \""""+lumtags[year]+"""\"; 
  string puname = \""""+puname[year]+"""\";
  string puweight = \""""+puweights[year]+"""\";
  string jetvetoname = \""""+jetvetoname[year]+"""\";
  string elecyr = \""""+elecyr[year]+"""\";
  string METyr = \""""+METyr[year]+"""\";
  string METsimpleyr = \""""+METsimpleyr[year]+"""\";
  string btagname = \""""+btagname[year]+"""\";
  string lightwp = \""""+lightwps[year]+"""\";
  
  std::vector<int> btagptbins = {15,20,30,50,70,100,150,200,300,400,500,600,800,1000,1200,1500};
  std::vector<std::vector<float>> btageffs = """ + to_cpp_vec2d(btageffsdict[year]) + """;
  """)
  

  ROOT.gInterpreter.Declare("""
  auto pileupcorrset = correction::CorrectionSet::from_file("/cvmfs/cms-griddata.cern.ch/cat/metadata/LUM/"+yrstr+"/"+lumtag+"/"+puweight+".json.gz");
  auto btagcorrset = correction::CorrectionSet::from_file("/cvmfs/cms-griddata.cern.ch/cat/metadata/BTV/"+yrstr+"/"+btvtag+"/btagging.json.gz");
  auto electroncorrset = correction::CorrectionSet::from_file("/cvmfs/cms-griddata.cern.ch/cat/metadata/EGM/"+yrstr+"/"+egmtag+"/electron.json.gz");
  auto muoncorrset = correction::CorrectionSet::from_file("/cvmfs/cms-griddata.cern.ch/cat/metadata/MUO/"+yrstr+"/"+muotag+"/muon_Z.json.gz");
  auto jetvetocorrset = correction::CorrectionSet::from_file("/cvmfs/cms-griddata.cern.ch/cat/metadata/JME/"+jmeyrstr+"/"+jmetag+"/jetvetomaps.json.gz");
  auto path = (jmeyrstr == "Run3-25Prompt-Winter25-NanoAODv15") 
            ? "/cvmfs/cms-griddata.cern.ch/cat/metadata/JME/Run3-24CDEReprocessingFGHIPrompt-Summer24-NanoAODv15/2026-06-05/jetid.json.gz"
            : "/cvmfs/cms-griddata.cern.ch/cat/metadata/JME/" + jmeyrstr + "/" + jmetag + "/jetid.json.gz";
  auto jetidcorrset = correction::CorrectionSet::from_file(path);

  auto pileupcorr = pileupcorrset->at(puname);
  auto jetidAK4Tcorr = jetidcorrset->at("AK4PUPPI_Tight");
  auto jetidAK4TLcorr = jetidcorrset->at("AK4PUPPI_TightLeptonVeto");
  auto jetidAK8Tcorr = jetidcorrset->at("AK8PUPPI_Tight");
  auto jetidAK8TLcorr = jetidcorrset->at("AK8PUPPI_TightLeptonVeto");
  auto btagwpbccorr = btagcorrset->at(btagname);
  auto btagwplcorr = btagcorrset->at(lightwp);
  auto jetvetocorr = jetvetocorrset->at(jetvetoname);
  auto electroncorr = electroncorrset->at("Electron-ID-SF");
  auto muonidcorr = muoncorrset->at("NUM_MediumID_DEN_TrackerMuons");
  auto muonisocorr = muoncorrset->at(muonisoname);
  """)

  if year != '2024' and year != '2025':
    ROOT.gInterpreter.Declare("""
    auto METcorrset = correction::CorrectionSet::from_file("/cvmfs/cms-griddata.cern.ch/cat/metadata/JME/"+yrstr+"/"+jmetag+"/met_xyCorrections_"+METsimpleyr+"_"+METyr+".json.gz");
    auto METcorr = METcorrset->at("met_xy_corrections");
    """)

  if not isMC:
    ROOT.gInterpreter.Declare("""
    auto ak4corrset = correction::CorrectionSet::from_file("/cvmfs/cms-griddata.cern.ch/cat/metadata/JME/"+jmeyrstr+"/"+jmetag+"/jet_jerc.json.gz"); 
    auto ak8corrset = correction::CorrectionSet::from_file("/cvmfs/cms-griddata.cern.ch/cat/metadata/JME/"+jmeyrstr+"/"+jmetag+"/fatJet_jerc.json.gz"); 
    auto ak4corr = ak4corrset->compound().at(jecyr+"_"+jecver+"_DATA_L1L2L3Res_AK4PFPuppi");
    auto ak4corrL1 = ak4corrset->at(jecyr+"_"+jecver+"_DATA_L1FastJet_AK4PFPuppi");
    auto ak8corr = ak8corrset->compound().at(jecyr+"_"+jecver+"_DATA_L1L2L3Res_AK8PFPuppi");
    """)
  else:
    print(f"{jecyr[year]}_{jecver[year]}_MC_L1L2L3Res_AK4PFPuppi")
    print(f"{jecyr[year]}_{jecver[year]}_MC_L1FastJet_AK4PFPuppi")          
    print(f"{jecyr[year]}_{jecver[year]}_MC_Total_AK4PFPuppi")        
    print(f"{jeryr[year]}_MC_PtResolution_AK4PFPuppi")                
    print(f"{jeryr[year]}_MC_ScaleFactor_AK4PFPuppi")                      
    print(f"{jecyr[year]}_{jecver[year]}_MC_L1L2L3Res_AK8PFPuppi")     
    print(f"{jecyr[year]}_{jecver[year]}_MC_Total_AK8PFPuppi")             

    ROOT.gInterpreter.Declare("""
    string jeryr = \""""+jeryr[year]+"""\";
    auto ak4corrset = correction::CorrectionSet::from_file("/cvmfs/cms-griddata.cern.ch/cat/metadata/JME/"+jmeyrstr+"/"+jmetag+"/jet_jerc.json.gz"); 
    auto ak8corrset = correction::CorrectionSet::from_file("/cvmfs/cms-griddata.cern.ch/cat/metadata/JME/"+jmeyrstr+"/"+jmetag+"/fatJet_jerc.json.gz"); 

    auto ak4corr = ak4corrset->compound().at(jecyr+"_"+jecver+"_MC_L1L2L3Res_AK4PFPuppi");
    auto ak4corrL1 = ak4corrset->at(jecyr+"_"+jecver+"_MC_L1FastJet_AK4PFPuppi");
    auto ak4corrUnc = ak4corrset->at(jecyr+"_"+jecver+"_MC_Total_AK4PFPuppi");
    auto ak4ptres = ak4corrset->at(jeryr+"_MC_PtResolution_AK4PFPuppi");
    auto ak4jer = ak4corrset->at(jeryr+"_MC_ScaleFactor_AK4PFPuppi");
    auto ak8corr = ak8corrset->compound().at(jecyr+"_"+jecver+"_MC_L1L2L3Res_AK8PFPuppi");
    auto ak8corrUnc = ak8corrset->at(jecyr+"_"+jecver+"_MC_Total_AK8PFPuppi");
    """) 

    
    
  # ------------------ Flag Cuts ------------------
  flagCuts = CutGroup('FlagCuts')
  flagCuts.Add('Bad Event Filters', 'Flag_EcalDeadCellTriggerPrimitiveFilter == 1 && Flag_goodVertices == 1 && Flag_eeBadScFilter == 1 && Flag_globalSuperTightHalo2016Filter == 1 && Flag_BadPFMuonFilter == 1 && Flag_BadPFMuonDzFilter == 1')
  flagCuts.Add('Event has jets', 'nJet > 0 && nFatJet > 0') # need jets 
  
  # ------------------ Golden JSON (Data) || GEN Info (MC) ------------------
  gjsonVars = VarGroup('GoldenJsonVars')
  gjsonCuts = CutGroup('GoldenJsonCuts')
  if not isMC: # apply golden json to data
    gjsonVars.Add("passesJSON", "goldenjson(myLumiMask, run, luminosityBlock)") # function name, parameters are branches in the file or defined objects
    gjsonCuts.Add("Data passes Golden JSON", "passesJSON == 1") 
  else:
    gjsonVars.Add("PileupWeights", "pufunc(pileupcorr, Pileup_nTrueInt)")
    
  #---------------------- Random MC splitting ----------------------
  # if isMC:
  #   RandVars = VarGroup('Random number gen')
  #   RandVars.Add("seed","int(Jet_phi[0]*100000)")
  #   RandVars.Add("uniform","TRandom3 rand(seed); return rand.Uniform(0.0,290.0)")
  #   RandVars.Add('randyear','uniform < 7.99 ? string("2022") : (uniform < 34.67 ? string("2022EE") : (uniform < 52.63 ? string("2023") : (uniform < 62.31 ? string("2023BPix") : (uniform < 172.13 ? string("2024") : string("2025")))))')
  #   Random = CutGroup('Dataset splitting')
  #   Random.Add("Random split","randyear == year")

  # ------------------ LEPTON Definitions ------------------
  lVars = VarGroup('LeptonVars')
  
  lVars.Add("Electron_passIP", "elIP(Electron_dz, Electron_dxy, Electron_eta)")
  lVars.Add("TPassMu", "abs(Muon_eta)<2.4 && Muon_mediumId==1 && Muon_miniIsoId>=3 && abs(Muon_dz) < 0.5 && Muon_dxy < 0.2")
  lVars.Add("TPassEl", "(abs(Electron_eta)<1.442 || (abs(Electron_eta)>1.566 && abs(Electron_eta)<2.5)) && Electron_mvaNoIso_WP80 == 1 && Electron_miniPFRelIso_all<0.1 && Electron_passIP == 1")
  lVars.Add("VetoMu", "TPassMu && (Muon_pt>25)")
  lVars.Add("VetoEl", "TPassEl && (Electron_pt>25)")
  lVars.Add("SignalIsoMu", "TPassMu && (Muon_pt>=55)")
  lVars.Add("SignalIsoEl", "TPassEl && (Electron_pt>=55)")
  lVars.Add("nVetoLep", "(int) (Sum(VetoMu)+Sum(VetoEl))")
  lVars.Add("SMuon_pt", "Muon_pt[SignalIsoMu == true]")
  lVars.Add("SMuon_eta", "Muon_eta[SignalIsoMu == true]")
  lVars.Add("SMuon_phi", "Muon_phi[SignalIsoMu == true]")
  lVars.Add("SMuon_mass", "Muon_mass[SignalIsoMu == true]")
  lVars.Add("SElectron_pt", "Electron_pt[SignalIsoEl == true]")
  lVars.Add("SElectron_eta", "Electron_eta[SignalIsoEl == true]")
  lVars.Add("SElectron_phi", "Electron_phi[SignalIsoEl == true]")
  lVars.Add("SElectron_mass", "Electron_mass[SignalIsoEl == true]")
  lVars.Add("Muon_P4", "fVectorConstructor(Muon_pt,Muon_eta,Muon_phi,Muon_mass)")
  lVars.Add("SMuon_P4", "fVectorConstructor(SMuon_pt,SMuon_eta,SMuon_phi,SMuon_mass)")
  lVars.Add("SElectron_P4", "fVectorConstructor(SElectron_pt,SElectron_eta,SElectron_phi,SElectron_mass)")
  lVars.Add("SMuon_jetIdx", "Muon_jetIdx[SignalIsoMu == true]")
  lVars.Add("SElectron_jetIdx", "Electron_jetIdx[SignalIsoEl]")
  lVars.Add("nSignalIsoMu", "(int) Sum(SignalIsoMu)")
  lVars.Add("nSignalIsoEl", "(int) Sum(SignalIsoEl)")
  lVars.Add("VetoIsoMu", "(VetoMu == true && Muon_pt < 55)")
  lVars.Add("VetoIsoEl", "(VetoEl == true && Electron_pt < 55)")
  lVars.Add("nVetoIsoLep", "(int) (Sum(VetoIsoMu)+Sum(VetoIsoEl))")

  # ------------------ LEPTON SELECTION ------------------

  lVars.Add("isMu", "(nMuon>0) && (HLT_Mu50 || HLT_HighPtTkMu100 || HLT_Mu15_IsoVVVL_PFHT450) && (nSignalIsoMu==1) && (nVetoIsoLep==0) && (nElectron == 0 || nSignalIsoEl == 0)")
  lVars.Add("isEl", "(nElectron>0) && (HLT_Ele15_IsoVVVL_PFHT450 || HLT_Ele115_CaloIdVT_GsfTrkIdT || HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165 || HLT_Photon200) && (nSignalIsoEl==1) && (nVetoIsoLep==0) && (nMuon == 0 || nSignalIsoMu == 0)")

  lCuts = CutGroup('LeptonCuts')
  lCuts.Add("Event is either muon or electron", "isMu || isEl")
  lVars.Add("assignleps", "assign_leps(isMu,isEl,SignalIsoMu,SignalIsoEl,Muon_pt,Muon_eta,Muon_phi,Muon_mass,Muon_miniPFRelIso_all,Electron_pt,Electron_eta,Electron_phi,Electron_mass,Electron_miniPFRelIso_all)")
  lVars.Add("lepton_pt","assignleps[0]")
  lVars.Add("lepton_eta","assignleps[1]") 
  lVars.Add("lepton_phi","assignleps[2]")
  lVars.Add("lepton_sin_phi", "sin(lepton_phi)")
  lVars.Add("lepton_cos_phi", "cos(lepton_phi)")
  lVars.Add("lepton_mass","assignleps[3]")
  lVars.Add("lepton_miniIso","assignleps[4]")
  lVars.Add("lepton_ID","isMu ? 13 : 11")
  lVars.Add("lepton_btag", "0")

  # ------------------ JET Cleaning and JERC ------------------
  jVars = VarGroup('JetCleaningVars')
  
  jVars.Add("Jet_P4", "fVectorConstructor(Jet_pt,Jet_eta,Jet_phi,Jet_mass)")
  jVars.Add("FatJet_P4", "fVectorConstructor(FatJet_pt,FatJet_eta,FatJet_phi,FatJet_mass)")
  jVars.Add("Jet_EmEF","Jet_neEmEF + Jet_chEmEF")
  jVars.Add("DummyZero","float(0.0)")
  jVars.Add("Jet_jetId","jetidfunc(jetidAK4Tcorr,jetidAK4TLcorr,Jet_eta,Jet_chHEF,Jet_neHEF,Jet_chEmEF,Jet_neEmEF,Jet_muEF,Jet_chMultiplicity,Jet_neMultiplicity)")
  jVars.Add("FatJet_jetId","fatjetidfunc(jetidAK8Tcorr,jetidAK8TLcorr,FatJet_eta,FatJet_chHEF,FatJet_neHEF,FatJet_chEmEF,FatJet_neEmEF,FatJet_muEF,FatJet_chMultiplicity,FatJet_neMultiplicity)")
  
  if isMC:          #TODO fix dummy comments
    jVars.Add("GenJet_P4","fVectorConstructor(GenJet_pt,GenJet_eta,GenJet_phi,GenJet_mass)")
    jVars.Add("cleanedJets", "cleanJetsMC(debug,year,jesvar,ak4corr,ak4corrL1,ak4corrUnc,ak4ptres,ak4jer,ak8corr,ak8corrUnc,Jet_P4,Jet_rawFactor,Jet_muonSubtrFactor,Jet_area,Jet_EmEF,Jet_jetId,GenJet_P4,Jet_genJetIdx,SMuon_P4,SMuon_jetIdx,SElectron_P4,SElectron_jetIdx,Rho_fixedGridRhoFastjetAll,DummyZero,DummyZero)") # muon and EM factors unused in this call
    jVars.Add("cleanMets", "cleanJetsMC(debug,year,jesvar,ak4corr,ak4corrL1,ak4corrUnc,ak4ptres,ak4jer,ak8corr,ak8corrUnc,Jet_P4,Jet_rawFactor,Jet_muonSubtrFactor,Jet_area,Jet_EmEF,GenJet_P4,Jet_genJetIdx,SMuon_P4,SMuon_jetIdx,SElectron_P4,SElectron_jetIdx,Rho_fixedGridRhoFastjetAll,RawPuppiMET_pt,RawPuppiMET_phi)") # lepton args are unused in this call
    jVars.Add("GenJetAK8_P4", "fVectorConstructor(GenJetAK8_pt,GenJetAK8_eta,GenJetAK8_phi,GenJetAK8_mass)")
    jVars.Add("cleanFatJets", "cleanJetsMC(debug,year,jesvar,ak4corr,ak4corrL1,ak4corrUnc,ak4ptres,ak4jer,ak8corr,ak8corrUnc,FatJet_P4,FatJet_rawFactor,FatJet_rawFactor,FatJet_area,FatJet_area,FatJet_jetId,GenJetAK8_P4,FatJet_genJetAK8Idx,SMuon_P4,SMuon_jetIdx,SElectron_P4,SElectron_jetIdx,Rho_fixedGridRhoFastjetAll,DummyZero,DummyZero)")

  else:
    jVars.Add("cleanedJets", "cleanJetsData(run,debug,year,ak4corr,ak4corrL1,ak8corr,Jet_P4,Jet_rawFactor,Jet_muonSubtrFactor,Jet_area,Jet_EmEF,Jet_P4,SMuon_P4,SMuon_jetIdx,SElectron_P4,SElectron_jetIdx,Rho_fixedGridRhoFastjetAll,DummyZero,DummyZero)") # muon and EM factors unused in this call, args 16-17 are dummies
    jVars.Add("cleanMets", "cleanJetsData(run,debug,year,ak4corr,ak4corrL1,ak8corr,Jet_P4,Jet_rawFactor,Jet_muonSubtrFactor,Jet_area,Jet_EmEF,Jet_jetId,Jet_P4,Muon_P4,Muon_jetIdx,SElectron_P4,SElectron_jetIdx,Rho_fixedGridRhoFastjetAll,RawPuppiMET_pt,RawPuppiMET_phi)") # lepton args unused in this call, args 16-17 are dummies
    jVars.Add("cleanFatJets", "cleanJetsData(run,debug,year,ak4corr,ak4corrL1,ak8corr,FatJet_P4,FatJet_rawFactor,FatJet_rawFactor,FatJet_area,FatJet_area,FatJet_jetId,FatJet_P4,SMuon_P4,SMuon_jetIdx,SElectron_P4,SElectron_jetIdx,Rho_fixedGridRhoFastjetAll,DummyZero,DummyZero)") # args 12, 14, 16, 17 are dummies
  
  jVars.Add("cleanJet_pt", "cleanedJets[0]")
  jVars.Add("cleanJet_eta", "cleanedJets[1]")
  jVars.Add("cleanJet_phi", "cleanedJets[2]")
  jVars.Add("cleanJet_mass", "cleanedJets[3]")
  jVars.Add("cleanFatJet_pt", "cleanFatJets[0]")
  jVars.Add("cleanFatJet_eta", "cleanFatJets[1]")
  jVars.Add("cleanFatJet_phi", "cleanFatJets[2]")
  jVars.Add("cleanFatJet_mass", "cleanFatJets[3]")

  # ------------------ MET Selection ------------------
  metVars = VarGroup('METVars')
  metVars.Add("corrMET_pt","cleanMets[4][0]")
  metVars.Add("corrMET_phi","cleanMets[4][1]")
  metVars.Add("corrMET_sin_phi", "sin(corrMET_phi)")
  metVars.Add("corrMET_cos_phi", "cos(corrMET_phi)")
  metVars.Add("corrMET_dPhiLep","DeltaPhi(lepton_phi, corrMET_phi)")

  metCuts = CutGroup('METCuts')
  metCuts.Add("Pass corr MET > 60", "corrMET_pt > 60")

  # ------------------ HT Calculation and N Jets cuts ------------------
  gcjetVars = VarGroup('JetCountVars')
  gcjetVars.Add("DR_lepJets","DeltaR_VecAndFloat(cleanJet_eta,cleanJet_phi,lepton_eta,lepton_phi)")
  gcjetVars.Add("minDR_lepJet","Min(DR_lepJets)")
  gcjetVars.Add("ptrel_lepJets","ptRel(cleanJet_pt,cleanJet_eta,cleanJet_phi,cleanJet_mass,lepton_pt,lepton_eta,lepton_phi,lepton_mass)") 
  gcjetVars.Add("goodcleanJets", "cleanJet_pt > 30 && abs(cleanJet_eta) < 2.4 && (DR_lepJets > 0.4 || ptrel_lepJets > 20 && Jet_jetId > -1)")
  gcjetVars.Add("NJets","(int) Sum(goodcleanJets)")
  gcjetVars.Add("ptrel_lepJet_minDR","Min(ptrel_lepJets)")
  gcjetVars.Add("ptrel_lepJet_minDR_idx","ArgMin(ptrel_lepJets)")
  gcjetVars.Add("gcJet_HT","Sum(cleanJet_pt[goodcleanJets == true])")
  gcjetVars.Add("DR_lepFatJets","DeltaR_VecAndFloat(FatJet_eta,FatJet_phi,lepton_eta,lepton_phi)")
  gcjetVars.Add("ptrel_lepFatJets","ptRel(FatJet_pt,FatJet_eta,FatJet_phi,FatJet_mass,lepton_pt,lepton_eta,lepton_phi,lepton_mass)")
  gcjetVars.Add("ptrel_lepFatJet_minDR","Min(ptrel_lepFatJets)")
  gcjetVars.Add("ptrel_lepFatJet_minDR_idx","ArgMin(ptrel_lepFatJets)")
  gcjetVars.Add("goodcleanFatJets", "FatJet_pt > 200 && abs(FatJet_eta) < 2.4 && (DR_lepFatJets > 0.8 || ptrel_lepFatJets > 20)")
  gcjetVars.Add("NFatJets", "(int) Sum(goodcleanFatJets)")
  gcjetVars.Add("gcJet_ST","gcJet_HT + corrMET_pt + lepton_pt")
  gcjetVars.Add("gcJet_leptag", "0")
  
  jCuts = CutGroup('JetCuts')  
  jCuts.Add('Pass HT > 510', 'gcJet_HT > 510')
  jCuts.Add('3 AK8s Pass', 'NFatJets > 2')      # need to ensure three jets exist

  # ------------------ Jet pt ordering, counting, lepton association ------------------
  jetVars = VarGroup('JetVars')
  jetVars.Add("gcJet_pt_unsort", "cleanJet_pt[goodcleanJets == true]")
  jetVars.Add("gcJet_ptargsort","ROOT::VecOps::Reverse(ROOT::VecOps::Argsort(gcJet_pt_unsort))")
  jetVars.Add("gcJet_pt","reorder(gcJet_pt_unsort,gcJet_ptargsort)")
  jetVars.Add("gcJet_eta", "reorder(cleanJet_eta[goodcleanJets == true],gcJet_ptargsort)")
  jetVars.Add("gcJet_phi", "reorder(cleanJet_phi[goodcleanJets == true],gcJet_ptargsort)")
  jetVars.Add("gcJet_sin_phi", "sin(gcJet_phi)")
  jetVars.Add("gcJet_cos_phi", "cos(gcJet_phi)")
  jetVars.Add("gcJet_mass", "reorder(cleanJet_mass[goodcleanJets == true],gcJet_ptargsort)")
  jetVars.Add("gcJet_vetomap", "jetvetofunc(jetvetocorr, gcJet_eta, gcJet_phi)")
  if year != '2024' and year != '2025':
    jetVars.Add("gcJet_BTag", "reorder(Jet_btagPNetB[goodcleanJets == true],gcJet_ptargsort)")
  else:
    jetVars.Add("gcJet_BTag", "reorder(Jet_btagUParTAK4B[goodcleanJets == true],gcJet_ptargsort)")
  jetVars.Add("gcJet_BTagM", "gcJet_BTag > BTagM") 
  jetVars.Add("NJets_BTagM", "Sum(gcJet_BTagM)")
  jetVars.Add("gcBJet_pt","gcJet_pt[gcJet_BTagM == 1]")
  jetVars.Add("gcBJet_eta","gcJet_eta[gcJet_BTagM == 1]")
  jetVars.Add("gcBJet_phi","gcJet_phi[gcJet_BTagM == 1]")
  jetVars.Add("gcBJet_mass","gcJet_mass[gcJet_BTagM == 1]")

  jetVars.Add("gcBJet_P4","fVectorConstructor(gcBJet_pt,gcBJet_eta,gcBJet_phi,gcBJet_mass)")
  jetVars.Add("gcJet_P4", "fVectorConstructor(gcJet_pt,gcJet_eta,gcJet_phi,gcJet_mass)")

  jetVars.Add("gcFatJet_pt_unsort", "FatJet_pt[goodcleanFatJets == true]")
  jetVars.Add("gcFatJet_ptargsort","ROOT::VecOps::Reverse(ROOT::VecOps::Argsort(gcFatJet_pt_unsort))")
  jetVars.Add("gcFatJet_pt","reorder(gcFatJet_pt_unsort,gcFatJet_ptargsort)")  
  jetVars.Add("gcFatJet_eta", "reorder(FatJet_eta[goodcleanFatJets == true],gcFatJet_ptargsort)")
  jetVars.Add("gcFatJet_phi", "reorder(FatJet_phi[goodcleanFatJets == true],gcFatJet_ptargsort)")
  jetVars.Add("gcFatJet_sin_phi", "sin(gcFatJet_phi)")
  jetVars.Add("gcFatJet_cos_phi", "cos(gcFatJet_phi)")
  jetVars.Add("gcFatJet_mass", "reorder(FatJet_mass[goodcleanFatJets == true],gcFatJet_ptargsort)")
  jetVars.Add("gcFatJet_sdmass", "reorder(FatJet_msoftdrop[goodcleanFatJets == true],gcFatJet_ptargsort)")
  jetVars.Add("gcFatJet_subJetIdx1", "reorder(FatJet_subJetIdx1[goodcleanFatJets == true], gcFatJet_ptargsort)")
  jetVars.Add("gcFatJet_subJetIdx2", "reorder(FatJet_subJetIdx2[goodcleanFatJets == true], gcFatJet_ptargsort)")  
  jetVars.Add("gcFatJet_vetomap", "jetvetofunc(jetvetocorr, gcFatJet_eta, gcFatJet_phi)")
  jetVars.Add("gcFatJet_P4", "fVectorConstructor(gcFatJet_pt,gcFatJet_eta,gcFatJet_phi,gcFatJet_mass)")
  jetVars.Add("gcFatJet_btag", "0")
  jetVars.Add("gcFatJet_leptag", "0")
  jetVars.Add("gcFatJet_subJetBTag", "SubJet_btagUParTAK4B")

  bCuts = CutGroup("BTagCuts")
  bCuts.Add("Has bTags","NJets_BTagM > 0")
  
  if isMC:
    jetVars.Add("gcJet_hflav", "reorder(Jet_hadronFlavour[goodcleanJets == true],gcJet_ptargsort)")
    jetVars.Add("gcFatJet_hadronFlavour", "reorder(FatJet_hadronFlavour[goodcleanFatJets == true], gcFatJet_ptargsort)")
    jetVars.Add("btagWeights",'btagshapefunc("M",year,jesvar,btagwpbccorr,btagwplcorr,btagptbins,btageffs,BTagM,gcJet_pt,gcJet_eta,gcJet_BTag,gcJet_hflav)')
 #### WORK ON THESE! Ethan can compute the efficiencies we need.

  # ------------------ Fatjet tagging and truth ---------------
  tagVars = VarGroup("tagVars")

  tagVars.Add("gcFatJet_PNWM_T", "reorder(((FatJet_particleNetWithMass_TvsQCD * FatJet_particleNetWithMass_QCD) / (1.0 - FatJet_particleNetWithMass_TvsQCD))[goodcleanFatJets == true], gcFatJet_ptargsort)")
  tagVars.Add("gcFatJet_PNWM_W", "reorder(((FatJet_particleNetWithMass_WvsQCD * FatJet_particleNetWithMass_QCD) / (1.0 - FatJet_particleNetWithMass_WvsQCD))[goodcleanFatJets == true], gcFatJet_ptargsort)")
  tagVars.Add("gcFatJet_PNWM_Z", "reorder(((FatJet_particleNetWithMass_ZvsQCD * FatJet_particleNetWithMass_QCD) / (1.0 - FatJet_particleNetWithMass_ZvsQCD))[goodcleanFatJets == true], gcFatJet_ptargsort)")
  tagVars.Add("gcFatJet_PNWM_H4q", "reorder(((FatJet_particleNetWithMass_H4qvsQCD * FatJet_particleNetWithMass_QCD) / (1.0 - FatJet_particleNetWithMass_H4qvsQCD))[goodcleanFatJets == true], gcFatJet_ptargsort)")
  tagVars.Add("gcFatJet_PNWM_Hbb", "reorder(((FatJet_particleNetWithMass_HbbvsQCD * FatJet_particleNetWithMass_QCD) / (1.0 - FatJet_particleNetWithMass_HbbvsQCD))[goodcleanFatJets == true], gcFatJet_ptargsort)")
  tagVars.Add("gcFatJet_PNWM_Hcc", "reorder(((FatJet_particleNetWithMass_HccvsQCD * FatJet_particleNetWithMass_QCD) / (1.0 - FatJet_particleNetWithMass_HccvsQCD))[goodcleanFatJets == true], gcFatJet_ptargsort)")
  tagVars.Add("gcFatJet_PNWM_H", "gcFatJet_PNWM_Hcc + gcFatJet_PNWM_Hbb + gcFatJet_PNWM_H4q")
  tagVars.Add("gcFatJet_PNWM_ToQCD", "reorder(((FatJet_particleNetWithMass_TvsQCD) / (1.0 - FatJet_particleNetWithMass_TvsQCD))[goodcleanFatJets == true], gcFatJet_ptargsort)")
  tagVars.Add("gcFatJet_PNWM_WoQCD", "reorder(((FatJet_particleNetWithMass_WvsQCD) / (1.0 - FatJet_particleNetWithMass_WvsQCD))[goodcleanFatJets == true], gcFatJet_ptargsort)")
  tagVars.Add("gcFatJet_PNWM_ZoQCD", "reorder(((FatJet_particleNetWithMass_ZvsQCD) / (1.0 - FatJet_particleNetWithMass_ZvsQCD))[goodcleanFatJets == true], gcFatJet_ptargsort)")
  tagVars.Add("gcFatJet_PNWM_H4qoQCD", "reorder(((FatJet_particleNetWithMass_H4qvsQCD) / (1.0 - FatJet_particleNetWithMass_H4qvsQCD))[goodcleanFatJets == true], gcFatJet_ptargsort)")
  tagVars.Add("gcFatJet_PNWM_HbboQCD", "reorder(((FatJet_particleNetWithMass_HbbvsQCD) / (1.0 - FatJet_particleNetWithMass_HbbvsQCD))[goodcleanFatJets == true], gcFatJet_ptargsort)")
  tagVars.Add("gcFatJet_PNWM_HccoQCD", "reorder(((FatJet_particleNetWithMass_HccvsQCD) / (1.0 - FatJet_particleNetWithMass_HccvsQCD))[goodcleanFatJets == true], gcFatJet_ptargsort)")
  tagVars.Add("gcFatJet_PNWM_HoQCD", "gcFatJet_PNWM_HccoQCD + gcFatJet_PNWM_HbboQCD + gcFatJet_PNWM_H4qoQCD")
  tagVars.Add("gcFatJet_PNWM_newQCD", "1.0 / (1.0 + gcFatJet_PNWM_ToQCD + gcFatJet_PNWM_WoQCD + gcFatJet_PNWM_ZoQCD + gcFatJet_PNWM_HoQCD)")
  tagVars.Add("gcFatJet_PNWM_QCD", "reorder(FatJet_particleNetWithMass_QCD[goodcleanFatJets == true], gcFatJet_ptargsort)")
  tagVars.Add("gcFatJet_PNWM_regressedMass", "reorder((FatJet_mass * FatJet_particleNet_massCorr)[goodcleanFatJets == true], gcFatJet_ptargsort)")

   # Unused GPT and GPTWM vars
  tagVars.Add("gcFatJet_GPTWM_T", "reorder(FatJet_globalParT3_withMassTopvsQCD[goodcleanFatJets == true], gcFatJet_ptargsort)")
  tagVars.Add("gcFatJet_GPTWM_W", "reorder(FatJet_globalParT3_withMassWvsQCD[goodcleanFatJets == true], gcFatJet_ptargsort)")
  tagVars.Add("gcFatJet_GPTWM_Z", "reorder(FatJet_globalParT3_withMassZvsQCD[goodcleanFatJets == true], gcFatJet_ptargsort)")
  tagVars.Add("gcFatJet_GPTWM_ToQCD", "reorder((FatJet_globalParT3_withMassTopvsQCD/(1 - FatJet_globalParT3_withMassTopvsQCD))[goodcleanFatJets == true], gcFatJet_ptargsort)")
  tagVars.Add("gcFatJet_GPTWM_WoQCD", "reorder((FatJet_globalParT3_withMassWvsQCD/(1 - FatJet_globalParT3_withMassWvsQCD))[goodcleanFatJets == true], gcFatJet_ptargsort)")
  tagVars.Add("gcFatJet_GPTWM_ZoQCD", "reorder((FatJet_globalParT3_withMassZvsQCD/(1 - FatJet_globalParT3_withMassZvsQCD))[goodcleanFatJets == true], gcFatJet_ptargsort)")
  tagVars.Add("gcFatJet_GPT_T", "reorder((FatJet_globalParT3_TopbWqq + FatJet_globalParT3_TopbWtauhv)[goodcleanFatJets == true], gcFatJet_ptargsort)")
  tagVars.Add("gcFatJet_GPT_W", "reorder((FatJet_globalParT3_Xqq + FatJet_globalParT3_Xcs)[goodcleanFatJets == true], gcFatJet_ptargsort)")
  tagVars.Add("gcFatJet_GPT_ZH", "reorder((FatJet_globalParT3_Xbb + FatJet_globalParT3_Xcc + FatJet_globalParT3_Xqq + FatJet_globalParT3_XWW4q)[goodcleanFatJets == true], gcFatJet_ptargsort)")
  tagVars.Add("gcFatJet_GPT_QCD", "reorder(FatJet_globalParT3_QCD[goodcleanFatJets == true], gcFatJet_ptargsort)")
  tagVars.Add("gcFatJet_GPT_regressedMass", "reorder((FatJet_globalParT3_massCorrX2p * FatJet_mass * (1 - FatJet_rawFactor))[goodcleanFatJets == true], gcFatJet_ptargsort)")

  tagVars.Add("gcFatJet_GPTWM_T", "reorder(FatJet_globalParT3_withMassTopvsQCD[goodcleanFatJets == true], gcFatJet_ptargsort)")
  tagVars.Add("gcFatJet_GPTWM_W", "reorder(FatJet_globalParT3_withMassWvsQCD[goodcleanFatJets == true], gcFatJet_ptargsort)")
  tagVars.Add("gcFatJet_GPTWM_Z", "reorder(FatJet_globalParT3_withMassZvsQCD[goodcleanFatJets == true], gcFatJet_ptargsort)")
  
  if isSig:
    tagVars.Add("isTpTp", "true" if isTpTp else "false")
    tagVars.Add("temp_newDecayModes", "SPADecayModeSelection(nGenPart, GenPart_pdgId, GenPart_mass, GenPart_pt, GenPart_phi, GenPart_eta, GenPart_genPartIdxMother, GenPart_status, GenPart_statusFlags, isTpTp)")
    tagVars.Add("true_T_decays", "temp_newDecayModes[0]")
    tagVars.Add("true_B_decays", "temp_newDecayModes[1]")
    tagVars.Add("true_T_lepidx", "temp_newDecayModes[2]")
    tagVars.Add("true_B_lepidx", "temp_newDecayModes[3]")
    tagVars.Add("lep2idx", "temp_newDecayModes[4]")
    tagVars.Add("had1idx", "temp_newDecayModes[5]")
    tagVars.Add("had2idx", "temp_newDecayModes[6]")

    trainCuts = CutGroup("trainCuts")
    if isTpTp:
      trainCuts.Add("Has single lepton", "true_T_lepidx != -1")
    else:
      trainCuts.Add("Has single lepton", "true_B_lepidx != -1")

  if isMC:
    tagVars.Add("temp_gcFatJet_matching", "SPAfatjet_matching(region, nGenPart, GenPart_pdgId, GenPart_mass, GenPart_pt, GenPart_phi, GenPart_eta, GenPart_genPartIdxMother, GenPart_status, GenPart_statusFlags, gcFatJet_pt, gcFatJet_eta, gcFatJet_phi, gcFatJet_mass, gcFatJet_subJetIdx1, gcFatJet_subJetIdx2, gcFatJet_hadronFlavour, SubJet_hadronFlavour, true_T_lepidx, true_B_lepidx, lep2idx, had1idx, had2idx)")
    tagVars.Add("gcFatJet_truth", "temp_gcFatJet_matching[0]")
    tagVars.Add("gcFatJet_lep2idx", "int(temp_gcFatJet_matching[1][0])")
    tagVars.Add("gcFatJet_had1idx", "int(temp_gcFatJet_matching[1][1])")
    tagVars.Add("gcFatJet_had2idx", "int(temp_gcFatJet_matching[1][2])")
    tagVars.Add("gcFatJet_lep2partidx", "int(temp_gcFatJet_matching[2][0])")
    tagVars.Add("gcFatJet_had1partidx", "int(temp_gcFatJet_matching[2][1])")
    tagVars.Add("gcFatJet_had2partidx", "int(temp_gcFatJet_matching[2][2])")

    # trainCuts.Add("Has 3 matched jets", "gcFatJet_pt.size() == 3 && gcFatJet_canParts.size() == 3")

    # trainCuts.Add("Correct ak8 assignment", "gcFatJet_lep2partidx == lep2idx && (gcFatJet_had1partidx == had1idx || gcFatJet_had1partidx == had2idx) && (gcFatJet_had2partidx == had2idx || gcFatJet_had2partidx == had1idx)") 
    trainCuts.Add("Correct ak8 assignment", "gcFatJet_lep2partidx == lep2idx") #&& gcFatJet_had1partidx == had1idx && gcFatJet_had2partidx == had2idx") 
    # tagVars.Add("comp_primes", "get_lastcopy_tprimes(GenPart_pdgId, GenPart_statusFlags, GenPart_pt)")
    # tagVars.Add("comp_daughters", "get_tprime_daughters(comp_primes, GenPart_pdgId, GenPart_genPartIdxMother)")
    # tagVars.Add("gcFatJet_comp", "tag_ak8jets_with_genquarks(comp_daughters, GenPart_eta, GenPart_phi, GenPart_pdgId, gcFatJet_P4)")
  
  tagVars.Add("gcFatJet_tags", "jet_tagging(gcFatJet_PNWM_T, gcFatJet_PNWM_W, gcFatJet_PNWM_Z, gcFatJet_PNWM_H, gcFatJet_PNWM_QCD, gcFatJet_GPT_T, gcFatJet_GPT_W, gcFatJet_GPT_ZH, gcFatJet_GPT_QCD, gcFatJet_GPT_regressedMass, gcFatJet_GPTWM_T, gcFatJet_GPTWM_W, gcFatJet_GPTWM_Z, gcFatJet_subJetIdx1, gcFatJet_subJetIdx2, SubJet_btagUParTAK4B, BTagM,gcJet_P4,gcFatJet_P4,gcJet_BTagM, gcFatJet_GPTWM_ToQCD, gcFatJet_GPTWM_WoQCD, gcFatJet_GPTWM_ZoQCD)")
  tagVars.Add("gcFatJet_PNWMtags", "gcFatJet_tags[0]")
  tagVars.Add("gcFatJet_PNWM_MaxScores", "gcFatJet_tags[1]")
  tagVars.Add("gcFatJet_GPTtags", "gcFatJet_tags[1]")
  tagVars.Add("gcFatJet_GPTWMtags", "gcFatJet_tags[2]")

  # tagVars.Add("gcFatJet_nT","int count = 0; for(int i = 0; i < gcFatJet_PNWMtags.size();i++) { if(gcFatJet_PNWMtags[i] == 6) count++;} return count;")
  # tagVars.Add("gcFatJet_nW","int count = 0; for(int i = 0; i < gcFatJet_PNWMtags.size();i++) { if(gcFatJet_PNWMtags[i] == 24) count++;} return count;")
  # tagVars.Add("gcFatJet_nZ","int count = 0; for(int i = 0; i < gcFatJet_PNWMtags.size();i++) { if(gcFatJet_PNWMtags[i] == 23) count++;} return count;")
  # tagVars.Add("gcFatJet_nH","int count = 0; for(int i = 0; i < gcFatJet_PNWMtags.size();i++) { if(gcFatJet_PNWMtags[i] == 25) count++;} return count;")
  # tagVars.Add("gcFatJet_nB","int count = 0; for(int i = 0; i < gcFatJet_PNWMtags.size();i++) { if(gcFatJet_PNWMtags[i] == 0) count++;} return count;")

  #WORK ON THIS MORE -- need to just be isolated from the 3 highest-pt fat jets, not any of them...
  #jVars.Add("Isolated_AK4","standalone_Jet(gcJet_eta, gcJet_phi, gcFatJet_eta, gcFatJet_phi)")

  # ------------------ Add scale factors and MC jet-based calcs ------------------
  lepSFs = VarGroup('Lepton Scale Factors')
  
  if isMC:
    lepSFs.Add('elrecoSF', 'elrecofunc(electroncorr,elecyr,lepton_pt,lepton_eta,lepton_phi,lepton_ID)')
    lepSFs.Add('elidSF', 'elidfunc(electroncorr,elecyr,"wp80noiso",elecidWP,lepton_pt,lepton_eta,lepton_phi,lepton_ID)')
    lepSFs.Add('muonidSF', 'muidfunc(muonidcorr,lepton_pt,lepton_eta,lepton_ID)')
    lepSFs.Add('muonisoSF', 'muisofunc(muonisocorr,lepton_pt,lepton_eta,lepton_ID)')
   
  #jVars.Add("leptonRecoSF", "recofunc(electroncorr, muonidcorr, yrstr, lepton_pt, lepton_eta, isEl)") ## this is not right, but we'll figure out what corrections we need later
  #jVars.Add("leptonIDSF", "idfunc(muonidcorr,elid_pts,elid_etas,elecidsfs,elecidsfuncs,yrstr, lepton_pt, lepton_eta, isEl)") #at(0) 
  
  #jVars.Add("leptonIsoSF", "isofunc(muiso_pts,muiso_etas,muonisosfs,muonisosfunc,elid_pts,elid_etas,elecisosfs,elecisosfunc, lepton_pt, lepton_eta, isEl)")
  #jVars.Add("leptonHLTSF", "hltfunc(muonhltcorr,elhlt_pts,elhlt_etas,elechltsfs,elechltuncs,yrstr, lepton_pt, lepton_eta, isEl)")
  
  
  # ------------------ W and t reconstruction -----------------
#   recoVars = VarGroup("recoVars")
  
#   recoVars.Add("lepton_lv", "TLorentzVector v; v.SetPtEtaPhiM(lepton_pt, lepton_eta, lepton_phi, lepton_mass); return v;")
#   recoVars.Add("Wnu_lvs", "WReco(corrMET_pt, corrMET_phi, lepton_lv)")
#   recoVars.Add("W_lv", "Wnu_lvs[0]")
#   recoVars.Add("Nu_lv", "Wnu_lvs[1]")
#   recoVars.Add("Nu_pz", "Nu_lv.Pz()")
#   recoVars.Add("minMlbVec", "minMlb_calc(gcJet_pt, gcJet_eta, gcJet_phi, gcJet_mass, lepton_lv)")
#   recoVars.Add("dRWl", "W_lv.DeltaR(lepton_lv)")
#   recoVars.Add("minMlb", "minMlbVec[0]")
#   recoVars.Add("minMlb_idx", "minMlbVec[1]")
#   recoVars.Add("minMlb_lv","TLorentzVector bjet; bjet.SetPtEtaPhiM(gcJet_pt[minMlb_idx], gcJet_eta[minMlb_idx], gcJet_phi[minMlb_idx], gcJet_mass[minMlb_idx]); return bjet;")
#   recoVars.Add("minMlb_dR", "minMlbVec[2]")
#   recoVars.Add("lepton_source", "minMlb > 160 && minMlb_dR > 1 ? 0 : 1")
#   recoVars.Add("t_five", "tReco(lepton_source, gcJet_pt, gcJet_eta, gcJet_phi, gcJet_mass, W_lv, minMlb, minMlb_idx)")
#   recoVars.Add("t_dRWb", "t_five[4]")
#   recoVars.Add("t_lv", "TLorentzVector top; top.SetPtEtaPhiM(t_five[0], t_five[1], t_five[2], t_five[3]); return top;")
#   recoVars.Add("dRtl", "t_lv.DeltaR(lepton_lv)")
#   recoVars.Add("TBp", "TBprimeReco(t_lv, W_lv, lepton_source, gcFatJet_pt, gcFatJet_eta, gcFatJet_phi, gcFatJet_mass, gcFatJet_PNWMtags)")
#   recoVars.Add("tagTdecays", "int(TBp[0])")
#   recoVars.Add("tagBdecays", "int(TBp[1])")

#   if isTpTp:
#     recoVars.Add("J0_idx", "TBp[28]")
#     recoVars.Add("VLQ21_idx", "TBp[29]")
#     recoVars.Add("VLQ22_idx", "TBp[30]")
#   else:
#     recoVars.Add("J0_idx", "TBp[31]")
#     recoVars.Add("VLQ21_idx", "TBp[32]")
#     recoVars.Add("VLQ22_idx", "TBp[33]")
  
  # # -------------------------------------
  
  if isMC:
    nodeToPlot = a.Apply([flagCuts, gjsonVars, gjsonCuts, lVars, lCuts]) #RandVars, Random
  else:
    nodeToPlot = a.Apply([flagCuts, gjsonVars, gjsonCuts, lVars, lCuts])
  
  # # We want the BW decays that go to l + nu
  # ## These will be meaningless for non-signal, but shouldn't crash...
  # #a.Define("decayMODE", "decayModeSelection(region, nGenPart,GenPart_pdgId,GenPart_mass,GenPart_pt,GenPart_phi,GenPart_eta,GenPart_genPartIdxMother,GenPart_status)")	
  # #a.Define("isLeptWdecay", "(decayMODE == 101 || decayMODE == 105 || decayMODE == 106)") 
  # #a.Define("isLeptTdecay", "(1002 <= decayMODE && decayMODE <= 1007) || decayMODE == 1011 || decayMODE == 1012") 

  # # Solution to cleanJets() problem:
  # #       The analyzer .Apply() calls the analyzer .Define().  This .Define() calls self._collectionOrg.CollectionDefCheck(var, newNode).
  # #  This method executes this line: if re.search(r"\b" + re.escape(c+'s') + r"\b", action_str) and (c+'s' not in self._builtCollections):
  # #                                       print ('MAKING %ss for %s'%(c,action_str))
  # #  Apparently somethings get discarded from this _collectionOrg?
  # #  Instead force the .Apply() from the ActiveNode because the node .Apply() is better.
  
  newNode = a.ActiveNode.Apply(jVars)
  a.SetActiveNode(newNode)
  
  a.Apply([metVars, metCuts, gcjetVars, jCuts, jetVars, bCuts, tagVars, trainCuts])

  allColumns = a.GetColumnNames()
  columns = [] #allColumns
  for col in allColumns:
     if ("P4" in col) or ("cleanedJets" in col) or ("cleanFatJets" in col) or ("cleanMets" in col) or ("Dummy" in col): continue 
     if ("LHE" in col) and ("Weight" not in col) and (col != "LHE_HT") and (col != "LHE_Vpt") and (col != "gcHTCorr_WjetLHE"): continue
     if col.startswith("Muon") and ("_tightId" not in col) and ("_isPF" not in col) and ("tunep" not in col) and ("genPartFlav" not in col): continue
     if col.startswith("Electron") and ("genPartFlav" not in col): continue
     if col.startswith("Jet") and ("rawFactor" not in col): continue
     if col.startswith("FatJet") and ("rawFactor" not in col): continue
     if col.startswith("PPS") or col.startswith("Proton") or col.startswith("L1_"): continue
     if col.startswith("Gen") or col.startswith("RawPuppi") or col.startswith("Soft") or col.startswith("fixed"): continue
     if col.startswith("Sub")  or col.startswith("Calo") or col.startswith("Chs"): continue
     if col.startswith("Corr") or col.startswith("Fsr") or col.startswith("Tau"): continue
     if col.startswith("SV") or col.startswith("Puppi") or col.startswith("Photon") or col.startswith("Low"): continue
     if col.startswith("HLT") or col.startswith("HT") or col.startswith("boosted") or col.startswith("Deep"): continue
     if col.startswith("Flag") or col == "Bprime_gen_info" or col == "t_gen_info" or col == "W_gen_info" or col == "metxyoutput": continue
     if col == "assignleps" or col == "pnetoutput" or col == "t_output" or col == "Bprime_output" or col.startswith("Other"): continue
     if col.startswith("PS") or col.startswith("PV") or col.startswith("Tk") or col.startswith("Trig"): continue
     if col.startswith("nCorr") or col.startswith("nFsr"): continue
     if col.startswith("nGen") or col.startswith("nIso") or col.startswith("nLow"): continue
     if col.startswith("nOther") or col.startswith("nPS") or col.startswith("nPhoton"): continue
     if col.startswith("nSV") or col.startswith("nSub") or col.startswith("nTau") or col.startswith("nTrig"): continue
     if col.startswith("nboosted"): continue
     if col == "tauBUG" or col == "Matching" or col == "ObjectList" or col == "manual": continue
     if col.startswith("BeamSpot") or col.startswith("Lepton") or col.startswith("iLepton"): continue
     if col.startswith("MET") or col.startswith("RawPuppiMET"): continue
     if col.startswith("RJR_"): continue
     if col.startswith("gcFatJet_tags"): continue
     if col.startswith("Wnu"): continue
     if col.startswith("temp"): continue

     if col == "Isolated_AK4":
       columns.append(col)
       continue
     elif col.startswith("Iso"):
       continue
     
     columns.append(col)

  finalFile = "SPA_" + sample + era + "_" + year + "_" + str(testNum1) + ".root"
  if not isMC:
    finalFile = "SPA_" + sample + era + ver + "_" + year + "_" + str(testNum1) + ".root"
  
  mode = 'RECREATE'
  if jesvar != "Nominal":
    mode = 'UPDATE'
  
  a.Snapshot(columns, finalFile, "Events_"+jesvar, lazy=False, openOption=mode) #, saveRunChain=True)

  if jesvar == "Nominal":
    print("Cut statistics:")
    rep = a.DataFrame.Report()
    rep.Print()

  print("--------- Analysis End ---------")
    
  a.Close()

if not isMC:
  analyze("Nominal")
else:
  analyze("Nominal")
  #TODO fix why this not work?  shifts = ["Nominal","JECup","JECdn","JERup","JERdn"]
  #for shift in shifts:
  #  analyze(shift)
