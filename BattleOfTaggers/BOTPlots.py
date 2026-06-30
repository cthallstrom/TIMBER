
import os, sys, math, re
from ROOT import TFile, TTree, TH1D, TH2D, TCanvas, gStyle, gPad, TLegend, kBlue, kRed, kGreen, TLatex, kRainBow,TObject
from array import array

eff_types = ["mass","algo"]
#eff_types = ["algo"]
#eff_types = ["mass"]

dir_str = "root://cmseos.fnal.gov//store/user/lpchtop/TTBB_Jun2026_Run3/"
sample_files = ["RDF_TprimeTprime_Par-M-1200_TuneCP5_13p6TeV_amcatnlo-pythia8_2024_0.root","RDF_TprimeTprime_Par-M-1300_TuneCP5_13p6TeV_amcatnlo-pythia8_2024_0.root","RDF_TprimeTprime_Par-M-1400_TuneCP5_13p6TeV_amcatnlo-pythia8_2024_0.root","RDF_TprimeTprime_Par-M-1600_TuneCP5_13p6TeV_amcatnlo-pythia8_2024_0.root","RDF_TprimeTprime_Par-M-1700_TuneCP5_13p6TeV_amcatnlo-pythia8_2024_0.root","RDF_TprimeTprime_Par-M-1800_TuneCP5_13p6TeV_amcatnlo-pythia8_2024_0.root","RDF_TprimeTprime_Par-M-1900_TuneCP5_13p6TeV_amcatnlo-pythia8_2024_0.root","RDF_TprimeTprime_Par-M-2000_TuneCP5_13p6TeV_amcatnlo-pythia8_2024_0.root","RDF_TprimeTprime_Par-M-2100_TuneCP5_13p6TeV_amcatnlo-pythia8_2024_0.root","RDF_TprimeTprime_Par-M-2200_TuneCP5_13p6TeV_amcatnlo-pythia8_2024_0.root"]

test_files = ["RDF_TprimeTprime_Par-M-1200_TuneCP5_13p6TeV_amcatnlo-pythia8_2024_0.root","RDF_TprimeTprime_Par-M-1300_TuneCP5_13p6TeV_amcatnlo-pythia8_2024_0.root"]

files = [dir_str + x for x in sample_files]

TorB = "T"

ptbins = array('d',[200,300,400,480,560,650,740,1000,1280,1640,2000])
nbins = len(ptbins) - 1
#print(nbins)

def runAll(eff_types,ptbins,nbins,files,TorB):
    for eff in eff_types:
#        createRootFiles(eff,files,ptbins,nbins,TorB)
        plotEff(eff,TorB)

def createRootFiles(eff_type,file_strs,ptbins,nbins,TorB):
    for k,file_str in enumerate(file_strs):
        print(f"opening {file_str}")
        pattern = fr"RDF_({TorB}).*?Par-M-(\d+)"
        print(pattern)
        mass = re.search(pattern, file_str)
        mass_name = f"{mass.group(1)}_{mass.group(2)[0]}p{mass.group(2)[1]}TeV"
        print(f"processing {mass_name}")
        inFile = TFile.Open(file_str)
        t = inFile.Get("Events_Nominal")
        
        for i,matched in enumerate({"tagged","mistagged"}):
            if matched == "tagged":
                isMatched = True
            else:
                isMatched = False
                
            for j,part in enumerate({"t_quark","W_boson","Z_boson","H_boson"}):
                if part == "t_quark":
                    ID = 6
                elif part == "W_boson":
                    ID = 24
                elif part == "Z_boson":
                    ID = 23
                else:
                    ID = 25

                yaxis_str_d = part
                if not isMatched:
                    yaxis_str_d = f"non{part}"                
                    
                truth = TH1D(f"truth_{part}_{matched}", f";x;",nbins,ptbins)
                PNWM = TH1D(f"{part}_{matched}_PNWM_{mass_name}",f";Jet pt (GeV);N({part} {matched} PNWM jets)/N({yaxis_str_d} jets)",nbins,ptbins)
                GPT = TH1D(f"{part}_{matched}_GPT_{mass_name}",f";Jet pt (GeV);N({part} {matched} GPT jets)/N({yaxis_str_d} jets)",nbins,ptbins)
                GPTWM = TH1D(f"{part}_{matched}_GPTWM_{mass_name}",f";Jet pt (GeV);N({part} {matched} GPTWM jets)/N({yaxis_str_d} jets)",nbins,ptbins)
 
                truth.Sumw2() #Sum weights squared -> account for uncertainties. in future we divide this
                PNWM.Sumw2()
                GPT.Sumw2()
                GPTWM.Sumw2()
    
                for ievent in range(t.GetEntries()):
                    t.GetEntry(ievent)
                    nJets = t.nFatJet
                
                    for ijet in range(nJets):
                        a = 1
                        b = 1
                        c = 1
                        GPTWMscores = [t.gcFatJet_GPTWM_ToQCD[ijet] * a, t.gcFatJet_GPTWM_WoQCD[ijet] * b, t.gcFatJet_GPTWM_ZoQCD[ijet] * c]
                        GPTWMmaxindex = GPTWMscores.index(max(GPTWMscores))
                        
                        if GPTWMmaxindex == 0 and max(GPTWMscores) > 1:
                            GPTWMid = 6
                        elif GPTWMmaxindex == 1 and max(GPTWMscores) > 1:
                            GPTWMid = 24
                        elif GPTWMmaxindex == 2 and max(GPTWMscores) > 1:
                            if t.gcFatJet_GPT_regressedMass[ijet] < 105:
                                GPTWMid = 23
                            else:
                                GPTWMid = 25
                                            
                        else:
                            subjetIdx1 = int(t.gcFatJet_subJetIdx1[ijet])
                            subjetIdx2 = int(t.gcFatJet_subJetIdx2[ijet])
                            BTagM = 0.1272
                            if((subjetIdx1 >= 0 and t.mySubJet_btag[subjetIdx1] >= BTagM) or (subjetIdx2 >= 0 and t.mySubJet_btag[subjetIdx2] >= BTagM)):
                                GPTWMid = 5
                            else:
                                GPTWMid = 0

                        if isMatched and t.gcFatJet_truth[ijet] == ID:
                            truth.Fill(t.gcFatJet_pt[ijet])
            
                            if t.gcFatJet_PNWMtags[ijet] == ID:
                                PNWM.Fill(t.gcFatJet_pt[ijet])

                            if t.gcFatJet_GPTtags[ijet] == ID:
                                GPT.Fill(t.gcFatJet_pt[ijet])

                            if GPTWMid == ID:
                                GPTWM.Fill(t.gcFatJet_pt[ijet])

                        if not isMatched and t.gcFatJet_truth[ijet] != ID:
                            truth.Fill(t.gcFatJet_pt[ijet])
                        
                            if t.gcFatJet_PNWMtags[ijet] == ID:
                                PNWM.Fill(t.gcFatJet_pt[ijet])
                            
                            if t.gcFatJet_GPTtags[ijet] == ID:
                                GPT.Fill(t.gcFatJet_pt[ijet])

                            if GPTWMid == ID:
                                GPTWM.Fill(t.gcFatJet_pt[ijet])

                #print(PNWM.GetBinContent(1))
                PNWM.Divide(PNWM, truth, 1, 1, "B")
                GPT.Divide(GPT, truth, 1, 1, "B")
                GPTWM.Divide(GPTWM, truth, 1, 1, "B")
                
                if i == j and j == 0:
                    amode = "recreate"
                else:
                    amode = "update"

                if i == j and j == k and k == 0:
                    mmode = "recreate"
                else:
                    mmode = "update"
                    
                if eff_type == "mass":
                    histFile = TFile.Open(f"massEff/PNWM_{mass_name[0]}_massEff.root", mmode)
                    PNWM.Write()
                    histFile.Write()
                    histFile.Close()
                
                    histFile = TFile.Open(f"massEff/GPT_{mass_name[0]}_massEff.root", mmode)
                    GPT.Write()
                    histFile.Write()
                    histFile.Close()
                                
                    histFile = TFile.Open(f"massEff/GPTWM_{mass_name[0]}_massEff.root", mmode)
                    GPTWM.Write()
                    histFile.Write()
                    histFile.Close()
                elif eff_type == "algo":
                    histFile = TFile.Open(f"taggerEff/{mass_name}_taggerEff.root", amode)
                    PNWM.Write()
                    GPT.Write()
                    GPTWM.Write()      
                    #histFile.ls()
                    histFile.Write()
                    histFile.Close()
                    
                GPT.Reset()
                GPTWM.Reset()
                PNWM.Reset()
                truth.Reset()
    print("end processing")
                
def plotEff(eff_type,TorB):
    for matched in {"tagged","mistagged"}:
        for part in {"t_quark","W_boson","Z_boson","H_boson"}:
            if eff_type == "mass":
                for tagger in {"PNWM","GPT","GPTWM"}:
                    canvas_name = f"canv_{part}_{matched}_{tagger}"
                    canv1 = TCanvas(canvas_name,part,800,600)
                    gStyle.SetOptStat(0)
                    canv1.SetLeftMargin(0.15)
                    gStyle.SetPalette(kRainBow)
                    part_space = part.replace("_"," ")
                    tagger_full = ""
                    if tagger == "PNWM":
                        tagger_full = "ParticleNet"
                    elif tagger == "GPT":
                        tagger_full = "GloParT(MD)"
                    else:
                        tagger_full = "GloParT"

                    if matched == "mistagged" or part == "Z_boson" or canvas_name == "canv_W_boson_tagged_GPT": #mistagged
                        legend = TLegend(0.45,0.65,0.85,0.85)
                        legend.SetTextFont(43)
                        legend.SetTextSize(22)
                        legend.SetHeader(f"{part_space} {matched} {tagger_full}","C")
                    else:
                        legend = TLegend(0.20,0.15,0.57,0.37)
                        legend.SetTextFont(43)
                        legend.SetTextSize(22)
                        
                        legend.SetHeader(f"{part_space} {matched} {tagger_full}","R")

                    print("opening tagger file, branches below")
                    
                    tagger_file = TFile.Open(f"massEff/{tagger}_{TorB}_massEff.root","read")
                   # tagger_file.ls()
                    trees = [key.GetName() for key in tagger_file.GetListOfKeys() if key.GetClassName() == "TH1D"]
                    mass_trees = [match for match in trees if part in match and f"_{matched}" in match and tagger in match]
                
                    legend.SetNColumns(2)

                    title = tagger_file.Get(mass_trees[0]).GetYaxis().GetTitle().replace("_"," ").replace(tagger,tagger_full)
                    if part == "t_quark":
                        title = title.replace(" quark","")
                    else:
                        title = title.replace(" boson","")
                        
                    
                    for i,mass_name in enumerate(mass_trees):
                        mass_hist = tagger_file.Get(mass_name)

                        color_index = int(i * (gStyle.GetNumberOfColors() / len(mass_trees)))
                        color = gStyle.GetColorPalette(color_index)

                        mass_hist.SetMarkerStyle(20)
                        mass_hist.SetMarkerColor(color)
                        mass_hist.SetLineColor(color)
                        mass_hist.GetYaxis().SetRangeUser(0,1)
                        mass_hist.GetYaxis().SetTitle(title)

                        if i == 0:
                            mass_hist.Draw("pe")    
                        else:
                            mass_hist.Draw("pe same")

                        print(f"legend name from {mass_name} is ")

                        legend.AddEntry(mass_hist, f"{mass_name[-8]}{mass_name[-8]} {mass_name[-6]}.{mass_name[-4]}TeV")
                        #mass_hist.Reset()

                    text = TLatex()
                    text.SetNDC() 
                    text.SetTextSize(0.04)
                    text.SetTextFont(42)
                    text.SetTextAlign(11)
                    text.DrawLatex(0.15, 0.92, "Private work (CMS simulation)")
                    text.SetTextAlign(31)
                    text.DrawLatex(0.90, 0.92, "13.6 TeV")
                    
                    png_name = f"massEff/{TorB}_{part}_{matched}_{tagger}_massEff.png"
                    #canv1.BuildLegend(title=, option=)
                    legend.SetBorderSize(0)
                    legend.SetFillStyle(0)
                    legend.Draw()
                    canv1.SaveAs(png_name)
                    tagger_file.Close()
                    canv1.Close()
                    legend.Clear()
                    del canv1

            elif eff_type == "algo":
                for file_name in os.scandir("taggerEff"):
                    file_name = file_name.name
                    if file_name[-5:] == ".root" and file_name[0] == TorB:
                        mass_name = file_name[:8]
                        histFile = TFile.Open(f"taggerEff/{file_name}", "read")

                        if not histFile or histFile.IsZombie():
                            print(f"Error: Could not open file taggerEff/{file_name}")
                        
                        PNWM  = histFile.Get(f"{part}_{matched}_PNWM_{mass_name}")
                        GPT   = histFile.Get(f"{part}_{matched}_GPT_{mass_name}")
                        GPTWM = histFile.Get(f"{part}_{matched}_GPTWM_{mass_name}")

                        if not PNWM or not GPT or not GPTWM:
                            print(f"Error: One of the histograms was not found in {file_name}!")
                            print(f"Attempted name: {part}_{matched}_(tagger)_{mass_name}")
                        
                        PNWM.SetMarkerStyle(20)
                        GPT.SetMarkerStyle(20)
                        GPTWM.SetMarkerStyle(20)

                        PNWM.SetMarkerColor(kBlue)
                        GPT.SetMarkerColor(kRed)
                        GPTWM.SetMarkerColor(kGreen)

                        PNWM.SetLineColor(kBlue)
                        GPT.SetLineColor(kRed)
                        GPTWM.SetLineColor(kGreen)

                        PNWM.GetYaxis().SetRangeUser(0,1)
                        GPT.GetYaxis().SetRangeUser(0,1)
                        GPTWM.GetYaxis().SetRangeUser(0,1)

                        title = PNWM.GetYaxis().GetTitle().replace("_"," ").replace("PNWM","")
                        if part == "t_quark":
                            title = title.replace(" quark","")
                        else:
                            title = title.replace(" boson","")
                        
                        PNWM.GetYaxis().SetTitle(title)
                        GPT.GetYaxis().SetTitle(title)
                        GPTWM.GetYaxis().SetTitle(title)
                        
                        canvas_name = f"canv_{part}_{matched}"            
                        print(f"create {canvas_name} below")
                        canv1 = TCanvas(canvas_name,part,800,600)

                        gStyle.SetOptStat(0)
                        canv1.SetLeftMargin(0.15)

                        PNWM.Draw("pe")    
                        GPT.Draw("pe same")
                        GPTWM.Draw("pe same")

                        if matched == "mistagged" or part == "Z_boson": #mistagged
                            legend = TLegend(0.65,0.65,0.80,0.80)
                        else:
                            legend = TLegend(0.65,0.15,0.80,0.33)

                        mass_space = mass_name.replace("_"," ")
                        mass_space = mass_space.replace("p",".")
                        legend.SetTextFont(43)
                        legend.SetTextSize(24)
                        legend.SetHeader(f"{matched} at {mass_space}","C")
                        legend.SetBorderSize(0)
                        legend.SetFillStyle(0)
                        legend.AddEntry(PNWM, "ParticleNet")
                        legend.AddEntry(GPT, "GloParT(MD)")
                        legend.AddEntry(GPTWM, "GloParT")
                        legend.Draw()

                        text = TLatex()
                        text.SetNDC() 
                        text.SetTextSize(0.04)
                        text.SetTextFont(42)
                        text.SetTextAlign(11)
                        text.DrawLatex(0.15, 0.92, "Private work (CMS simulation)")
                        text.SetTextAlign(31)
                        text.DrawLatex(0.85, 0.92, "13.6 TeV")
                        
                        png_name = f"taggerEff/{part}_{matched}_{mass_name}_taggerEff.png"
                        canv1.SaveAs(png_name)

                        histFile.Close()
                        # PNWM.Reset()
                        # GPT.Reset()
                        # GPTWM.Reset()
                        canv1.Close()
                        del canv1

runAll(eff_types,ptbins,nbins,files,TorB)
