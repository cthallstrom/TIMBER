import os, sys, math, re
from ROOT import TFile, TTree, TH1D, TH2D, TCanvas, gStyle, gPad, TLatex

readFile = True
if readFile:
    file_str = "RDF_TprimeTprime_Par-M-1600_TuneCP5_13p6TeV_amcatnlo-pythia8_2024_0.root"
    inFile = TFile.Open(file_str)

    pattern = r"RDF_([TB]).*?Par-M-(\d+)"
    mass = re.search(pattern, file_str)
    name = f"{mass.group(1)}{mass.group(2)}GeV"

    truth = TH2D("jet_truth",";tagger ID;true ID",6,0,6,6,0,6)
    ourPNWM = TH2D("ourPNWMid",f";{name} our truth (no Pt, MET, or lep cuts);her truth",6,0,6,7,0,7)
    herPNWM = TH2D("herPNWMid",f";herPNWM ID;true ID",6,0,6,7,0,7)

    truth.Sumw2() #Sum weights squared -> account for uncertainties. in future we divide this
    ourPNWM.Sumw2()
    herPNWM.Sumw2()

    t = inFile.Get("Events_Nominal")
                
    truth.Reset()
    ourPNWM.Reset()
    herPNWM.Reset()


    for ievent in range(t.GetEntries()):
        
        t.GetEntry(ievent)
        nJets = t.nFatJet

        n_jets = min(len(t.gcFatJet_comp), len(t.gcFatJet_truth))

        for ijet in range(n_jets):
            if len(t.gcFatJet_comp[ijet]) != 1:
                herPNWMid = -1
            else:
                herPNWMid = t.gcFatJet_comp[ijet][0]

            i = -1  
            if herPNWMid == 0:
                i = 0.5
            elif herPNWMid == 5:
                i = 1.5
            elif herPNWMid == 24:
                i = 2.5
            elif herPNWMid == 23:
                i = 3.5
            elif herPNWMid == 25:
                i = 4.5
            elif herPNWMid == 6:
                i = 5.5
            elif herPNWMid == -1:
                i = 6.5

            if i < 0:
                continue

            for imode in range(0,7):  #fill the denoms into the correct ROW
                herPNWM.Fill(imode,i)

            PNWMid = int(t.gcFatJet_truth[ijet])

            if PNWMid == 0:
                ourPNWM.Fill(0.5,i)
            elif PNWMid == 5:
                ourPNWM.Fill(1.5,i)
            elif PNWMid == 24:
                ourPNWM.Fill(2.5,i)
            elif PNWMid == 23:
                ourPNWM.Fill(3.5,i)
            elif PNWMid == 25:
                ourPNWM.Fill(4.5,i)
            elif PNWMid == 6:
                ourPNWM.Fill(5.5,i)
        
            
    ourPNWM.Divide(ourPNWM, herPNWM, 1, 1, "B")

    histFile = TFile.Open(f"truthComparison.root", "recreate")

    ourPNWM.Write()

    histFile.Write()
    histFile.Close()

## Read histograms from file
histFile = TFile.Open(f"truthComparison.root")

PNWM = histFile.Get("ourPNWMid")

canv1 = TCanvas("c1","c1",800,600)

xlabels = ['udsc','b','W','Z', 'H', 't']
for ibin in range(1,ourPNWM.GetNbinsX()+1):
    PNWM.GetXaxis().SetBinLabel(ibin,xlabels[ibin-1])
    
ylabels = ['udsc','b','W','Z', 'H', 't', 'none']
for ibin in range(1,ourPNWM.GetNbinsY()+1):
    PNWM.GetYaxis().SetBinLabel(ibin,ylabels[ibin-1])

PNWM.SetMinimum(0.0)
PNWM.SetMaximum(1.0)

gStyle.SetOptStat(0)
gStyle.SetPaintTextFormat("1.2f")
canv1.SetLeftMargin(0.15)
    
PNWM.Draw("colz texte")
latex = TLatex()
latex.SetNDC()
latex.SetTextSize(0.04)
latex.SetTextAlign(11)
latex.DrawLatex(0.10, 0.92, "#bf{Private work} (CMS simulation)")
latex.SetTextAlign(31)
latex.DrawLatex(0.9, 0.92, "13.6 TeV")
gPad.Update()
canv1.SaveAs(f"tCnPtMETLepCuts.png")