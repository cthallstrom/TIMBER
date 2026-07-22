import h5py, numpy as np
from ROOT import TFile, TTree, TH1D, TH2D, TCanvas, gStyle, gPad, TLatex

file_str = "RDF_TprimeTprime_Par-M-1200_TuneCP5_13p6TeV_amcatnlo-pythia8_2024_0.root"
inFile = TFile.Open(file_str)

t = inFile.Get("Events_Nominal")

n_events = t.GetEntries()
n_Ak8 = 10
n_Ak4 = 10
n_features = n_Ak4 + n_Ak8 + 1

# Initialize jet and lepton arrays
mask_all = np.zeros((n_events, n_features))
mass_all = np.zeros((n_events, n_features))
pt_all = np.zeros((n_events, n_features))
eta_all = np.zeros((n_events, n_features))
cos_phi_all = np.zeros((n_events, n_features))
sin_phi_all = np.zeros((n_events, n_features))
btag_all = np.zeros((n_events, n_features))
leptag_all = np.zeros((n_events, n_features))

# Initialize MET arrays
met = np.zeros(n_events)
met_cos_phi = np.zeros(n_events)
met_sin_phi = np.zeros(n_events)


for event in range(t.GetEntries()):
    t.GetEntry(event)

    # Initialize padded fatjet arrays
    fatjet_padded_mass = np.full(n_Ak8, 0.0)
    fatjet_padded_pt = np.full(n_Ak8, 0.0)
    fatjet_padded_eta = np.full(n_Ak8, 0.0)
    fatjet_padded_sin_phi = np.full(n_Ak8, 0.0)
    fatjet_padded_cos_phi = np.full(n_Ak8, 0.0)
    fatjet_padded_btag = np.full(n_Ak8, 0.0)
    fatjet_padded_leptag = np.full(n_Ak8, 0.0)

    # Load fatjets from ROOT
    fatjet_mass = t.gcFatJet_mass
    fatjet_pt = t.gcFatJet_pt
    fatjet_eta = t.gcFatJet_eta
    fatjet_sin_phi = t.gcFatJet_sin_phi
    fatjet_cos_phi = t.gcFatJet_cos_phi

    # Pad the arrays
    fatjet_padded_mass[:len(fatjet_mass)] = fatjet_mass
    fatjet_padded_pt[:len(fatjet_pt)] = fatjet_pt
    fatjet_padded_eta[:len(fatjet_eta)] = fatjet_eta
    fatjet_padded_sin_phi[:len(fatjet_sin_phi)] = fatjet_sin_phi
    fatjet_padded_cos_phi[:len(fatjet_cos_phi)] = fatjet_cos_phi

    # Initialize padded ak4 jet arrays
    jet_padded_mass = np.full(n_Ak4, 0.0)
    jet_padded_pt = np.full(n_Ak4, 0.0)
    jet_padded_eta = np.full(n_Ak4, 0.0)
    jet_padded_sin_phi = np.full(n_Ak4, 0.0)
    jet_padded_cos_phi = np.full(n_Ak4, 0.0)
    jet_padded_btag = np.full(n_Ak4, 0.0)

    btag_mask = t.gcJet_BTagM

    # Get the ROOT branches and filter by btag
    bjets_mass = t.gcJet_mass[btag_mask]
    bjets_pt = t.gcJet_pt[btag_mask]
    bjets_eta = t.gcJet_eta[btag_mask]
    bjets_sin_phi = t.gcJet_sin_phi[btag_mask]
    bjets_cos_phi = t.gcJet_cos_phi[btag_mask]
    bjets_btag = t.gcJet_BTagM[btag_mask]

    # Fill the padded arrays with the filtered b-jets
    jet_padded_mass[:len(bjets_mass)] = bjets_mass
    jet_padded_pt[:len(bjets_pt)] = bjets_pt
    jet_padded_eta[:len(bjets_eta)] = bjets_eta
    jet_padded_sin_phi[:len(bjets_sin_phi)] = bjets_sin_phi
    jet_padded_cos_phi[:len(bjets_cos_phi)] = bjets_cos_phi
    jet_padded_btag[:len(bjets_btag)] = bjets_btag

    # Concatenate the arrays
    mass = np.concatenate(([t.lepton_mass], fatjet_padded_mass, jet_padded_mass))
    pt = np.concatenate(([t.lepton_pt], fatjet_padded_pt, jet_padded_pt))
    eta = np.concatenate(([t.lepton_eta], fatjet_padded_eta, jet_padded_eta))
    sin_phi = np.concatenate(([t.lepton_sin_phi], fatjet_padded_sin_phi, jet_padded_sin_phi))
    cos_phi = np.concatenate(([t.lepton_cos_phi], fatjet_padded_cos_phi, jet_padded_cos_phi))
    btag = np.concatenate(([0.0], np.full(n_Ak8, 0.0), jet_padded_btag))
    leptag = np.concatenate(([1.0], np.full(n_Ak8, 0.0), np.full(n_Ak4, 0.0)))

    # Append to 2d array
    mass_all[event] = mass
    pt_all[event] = pt
    eta_all[event] = eta
    cos_phi_all[event] = cos_phi
    sin_phi_all[event] = sin_phi
    btag_all[event] = btag
    leptag_all[event] = leptag

    # Fill MASK array
    mask_all = (mass_all != 0) | (leptag_all != 0) | (btag_all != 0)
    
    # Append the MET values
    met[event] = t.corrMET_pt
    met_sin_phi[event] = t.corrMET_sin_phi
    met_cos_phi[event] = t.corrMET_cos_phi

                
with h5py.File("NowwMET.h5", 'w') as f:
    Inputs = f.create_group('INPUTS')
    Momenta = Inputs.create_group('Momenta')
    ds_mask = Momenta.create_dataset('MASK', data=mask_all)
    ds_mass = Momenta.create_dataset('mass', data=mass_all)
    ds_pt = Momenta.create_dataset('pt', data=pt_all)
    ds_eta = Momenta.create_dataset('eta', data=eta_all)
    ds_cos_phi = Momenta.create_dataset('cos_phi', data=cos_phi_all)
    ds_sin_phi = Momenta.create_dataset('sin_phi', data=sin_phi_all)
    ds_btag = Momenta.create_dataset('btag', data=btag_all)
    ds_leptag = Momenta.create_dataset('leptag', data=leptag_all)

    Met = Inputs.create_group('MET')
    ds_met = Met.create_dataset('met', data=met)
    ds_met_cos_phi = Met.create_dataset('cos_phi', data=met_cos_phi)
    ds_met_sin_phi = Met.create_dataset('sin_phi', data=met_sin_phi)