// processDecayTree(), matchJets()
// These two functions help to differentiate between the bW and (H/Z)t trees
#include <iostream>

RVec<double> processDecayTree(Tprime_RestFrames_Container_W * W_rfc, Tprime_RestFrames_Container_t * t_rfc, int thread_index, float lepton_pt, float lepton_eta, float lepton_phi, float lepton_mass, RVec<float> fatjet_pt, RVec<float> fatjet_eta, RVec<float> fatjet_phi, RVec<float> fatjet_mass, float met_pt, float met_phi, RVec<float> jet_pt, RVec<float> jet_eta, RVec<float> jet_phi, RVec<float> jet_mass, RVec<float> jet_BTag, RVec<float> isoAK4, char decayMode) {
  RVec<TLorentzVector> jets;
  int i = 0; 

  // Make an RVec of valid jets for the possible b.
  TLorentzVector jet;
  for (; i < isoAK4.size(); i++) {
    //  stand alone         b-tagged
    if (decayMode == 1 && jet_BTag[i] == 1) {
      jet.SetPtEtaPhiM(jet_pt[i], jet_eta[i], jet_phi[i], jet_mass[i]);
      jets.push_back(jet);
    } 
  }   

  //  std::cout << "-------------------------------------------" << std::endl;
  RVec<double> result;
  if (jets.size() == 0) { // analyze bW tree
    result = W_rfc->return_W_doubles(thread_index, lepton_pt, lepton_eta, lepton_phi, lepton_mass, fatjet_pt, fatjet_eta, fatjet_phi, fatjet_mass, met_pt, met_phi);
    result.push_back(0.0); // 0 is for W tree
  } else { // analyze (H/Z)t tree
    result = t_rfc->return_t_doubles(thread_index, lepton_pt, lepton_eta, lepton_phi, lepton_mass, fatjet_pt, fatjet_eta, fatjet_phi, fatjet_mass, met_pt, met_phi, jets);
    result.push_back(1.0); // 1 is for t tree
  }
  return result;
}


RVec<int> matchJets(double J0_E, double VLQ2_E, RVec<float> fatjet_pt, RVec<float> fatjet_eta, RVec<float> fatjet_phi, RVec<float> fatjet_mass) {
  int j0_idx = -1;
  int vlq21_idx = -1;
  int vlq22_idx = -1;
  TLorentzVector fj;
  TLorentzVector fj_2;
  int numOfLoops = 3;
  
  for (int i; i < numOfLoops; i++) {
    fj.SetPtEtaPhiM(fatjet_pt[i],fatjet_eta[i],fatjet_phi[i],fatjet_mass[i]);
    if (J0_E == fj.E()) { j0_idx = i; }
    for (int k; k < numOfLoops; k++) {
      fj_2.SetPtEtaPhiM(fatjet_pt[k],fatjet_eta[k],fatjet_phi[k],fatjet_mass[k]);
      if (VLQ2_E == fj.E() + fj_2.E()) {
	if (fj.M() > fj_2.M()) {
	  vlq21_idx = i;
	  vlq22_idx = k;
	}
      }
    }
  }
  RVec<int> matched_idx = {j0_idx, vlq21_idx, vlq22_idx};
  return matched_idx;
}
