import os, sys, math, re
from ROOT import TFile, TTree, TH1D, TH2D, TCanvas, gStyle, gPad, TLatex

readFile = True
if readFile:
    file_str = "RDF_TprimeTprime_Par-M-1700_TuneCP5_13p6TeV_amcatnlo-pythia8_2024_0.root"
    inFile = TFile.Open(file_str)

    pattern = r"RDF_([TB]).*?Par-M-(\d+)"
    mass = re.search(pattern, file_str)
    name = f"{mass.group(1)}{mass.group(2)}GeV"

    truth = TH2D("jet_truth",";tagger ID;true ID",10,0,10,6,0,6)
    PNWM = TH2D("jet_PNWMid",f";{name} PNWM decay modes;true decay modes",10,0,10,6,0,6)

    truth.Sumw2() #Sum weights squared -> account for uncertainties. in future we divide this
    PNWM.Sumw2()

    t = inFile.Get("Events_Nominal")

    for ievent in range(t.GetEntries()):
        
        t.GetEntry(ievent)
        nJets = t.nFatJet
        i = 0
        
        for ijet in range(nJets):

            PNWMid = t.tagTdecays

            # Fill truth info into all x-axis values
            if t.decayFinds[ijet] == 1:   #deciding on the truth, we can just look at the truth from our truth vector
                i = 0.5      
            elif t.decayFinds[ijet] == 2:
                i = 1.5
            elif t.decayFinds[ijet] == 3:
                i = 2.5
            elif t.decayFinds[ijet] == 4:
                i = 3.5
            elif t.decayFinds[ijet] == 5:
                i = 4.5
            elif t.decayFinds[ijet] == 6:
                i = 5.5

            for imode in range(0,10):  #fill the denoms into the correct ROW
                truth.Fill(imode,i)
            
                    
            # Fill reconstructed info into only the right x-axis value
            # taggedTjet = 1, taggedWjet = 2, untaggedTlep = 3, untaggedWlep = 4
            if PNWMid == 1:
                PNWM.Fill(0.5,i)
            elif PNWMid == 2:
                PNWM.Fill(1.5,i)
            elif PNWMid == 3:
                PNWM.Fill(2.5,i)
            elif PNWMid == 4:
                PNWM.Fill(3.5,i)
            elif PNWMid == 5:
                PNWM.Fill(4.5,i)
            elif PNWMid == 6:
                PNWM.Fill(5.5,i)
            elif PNWMid == 7:
                PNWM.Fill(6.5,i)
            elif PNWMid == 8:
                PNWM.Fill(7.5,i)
            elif PNWMid == 9:
                PNWM.Fill(8.5,i)
            elif PNWMid == 0:
                PNWM.Fill(9.5,i)

            
    PNWM.Divide(PNWM, truth, 1, 1, "B")

    histFile = TFile.Open(f"/uscms_data/d3/cai/run3VLQ/TIMBER/cMatrices/{name}_L.root", "recreate")

    PNWM.Write()

    histFile.Write()
    histFile.Close()

## Read histograms from file
histFile = TFile.Open(f"/uscms_data/d3/cai/run3VLQ/TIMBER/cMatrices/{name}_L.root")

PNWM = histFile.Get("jet_PNWMid")

canv1 = TCanvas("c1","c1",800,600)

xlabels = ['bWbW','tZtZ','tHtH','tZtH', 'tZbW', 'tHbW', 'TH', 'TZ', 'BW', 'none']
for ibin in range(1,PNWM.GetNbinsX()+1):
    PNWM.GetXaxis().SetBinLabel(ibin,xlabels[ibin-1])
    
ylabels = ['bWbW','tZtZ','tHtH','tZtH', 'tZbW', 'tHbW']
for ibin in range(1,PNWM.GetNbinsY()+1):
    PNWM.GetYaxis().SetBinLabel(ibin,ylabels[ibin-1])

    
PNWM.SetMinimum(5e-5)
PNWM.SetMaximum(0.5)
gPad.SetLogz(1)

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
canv1.SaveAs(f"/uscms_data/d3/cai/run3VLQ/TIMBER/cMatrices/{name}_new_whichLep_PNWMdecayTags.png")