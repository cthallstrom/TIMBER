using namespace std;
using namespace ROOT::VecOps;

//'private' function for fatjet_matching
// auto get_daughters(int idx, unsigned int length, RVec<short> GenPart_genPartIdxMother) 
// {
//   vector<unsigned int> daughters;
//   //  std::cout << daughters << std::endl;
//   daughters.clear();
//   // std::cout << daughters << std::endl;
//   for (unsigned int d = idx; d < length; d++){
// 	  if (GenPart_genPartIdxMother[d]!=idx) continue;
// 	  daughters.push_back(d); //get a list of all the daughters of this particle
//   }

//   return daughters;
// }

auto SPAfatjet_matching(string sample, unsigned int nGenPart, RVec<int> &GenPart_pdgId, RVec<float> &GenPart_mass, RVec<float> &GenPart_pt, RVec<float> &GenPart_phi, RVec<float> &GenPart_eta, RVec<short> &GenPart_genPartIdxMother, RVec<int> &GenPart_status, RVec<unsigned short> &GenPart_statusFlags, RVec<float> &gcFatJet_pt, RVec<float> &gcFatJet_eta, RVec<float> &gcFatJet_phi, RVec<float> &gcFatJet_M, RVec<short> &gcFatJet_subj_idx1, RVec<short> &gcFatJet_subj_idx2,RVec<unsigned char> &gcFatJet_hadronFlavour, RVec<unsigned char> &SubJet_hadronFlavour, int Tlepidx, int Blepidx, int lep2idx, int had1idx, int had2idx)
{
  RVec<int> pID; //particle id of the parent
  RVec<int> pStatus; //where in the chain the parent particle is?
  RVec<float> pPt;
  RVec<float> pEta;
  RVec<float> pPhi;
  RVec<float> pM;
  RVec<int> pIdx;
  
  RVec<int> d0ID;
  RVec<int> d0Status;
  RVec<float> d0Pt;
  RVec<float> d0Eta;
  RVec<float> d0Phi;
  RVec<float> d0M;
  
  RVec<int> d1ID;
  RVec<int> d1Status;
  RVec<float> d1Pt;
  RVec<float> d1Eta;
  RVec<float> d1Phi;
  RVec<float> d1M;
  
  RVec<int> d2ID;
  RVec<int> d2Status;
  RVec<float> d2Pt;
  RVec<float> d2Eta;
  RVec<float> d2Phi;
  RVec<float> d2M;

  // std::cout << "Inside fatjet_matching. Will now beign matching:" << std::endl;
  // std::cout << "There are " << nGenPart << " particles in total."  << std::endl;
  //std::cout << "===================================" << std::endl;
  for(unsigned int i = 0; i < 120; i++){ //Changed top of range from nGenPart to 60
    int p = i; //initialize the parent idx
    int id = GenPart_pdgId[p];
    //std::cout << "Starting particle " << i << " it is a: " << id << " Mother is " << GenPart_genPartIdxMother[i] << " of type " << GenPart_pdgId[GenPart_genPartIdxMother[i]] << std::endl;
    
    bool hasRadiation = false;
    bool hasLepton = false;

    if(abs(id) == 23 || abs(id) == 24 || abs(id) == 25 || abs(id) == 6){
      //std::cout << "\t Now checking for radiation and leptons." << std::endl;
      vector<unsigned int> daughters = get_daughters(p, nGenPart, GenPart_genPartIdxMother);

      //check for radiation and leptons
      for (unsigned int j = 0; j < daughters.size(); j++){
	      int dID = GenPart_pdgId[daughters[j]];
	      if(abs(dID) == abs(id)) { //radiation check
	      //std::cout << "\t particle has radiation to " << j << " daughter, at idx " << daughters[j] << std::endl;
	      hasRadiation = true;
	      }else if(abs(dID) == 24 || abs(dID) == 23) { //check t->Wb->leptons and H->WW->leptons, check H->ZZ->leptons

	        vector<unsigned int>granddaughters = get_daughters(daughters.at(j), nGenPart, GenPart_genPartIdxMother);
	  
          //print out granddaughters
          if(granddaughters.size() == 2) {
            //std::cout << "\t \t We're checkign for leptons in daughter " << j << " of type " << dID << " which has 2 daughters: " << GenPart_pdgId[granddaughters.at(0)] << " and " << GenPart_pdgId[granddaughters.at(1)] <<  std::endl;
          } else if(granddaughters.size() == 1) {
              //std::cout << "\t \t We're checking for leptons in daughter " << j << " of type " << dID << " which has 1 daughter: " << GenPart_pdgId[granddaughters.at(0)] <<  std::endl;
          } else if (granddaughters.size() > 2) {
            //std::cout << "\t \t We're looking at a " << dID << " which has more than 2 daughters???" << std::endl;
          } else {
            //std::cout << "\t \t We're looking at a " << dID << " with no daughters" << std::endl;
          }
	  
          //check for -> w photon decay or -> w gluon decay
          while(granddaughters.size() == 1 || GenPart_pdgId[granddaughters[0]] == 22 || GenPart_pdgId[granddaughters[1]] == 22 || GenPart_pdgId[granddaughters[0]] == 21 || GenPart_pdgId[granddaughters[1]] == 21) {
            while(granddaughters.size() == 1) {
              //std::cout << "\t \t \t W/Z at idx " << daughters[j] << " has only one daughter " << GenPart_pdgId[granddaughters[0]] << ", we are jumping down the chain to " << granddaughters[0] << std::endl;
              daughters[j] = granddaughters[0];
              granddaughters = get_daughters(daughters[j], nGenPart, GenPart_genPartIdxMother);
            } 

            if(GenPart_pdgId[granddaughters[0]] == 22 || GenPart_pdgId[granddaughters[1]] == 22 || GenPart_pdgId[granddaughters[0]] == 21 || GenPart_pdgId[granddaughters[1]] == 21) {
              //std::cout << "\t \t \t W/Z has a " << GenPart_pdgId[granddaughters[1]] << " daughter at " << granddaughters[1] << " we will jump down the chain to " << granddaughters[0] << std::endl;
              daughters[j] = granddaughters[0];
              granddaughters = get_daughters(daughters[0], nGenPart, GenPart_genPartIdxMother);
            }
	        }
	  
          if(abs(GenPart_pdgId[granddaughters[0]]) > 10 && abs(GenPart_pdgId[granddaughters[0]]) < 17) {hasLepton = true;}
          if(abs(GenPart_pdgId[granddaughters[1]]) > 10 && abs(GenPart_pdgId[granddaughters[1]]) < 17) {hasLepton = true;}
	      }else if(abs(dID) > 10 && abs(dID) < 17) {hasLepton = true;}
      }
      //if(hasRadiation || hasLepton || GenPart_pt[p] < 175) {
      //	      //std::cout << "\t \t Particle either has radiation, a lepton, or is too soft. skip this one." << std::endl;
      //      continue;
      //}
      
      //skip this particle if...
      if(hasRadiation) continue;
      if(hasLepton) continue;
      if(GenPart_pt[p] < 175) {
	      //std::cout << "\t Particle too soft, pt = " << GenPart_pt[p] << " ID = " << id << std::endl;
	      continue;
      }
      
      vector<unsigned int> siblings;
      
      if(abs(id) == 24) { //if W
	      //std::cout << "\t particle is a W, will now investigate the dR." << std::endl;
	
	      float dR = 1000;
	
        //find topmost mother of a repeating chain
        while(GenPart_genPartIdxMother[p] != -1 && abs(GenPart_pdgId[GenPart_genPartIdxMother[p]]) == 24) {p = GenPart_genPartIdxMother[p];}
        siblings = get_daughters(GenPart_genPartIdxMother[p], nGenPart, GenPart_genPartIdxMother);

	      if(abs(GenPart_pdgId[GenPart_genPartIdxMother[p]]) == 6) { //dRWB
          //dr btwn current particle and its sibling
          //std::cout << "\t W from top: sibling 1 = " << GenPart_pdgId[siblings[1]] << " and 0 is " << GenPart_pdgId[siblings[0]] << std::endl;
          dR = (GenPart_eta[p], GenPart_eta[siblings[1]], GenPart_phi[p], GenPart_phi[siblings[1]]);
          //std::cout << "\t \t dr to 1 is " << dR << std::endl;
	  
          if(abs(GenPart_pdgId[siblings[1]]) == 24) {
            dR = DeltaR(GenPart_eta[p], GenPart_eta[siblings[0]], GenPart_phi[p], GenPart_phi[siblings[0]]);
            //std::cout << "\t \t dr to 0 is " << dR << std::endl;
          }
	  
	      }else if(abs(GenPart_pdgId[GenPart_genPartIdxMother[p]]) == 25){ //dRWW
          //std::cout << "\t W from H" << std::endl;
          if(GenPart_pdgId[p]*GenPart_pdgId[siblings[0]] > 0) {
            dR = DeltaR(GenPart_eta[p], GenPart_eta[siblings[1]], GenPart_phi[p], GenPart_phi[siblings[1]]); 
          }else{
            dR = DeltaR(GenPart_eta[p], GenPart_eta[siblings[0]], GenPart_phi[p], GenPart_phi[siblings[0]]);
          }
	      }     
	
	      //std::cout << "\t dR W from top or H = " << dR << std::endl;
	
	      if(dR < 0.8) continue; 
      } //end of if W
      
      if(abs(id) == 23) { //if Z
	      float dRZZ = 1000;

        //std::cout << "\t particle is a Z, will now investigate the dR." << std::endl;
        
        //find topmost mother of a repeating chain
        while(GenPart_genPartIdxMother[p] != -1 && abs(GenPart_pdgId[GenPart_genPartIdxMother[p]]) == 23) {p = GenPart_genPartIdxMother[p];}
        siblings = get_daughters(GenPart_genPartIdxMother[p], nGenPart, GenPart_genPartIdxMother);
        
          if(abs(GenPart_genPartIdxMother[p]) == 25) {
            float dr = 1000;
            if(GenPart_pdgId[p]*GenPart_pdgId[siblings[0]] > 0) {
              dr = DeltaR(GenPart_eta[p], GenPart_eta[siblings[1]], GenPart_phi[p], GenPart_phi[siblings[1]]); 
            }else{
              dr = DeltaR(GenPart_eta[p], GenPart_eta[siblings[0]], GenPart_phi[p], GenPart_phi[siblings[0]]);
            }
            if(dr < dRZZ) dRZZ = dr;
          }

          //std::cout << "\t \t dR = " << dRZZ << std::endl;
          if(dRZZ < 0.8) continue; // Z from merged H
      }
              
      if(daughters.size() < 2) {
          //std::cout << daughters.size() << " daughters from " << GenPart_pdgId[p] << std::endl;
          continue;
      }

      pStatus.push_back(GenPart_status[p]);
      pID.push_back(GenPart_pdgId[p]);
	  pIdx.push_back(p);
      pPt.push_back(GenPart_pt[p]);
      pEta.push_back(GenPart_eta[p]);
      pPhi.push_back(GenPart_phi[p]);
      pM.push_back(GenPart_mass[p]);
  
      if(abs(id) != 6) {
	
        d0Status.push_back(GenPart_status[daughters.at(0)]);
        d0ID.push_back(GenPart_pdgId[daughters.at(0)]);
        d0Pt.push_back(GenPart_pt[daughters.at(0)]);
        d0Eta.push_back(GenPart_eta[daughters.at(0)]);
        d0Phi.push_back(GenPart_phi[daughters.at(0)]);
        d0M.push_back(GenPart_mass[daughters.at(0)]);

        d1Status.push_back(GenPart_status[daughters.at(1)]);
        d1ID.push_back(GenPart_pdgId[daughters.at(1)]);
        d1Pt.push_back(GenPart_pt[daughters.at(1)]);
        d1Eta.push_back(GenPart_eta[daughters.at(1)]);
        d1Phi.push_back(GenPart_phi[daughters.at(1)]);
        d1M.push_back(GenPart_mass[daughters.at(1)]);

        d2Status.push_back(-99);
        d2ID.push_back(-99);
        d2Pt.push_back(-99.9);
        d2Eta.push_back(-99.9);
        d2Phi.push_back(-99.9);
        d2M.push_back(-99.9);

      }else{ //if is t
        //Can mess around with value if needed
        unsigned int W = 1000;
        unsigned int b = 1000;
        
        if(abs(GenPart_pdgId[daughters.at(0)]) == 24) {
          W = daughters.at(0);
          b = daughters.at(1);
          //std::cout << "\t W is 0th daughter: " << GenPart_pdgId[W] << ", b is: " << GenPart_pdgId[b] << std::endl;
        }else{
          W = daughters.at(1);
          b = daughters.at(0);
          //std::cout <<  "\t W is 1st daughter: " << GenPart_pdgId[W] << ", b is: " << GenPart_pdgId[b] << std::endl;
        }
	
	      vector<unsigned int> W_daughters = get_daughters(W, nGenPart, GenPart_genPartIdxMother);


        d0Status.push_back(GenPart_status[b]);
        d0ID.push_back(GenPart_pdgId[b]);
        d0Pt.push_back(GenPart_pt[b]);
        d0Eta.push_back(GenPart_eta[b]);
        d0Phi.push_back(GenPart_phi[b]);
        d0M.push_back(GenPart_mass[b]);

        //std::cout << "\t \t b has been assigned" << std::endl;
        //std::cout << "\t Now pushing back W daughters 0 and 1: " << GenPart_pdgId[W_daughters.at(0)] << ", " << GenPart_pdgId[W_daughters.at(1)] << std::endl;
        
        d1Status.push_back(GenPart_status[W_daughters.at(0)]);
        d1ID.push_back(GenPart_pdgId[W_daughters.at(0)]);
        d1Pt.push_back(GenPart_pt[W_daughters.at(0)]);
        d1Eta.push_back(GenPart_eta[W_daughters.at(0)]);
        d1Phi.push_back(GenPart_phi[W_daughters.at(0)]);
        d1M.push_back(GenPart_mass[W_daughters.at(0)]);

        d2Status.push_back(GenPart_status[W_daughters.at(1)]);
        d2ID.push_back(GenPart_pdgId[W_daughters.at(1)]);
        d2Pt.push_back(GenPart_pt[W_daughters.at(1)]);
        d2Eta.push_back(GenPart_eta[W_daughters.at(1)]);
        d2Phi.push_back(GenPart_phi[W_daughters.at(1)]);
        d2M.push_back(GenPart_mass[W_daughters.at(1) ]);
      }
    }
  }

  RVec<float> fatjet_truth;
  RVec<float> fatjet_slot;
  RVec<float> particle_slot (3, 0);
  particle_slot.clear();
  RVec<float> fatjet_matchedPt;

  // if(pID.size() == 3){
  //  std::cout << "===================== True Particle Candidates ====================" << std::endl;
  //  std::cout << pIdx << ", " << pID << " Jets to match: " << gcFatJet_pt.size() <<std::endl;
  //  std::cout << "===================== leptonic and hadronic options ====================" << std::endl;
  //  std::cout << GenPart_pdgId[Tlepidx] << " {" << lep2idx << ", " << had1idx << ", " << had2idx << "}" << "{" << GenPart_pdgId[lep2idx] << ", " << GenPart_pdgId[had1idx] << ", " << GenPart_pdgId[had2idx] << "}" << endl;
  // }

  //std::cout << "===================== Investigating " << gcFatJet_pt.size() << " fatJets ====================" << std::endl;

  // cout << "Start of Event" << endl;
  // cout << particle_slot << endl;

  int lepFJIdx = -3;
  int had1FJIdx = -3;
  int had2FJIdx = -3;

  for(unsigned int i = 0; i < gcFatJet_pt.size(); i++){
    TLorentzVector fatjet, truePart, d0, d1, d2;
    
    fatjet.SetPtEtaPhiM(gcFatJet_pt[i], gcFatJet_eta[i], gcFatJet_phi[i], gcFatJet_M[i]);
    //std::cout << "fatjet " << i << std::endl;
    float minDR = 1000;
    float matchedPt= -99;
    int matchedID = 0;
	  int matchedIdx = -1;
    bool isWmatched = false;
    bool isHmatched = false;
    bool isZmatched = false;
    bool isTmatched = false;
    bool isJmatched = false;
    bool isBmatched = false;

    for(unsigned int j = 0; j < pPt.size(); j++){
      truePart.SetPtEtaPhiM(pPt[j], pEta[j], pPhi[j], pM[j]);
      //cout << pIdx[j] << ", ";
      if(fatjet.DeltaR(truePart) < minDR) {
        //std::cout << "\t fatjet DeltaR with truePart " << j << " = " << fatjet.DeltaR(truePart) << std::endl;
        minDR = fatjet.DeltaR(truePart);
        matchedPt = pPt[j];
        matchedID = abs(pID[j]);
		    matchedIdx = pIdx[j];
        d0.SetPtEtaPhiM(d0Pt[j], d0Eta[j], d0Phi[j], d0M[j]);
        d1.SetPtEtaPhiM(d1Pt[j], d1Eta[j], d1Phi[j], d1M[j]);
        d2.SetPtEtaPhiM(d2Pt[j], d2Eta[j], d2Phi[j], d2M[j]);
        //std::cout << "\t Succesfully initialized daughter TLorentz Vecs" << std::endl;
      }
    } //cout << endl;
    
    bool WallDsInJet = false;
    bool TallDsInJet = false;
    if(matchedID != 6 && fatjet.DeltaR(d0) < 0.8 && fatjet.DeltaR(d1) < 0.8) WallDsInJet = true;
    if(matchedID == 6 && fatjet.DeltaR(d0) < 0.8 && fatjet.DeltaR(d1) < 0.8 && fatjet.DeltaR(d2) < 0.8) TallDsInJet = true;
    if(minDR < 0.8 && matchedID == 24 && WallDsInJet) isWmatched = true;
    if(minDR < 0.8 && matchedID == 25 && WallDsInJet) isHmatched = true;
    if(minDR < 0.8 && matchedID == 23 && WallDsInJet) isZmatched = true;
    if(minDR < 0.8 && matchedID == 6  && TallDsInJet) isTmatched = true;

    if(matchedIdx == lep2idx) {
      //std::cout << "Assigning lep2idx: " << matchedIdx<< endl;
      lepFJIdx = i;
      particle_slot[0] = matchedIdx;
      //cout << "part is: " << particle_slot[0] << endl;
    }
    if(matchedIdx == had1idx) {
      //std::cout << "Assigning had1idx: " << matchedIdx<< endl;
      had1FJIdx = i;
      particle_slot[1] = matchedIdx;
      //cout << "part is: " << particle_slot[1] << endl;
    }
    if(matchedIdx == had2idx) {
      //std::cout << "Assigning had2idx: " << matchedIdx<< endl;
      had2FJIdx = i; 
      particle_slot[2] = matchedIdx;
      //cout << "part is: " << particle_slot[2] << endl;
    }

    if(isWmatched || isZmatched || isHmatched || isTmatched) {
      //std::cout << "\t Found a match for the fatjet: W - " << isWmatched << ", H - " << isHmatched << ", Z - " << isZmatched << ", t - " << isTmatched << std::endl;
      fatjet_matchedPt.push_back(matchedPt);
    }else{
      //std::cout << "\t did not find a match for the fatjet" << std::endl;
      fatjet_matchedPt.push_back(-99.9);
    }
    // Pt cuts to put back when ready: W = 200, Z = 200, T = 400, H = 300
    if(not (isWmatched) && not (isZmatched) && not (isTmatched) && not (isHmatched)) {
      //std::cout << "\t Unmatched or matchedPt (" << matchedPt << ") does not meet requirements. Investigating subjets" << std::endl;
      int firstsub = gcFatJet_subj_idx1[i];
      int secondsub = gcFatJet_subj_idx2[i];
      
      if(firstsub > -1) {
        //std::cout << "\t \t first subjet hadron flavour is: "<< int(SubJet_hadronFlavour[firstsub]) << std::endl;
        if(int(SubJet_hadronFlavour[firstsub]) == 5) isBmatched = true;
      }

      if(secondsub > -1) {
        //std::cout << "\t \t second subjet hadron flavour is: "<< int(SubJet_hadronFlavour[secondsub]) << std::endl;
        if(int(SubJet_hadronFlavour[secondsub]) == 5) isBmatched = true;
      }
      //if(gcFatJet_hadronFlavour[i] == 5) isBmatched = true;
      
      if(not isBmatched) {
        //std::cout << "\t \t \t jet is light quarks." << std::endl;
        isJmatched = true;
      }else{
	      //std::cout << "\t \t \t jet is b matched" << std::endl;
      }
    }

    if(isJmatched) fatjet_truth.push_back(0);
    else if(isTmatched) fatjet_truth.push_back(6);
    else if(isHmatched) fatjet_truth.push_back(25);
    else if(isZmatched) fatjet_truth.push_back(23);
    else if(isWmatched) fatjet_truth.push_back(24);
    else if(isBmatched) fatjet_truth.push_back(5);

    fatjet_matchedPt.push_back(matchedPt);
  
    // std::cout << "Truth is: " << fatjet_truth[i] << std::endl;
    // std::cout << "=============== Done with FatJets =================" << std::endl << std::endl << std::endl;
  }
  fatjet_slot.push_back(lepFJIdx);
  fatjet_slot.push_back(had1FJIdx);
  fatjet_slot.push_back(had2FJIdx);

  RVec<RVec<float>> returns;
  returns.push_back(fatjet_truth);
  returns.push_back(fatjet_slot);
  returns.push_back(particle_slot);
  //std::cout << particle_slot << ", " << lep2idx << ", " << had1idx << ", " << had2idx << endl;
  return returns;
}

auto SPADecayModeSelection(unsigned int nGenPart, ROOT::VecOps::RVec<int>& GenPart_pdgId, ROOT::VecOps::RVec<float>& GenPart_mass, ROOT::VecOps::RVec<float>& GenPart_pt, ROOT::VecOps::RVec<float>& GenPart_phi, ROOT::VecOps::RVec<float>& GenPart_eta, ROOT::VecOps::RVec<short>& GenPart_genPartIdxMother, ROOT::VecOps::RVec<int>& GenPart_status, ROOT::VecOps::RVec<short> GenPart_statusFlags, bool isTpTp)
{
	int TdecayMode;
	int BdecayMode;
	RVec<int> primes;
	RVec<int> Ws;
	RVec<int> ts;

	bool isLastCopy = false;

	// Find the last copy of the VLQs
	for(int i = 0; i < nGenPart; i++) {
		isLastCopy = false;
		if(abs(GenPart_pdgId[i]) == 6000006 || abs(GenPart_pdgId[i]) == 6000007){
			isLastCopy = (GenPart_statusFlags[i] >> 13) & 1;
			if(isLastCopy) primes.push_back(i);
		}
	}

	RVec<RVec<int>> daughters;
	int motherIdx;
	int motherId;
	int grandmotherId;
	int id;
	int nLepW = 0;
	int nLepT = 0;

	// Find daughters of VLQs and assign leptonic particle
	for(int i = 0; i < nGenPart; i++) {
		motherIdx = GenPart_genPartIdxMother[i];
		motherId = GenPart_pdgId[motherIdx];
		grandmotherId = GenPart_pdgId[GenPart_genPartIdxMother[motherIdx]];

		if(motherIdx < 0) continue;

		id = GenPart_pdgId[i];

		// If not tZWHb, continue
		if(abs(id) != 5 && abs(id) != 6 && abs(id) != 23 && abs(id) != 24 && abs(id) != 25) continue;

		if(motherIdx == primes[0]) daughters[0].push_back(i);
		if(motherIdx == primes[1]) daughters[1].push_back(i);
	}

	// If the daughters are W or t, get their indices
	for(int x = 0; x < 2; x++){
		for(int y = 0; y < 2; y++){
			if(abs(GenPart_pdgId[daughters[x][y]]) == 24) Ws.push_back(daughters[x][y]);
			if(abs(GenPart_pdgId[daughters[x][y]]) == 6) ts.push_back(daughters[x][y]);
		}
	} 

	int nH = 0;
    int nt = 0;   
	int nZ = 0;
    int nb = 0;    
	int nW = 0;

	// Count how many of each decay product we have
	for(int i = 0; i < 2; i++){
		for(int j = 0; j < daughters[i].size(); j++){
			int idx = daughters[i][j];
			int pdgid = abs(GenPart_pdgId[idx]);

			if(pdgid == 25) nH++;
			else if(pdgid == 24) nW++;
			else if(pdgid == 23) nZ++;
			else if(pdgid == 6) nt++;
			else if (pdgid == 5) nb++;
		}
	}
	int Tmode = 0;

	// Assign TTbar decay mode
	if(abs(GenPart_pdgId[primes[0]]) == 6000006 && abs(GenPart_pdgId[primes[1]]) == 6000006){
		if(nb == 2 && nW == 2) Tmode = 1;
		else if(nt == 2 && nZ == 2) Tmode = 2;
		else if(nt == 2 && nH == 2) Tmode = 3;
		else if(nt == 2 && nH == 1 && nZ == 1) Tmode = 4;
		else if(nt == 1 && nZ == 1 && nb == 1 && nW == 1) Tmode = 5;
		else if(nt == 1 && nH == 1 && nb == 1 && nW == 1) Tmode = 6;
		else Tmode = -1;
	}

	int Bmode = 0;
	// Assign BBbar decay mode
	if(abs(GenPart_pdgId[primes[0]]) == 6000007 && abs(GenPart_pdgId[primes[1]]) == 6000007){
		if(nt == 2 && nW == 2) Bmode = 1;
		else if(nb == 2 && nZ == 2) Bmode = 2;
		else if(nb == 2 && nH == 2) Bmode = 3;
		else if(nb == 2 && nH == 1 && nZ == 1) Bmode = 4;
		else if(nb == 1 && nZ == 1 && nt == 1 && nW == 1) Bmode = 5;
		else if(nb == 1 && nH == 1 && nt == 1 && nW == 1) Bmode = 6;
		else Bmode = -1;
	}

	// Figure out how many leptons we have
	// Code taken from Nicolas's decay mode finder
	int index, prev, child;
	// W's
	int ogWidx = -1;
	for (int i = 0; i < Ws.size(); i++) {
		index = prev = Ws.at(i);

		for (++index;index < nGenPart; index++) {
			if (GenPart_genPartIdxMother[index] == prev) { // Found a child of W!
				child = abs(GenPart_pdgId[index]);

				if (child == 24) { // it's a W
				prev = index;
				} else if (11 <= child && child <= 16) { // it's a lepton!
					ogWidx = Ws.at(i);
					Tmode += 100;
					Bmode += 100;
					break;
				} else { break; } // non-leptonic decay
			}
		}
	}

	// t's
	int ogTidx = -1;
	for (int i = 0; i < ts.size(); i++) {
		index = prev = ts.at(i);
		
		for (++index; index < nGenPart; index++) {
			if (GenPart_genPartIdxMother[index] == prev) { // Found a child of t!
				child = abs(GenPart_pdgId[index]);
                if (child == 6 || child ==24) { // it's a t or a W
                    prev = index;
                } else if (11 <= child && child <= 16) { // it's a lepton!
					          ogTidx = ts.at(i);
                    Tmode += 1000;
                    Bmode += 1000;
                    break;
                } else { break; } // non-leptonic decay
			}
		}  
	}

  int current_top = ogTidx;
	int bidx;
  for (int i = ogTidx + 1; i < nGenPart; i++) {
    if (GenPart_genPartIdxMother[i] == current_top && abs(GenPart_pdgId[i]) == 6) {
      current_top = i; // Follow the top line to its final state
    }
  }
  for (int i = 0; i < nGenPart; i++) {
    if (GenPart_genPartIdxMother[i] == current_top && abs(GenPart_pdgId[i]) == 5) {
      bidx = i;
      break;
    }
  }

    
  int TleptonicIdx = -1;
  int BleptonicIdx = -1;
  if((Tmode < 107 && Tmode > 100) || (Tmode < 1007 && Tmode > 1000)) {
      TdecayMode = Tmode;
      if(ogTidx != -1) TleptonicIdx = ogTidx;
      else if(ogWidx != -1) TleptonicIdx = ogWidx;
  }

  if((Bmode < 107 && Bmode > 100) || (Bmode < 1007 && Bmode > 1000)) {
      BdecayMode = Bmode;
      if(ogTidx != -1) BleptonicIdx = ogTidx;
      else if(ogWidx != -1) BleptonicIdx = ogWidx;
  }

	int idx = -1;
	int lepVLQidx = -1;
	int lep2idx = -1; // idx of the particle that is paired with the leptonic particle
	int had1idx = -1;
	int had2idx = -1;

	if(isTpTp) idx = TleptonicIdx;
	else idx = BleptonicIdx;

	//cout << "idx, TleptonicIdx" << idx << ", " << TleptonicIdx << endl;

	// while (idx >= 0 && abs(GenPart_pdgId[GenPart_genPartIdxMother[idx]]) != 6000006) {
    // 	idx = GenPart_genPartIdxMother[idx];
	// }
	// std::cout << "lepVLQidx: " << GenPart_genPartIdxMother[idx] << std::endl;
	// std::cout << "VLQ idxs: " << primes[0] << ", " << primes[1] << std::endl;
	if(GenPart_genPartIdxMother[idx] != -1) lepVLQidx = GenPart_genPartIdxMother[idx];

	if (lepVLQidx == primes[0]) {
		int d0 = daughters[0][0];
		int d1 = daughters[0][1];

		// Check if daughters ARE the leptonic particle
		if (d0 == ogTidx || d0 == ogWidx) {
			lep2idx = d1;
			had1idx = daughters[1][0];
			had2idx = daughters[1][1];
		} 
		// Otherwise check d1
		else if (d1 == ogTidx || d1 == ogWidx) {
			lep2idx = d0;
			had1idx = daughters[1][0];
			had2idx = daughters[1][1];
		}
	}

	if (lepVLQidx == primes[1]) {
		int d0 = daughters[1][0];
		int d1 = daughters[1][1];

		// Check if daughters ARE the leptonic particle
		if (d0 == ogTidx || d0 == ogWidx) {
			lep2idx = d1;
			had1idx = daughters[0][0];
			had2idx = daughters[0][1];
		} 
		// Otherwise check d1
		else if (d1 == ogTidx || d1 == ogWidx) {
			lep2idx = d0;
			had1idx = daughters[0][0];
			had2idx = daughters[0][1];
		}
	}
	
	//std::cout << "Modes are: " << TdecayMode << ", " << BdecayMode << std::endl;
  //cout << bidx << endl;
	RVec<int> decayModes;
	decayModes.push_back(TdecayMode);
	decayModes.push_back(BdecayMode);
  decayModes.push_back(TleptonicIdx);
  decayModes.push_back(BleptonicIdx);
	decayModes.push_back(lep2idx);
	decayModes.push_back(had1idx);
	decayModes.push_back(had2idx);
  if((TdecayMode < 1007 && TdecayMode > 1000) || (BdecayMode < 1007 && BdecayMode > 1000)){
    decayModes.push_back(bidx);
  } else decayModes.push_back(-1);
  //cout << decayModes[7] << " Leptonic pair is: " << GenPart_pdgId[lep2idx] << " idx is: " << lep2idx << endl;
	return decayModes;
}

auto SPAIndexMatcher(RVec<float> gcFatJet_eta, RVec<float> gcFatJet_phi, RVec<float> GenPart_eta, RVec<float> GenPart_phi, int lep2idx, int had1idx, int had2idx)
{
  float minDRlep2 = 999.9;
  float minDRhad1 = 999.9;
  float minDRhad2 = 999.9;

  int lep2FJidx = -1;
  int had1FJidx = -1;
  int had2FJidx = -1;

  for(int ijet = 0; ijet < gcFatJet_eta.size(); ijet++){
    if(DeltaR(gcFatJet_eta[ijet], GenPart_eta[lep2idx], gcFatJet_phi[ijet], GenPart_phi[lep2idx]) < minDRlep2) {
      minDRlep2 = DeltaR(gcFatJet_eta[ijet], GenPart_eta[lep2idx], gcFatJet_phi[ijet], GenPart_phi[lep2idx]);
      lep2FJidx = ijet;
    }
    if(DeltaR(gcFatJet_eta[ijet], GenPart_eta[had1idx], gcFatJet_phi[ijet], GenPart_phi[had1idx]) < minDRhad1) {
      minDRhad1 = DeltaR(gcFatJet_eta[ijet], GenPart_eta[had1idx], gcFatJet_phi[ijet], GenPart_phi[had1idx]);
      had1FJidx = ijet;
    }
    if(DeltaR(gcFatJet_eta[ijet], GenPart_eta[had2idx], gcFatJet_phi[ijet], GenPart_phi[had2idx]) < minDRhad2) {
      minDRhad2 = DeltaR(gcFatJet_eta[ijet], GenPart_eta[had2idx], gcFatJet_phi[ijet], GenPart_phi[had2idx]);
      had2FJidx = ijet;
    }
  }

  RVec<int> indices;
  if(lep2FJidx == had1FJidx || had1FJidx == had2FJidx || had2FJidx == lep2FJidx) indices.push_back(-1);
  else{
    indices.push_back(lep2FJidx);
    indices.push_back(had1FJidx);
    indices.push_back(had2FJidx);
  }
  //cout << indices << endl;

  return indices;
}