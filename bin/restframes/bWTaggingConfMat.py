import os, sys, math, re
from ROOT import TFile, TTree, TH1D, TH2D, TCanvas, gStyle, gPad, TLatex


dir_str = "/uscms/home/hlarson/nobackup/run3VLQ/TIMBER/"
#sample_files = ["RDF_TprimeTprime_Par-M-1300_TuneCP5_13p6TeV_amcatnlo-pythia8_2024_0.root","RDF_TprimeTprime_Par-M-1700_TuneCP5_13p6TeV_amcatnlo-pythia8_2024_0.root","RDF_TprimeTprime_Par-M-1900_TuneCP5_13p6TeV_amcatnlo-pythia8_2024_0.root"]
sample_files = ["RDF_TprimeTprime_Par-M-1300_TuneCP5_13p6TeV_amcatnlo-pythia8_2024_0.root"]
files = [dir_str + x for x in sample_files]

for k,file_str in enumerate(files):
    inFile = TFile.Open(file_str)
    mass = ((k + 1) * 2) + 1
    fname = f"pDM_confMat_1p{mass}"

    truth = TH2D("jet_truth",";tagger ID;true ID",2,0,2,2,0,2)
    bWTag = TH2D("jet_bW_vs_(H/Z)t",f";bW or (H/Z)t;true ID",2,0,2,2,0,2)

    truth.Sumw2() #Sum weights squared -> account for uncertainties. in future we divide this
    bWTag.Sumw2()

    BTagM = 0.1272
    BTagL = 0.0246

    t = inFile.Get("Events_Nominal")

    for ievent in range(t.GetEntries()):
        
        t.GetEntry(ievent)
        nJets = t.nFatJet
        i = 0
        if t.decayFinds[0] == 1: #bW
            i = 0.5
        elif t.decayFinds[0] == 5 or t.decayFinds[0] == 6: #tZbW or bWtZ OR tHbW or bWtH
            if t.decayFinds[1] == 1: #VLQ1toT = 1 -> t(Z/H)bW so VLQ1 is a top decay
                i = 1.5
            else:
                i = 0.5
        else:                #t(Z/H)
            i = 1.5
            
        for imode in range(0,3):  #fill the denoms into the correct ROW
            truth.Fill(imode,i)
            
        for ijet in range(nJets):
            if t.Isolated_AK4[ijet] == 1 and t.gcJet_BTag[ijet] == 1:
                print(f"filling bWTag 1.5, {i}")
                bWTag.Fill(1.5,i)
            else:
                print(f"filling bWTag 0.5, {i}")
                bWTag.Fill(0.5,i)
            
    print(bWTag.GetBinContent(2))
    bWTag.Divide(bWTag, truth, 1, 1, "B")
    histFile = TFile.Open(f"{fname}_L.root", "recreate")
    #bWTag.Write()
    bWTag.SetDirectory(histFile) 
    histFile.Write()
    histFile.Close()
                    
    truth.Reset()

    
## Read histograms from file
for k,f in enumerate(files):
    mass = ((k + 1) * 2) + 1
    fname = f"pDM_confMat_1p{mass}"
    histFile = TFile.Open(f"{fname}_L.root")

    #histFile.ls()
    histFile.GetListOfKeys()

    bWTag = histFile.Get("jet_bW_vs_(H/Z)t")
    if not bWTag:
        print(f"Error: bWTag was not found in {fname}!")
        continue
    
    canv1 = TCanvas("c1","c1",800,600)

    labels = ['decay to bW','decay to t(Z/H)']
    for ibin in range(1,bWTag.GetNbinsY()+1):
        bWTag.GetYaxis().SetBinLabel(ibin,labels[ibin-1])
        bWTag.GetXaxis().SetBinLabel(ibin,labels[ibin-1])

    bWTag.SetMinimum(0.0)
    bWTag.SetMaximum(1.0)

    gStyle.SetOptStat(0)
    gStyle.SetPaintTextFormat("1.2f")
    canv1.SetLeftMargin(0.15)

    bWTag.Draw("colz texte")
    latex = TLatex()
    latex.SetNDC()
    latex.SetTextSize(0.04)
    latex.SetTextAlign(11)
    latex.DrawLatex(0.10, 0.92, "#bf{Private work} (CMS simulation)")
    latex.SetTextAlign(31)
    latex.DrawLatex(0.9, 0.92, "13.6 TeV")
    gPad.Update()
    canv1.SaveAs(f"confMat/{fname}_L.png")

    
