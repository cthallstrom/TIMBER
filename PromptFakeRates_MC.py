from TIMBER.Analyzer import *
from TIMBER.Tools.Common import *
import ROOT
from ROOT import TFile
import sys, os
import gc
import array


gc.disable()

from TIMBER.Tools.RestFramesHandler import load_restframes
import correctionlib
correctionlib.register_pyroot_binding()

sys.path.append('../../')
sys.path.append('../../../')

# ------------------ Command Line Arguments and Parsing -------------------
inputFiles = sys.argv[1] #fileList
# Are all the files running if 0 and 8?
testNum1 = sys.argv[2]   #first file in the list to use
testNum2 = sys.argv[3]   #last file in the list to use
year = sys.argv[4]       #2022, 2022EE, 2023, 2023BPix

# Make the New .txt file from line testNum1 to testNum2 because TIMBER can handle .txt of .root's files
print(f"Input File Path: {inputFiles}")
with open(inputFiles) as fp:
  lines = fp.readlines()

start = int(testNum1)
end = int(testNum2)

print(f"TestNum 1: {start} and TestNum 2: {end}")

print("Adding files to trimmed_input.txt")
filelist = []
for i, line in enumerate(lines):
  if i in range(start,end+1):
    filelist.append(line.strip())
print(filelist)

print("Number of Entries:",len(filelist))
print("list contents:",filelist)
sampleName = filelist[0]
print(f"Sample Name: {sampleName}")

# Parse the incoming file names to assign labels
isSig = ("Bprime" in sampleName)
isMadgraphBkg = (("QCD" in sampleName) or ("madgraphMLM" in sampleName))
isTOP = (("Mtt" in sampleName) or ("ST" in sampleName) or ("ttZ" in sampleName) or ("ttW" in sampleName) or ("ttH" in sampleName) or ("TTTo" in sampleName))
isTT = (("TT_Tune" in sampleName) or ("Mtt" in sampleName) or ("TTTo" in sampleName))
isVV = (("WW_" in sampleName) or ("WZ_" in sampleName) or ("ZZ_" in sampleName))
isSM = ("Muon" in sampleName)
isSE = (("SingleElectron" in sampleName) or ("EGamma" in sampleName))
isMC = not (("Single" in sampleName) or ("Muon" in sampleName) or ("EGamma" in sampleName) or ("MuonEG" in sampleName) or ("Tau/" in sampleName))
dataset = int(-1)
if "MuonEG" in sampleName: dataset = 2
elif ("Muon" in sampleName) or ("Muon0" in sampleName) or ("Muon1" in sampleName): dataset = 1
elif ("EGamma" in sampleName) or ("EGamma0" in sampleName) or ("EGamma1" in sampleName): dataset = 3
elif "Tau/" in sampleName: dataset = 4


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
print('dataset = ', dataset)
def analyze(jesvar):
  ROOT.gInterpreter.ProcessLine('string jesvar = "' + jesvar + '"; ')

  # Create analyzer instance
  # is filelist still what you want it be here
  a = analyzer(filelist)


  tightLooseLabel = VarGroup("TLLabel")
  tightLooseLabel.Add("elLoose", 'Electron_pt > 10 && abs(Electron_eta) < 2.5 && (Electron_mvaIso_WP90 == 1)')
  tightLooseLabel.Add("elTight", 'Electron_pt > 10 && abs(Electron_eta) < 2.5 && Electron_mvaIso_WP80 == 1')
  tightLooseLabel.Add("muLoose", 'Muon_pt >= 15 && abs(Muon_eta) < 2.4 && Muon_looseId == 1 && abs(Muon_dxy) < 0.2 && abs(Muon_dz) < 0.5 && Muon_pfIsoId >= 2')
  tightLooseLabel.Add("muTight", 'Muon_pt >= 15 && abs(Muon_eta) < 2.4 && Muon_mediumId == 1 && abs(Muon_dxy) < 0.2 && abs(Muon_dz) < 0.5 && Muon_pfIsoId >= 3')
  tightLooseLabel.Add('goodTaumu', 'Tau_pt > 20 && abs(Tau_eta) < 2.5 && abs(Tau_dz) < 0.2 && Tau_idDeepTau2018v2p5VSmu >= 1')
  tightLooseLabel.Add('goodTaue', 'goodTaumu == 1 && Tau_idDeepTau2018v2p5VSe >= 2')
  tightLooseLabel.Add('tauLoose', 'goodTaue == 1 && Tau_idDeepTau2018v2p5VSjet >= 2')
  tightLooseLabel.Add('tauTight', 'goodTaue == 1 && Tau_idDeepTau2018v2p5VSjet >= 4')

  promptNPLabel = VarGroup("PNPLabel")
  promptNPLabel.Add("elPrompt", 'Electron_genPartFlav == 1 || Electron_genPartFlav == 22 || Electron_genPartFlav == 15')
  promptNPLabel.Add("muPrompt", 'Muon_genPartFlav == 1 || Muon_genPartFlav == 15')
  promptNPLabel.Add("tauPrompt", 'Tau_genPartFlav == 5')
  # 5 = from a b quark, 4 = from a c quark, 3 = from a light quark "or unknown", 0 = "unmatched"
  # Useful to make histograms of fake rate using only 4s & 5s, and then only 0s & 3s, as well as all together.
  promptNPLabel.Add("elFake", 'Electron_genPartFlav == 3 || Electron_genPartFlav == 4 || Electron_genPartFlav == 5 || Electron_genPartFlav == 0')
  promptNPLabel.Add("muFake", 'Muon_genPartFlav == 3 || Muon_genPartFlav == 4 || Muon_genPartFlav == 0 || Muon_genPartFlav == 5')
  promptNPLabel.Add("tauFake", 'Tau_genPartFlav == 0') # not the same info here

  histItems = VarGroup("histItems")
  histItems.Add("elDen", "elLoose && elPrompt")
  histItems.Add("elNum", "elTight && elPrompt")
  histItems.Add("muDen", "muLoose && muPrompt")
  histItems.Add("muNum", "muTight && muPrompt")
  histItems.Add("tauDen", "tauLoose && tauPrompt")
  histItems.Add("tauNum", "tauTight && tauPrompt")
  histItems.Add("elPtDen", "Electron_pt[elDen]")
  histItems.Add("elEtaDen", "Electron_eta[elDen]")
  histItems.Add("elPtNum", "Electron_pt[elNum]")
  histItems.Add("elEtaNum", "Electron_eta[elNum]")
  histItems.Add("muPtDen", "Muon_pt[muDen]")
  histItems.Add("muEtaDen", "abs(Muon_eta[muDen])")
  histItems.Add("muPtNum", "Muon_pt[muNum]")
  histItems.Add("muEtaNum", "abs(Muon_eta[muNum])")
  histItems.Add("tauPtDen", "Tau_pt[tauDen]")
  histItems.Add("tauEtaDen", "abs(Tau_eta[tauDen])")
  histItems.Add("tauPtNum", "Tau_pt[tauNum]")
  histItems.Add("tauEtaNum", "abs(Tau_eta[tauNum])")


  fakeTL = VarGroup("FakeTightToLoose")
  fakeTL.Add("elFakeDen", "elLoose && elFake")
  fakeTL.Add("muFakeDen", "muLoose && muFake")
  fakeTL.Add("tauFakeDen", "tauLoose && tauFake")
  fakeTL.Add("elFakeNum", "elTight && elFake")
  fakeTL.Add("muFakeNum", "muTight && muFake")
  fakeTL.Add("tauFakeNum", "tauTight && tauFake")


  # Electrons
  fakeTL.Add("elPtFakeDen",  "Electron_pt[elFakeDen]")
  fakeTL.Add("elEtaFakeDen", "Electron_eta[elFakeDen]")
  fakeTL.Add("elPtFakeNum",  "Electron_pt[elFakeNum]")
  fakeTL.Add("elEtaFakeNum", "Electron_eta[elFakeNum]")

  # Muons
  fakeTL.Add("muPtFakeDen",  "Muon_pt[muFakeDen]")
  fakeTL.Add("muEtaFakeDen", "abs(Muon_eta[muFakeDen])")
  fakeTL.Add("muPtFakeNum",  "Muon_pt[muFakeNum]")
  fakeTL.Add("muEtaFakeNum", "abs(Muon_eta[muFakeNum])")

  # Taus
  fakeTL.Add("tauPtFakeDen",  "Tau_pt[tauFakeDen]")
  fakeTL.Add("tauEtaFakeDen", "abs(Tau_eta[tauFakeDen])")
  fakeTL.Add("tauPtFakeNum",  "Tau_pt[tauFakeNum]")
  fakeTL.Add("tauEtaFakeNum", "abs(Tau_eta[tauFakeNum])")


  ptbins  = [10.0, 20.0, 30.0, 40.0, 50.0, 70.0, 100.0, 200.0, 9999.0]
  etabinsmutau = [0,0.9,1.2,2.1,2.4]
  etabinsel = [-2.5, -2.0, -1.566, -1.444, -0.8, 0.0, 0.8, 1.444, 1.566, 2.0, 2.5]

  a.Apply(tightLooseLabel)
  a.Apply(promptNPLabel)
  a.Apply(histItems)
  a.Apply(fakeTL)

  ptvec = ROOT.std.vector('double')(ptbins)
  etavecel = ROOT.std.vector('double')(etabinsel)
  etavecmu = ROOT.std.vector('double')(etabinsmutau)

  ptarr = array.array('d', ptbins)
  etaarrel = array.array('d', etabinsel)
  etaarrmu = array.array('d', etabinsmutau)


  fh_el_den = a.DataFrame.Histo2D(("fh_el_den", "Electron Fake Denominator; pT; eta", len(ptbins)-1, ptarr, len(etabinsel)-1, etaarrel), "elPtFakeDen", "elEtaFakeDen")
  fh_el_num = a.DataFrame.Histo2D(("fh_el_num", "Electron Fake Numerator; pT; eta", len(ptbins)-1, ptarr, len(etabinsel)-1, etaarrel), "elPtFakeNum", "elEtaFakeNum")
  fh_mu_den = a.DataFrame.Histo2D(("fh_mu_den", "Muon Fake Denominator; pT; eta", len(ptbins)-1, ptarr, len(etabinsmutau)-1, etaarrmu), "muPtFakeDen", "muEtaFakeDen")
  fh_mu_num = a.DataFrame.Histo2D(("fh_mu_num", "Muon Fake Numerator; pT; eta", len(ptbins)-1, ptarr, len(etabinsmutau)-1, etaarrmu), "muPtFakeNum", "muEtaFakeNum")
  fh_tau_den = a.DataFrame.Histo2D(("fh_tau_den", "Tau Fake Denominator; pT; eta", len(ptbins)-1, ptarr, len(etabinsmutau)-1, etaarrmu), "tauPtFakeDen", "tauEtaFakeDen")
  fh_tau_num = a.DataFrame.Histo2D(("fh_tau_num", "Tau Fake Numerator; pT; eta", len(ptbins)-1, ptarr, len(etabinsmutau)-1, etaarrmu), "tauPtFakeNum", "tauEtaFakeNum")
  h_el_den = a.DataFrame.Histo2D(("h_el_den", "Prompt Electron Denominator; pT; eta", len(ptbins)-1, ptarr, len(etabinsel)-1, etaarrel), "elPtDen", "elEtaDen")
  h_el_num = a.DataFrame.Histo2D(("h_el_num", "Prompt Electron Numerator; pT; eta", len(ptbins)-1, ptarr, len(etabinsel)-1, etaarrel), "elPtNum", "elEtaNum")
  h_mu_den = a.DataFrame.Histo2D(("h_mu_den", "Prompt Muon Denominator; pT; eta", len(ptbins)-1, ptarr, len(etabinsmutau)-1, etaarrmu), "muPtDen", "muEtaDen")
  h_mu_num = a.DataFrame.Histo2D(("h_mu_num", "Prompt Muon Numerator; pT; eta", len(ptbins)-1, ptarr, len(etabinsmutau)-1, etaarrmu), "muPtNum", "muEtaNum")
  h_tau_den = a.DataFrame.Histo2D(("h_tau_den", "Prompt Tau Denominator; pT; eta", len(ptbins)-1, ptarr, len(etabinsmutau)-1, etaarrmu), "tauPtDen", "tauEtaDen")
  h_tau_num = a.DataFrame.Histo2D(("h_tau_num", "Prompt Tau Numerator; pT; eta", len(ptbins)-1, ptarr, len(etabinsmutau)-1, etaarrmu), "tauPtNum", "tauEtaNum")

  finalFile = 'MCPFRate_'+sample + era + "_" + year + "_" + str(testNum1) + ".root"
  outfile = ROOT.TFile.Open(finalFile, "RECREATE")
  for h in [fh_el_den, fh_el_num, fh_mu_den,fh_mu_num,fh_tau_den, fh_tau_num, h_el_den,h_el_num,h_mu_den,h_mu_num,h_tau_den,h_tau_num]:
    h.GetValue().Write()
  outfile.Close()

  print("Done analyzing!")

analyze("Nominal")
