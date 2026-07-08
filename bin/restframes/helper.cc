// processDecayTree(), matchJets()
// These two functions help to differentiate between the bW and (H/Z)t trees
#include <iostream>

RVec<double> processDecayTree(Tprime_RestFrames_Container_W * W_rfc, Tprime_RestFrames_Container_t * t_rfc, int thread_index, float lepton_pt, float lepton_eta, float lepton_phi, float lepton_mass, RVec<float> fatjet_pt, RVec<float> fatjet_eta, RVec<float> fatjet_phi, RVec<float> fatjet_mass, float met_pt, float met_phi, RVec<TLorentzVector> bjets, TLorentzVector minMlb_lv, int decayMode) {
  RVec<TLorentzVector> jets;
  int i = 0; 

  // Make an RVec of valid jets for the possible b.
  // for (; i < isoAK4.size(); i++) {
  //   //  stand alone         b-tagged
  //   if (jet_BTag[i] == 1) {
  //     jets.push_back(bjets[i]);
  //   } 
  // }   

  //  std::cout << "-------------------------------------------" << std::endl;
  RVec<double> result;
  if (decayMode == 0) { // analyze bW tree
    result = W_rfc->return_W_doubles(thread_index, lepton_pt, lepton_eta, lepton_phi, lepton_mass, fatjet_pt, fatjet_eta, fatjet_phi, fatjet_mass, met_pt, met_phi);
    result.push_back(0.0); // 0 is for W tree
  } else { // analyze (H/Z)t tree
    result = t_rfc->return_t_doubles(thread_index, lepton_pt, lepton_eta, lepton_phi, lepton_mass, fatjet_pt, fatjet_eta, fatjet_phi, fatjet_mass, met_pt, met_phi, bjets, minMlb_lv);
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
  double diff = 1000;
  double diff_V = 1000;
 
  for (int i = 0; i < numOfLoops; i++) {
    fj.SetPtEtaPhiM(fatjet_pt[i],fatjet_eta[i],fatjet_phi[i],fatjet_mass[i]);
    if(J0_E == fj.E()) {
      j0_idx = i;
    }

    for (int k = 0; k < numOfLoops; k++) {
      fj_2.SetPtEtaPhiM(fatjet_pt[k],fatjet_eta[k],fatjet_phi[k],fatjet_mass[k]);
      double V_E = abs(VLQ2_E - fj.E() - fj_2.E());
      if(VLQ2_E == V_E) {
	if (fj.M() > fj_2.M()) {
	  vlq21_idx = i;
	  vlq22_idx = k;
	} else {
	  vlq21_idx = k;
	  vlq22_idx = i;
	}
      }
    }
  }
  
  RVec<int> matched_idx = {j0_idx, vlq21_idx, vlq22_idx};
  return matched_idx;
}


int R_decayTypes(int lepton_source, int J0_idx, int VLQ21_idx, int VLQ22_idx, RVec<int> PNWMtags) {
  // PNWM_id key:                      |       PNWM_tags key
  //  0 -> QCD         1 -> bWbW       |        0 -> QCD     23 -> Z   
  //  2 -> tZtZ        3 -> tHtH       |        5 -> b       24 -> W
  //  4 -> tZtH        5 -> tZbW       |        6 -> t       25 -> H
  //  6 -> tHbW        7 -> tH         |
  //  8 -> tZ          9 -> bW         |

  int PNWM_ID = 0;
  
  if (lepton_source == 0 && PNWMtags.at(J0_idx) == 5) { //bW ??  
    if (PNWMtags.at(VLQ21_idx) == 0 || PNWMtags.at(VLQ22_idx) == 0) PNWM_ID = 9; //medium purity, bW
    
    else if(PNWMtags.at(VLQ21_idx) == 6 || PNWMtags.at(VLQ22_idx) == 6) { //bW t?
      if(PNWMtags.at(VLQ22_idx) == 25 || PNWMtags.at(VLQ22_idx) == 25) PNWM_ID = 6; //bW tH
      if(PNWMtags.at(VLQ22_idx) == 23 || PNWMtags.at(VLQ22_idx) == 23) PNWM_ID = 5; //bW tZ
    }
    else if ((PNWMtags.at(VLQ21_idx) == 5 || PNWMtags.at(VLQ22_idx) == 5) && PNWMtags.at(VLQ21_idx) == 24 || PNWMtags.at(VLQ22_idx) == 24) PNWM_ID = 1; //bW bW
  }

  else if (lepton_source == 1) { //t? ??
    if (PNWMtags.at(J0_idx) == 23) { //tZ ??
      if (PNWMtags.at(VLQ21_idx) == 0 || PNWMtags.at(VLQ22_idx) == 0) PNWM_ID = 8; //medium purity, tZ
    
      else if(PNWMtags.at(VLQ21_idx) == 6 || PNWMtags.at(VLQ22_idx) == 6) { //tZ t?
	if(PNWMtags.at(VLQ22_idx) == 25 || PNWMtags.at(VLQ22_idx) == 25) PNWM_ID = 4; //tZ tH
	if(PNWMtags.at(VLQ22_idx) == 23 || PNWMtags.at(VLQ22_idx) == 23) PNWM_ID = 2; //tZ tZ
      }
      else if ((PNWMtags.at(VLQ21_idx) == 5 || PNWMtags.at(VLQ22_idx) == 5) && PNWMtags.at(VLQ21_idx) == 24 || PNWMtags.at(VLQ22_idx) == 24) PNWM_ID = 5; //tZ bW
    }
    else if (PNWMtags.at(J0_idx) == 25) { //tH ??
      if (PNWMtags.at(VLQ21_idx) == 0 || PNWMtags.at(VLQ22_idx) == 0) PNWM_ID = 7; //medium purity, tH
    
      else if(PNWMtags.at(VLQ21_idx) == 6 || PNWMtags.at(VLQ22_idx) == 6) { //tH t?
	if(PNWMtags.at(VLQ22_idx) == 25 || PNWMtags.at(VLQ22_idx) == 25) PNWM_ID = 4; //tH tZ
	if(PNWMtags.at(VLQ22_idx) == 23 || PNWMtags.at(VLQ22_idx) == 23) PNWM_ID = 3; //tH tH
      }
    }
  }
  else {
    std::cout << "encountered an event that didnt have a leptonic particle??" << std::endl;
}

  	
