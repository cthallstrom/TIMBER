import os, sys, math, re
from ROOT import TFile, TTree, TH1D, TH2D, TCanvas, gStyle, gPad, TLatex

readFile = True
if readFile:
    file_str = "root://cmseos.fnal.gov//store/user/lpchtop/TTBB_Jun2026_Run3//RDF_TprimeTprime_Par-M-1900_TuneCP5_13p6TeV_amcatnlo-pythia8_2024_0.root"
    inFile = TFile.Open(file_str)

    pattern = r"RDF_([TB]).*?Par-M-(\d+)"
    mass = re.search(pattern, file_str)
    name = f"{mass.group(1)}{mass.group(2)}GeV"

    truth = TH2D("jet_truth",";tagger ID;true ID",6,0,6,6,0,6)
    PNWM = TH2D("jet_PNWMid",f";{name} L PNWM ID;true ID",6,0,6,6,0,6)
    GPT = TH2D("jet_GPTid",f";{name} L GPT ID;true ID",6,0,6,6,0,6)
    GPTWM = TH2D("jet_GPTWMid",f";{name} L GPTWM ID;true ID",6,0,6,6,0,6)

    truth.Sumw2() #Sum weights squared -> account for uncertainties. in future we divide this
    PNWM.Sumw2()
    GPT.Sumw2()
    GPTWM.Sumw2()

    t = inFile.Get("Events_Nominal")

    GPTWMmin = 1000
    BTagM = 0.1272
    BTagL = 0.0246

    a = 0.5
    b = 1.85
    c = 2.8

    # for a in [h / 100.0 for h in range(30, 80, 5)]:
    #     for b in [k / 100.0 for k in range(150, 190, 5)]:
    #         for c in [l / 100.0 for l in range(250, 300, 5)]:
    #             print(f"{a}, {b}, {c}")
                
    GPTWMsum = 0
    truth.Reset()
    PNWM.Reset()
    GPT.Reset()
    GPTWM.Reset()

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

            GPTscores = [t.gcFatJet_GPT_T[ijet], t.gcFatJet_GPT_W[ijet], t.gcFatJet_GPT_ZH[ijet], t.gcFatJet_GPT_QCD[ijet]]
            GPTmaxindex = GPTscores.index(max(GPTscores))

            if GPTmaxindex == 0:
                GPTid = 6
            elif GPTmaxindex == 1:
                GPTid = 24
            elif GPTmaxindex == 2:
                if t.gcFatJet_GPT_regressedMass[ijet] > 105:
                    GPTid = 25
                else:
                    GPTid = 23
                
            elif GPTmaxindex == 3:
                subjetIdx1 = int(t.gcFatJet_subJetIdx1[ijet])
                subjetIdx2 = int(t.gcFatJet_subJetIdx2[ijet])
                if((subjetIdx1 >= 0 and t.mySubJet_btag[subjetIdx1] >= BTagL) or (subjetIdx2 >= 0 and t.mySubJet_btag[subjetIdx2] >= BTagL)):
                    GPTid = 5
                else:
                    GPTid = 0

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
                if((subjetIdx1 >= 0 and t.mySubJet_btag[subjetIdx1] >= BTagL) or (subjetIdx2 >= 0 and t.mySubJet_btag[subjetIdx2] >= BTagL)):
                    GPTWMid = 5
                else:
                    GPTWMid = 0


            # Fill truth info into all x-axis values
            if t.gcFatJet_truth[ijet] == 0:   #deciding on the truth, we can just look at the truth from our truth vector
                i = 0.5      
            elif t.gcFatJet_truth[ijet] == 5:
                i = 1.5
            elif t.gcFatJet_truth[ijet] == 24:
                i = 2.5
            elif t.gcFatJet_truth[ijet] == 23:
                i = 3.5
            elif t.gcFatJet_truth[ijet] == 25:
                i = 4.5
            elif t.gcFatJet_truth[ijet] == 6:
                i = 5.5

            for imode in range(0,7):  #fill the denoms into the correct ROW
                truth.Fill(imode,i)
            
                    
            # Fill reconstructed info into only the right x-axis value
            #taggedTjet = 1, taggedWjet = 2, untaggedTlep = 3, untaggedWlep = 4
            if PNWMid == 0:
                PNWM.Fill(0.5,i)
            elif PNWMid == 5:
                PNWM.Fill(1.5,i)
            elif PNWMid == 24:
                PNWM.Fill(2.5,i)
            elif PNWMid == 23:
                PNWM.Fill(3.5,i)
            elif PNWMid == 25:
                PNWM.Fill(4.5,i)
            elif PNWMid == 6:
                PNWM.Fill(5.5,i)
        
            if GPTid == 0:
                GPT.Fill(0.5,i)
            elif GPTid == 5:
                GPT.Fill(1.5,i)
            elif GPTid == 24:
                GPT.Fill(2.5,i)
            elif GPTid == 23:
                GPT.Fill(3.5,i)
            elif GPTid == 25:
                GPT.Fill(4.5,i)
            elif GPTid == 6:
                GPT.Fill(5.5,i)

            if GPTWMid == 0:
                GPTWM.Fill(0.5,i)
            elif GPTWMid == 5:
                GPTWM.Fill(1.5,i)
            elif GPTWMid == 24:
                GPTWM.Fill(2.5,i)
            elif GPTWMid == 23:
                GPTWM.Fill(3.5,i)
            elif GPTWMid == 25:
                GPTWM.Fill(4.5,i)
            elif GPTWMid == 6:
                GPTWM.Fill(5.5,i)
            
    PNWM.Divide(PNWM, truth, 1, 1, "B")
    GPT.Divide(GPT, truth, 1, 1, "B")
    GPTWM.Divide(GPTWM, truth, 1, 1, "B")

    for x in range(0,6):
        for y in range(0,6):
            if x != y:
                GPTWMsum += GPTWM.GetBinContent(GPTWM.FindBin(x, y)) ** 2

    GPTWMdiag = math.sqrt(GPTWMsum)

    if GPTWMdiag < GPTWMmin:
        GPTWMmin = GPTWMdiag
        abc = [a, b, c]
    print(GPTWMdiag)


    #Stop editing the indents here when switching between loop/noloop
    print(f"Min diag is: {GPTWMmin}, abc are: {abc}")



    histFile = TFile.Open(f"/uscms_data/d3/cai/run3VLQ/TIMBER/cMatrices/{name}_L.root", "recreate")

    PNWM.Write()
    GPT.Write()
    GPTWM.Write()

    histFile.Write()
    histFile.Close()

## Read histograms from file
histFile = TFile.Open(f"/uscms_data/d3/cai/run3VLQ/TIMBER/cMatrices/{name}_L.root")

PNWM = histFile.Get("jet_PNWMid")
GPT = histFile.Get("jet_GPTid")
GPTWM = histFile.Get("jet_GPTWMid")

canv1 = TCanvas("c1","c1",800,600)

xlabels = ['udsc','b','W','Z', 'H', 't']
for ibin in range(1,GPT.GetNbinsX()+1):
    GPT.GetXaxis().SetBinLabel(ibin,xlabels[ibin-1])
    PNWM.GetXaxis().SetBinLabel(ibin,xlabels[ibin-1])
    GPTWM.GetXaxis().SetBinLabel(ibin,xlabels[ibin-1])
    
ylabels = ['udsc','b','W','Z', 'H', 't']
for ibin in range(1,GPT.GetNbinsY()+1):
    GPT.GetYaxis().SetBinLabel(ibin,ylabels[ibin-1])
    PNWM.GetYaxis().SetBinLabel(ibin,ylabels[ibin-1])
    GPTWM.GetYaxis().SetBinLabel(ibin,ylabels[ibin-1])

PNWM.SetMinimum(0.0)
PNWM.SetMaximum(1.0)
GPT.SetMinimum(0.0)
GPT.SetMaximum(1.0)
GPTWM.SetMinimum(0.0)
GPTWM.SetMaximum(1.0)

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
canv1.SaveAs(f"/uscms_data/d3/cai/run3VLQ/TIMBER/cMatrices/{name}_L_PNWM.png")

GPT.Draw("colz texte")
latex = TLatex()
latex.SetNDC()
latex.SetTextSize(0.04)
latex.SetTextAlign(11)
latex.DrawLatex(0.10, 0.92, "#bf{Private work} (CMS simulation)")
latex.SetTextAlign(31)
latex.DrawLatex(0.9, 0.92, "13.6 TeV")
gPad.Update()
canv1.SaveAs(f"/uscms_data/d3/cai/run3VLQ/TIMBER/cMatrices/{name}_L_GPT.png")

GPTWM.Draw("colz texte")
latex = TLatex()
latex.SetNDC()
latex.SetTextSize(0.04)
latex.SetTextAlign(11)
latex.DrawLatex(0.10, 0.92, "#bf{Private work} (CMS simulation)")
latex.SetTextAlign(31)
latex.DrawLatex(0.9, 0.92, "13.6 TeV")
gPad.Update()
canv1.SaveAs(f"/uscms_data/d3/cai/run3VLQ/TIMBER/cMatrices/{name}_L_GPTWM.png")
