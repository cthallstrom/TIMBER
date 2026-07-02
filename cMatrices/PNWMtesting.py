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
    ourPNWM = TH2D("ourPNWMid",f";{name} M ourPNWM ID;herPNWM ID",6,0,6,6,0,6)
    herPNWM = TH2D("herPNWMid",f";herPNWM ID;true ID",6,0,6,6,0,6)

    truth.Sumw2() #Sum weights squared -> account for uncertainties. in future we divide this
    ourPNWM.Sumw2()
    herPNWM.Sumw2()

    t = inFile.Get("Events_Nominal")

    BTagM = 0.1272
    BTagL = 0.0246
                
    truth.Reset()
    ourPNWM.Reset()
    herPNWM.Reset()


    for ievent in range(t.GetEntries()):
        
        t.GetEntry(ievent)
        nJets = t.nFatJet
        i = 0
        
        for ijet in range(nJets):

            PNWMscores = [t.gcFatJet_PNWM_T[ijet], t.gcFatJet_PNWM_W[ijet], t.gcFatJet_PNWM_Z[ijet], t.gcFatJet_PNWM_H[ijet], t.gcFatJet_PNWM_QCD[ijet]]
            PNWMmaxindex = PNWMscores.index(max(PNWMscores))

            if PNWMmaxindex == 0:
                PNWMid = 6
            elif PNWMmaxindex == 1:
                PNWMid = 24
            elif PNWMmaxindex == 2:
                PNWMid = 23
            elif PNWMmaxindex == 3:
                PNWMid = 25
            elif PNWMmaxindex == 4:
                subjetIdx1 = int(t.gcFatJet_subJetIdx1[ijet])
                subjetIdx2 = int(t.gcFatJet_subJetIdx2[ijet])
                if((subjetIdx1 >= 0 and t.mySubJet_btag[subjetIdx1] >= BTagL) or (subjetIdx2 >= 0 and t.mySubJet_btag[subjetIdx2] >= BTagL)):
                    PNWMid = 5
                else:
                    PNWMid = 0

            herPNWMscores = [t.gcFatJet_PNWM_ToQCD[ijet], t.gcFatJet_PNWM_WoQCD[ijet], t.gcFatJet_PNWM_ZoQCD[ijet], t.gcFatJet_PNWM_HoQCD[ijet], t.gcFatJet_PNWM_newQCD[ijet]]
            herPNWMmaxindex = herPNWMscores.index(max(herPNWMscores))

            if herPNWMmaxindex == 0:
                herPNWMid = 6
            elif herPNWMmaxindex == 1:
                herPNWMid = 24
            elif herPNWMmaxindex == 2:
                herPNWMid = 23
            elif herPNWMmaxindex == 3:
                herPNWMid = 25
            elif herPNWMmaxindex == 4:
                subjetIdx1 = int(t.gcFatJet_subJetIdx1[ijet])
                subjetIdx2 = int(t.gcFatJet_subJetIdx2[ijet])
                if((subjetIdx1 >= 0 and t.mySubJet_btag[subjetIdx1] >= BTagL) or (subjetIdx2 >= 0 and t.mySubJet_btag[subjetIdx2] >= BTagL)):
                    herPNWMid = 5
                else:
                    herPNWMid = 0

                
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

            for imode in range(0,7):  #fill the denoms into the correct ROW
                herPNWM.Fill(imode,i)
            
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

    histFile = TFile.Open(f"PNWMcomparison.root", "recreate")

    ourPNWM.Write()

    histFile.Write()
    histFile.Close()

## Read histograms from file
histFile = TFile.Open(f"PNWMcomparison.root")

PNWM = histFile.Get("ourPNWMid")

canv1 = TCanvas("c1","c1",800,600)

xlabels = ['udsc','b','W','Z', 'H', 't']
for ibin in range(1,ourPNWM.GetNbinsX()+1):
    PNWM.GetXaxis().SetBinLabel(ibin,xlabels[ibin-1])
    
ylabels = ['udsc','b','W','Z', 'H', 't']
for ibin in range(1,ourPNWM.GetNbinsY()+1):
    PNWM.GetYaxis().SetBinLabel(ibin,ylabels[ibin-1])

# PNWM.SetMinimum(0.0)
# PNWM.SetMaximum(1.0)

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
canv1.SaveAs(f"PNWMcomparison1600.png")