import h5py, numpy as np
from ROOT import TFile, TTree, TH1D, TH2D, TCanvas, gStyle, gPad, TLatex

file_str = "RDF_TprimeTprime_Par-M-1900_TuneCP5_13p6TeV_amcatnlo-pythia8_2024_0.root"
inFile = TFile.Open(file_str)

t = inFile.Get("Events_Nominal")

final_pt = np.zeros((t.GetEntries(), 10), dtype = float)
final_pt = np.zeros((t.GetEntries(), 10), dtype = float)

for event in range(t.GetEntries()):
    t.GetEntry(event)

    padded_mass = np.full(10, 0)
    padded_pt = np.full(10, 0)
    padded_eta = np.full(10, 0)
    padded_sin_phi = np.full(10, 0)
    padded_cos_phi = np.full(10, 0)
    padded_btag = np.full(10, 0)

    mass = t.gcFatJet_mass
    pt = t.gcFatJet_pt
    eta = t.gcFatJet_eta

    padded_pt[:len(pt)] = pt

    final_pt[event, :] = padded_pt

with h5py.File("Test2h5.h5", 'w') as f:
    f.create_dataset('gcFatJet_pt', data = final_pt)




