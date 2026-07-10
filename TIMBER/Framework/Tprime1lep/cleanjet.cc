
// Methods in this file:
// assign_leps(C), cleanJets()

// --------------------------------------------------------
//       JET CLEANING FXN
// --------------------------------------------------------

using namespace std;
using namespace ROOT::VecOps;

//  correction::CompoundCorrection::Ref ak4corr;
//  correction::Correction::Ref ak4corrUnc;
//  correction::Correction::Ref ak4ptres;
//  correction::Correction::Ref ak4jer;

// Commented Method Only
    
// ---- Assign Leptons Function ----
RVec<float> assign_leps(bool isMu, bool isEl, RVec<int> &TPassMu, RVec<int> &TPassEl, RVec<float> &Muon_pt, RVec<float> &Muon_eta, RVec<float> &Muon_phi, RVec<float> &Muon_mass, RVec<float> &Muon_miniPFRelIso_all, RVec<float> &Electron_pt, RVec<float> &Electron_eta, RVec<float> &Electron_phi, RVec<float> &Electron_mass, RVec<float> &Electron_miniPFRelIso_all)
{

  float lep_pt = -9;
  float lep_eta = -9;
  float lep_phi = -9; 
  float lep_mass = -9;
  float lep_miniIso = -9;

  if(isMu){
    for(unsigned int imu=0; imu < Muon_pt.size(); imu++) {
      if(TPassMu.at(imu) == 1){
       if (lep_pt > -1) cout << "Problem: found two muons with TPassMu = 1" << endl;
      lep_pt = Muon_pt.at(imu);
      lep_eta = Muon_eta.at(imu);
      lep_phi = Muon_phi.at(imu);
       lep_mass = Muon_mass.at(imu);
       lep_miniIso = Muon_miniPFRelIso_all.at(imu);
      }
    }
  }else if(isEl){
    for(unsigned int iel=0; iel < Electron_pt.size(); iel++) {
      if(TPassEl.at(iel) == 1){
       if (lep_pt > -1) cout << "Problem: found two electrons with TPassEl = 1" << endl;
       lep_pt = Electron_pt.at(iel);
       lep_eta = Electron_eta.at(iel);
       lep_phi = Electron_phi.at(iel);
       lep_mass = Electron_mass.at(iel);
       lep_miniIso = Electron_miniPFRelIso_all.at(iel);
      }
    }
  }
  
  RVec<float> lepVec = {lep_pt,lep_eta,lep_phi,lep_mass,lep_miniIso};
  return lepVec;
};

// ---- Clean Jets MC Function ----
RVec<RVec<float>> cleanJetsMC (const bool &debug, const string &campaign, const string &jesvar, 
 correction::CompoundCorrection::Ref& ak4corr, correction::Correction::Ref& ak4corrL1, correction::Correction::Ref& ak4corrUnc, correction::Correction::Ref& ak4ptres, correction::Correction::Ref& ak4jer,
 correction::CompoundCorrection::Ref& ak8corr, correction::Correction::Ref& ak8corrUnc, 
 const RVec<TLorentzVector> &jt_p4, const RVec<float> &jt_rf, const RVec<float> &jt_murf, const RVec<float> &jt_area, const RVec<float> &jt_em, const RVec<int> &jt_id, 
 const RVec<TLorentzVector> &genjt_p4, const RVec<int> &jt_genidx, const RVec<TLorentzVector> &mu_p4, const RVec<int> mu_jetid, 
 const RVec<TLorentzVector> &el_p4, const RVec<int> &el_jetid, const float &rho, const float &met, const float &phi) 
{
  if (met == 0 && debug) cout << "---------------------------------------------------------------\n";
  
  RVec<float> cleanJetPt(jt_p4.size()), cleanJetEta(jt_p4.size()), cleanJetPhi(jt_p4.size()), cleanJetMass(jt_p4.size());//, rawfact(jt_p4.size());
  
  string jervar = "nom";
  float jesuncmult = 0;
  if (jesvar == "JERup") jervar = "up";
  else if (jesvar == "JERdn") jervar = "down";
  else if (jesvar == "JECup") jesuncmult = 1.0;
  else if (jesvar == "JECdn") jesuncmult = -1.0;
  
  correction::CompoundCorrection::Ref jescorr;
  correction::Correction::Ref jescorrUnc;
  float drmax = 0.2;
  if (ROOT::VecOps::Mean(jt_area) < 1.0) {jescorr = ak4corr; jescorrUnc = ak4corrUnc;}
  else {drmax = 0.4; jescorr = ak8corr; jescorrUnc = ak8corrUnc;}    
  
  float metx = met*cos(phi);
  float mety = met*sin(phi);
  //if (met > 0 && debug) std::cout<< "Incoming met = " << met << ", phi = " << phi << std::endl;
  
  for (unsigned int ijet = 0; ijet < jt_p4.size(); ijet++) {
    if (met == 0 && debug) std::cout<< "Incoming jet, pt = " << jt_p4[ijet].Pt() << ", phi = " << jt_p4[ijet].Phi() << std::endl;
    TLorentzVector jet = jt_p4[ijet];
    int jetid = jt_id[ijet];   
    float rf = jt_rf[ijet];
    
    if(ROOT::VecOps::Mean(jt_area) < 1.0 && met == 0){ // only clean leptons out of AK4 jets (AK8 will require DR > 0.8 from lepton)
      for (unsigned int imu = 0; imu < mu_p4.size(); imu++){
	if (mu_jetid[imu] != ijet) continue;                      // only consider muons matched to this jet
	if (jetid < 2 || jet.DeltaR(mu_p4[imu]) > 0.4) continue; // bad jet, or too far from muon
	jet *= (1 - rf);                                         // first undo the JEC
	jet -= mu_p4[imu];                                       // subtract muon if it's sensible
	rf = 0;                                                  // indicate that this is the raw jet
      }
      for (unsigned int iel = 0; iel < el_p4.size(); iel++){     // same for electrons
	if (el_jetid[iel] != ijet) continue;
	if (jetid < 2 || jet.DeltaR(el_p4[iel]) > 0.4) continue;   
	jet *= (1 - rf); 
	jet -= el_p4[iel]; 
	rf = 0; 
      }
    }
    if (met == 0 && debug) std::cout<< "Post Lepton jet, pt = " << jet.Pt() << ", phi = " << jet.Phi() << std::endl;
    
    float jes = 1.0; float jesL1 = 1.0; float jer = 1.0; float unc = 1.0;
    jet = jet * (1 - rf);                                                         // rf = 0 if JEC undone above
    
    if (met == 0 && debug) std::cout<< "Print 3 jet, pt = " << jet.Pt() << ", phi = " << jet.Phi() << std::endl;
    
    if (met > 0 && jt_em[ijet] > 0.9) continue;                                    // not these jets for MET 
    if (met > 0) jet *= (1 - jt_murf[ijet]);                                       // further correct raw to muon-substracted raw for T1.
    float rawpt = jet.Pt();
    
    if (campaign == "2023BPix" || campaign == "2024" || campaign == "2025") {
      jes = jescorr->evaluate({jt_area[ijet],jet.Eta(),jet.Phi(),rawpt,rho}); // Data & MC get jes for 2023BPix
    }
    else {
      jes = jescorr->evaluate({jt_area[ijet],jet.Eta(),rawpt,rho}); // Data & MC get jes for other campaigns
    }
    if (met > 0) jesL1 = ak4corrL1->evaluate({jt_area[ijet],jet.Eta(),rawpt,rho}); // L1-only jes for MET T1
    
    // ----- MC specific: ----- 
    float res = ak4ptres->evaluate({jet.Eta(),rawpt*jes,rho});
    float sf = ak4jer->evaluate({jet.Eta(),rawpt*jes});
    bool smeared = false;                                                       // MC only gets a JER smear, one of 2 methods below:
    if(jt_genidx[ijet] > -1 && genjt_p4[jt_genidx[ijet]].Pt() > 0){   
      double dPt = fabs(genjt_p4[jt_genidx[ijet]].Pt() - rawpt*jes);
      double dR = genjt_p4[jt_genidx[ijet]].DeltaR(jet);
      if(dR < drmax && dPt < 3*rawpt*jes*res){
        jer = max(0.0, 1.0 + (sf - 1.0)*(rawpt*jes - genjt_p4[jt_genidx[ijet]].Pt())/(rawpt*jes));
        smeared = true;
      }
    }
    if (!smeared) {
      TRandom3 rand(abs(static_cast<int>(jet.Phi()*1e4)));
      jer = max(0.0, 1.0 + rand.Gaus(0, res)*sqrt(max(0.0, sf*sf - 1.0)));
    }
    unc = 1.0 + jesuncmult*(jescorrUnc->evaluate({jet.Eta(),rawpt*jes*jer}));   // MC gets JEC unc
    // -----
    
    TLorentzVector jetL1 = jet*jesL1*jer*unc;
    jet = jet*jes*jer*unc;                                                        // evals to jes*1 for data.
    
    if (met == 0 && debug) std::cout<< "Print last jet, pt = " << jet.Pt() << ", phi = " << jet.Phi() << std::endl;
    
    rf = 1.0 - 1.0/(jes*jer*unc); 
    if (jet.Pt() > 15) {
      metx += (jetL1 - jet).Px();
      mety += (jetL1 - jet).Py();
    }
    
    cleanJetPt[ijet] = jet.Pt();
    cleanJetEta[ijet] = jet.Eta();
    cleanJetPhi[ijet] = jet.Phi();
    cleanJetMass[ijet] = jet.M();
  }
  
  TVector2 corrmet(metx,mety);
  RVec<float> corrmets = {float(corrmet.Mod()),float(TVector2::Phi_mpi_pi(corrmet.Phi()))};
  RVec<RVec<float>> output = {cleanJetPt, cleanJetEta, cleanJetPhi, cleanJetMass, corrmets};
  
  return output;
};

RVec<RVec<float>> cleanJetsMC (const bool &debug, const string &campaign, const string &jesvar, 
 correction::CompoundCorrection::Ref& ak4corr, correction::Correction::Ref& ak4corrL1, correction::Correction::Ref& ak4corrUnc, correction::Correction::Ref& ak4ptres, correction::Correction::Ref& ak4jer,
 correction::CompoundCorrection::Ref& ak8corr, correction::Correction::Ref& ak8corrUnc, 
 const RVec<TLorentzVector> &jt_p4, const RVec<float> &jt_rf, const RVec<float> &jt_murf, const RVec<float> &jt_area, const RVec<float> &jt_em, const RVec<int> &jt_id, 
 const RVec<TLorentzVector> &genjt_p4, const RVec<int> &jt_genidx, const float &rho, const float &met, const float &phi) 
{
  if (met == 0 && debug) cout << "---------------------------------------------------------------\n";
  
  RVec<float> cleanJetPt(jt_p4.size()), cleanJetEta(jt_p4.size()), cleanJetPhi(jt_p4.size()), cleanJetMass(jt_p4.size());//, rawfact(jt_p4.size());
  
  string jervar = "nom";
  float jesuncmult = 0;
  if (jesvar == "JERup") jervar = "up";
  else if (jesvar == "JERdn") jervar = "down";
  else if (jesvar == "JECup") jesuncmult = 1.0;
  else if (jesvar == "JECdn") jesuncmult = -1.0;
  
  correction::CompoundCorrection::Ref jescorr;
  correction::Correction::Ref jescorrUnc;
  float drmax = 0.2;
  if (ROOT::VecOps::Mean(jt_area) < 1.0) {jescorr = ak4corr; jescorrUnc = ak4corrUnc;}
  else {drmax = 0.4; jescorr = ak8corr; jescorrUnc = ak8corrUnc;}    
  
  float metx = met*cos(phi);
  float mety = met*sin(phi);
  //if (met > 0 && debug) std::cout<< "Incoming met = " << met << ", phi = " << phi << std::endl;
  
  for (unsigned int ijet = 0; ijet < jt_p4.size(); ijet++) {
    if (met == 0 && debug) std::cout<< "Incoming jet, pt = " << jt_p4[ijet].Pt() << ", phi = " << jt_p4[ijet].Phi() << std::endl;
    TLorentzVector jet = jt_p4[ijet];
    int jetid = jt_id[ijet];   
    float rf = jt_rf[ijet];
    float jes = 1.0; float jesL1 = 1.0; float jer = 1.0; float unc = 1.0;
    jet = jet * (1 - rf);                                                         // rf = 0 if JEC undone above
    
    if (met > 0 && jt_em[ijet] > 0.9) continue;                                    // not these jets for MET 
    if (met > 0) jet *= (1 - jt_murf[ijet]);                                       // further correct raw to muon-substracted raw for T1.
    float rawpt = jet.Pt();
    
    if (campaign == "2023BPix" || campaign == "2024" || campaign == "2025") {
      jes = jescorr->evaluate({jt_area[ijet],jet.Eta(),jet.Phi(),rawpt,rho}); // Data & MC get jes for 2023BPix
    }
    else {
      jes = jescorr->evaluate({jt_area[ijet],jet.Eta(),rawpt,rho}); // Data & MC get jes for other campaigns
    }
    if (met > 0) jesL1 = ak4corrL1->evaluate({jt_area[ijet],jet.Eta(),rawpt,rho}); // L1-only jes for MET T1
    
    // ----- MC specific: ----- 
    float res = ak4ptres->evaluate({jet.Eta(),rawpt*jes,rho});
    float sf = ak4jer->evaluate({jet.Eta(),rawpt*jes});
    bool smeared = false;                                                       // MC only gets a JER smear, one of 2 methods below:
    if(jt_genidx[ijet] > -1 && genjt_p4[jt_genidx[ijet]].Pt() > 0){   
      double dPt = fabs(genjt_p4[jt_genidx[ijet]].Pt() - rawpt*jes);
      double dR = genjt_p4[jt_genidx[ijet]].DeltaR(jet);
      if(dR < drmax && dPt < 3*rawpt*jes*res){
        jer = max(0.0, 1.0 + (sf - 1.0)*(rawpt*jes - genjt_p4[jt_genidx[ijet]].Pt())/(rawpt*jes));
        smeared = true;
      }
    }
    if (!smeared) {
      TRandom3 rand(abs(static_cast<int>(jet.Phi()*1e4)));
      jer = max(0.0, 1.0 + rand.Gaus(0, res)*sqrt(max(0.0, sf*sf - 1.0)));
    }
    unc = 1.0 + jesuncmult*(jescorrUnc->evaluate({jet.Eta(),rawpt*jes*jer}));   // MC gets JEC unc
    // -----
    
    TLorentzVector jetL1 = jet*jesL1*jer*unc;
    jet = jet*jes*jer*unc;                                                        // evals to jes*1 for data.
    
    if (met == 0 && debug) std::cout<< "Print last jet, pt = " << jet.Pt() << ", phi = " << jet.Phi() << std::endl;
    
    rf = 1.0 - 1.0/(jes*jer*unc); 
    if (jet.Pt() > 15) {
      metx += (jetL1 - jet).Px();
      mety += (jetL1 - jet).Py();
    }
    
    cleanJetPt[ijet] = jet.Pt();
    cleanJetEta[ijet] = jet.Eta();
    cleanJetPhi[ijet] = jet.Phi();
    cleanJetMass[ijet] = jet.M();
  }
  
  TVector2 corrmet(metx,mety);
  RVec<float> corrmets = {float(corrmet.Mod()),float(TVector2::Phi_mpi_pi(corrmet.Phi()))};
  RVec<RVec<float>> output = {cleanJetPt, cleanJetEta, cleanJetPhi, cleanJetMass, corrmets};
  
  return output;
};

RVec<RVec<float>> cleanJetsMC (const bool &debug, const string &campaign, const string &jesvar, 
 correction::CompoundCorrection::Ref& ak4corr, correction::Correction::Ref& ak4corrL1, correction::Correction::Ref& ak4corrUnc, correction::Correction::Ref& ak4ptres, correction::Correction::Ref& ak4jer,
 correction::CompoundCorrection::Ref& ak8corr, correction::Correction::Ref& ak8corrUnc, 
 const RVec<TLorentzVector> &jt_p4, const RVec<float> &jt_rf, const RVec<float> &jt_murf, const RVec<float> &jt_area, const RVec<float> &jt_em, 
 const RVec<TLorentzVector> &genjt_p4, const RVec<int> &jt_genidx, const RVec<TLorentzVector> &mu_p4, const RVec<int> mu_jetid, 
			       const RVec<TLorentzVector> &el_p4, const RVec<int> &el_jetid, const float &rho, const float &met, const float &phi) 
{
	RVec<int> jet_id(jt_p4.size(),9); // jetid isn't in 2024 NanoAOD, we assume all jets should pass so assign a value > 2
	return cleanJetsMC(debug,campaign,jesvar,ak4corr,ak4corrL1,ak4corrUnc,ak4ptres,ak4jer,ak8corr,ak8corrUnc,jt_p4,jt_rf,jt_murf,jt_area,jt_em,jet_id,genjt_p4,jt_genidx,mu_p4,mu_jetid,el_p4,el_jetid,rho,met,phi);
}

// Clean Jets Data Function
RVec<RVec<float>> cleanJetsData (const float run, const bool &debug, const string &campaign,
 correction::CompoundCorrection::Ref& ak4corr, correction::Correction::Ref& ak4corrL1,
 correction::CompoundCorrection::Ref& ak8corr,
 const RVec<TLorentzVector> &jt_p4, const RVec<float> &jt_rf, const RVec<float> &jt_murf, const RVec<float> &jt_area, const RVec<float> &jt_em, const RVec<int> &jt_id, 
 const RVec<TLorentzVector> &genjt_p4, const RVec<int> &jt_genidx, const RVec<TLorentzVector> &mu_p4, const RVec<int> mu_jetid, 
 const RVec<TLorentzVector> &el_p4, const RVec<int> &el_jetid, const float &rho, const float &met, const float &phi) 
{
  if (met == 0 && debug) cout << "---------------------------------------------------------------\n";
  
  RVec<float> cleanJetPt(jt_p4.size()), cleanJetEta(jt_p4.size()), cleanJetPhi(jt_p4.size()), cleanJetMass(jt_p4.size());//, rawfact(jt_p4.size());
  
  correction::CompoundCorrection::Ref jescorr;
  float drmax = 0.2;
  if (ROOT::VecOps::Mean(jt_area) < 1.0) {jescorr = ak4corr;}
  else {drmax = 0.4; jescorr = ak8corr;}    
  
  float metx = met*cos(phi);
  float mety = met*sin(phi);
  //if (met > 0 && debug) std::cout<< "Incoming met = " << met << ", phi = " << phi << std::endl;
  
  for (unsigned int ijet = 0; ijet < jt_p4.size(); ijet++) {
    if (met == 0 && debug) std::cout<< "Incoming jet, pt = " << jt_p4[ijet].Pt() << ", phi = " << jt_p4[ijet].Phi() << std::endl;
    TLorentzVector jet = jt_p4[ijet];
    int jetid = jt_id[ijet];   
    float rf = jt_rf[ijet];
    
    if(ROOT::VecOps::Mean(jt_area) < 1.0 && met == 0){ // only clean leptons out of AK4 jets (AK8 will require DR > 0.8 from lepton)
      for (unsigned int imu = 0; imu < mu_p4.size(); imu++){
	if (mu_jetid[imu] != ijet) continue;                      // only consider muons matched to this jet
	if (jetid < 2 || jet.DeltaR(mu_p4[imu]) > 0.4) continue; // bad jet, or too far from muon
	jet *= (1 - rf);                                         // first undo the JEC
	jet -= mu_p4[imu];                                       // subtract muon if it's sensible
	rf = 0;                                                  // indicate that this is the raw jet
      }
      for (unsigned int iel = 0; iel < el_p4.size(); iel++){     // same for electrons
	if (el_jetid[iel] != ijet) continue;
	if (jetid < 2 || jet.DeltaR(el_p4[iel]) > 0.4) continue;   
	jet *= (1 - rf); 
	jet -= el_p4[iel]; 
	rf = 0; 
      }
    }
    
    if (met == 0 && debug) std::cout<< "Post Lepton jet, pt = " << jet.Pt() << ", phi = " << jet.Phi() << std::endl;
    
    float jes = 1.0; float jesL1 = 1.0; 
    jet = jet * (1 - rf);                                                         // rf = 0 if JEC undone above
    
    if (met == 0 && debug) std::cout<< "Print 3 jet, pt = " << jet.Pt() << ", phi = " << jet.Phi() << std::endl;
    
    if (met > 0 && jt_em[ijet] > 0.9) continue;                                    // not these jets for MET 
    if (met > 0) jet *= (1 - jt_murf[ijet]);                                       // further correct raw to muon-substracted raw for T1.
    float rawpt = jet.Pt();

    if (campaign == "2023BPix" || campaign == "2024" || campaign == "2025") {
	 jes = jescorr->evaluate({jt_area[ijet],jet.Eta(),jet.Phi(),rawpt,rho,run}); // Data & MC get jes for 2023BPix
    }
    else{ // if (campaign == "2023") {
         jes = jescorr->evaluate({jt_area[ijet],jet.Eta(),rawpt,rho,run}); // Data & MC get jes for other campaigns
	 //    } else {
         //jes = jescorr->evaluate({jt_area[ijet],jet.Eta(),rawpt,rho}); // Data & MC get jes for other campaigns
    }

    if (met > 0) jesL1 = ak4corrL1->evaluate({jt_area[ijet],jet.Eta(),rawpt,rho}); // L1-only jes for MET T1
    
    TLorentzVector jetL1 = jet*jesL1;
    jet = jet*jes;                                                     // evals to jes*1 for data.
    
    if (met == 0 && debug) std::cout<< "Print last jet, pt = " << jet.Pt() << ", phi = " << jet.Phi() << std::endl;
    
    rf = 1.0 - 1.0/jes; 
    if (jet.Pt() > 15) {
      metx += (jetL1 - jet).Px();
      mety += (jetL1 - jet).Py();
    }
    
    cleanJetPt[ijet] = jet.Pt();
    cleanJetEta[ijet] = jet.Eta();
    cleanJetPhi[ijet] = jet.Phi();
    cleanJetMass[ijet] = jet.M();
  }
  
  TVector2 corrmet(metx,mety);
  RVec<float> corrmets = {float(corrmet.Mod()),float(TVector2::Phi_mpi_pi(corrmet.Phi()))};
  RVec<RVec<float>> output = {cleanJetPt, cleanJetEta, cleanJetPhi, cleanJetMass, corrmets};
  
  return output;
};

RVec<RVec<float>> cleanJetsData (const float run, const bool &debug, const string &campaign,
 correction::CompoundCorrection::Ref& ak4corr, correction::Correction::Ref& ak4corrL1,
 correction::CompoundCorrection::Ref& ak8corr,
 const RVec<TLorentzVector> &jt_p4, const RVec<float> &jt_rf, const RVec<float> &jt_murf, const RVec<float> &jt_area, const RVec<float> &jt_em, const RVec<int> &jt_id, 
 const RVec<TLorentzVector> &genjt_p4, const RVec<int> &jt_genidx, const float &rho, const float &met, const float &phi) 
{
  if (met == 0 && debug) cout << "---------------------------------------------------------------\n";
  
  RVec<float> cleanJetPt(jt_p4.size()), cleanJetEta(jt_p4.size()), cleanJetPhi(jt_p4.size()), cleanJetMass(jt_p4.size());//, rawfact(jt_p4.size());
  
  correction::CompoundCorrection::Ref jescorr;
  float drmax = 0.2;
  if (ROOT::VecOps::Mean(jt_area) < 1.0) {jescorr = ak4corr;}
  else {drmax = 0.4; jescorr = ak8corr;}    
  
  float metx = met*cos(phi);
  float mety = met*sin(phi);
  //if (met > 0 && debug) std::cout<< "Incoming met = " << met << ", phi = " << phi << std::endl;
  
  for (unsigned int ijet = 0; ijet < jt_p4.size(); ijet++) {
    if (met == 0 && debug) std::cout<< "Incoming jet, pt = " << jt_p4[ijet].Pt() << ", phi = " << jt_p4[ijet].Phi() << std::endl;
    TLorentzVector jet = jt_p4[ijet];
    int jetid = jt_id[ijet];   
    float rf = jt_rf[ijet];    
    float jes = 1.0; float jesL1 = 1.0; 
    jet = jet * (1 - rf);                                                         // rf = 0 if JEC undone above    
    
    if (met > 0 && jt_em[ijet] > 0.9) continue;                                    // not these jets for MET 
    if (met > 0) jet *= (1 - jt_murf[ijet]);                                       // further correct raw to muon-substracted raw for T1.
    float rawpt = jet.Pt();
    if (campaign == "2023BPix" || campaign == "2024" || campaign == "2025") {
	 jes = jescorr->evaluate({jt_area[ijet],jet.Eta(),jet.Phi(),rawpt,rho,run}); // Data & MC get jes for 2023BPix
    }
    else{ // if (campaign == "2023") {
         jes = jescorr->evaluate({jt_area[ijet],jet.Eta(),rawpt,rho,run}); // Data & MC get jes for other campaigns
	 //    } else {
         //jes = jescorr->evaluate({jt_area[ijet],jet.Eta(),rawpt,rho}); // Data & MC get jes for other campaigns
    }

    if (met > 0) {
	    jesL1 = ak4corrL1->evaluate({jt_area[ijet],jet.Eta(),rawpt,rho}); // L1-only jes for MET T1
    }

    TLorentzVector jetL1 = jet*jesL1;
    jet = jet*jes;                                                     // evals to jes*1 for data.
    
    if (met == 0 && debug) std::cout<< "Print last jet, pt = " << jet.Pt() << ", phi = " << jet.Phi() << std::endl;
    
    rf = 1.0 - 1.0/jes; 
    if (jet.Pt() > 15) {
      metx += (jetL1 - jet).Px();
      mety += (jetL1 - jet).Py();
    }
    
    cleanJetPt[ijet] = jet.Pt();
    cleanJetEta[ijet] = jet.Eta();
    cleanJetPhi[ijet] = jet.Phi();
    cleanJetMass[ijet] = jet.M();
  }
  
  TVector2 corrmet(metx,mety);
  RVec<float> corrmets = {float(corrmet.Mod()),float(TVector2::Phi_mpi_pi(corrmet.Phi()))};
  RVec<RVec<float>> output = {cleanJetPt, cleanJetEta, cleanJetPhi, cleanJetMass, corrmets};
  
  return output;
};

RVec<RVec<float>> cleanJetsData (const float run, const bool &debug, const string &campaign,
 correction::CompoundCorrection::Ref& ak4corr, correction::Correction::Ref& ak4corrL1,
 correction::CompoundCorrection::Ref& ak8corr,
 const RVec<TLorentzVector> &jt_p4, const RVec<float> &jt_rf, const RVec<float> &jt_murf, const RVec<float> &jt_area, const RVec<float> &jt_em, //jet_id is removed
 const RVec<TLorentzVector> &genjt_p4, const RVec<int> &jt_genidx, const RVec<TLorentzVector> &mu_p4, const RVec<int> mu_jetid, 
 const RVec<TLorentzVector> &el_p4, const RVec<int> &el_jetid, const float &rho, const float &met, const float &phi) {
 
  RVec<int> jet_id(jt_p4.size(),9);
  return cleanJetsData(run, debug, campaign, ak4corr, ak4corrL1, ak8corr, jt_p4, jt_rf, jt_murf, jt_area, jt_em, jet_id, genjt_p4, jt_genidx, mu_p4, mu_jetid, el_p4, el_jetid, rho, met, phi);
 }
//May not be fully implemented. Worth double checking.
