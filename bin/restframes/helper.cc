// R_processDecayTree(), R_matchJets(), R_decays()
// These two functions help to differentiate between the bW and (H/Z)t trees
#include <iostream>

RVec<double> R_processDecayTree(Tprime_RestFrames_Container_W * W_rfc, Tprime_RestFrames_Container_t * t_rfc, int thread_index, float lepton_pt, float lepton_eta, float lepton_phi, float lepton_mass, RVec<float> fatjet_pt, RVec<float> fatjet_eta, RVec<float> fatjet_phi, RVec<float> fatjet_mass, float met_pt, float met_phi, RVec<TLorentzVector> bjets, TLorentzVector minMlb_lv, int decayMode, int J0_idx, int VLQ1_idx, int VLQ2_idx) {

  RVec<double> result;
  if (decayMode == 0) { // analyze bW tree
    result = W_rfc->return_W_doubles(thread_index, lepton_pt, lepton_eta, lepton_phi, lepton_mass, fatjet_pt, fatjet_eta, fatjet_phi, fatjet_mass, met_pt, met_phi);//, J0_idx, VLQ1_idx, VLQ2_idx);
    result.push_back(0.0); // 0 is for W tree
  } else { // analyze (H/Z)t tree
    result = t_rfc->return_t_doubles(thread_index, lepton_pt, lepton_eta, lepton_phi, lepton_mass, fatjet_pt, fatjet_eta, fatjet_phi, fatjet_mass, met_pt, met_phi, bjets, minMlb_lv);//, J0_idx, VLQ1_idx, VLQ2_idx);
    result.push_back(1.0); // 1 is for t tree
  }
  return result;
}


RVec<int> R_matchJets(double J0_E, double VLQ2_E, RVec<TLorentzVector> fj) {
  int j0_idx = -1;
  int vlq21_idx = -1;
  int vlq22_idx = -1;
  int numOfLoops = 3;
  double diff = 1000;
  double diff_V = 1000;
  // std::cout << "J0 E = " << J0_E << std::endl;
  // std::cout << "VLQ2 E = " << VLQ2_E << std::endl;

  // std::cout << "fj[0] E = " << fj[0].E() << std::endl;
  // std::cout << "fj[1] E = " << fj[1].E() << std::endl;
  // std::cout << "fj[2] E = " << fj[2].E() << std::endl;

  double d = 0.0001;
  
  if(abs(J0_E - fj[0].E()) < d) {
    j0_idx = 0;
    if (fj[1].M() > fj[2].M()) {
      vlq21_idx = 1;
      vlq22_idx = 2;
    } else {
      vlq21_idx = 2;
      vlq22_idx = 1;
    }
    }
  else if(abs(J0_E - fj[1].E()) < d) {
    j0_idx = 1;
    if (fj[0].M() > fj[2].M()) {
      vlq21_idx = 0;
      vlq22_idx = 2;
    } else {
      vlq21_idx = 2;
      vlq22_idx = 0;
    }
  }
  else if(abs(J0_E - fj[2].E()) < d) {
    j0_idx = 2;
    if (fj[0].M() > fj[1].M()) {
      vlq21_idx = 0;
      vlq22_idx = 1;
    } else {
      vlq21_idx = 1;
      vlq22_idx = 0;
    }
  }
    
  RVec<int> matched_idx = {j0_idx, vlq21_idx, vlq22_idx};

  return matched_idx;
}


RVec<int> R_decays(int lepton_source, int J0_idx, int VLQ21_idx, int VLQ22_idx, RVec<int> PNWMtags) {
  if (J0_idx == -1 || VLQ21_idx == -1 || VLQ22_idx == -1) {
    return {-1, 0};
  }
  
  // PNWM_id key Tp(Bp):                 |    PNWM_tags key
  //  0 -> QCD(QCD)     1 -> bWbW(tWtW)  |    0 -> QCD     23 -> Z   
  //  2 -> tZtZ(bZbZ)   3 -> tHtH(bHbH)  |    5 -> b       24 -> W
  //  4 -> tZtH(bZbH)   5 -> tZbW(bZtW)  |    6 -> t       25 -> H
  //  6 -> tHbW(bHtW)   7 -> tH(bH)      |
  //  8 -> tZ(bZ)       9 -> bW(tW)      |
  
  int mode = 0;
  int Bmode = 0;
  
  if (lepton_source == 0) { //W? ??
    if (PNWMtags.at(J0_idx) == 5) { //bW ??
      if(PNWMtags.at(VLQ21_idx) == 6 || PNWMtags.at(VLQ22_idx) == 6) { //bW t?
	      if(PNWMtags.at(VLQ22_idx) == 25 || PNWMtags.at(VLQ22_idx) == 25) mode = 6; //bW tH
	      if(PNWMtags.at(VLQ22_idx) == 23 || PNWMtags.at(VLQ22_idx) == 23) mode = 5; //bW tZ
      }
      else if (PNWMtags.at(VLQ21_idx) == 5 || PNWMtags.at(VLQ22_idx) == 5) { //bW b?
	      if (PNWMtags.at(VLQ21_idx) == 24 || PNWMtags.at(VLQ22_idx) == 24) mode = 1; //bW bW
      }
    }
    else if (PNWMtags.at(J0_idx) == 6) { //tW ??
      if (PNWMtags.at(VLQ21_idx) == 6 || PNWMtags.at(VLQ22_idx) == 6) { //tW t?
	      if (PNWMtags.at(VLQ21_idx) == 24 || PNWMtags.at(VLQ22_idx) == 24) Bmode = 1; //tW tW
      }
      else if (PNWMtags.at(VLQ21_idx) == 5 || PNWMtags.at(VLQ22_idx) == 5) { //tW b?
	      if (PNWMtags.at(VLQ21_idx) == 23 || PNWMtags.at(VLQ22_idx) == 23) Bmode = 5; //tW bZ
	      if (PNWMtags.at(VLQ21_idx) == 25 || PNWMtags.at(VLQ22_idx) == 25) Bmode = 6; //tW bH
      }
    }
  }
  
  else if (lepton_source == 1) { //t? ??
    if (PNWMtags.at(J0_idx) == 23) { //tZ ??
      if(PNWMtags.at(VLQ21_idx) == 6 || PNWMtags.at(VLQ22_idx) == 6) { //tZ t?
	      if(PNWMtags.at(VLQ22_idx) == 25 || PNWMtags.at(VLQ22_idx) == 25) mode = 4; //tZ tH
	      if(PNWMtags.at(VLQ22_idx) == 23 || PNWMtags.at(VLQ22_idx) == 23) mode = 2; //tZ tZ
      }
      else if (PNWMtags.at(VLQ21_idx) == 5 || PNWMtags.at(VLQ22_idx) == 5) { //tZ b?
	      if (PNWMtags.at(VLQ21_idx) == 24 || PNWMtags.at(VLQ22_idx) == 24) mode = 5; //tZ bW
      }
    }
    else if (PNWMtags.at(J0_idx) == 25) { //tH ??
      if(PNWMtags.at(VLQ21_idx) == 6 || PNWMtags.at(VLQ22_idx) == 6) { //tH t?
        if(PNWMtags.at(VLQ22_idx) == 23 || PNWMtags.at(VLQ22_idx) == 23) mode = 4; //tH tZ
        if(PNWMtags.at(VLQ22_idx) == 25 || PNWMtags.at(VLQ22_idx) == 25) mode = 3; //tH tH
      }
      else if (PNWMtags.at(VLQ21_idx) == 5 || PNWMtags.at(VLQ22_idx) == 5) { //tH b?
	      if (PNWMtags.at(VLQ21_idx) == 24 || PNWMtags.at(VLQ22_idx) == 24) mode = 5; //tH bW
      }
    }
    else if (PNWMtags.at(J0_idx) == 23) { //tW ??
      if (PNWMtags.at(VLQ21_idx) == 6 || PNWMtags.at(VLQ22_idx) == 6) { //tW t?
	      if (PNWMtags.at(VLQ21_idx) == 24 || PNWMtags.at(VLQ22_idx) == 24) Bmode = 1; //tW tW
      }
      else if (PNWMtags.at(VLQ21_idx) == 5 || PNWMtags.at(VLQ22_idx) == 5) { //tW b?
        if (PNWMtags.at(VLQ21_idx) == 23 || PNWMtags.at(VLQ22_idx) == 23) Bmode = 5; //tW bZ
        if (PNWMtags.at(VLQ21_idx) == 25 || PNWMtags.at(VLQ22_idx) == 25) Bmode = 6; //tW bH
      }
      else mode = 9;
    }
  }

  if (PNWMtags.at(J0_idx) != 25 && PNWMtags.at(J0_idx) != 24 && PNWMtags.at(J0_idx) != 23 && PNWMtags.at(J0_idx) != 5) {//AK8 for lepVLQ doesnt match decay modes -> medium purity
    if(PNWMtags.at(VLQ21_idx) == 5 || PNWMtags.at(VLQ22_idx) == 5) { //b?
      if (PNWMtags.at(VLQ21_idx) == 24 || PNWMtags.at(VLQ22_idx) == 24) mode = 9; //medium purity, bW
      if (PNWMtags.at(VLQ21_idx) == 23 || PNWMtags.at(VLQ22_idx) == 23) { //medium purity, bZ
	Bmode = 8; 
      }
      if (PNWMtags.at(VLQ21_idx) == 25 || PNWMtags.at(VLQ22_idx) == 25) { //medium purity, bH
	Bmode = 7;
      }
    } else if(PNWMtags.at(VLQ21_idx) == 6 || PNWMtags.at(VLQ22_idx) == 6) { //t?
      if (PNWMtags.at(VLQ21_idx) == 24 || PNWMtags.at(VLQ22_idx) == 24) {//medium purity, tW
	 Bmode = 9;
      }
      if (PNWMtags.at(VLQ21_idx) == 23 || PNWMtags.at(VLQ22_idx) == 23) mode = 8; //medium purity, tZ
      if (PNWMtags.at(VLQ21_idx) == 25 || PNWMtags.at(VLQ22_idx) == 25) mode = 7; //medium purity, tH
    }   
  }
  return {mode, Bmode}; //first index what are the tags, but only for tprime options, second is for bprime options
}

