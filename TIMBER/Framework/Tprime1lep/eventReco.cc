#include <iostream>
using namespace std;
using namespace ROOT::VecOps;

auto WReco(float corrMET_pt, float corrMET_phi, TLorentzVector lepton_lv) {

    const double MW = 80.4;
	double METpx = corrMET_pt * cos(corrMET_phi);
	double METpy = corrMET_pt * sin(corrMET_phi);
	double METpt = corrMET_pt;
	TLorentzVector W_lv_1, W_lv_2, W_lv, Nulv_1, Nulv_2, Nulv;
	double nuPz_1;
	double nuPz_2;

    double Dtmp = MW*MW - lepton_lv.M()*lepton_lv.M() + 2*(lepton_lv.Px()*METpx + lepton_lv.Py()*METpy);
	double Atmp = 4.0*(lepton_lv.Energy()*lepton_lv.Energy() - lepton_lv.Pz()*lepton_lv.Pz());
	double Btmp = -4.0*Dtmp*lepton_lv.Pz();
	double Ctmp = 4.0*lepton_lv.Energy()*lepton_lv.Energy()*METpt*METpt - Dtmp*Dtmp;
	
	double DETtmp = Btmp*Btmp - 4.0*Atmp*Ctmp;

	if(DETtmp >= 0)
	{
		nuPz_1 = (-Btmp + TMath::Sqrt(DETtmp))/(2.0*Atmp);
		nuPz_2 = (-Btmp - TMath::Sqrt(DETtmp))/(2.0*Atmp);
		Nulv_1.SetPxPyPzE(METpx,METpy,nuPz_1,TMath::Sqrt((METpt)*(METpt)+(nuPz_1)*(nuPz_1)));
		Nulv_2.SetPxPyPzE(METpx,METpy,nuPz_2,TMath::Sqrt((METpt)*(METpt)+(nuPz_2)*(nuPz_2)));
	}
	else
	{
		nuPz_1 = -Btmp/(2.0*Atmp);
		nuPz_2 = -Btmp/(2.0*Atmp);
		// does another quad solution for pT and scales pT in result. Reduces M, pT, DR.
		double alpha = lepton_lv.Px()*METpx/METpt + lepton_lv.Py()*METpy/METpt;
		double Delta = MW*MW - lepton_lv.M()*lepton_lv.M();
		Atmp = 4.0*(lepton_lv.Pz()*lepton_lv.Pz() - lepton_lv.Energy()*lepton_lv.Energy() + alpha*alpha);
		Btmp = 4.0*alpha*Delta;
		Ctmp = Delta*Delta;
		float DETtmp2 = Btmp*Btmp - 4.0*Atmp*Ctmp;
		double pTnu_1 = (-Btmp + TMath::Sqrt(DETtmp2))/(2.0*Atmp);
		double pTnu_2 = (-Btmp - TMath::Sqrt(DETtmp2))/(2.0*Atmp);
		Nulv_1.SetPxPyPzE(METpx*pTnu_1/METpt,METpy*pTnu_1/METpt,nuPz_1,TMath::Sqrt(pTnu_1*pTnu_1 + nuPz_1*nuPz_1));
		Nulv_2.SetPxPyPzE(METpx*pTnu_2/METpt,METpy*pTnu_2/METpt,nuPz_2,TMath::Sqrt(pTnu_2*pTnu_2 + nuPz_2*nuPz_2));
	}
    W_lv_1 = Nulv_1 + lepton_lv;
	W_lv_2 = Nulv_2 + lepton_lv;
	
	if(fabs(W_lv_1.M() - MW) < fabs(W_lv_2.M() - MW)) {
		W_lv = W_lv_1;
		Nulv = Nulv_1;
	}
	else {
		W_lv = W_lv_2;
		Nulv = Nulv_2;
	}
	RVec<TLorentzVector> Wnu;
	Wnu.push_back(W_lv);
	Wnu.push_back(Nulv);
	return Wnu;
}

ROOT::VecOps::RVec<float> tReco(int lepton_source, ROOT::VecOps::RVec<float>& jet_pt, ROOT::VecOps::RVec<float>& jet_eta, ROOT::VecOps::RVec<float>& jet_phi, ROOT::VecOps::RVec<float>& jet_mass, TLorentzVector W_lv, float minMleppJet, int MinMlj_idx){
	float t_mass = -999;
	float t_pt = -999;
	float t_eta = -999;
	float t_phi = -999;
	float t_dRWb = -999;
	float deltaRbW = 999;
	int bIdx = 999;
	TLorentzVector jet_lv, t_lv;
	for(unsigned int ijet=0; ijet < jet_pt.size(); ijet++)
	{
		jet_lv.SetPtEtaPhiM(jet_pt.at(ijet),jet_eta.at(ijet),jet_phi.at(ijet),jet_mass.at(ijet));
		if(jet_lv.DeltaR(W_lv) < deltaRbW)
		{
			deltaRbW = jet_lv.DeltaR(W_lv);
			bIdx = ijet;
		}
	}
	
	// Form a leptonic top candidate if the b is close enough
	if(lepton_source == 1)
	{
		if(deltaRbW > 0.8) {bIdx = MinMlj_idx;} // use a close b unless it doesn't exist
		TLorentzVector bottom_lv;
		bottom_lv.SetPtEtaPhiM(jet_pt.at(bIdx),jet_eta.at(bIdx),jet_phi.at(bIdx),jet_mass.at(bIdx));
		t_lv = bottom_lv + W_lv;
		t_mass = t_lv.M();
		t_pt = t_lv.Pt();
		t_eta = t_lv.Eta();
		t_phi = t_lv.Phi();
		t_dRWb = bottom_lv.DeltaR(W_lv);
	}
	else
	{
		t_pt = 9999;
		t_eta = 9;
		t_phi = 9;
		t_mass = -999;
	}
	ROOT::VecOps::RVec<float> t_FiveVec = {t_pt,t_eta,t_phi,t_mass,t_dRWb};
	return t_FiveVec;
}

// need to figure out isNominal and how a lamda function works
// Find btag value that we will be using and understand what needs to change here for that
auto minMleppJet_calc(ROOT::VecOps::RVec<float>& jet_pt, ROOT::VecOps::RVec<float>& jet_eta,ROOT::VecOps::RVec<float>& jet_phi, ROOT::VecOps::RVec<float>& jet_mass, TLorentzVector lepton_lv, ROOT::VecOps::RVec<float>& Jet_btagDeepFlavB_GCJ, float BTagM)
{
	//std::cout << "Entered Mlj calculation" << std::endl;
	float MinMlj_idx = -1; // This gets changed into int in .Define()
	float minMleppJet = 1e8;
	ROOT::VecOps::RVec<int> theJetBTag_JetSubCalc_PtOrdered (jet_pt.size(),0);
	float NJetsDeepFlavwithSF_JetSubCalc = 0;
	TLorentzVector jet_lv;
	
	for(unsigned int ijet=0; ijet < jet_pt.size(); ijet++)
	{
		jet_lv.SetPtEtaPhiM(jet_pt.at(ijet),jet_eta.at(ijet),jet_phi.at(ijet),jet_mass.at(ijet));
		if(Jet_btagDeepFlavB_GCJ[ijet] > BTagM){theJetBTag_JetSubCalc_PtOrdered.at(ijet) = 1;} // BTagged or not
		else if(Jet_btagDeepFlavB_GCJ[ijet] < BTagM){theJetBTag_JetSubCalc_PtOrdered.at(ijet) = 0;}
		
		if((lepton_lv + jet_lv).M() < minMleppJet)
		{
			minMleppJet = fabs((lepton_lv + jet_lv).M());
			MinMlj_idx = ijet;
		}
	}
	ROOT::VecOps::RVec<float> minMlj = {minMleppJet, MinMlj_idx};
	//std::cout << minMlj << std::endl;
	return minMlj;
}

auto minMlb_calc(ROOT::VecOps::RVec<float>& jet_pt, ROOT::VecOps::RVec<float>& jet_eta,ROOT::VecOps::RVec<float>& jet_phi, ROOT::VecOps::RVec<float>& jet_mass, TLorentzVector lepton_lv) {
	float minMlb_idx = -1; // This gets changed into int in .Define()
	float minMlb = 1e8;
	float minMlbDR = 1000;
	TLorentzVector bjet;
	
	for(unsigned int ijet=0; ijet < jet_pt.size(); ijet++)
	{       
		bjet.SetPtEtaPhiM(jet_pt.at(ijet),jet_eta.at(ijet),jet_phi.at(ijet),jet_mass.at(ijet));

		if((lepton_lv + bjet).M() < minMlb) {
			minMlb = fabs((lepton_lv + bjet).M());
			minMlb_idx = ijet;
			minMlbDR = lepton_lv.DeltaR(bjet);
		}
	}
	ROOT::VecOps::RVec<float> minMlbVec = {minMlb, minMlb_idx, minMlbDR};
	return minMlbVec;
}


// Fxn to return any and all float TPrime and BPrime variables needed for plotting
// ----------------------------------------------------------------------------------------------------------------------------------------------------------------
RVec<float> TBprimeReco(TLorentzVector t_lv, TLorentzVector W_lv, int lepton_source, RVec<float>& gcFatJet_pt, RVec<float>& gcFatJet_eta, RVec<float>& gcFatJet_phi, RVec<float>& gcFatJet_mass, RVec<int>& PNWMtags)
{
	TLorentzVector jet_lv;
	std::vector<pair<TLorentzVector,int>> jets_lv;
	float dRjX = 0;
	bool isLeptonic_W = false;
	bool isLeptonic_t = false;
	RVec<int> PNWM_ID;
	for(unsigned int ijet=0; ijet < gcFatJet_pt.size(); ijet++)
	{
		jet_lv.SetPtEtaPhiM(gcFatJet_pt.at(ijet),gcFatJet_eta.at(ijet),gcFatJet_phi.at(ijet),gcFatJet_mass.at(ijet));
		if(lepton_source == 0)
		{
			dRjX = jet_lv.DeltaR(W_lv);
			isLeptonic_W = true;
		}
		if(lepton_source == 1)
		{
			dRjX = jet_lv.DeltaR(t_lv);
			isLeptonic_t = true;
		}
		// Get 3 highest-pT jets that are not close to t/W (deltaR > .8) and store AK8 index and 4-vector
		if(jets_lv.size() >= 3){break;}
		if(jet_lv.DeltaR(t_lv) > 0.8 and isLeptonic_t) {jets_lv.push_back(std::make_pair(jet_lv,ijet));}
		if(jet_lv.DeltaR(W_lv) > 0.8 and isLeptonic_W) {jets_lv.push_back(std::make_pair(jet_lv,ijet));}
		//std::cout << ijet << ", " << jet_lv.Pt() << std::endl;
		if(PNWMtags.at(ijet) == 6) PNWM_ID.push_back(1);
		else if (PNWMtags.at(ijet) == 0) PNWM_ID.push_back(0);
		else if(PNWMtags.at(ijet) == 25) PNWM_ID.push_back(2);
		else if(PNWMtags.at(ijet) == 23) PNWM_ID.push_back(3);
		else if(PNWMtags.at(ijet) == 24) PNWM_ID.push_back(4);
		else if(PNWMtags.at(ijet) == 5) PNWM_ID.push_back(5);
	}
	
	float Tprime1_Mass = -999;
	float Tprime2_Mass = -999;
	float Tprime1_Pt = -9999;
	float Tprime2_Pt = -9999;
	float Tprime1_Eta = 9;
	float Tprime2_Eta = 9;
	float Tprime1_Phi = 9;
	float Tprime2_Phi = 9;
	float Tprime1_deltaR = -9;
	float Tprime2_deltaR = -9;
	float Bprime1_Mass = -999;
	float Bprime2_Mass = -999;
	float Bprime1_Pt = -9999;
	float Bprime2_Pt = -9999;
	float Bprime1_Eta = 9;
	float Bprime2_Eta = 9;
	float Bprime1_Phi = 9;
	float Bprime2_Phi = 9;
	float Bprime1_deltaR = -9;
	float Bprime2_deltaR = -9;
	
	float leptonicTprimeJetIDs = -1; //Changed into int within .Define()
	float leptonicBprimeJetIDs = -1;
	int leptonicTprimeJetIdx = -1;
	int leptonicBprimeJetIdx = -1;
	
	bool validTDecay = false;
	bool validBDecay = false;

	// In order to match the truth decay mode finder, order starting from 1 is:
	// For Tp: bWbW, tZtZ, tHtH, tZtH, tZbW, tHbW
	// For Bp: tWtW, bZbZ, bHbH, bZbH, bZtW, bHtW
	// invalid decays: tH, tZ, bW are 7,8,9
	// 0 indicates a completely disallowed decay
	float tagTDecayMode = 0;
	float tagBDecayMode = 0;
	
	RVec<float> hadronicTprimeJetIDs (2,0);
	RVec<float> hadronicBprimeJetIDs (2,0);
	RVec<int> hadronicTprimeJetIdxs (2,0);
	RVec<int> hadronicBprimeJetIdxs (2,0);
	
	// ----------------------------------------------------------------------------
	// VLQ Decay -- 3 AK8 jets away from leptonic particle
	// ----------------------------------------------------------------------------
	if(jets_lv.size() > 3) {std::cout << "Problem: > 3 AK8s for Tprime reco" << std::endl;}
	if(jets_lv.size() == 3)
	{				
		// ----------------------------------------------------------------------------
		// DeepAK8 SECTION -- TT
		// ----------------------------------------------------------------------------
		
		// get the tags

		// pair up the jet tag with the pT index 0,1,2 and sort by tag (orders J, T, H, Z, W, B)
		std::vector <pair<float,int>> decayJets;
		decayJets.push_back(std::make_pair(PNWM_ID.at(jets_lv.at(0).second), 0));
		decayJets.push_back(std::make_pair(PNWM_ID.at(jets_lv.at(1).second), 1));
		decayJets.push_back(std::make_pair(PNWM_ID.at(jets_lv.at(2).second), 2));
		std::sort(decayJets.begin(),decayJets.end());

		float jet1_tag = decayJets[0].first;
		float jet2_tag = decayJets[1].first;
		float jet3_tag = decayJets[2].first;

		int jet1_idx = decayJets[0].second;
		int jet2_idx = decayJets[1].second;
		int jet3_idx = decayJets[2].second;
		
		// Start forming 4 particle groups
		TLorentzVector Tprime1_lv;
		TLorentzVector Tprime2_lv;
		TLorentzVector Bprime1_lv;
		TLorentzVector Bprime2_lv;
		if(isLeptonic_t)
		{
            // Mass of (t_lv + jet_lv) - Mass of (sum of other two jets)
		    float massDiff1=(t_lv+jets_lv.at(jet2_idx).first).M()-(jets_lv.at(jet1_idx).first+jets_lv.at(jet3_idx).first).M();
            float massDiff2=(t_lv+jets_lv.at(jet3_idx).first).M()-(jets_lv.at(jet1_idx).first+jets_lv.at(jet2_idx).first).M();
            float massDiff3=(t_lv+jets_lv.at(jet1_idx).first).M()-(jets_lv.at(jet2_idx).first+jets_lv.at(jet3_idx).first).M();

            //Check the dnn tags to see if it is a tH bW decay
			if(decayJets.at(0).first==2 && decayJets.at(1).first==4 && decayJets.at(2).first==5)
			{ // TT -> tH bW, BB -> tW bH
				validTDecay = true;
				tagTDecayMode = 6;
				leptonicTprimeJetIdx = jet1_idx;
				hadronicTprimeJetIdxs = {jet2_idx, jet3_idx};
				leptonicTprimeJetIDs = 2; // assign the H with the leptonic top
				hadronicTprimeJetIDs = {4,5};      // assign the b & W as hadronic
                // Create VLQ lv's by adding top higgs and W b
				Tprime1_lv = t_lv+jets_lv.at(decayJets.at(0).second).first; // decayJets.second gives the jets_lv index to get 4-vec
				Tprime2_lv = jets_lv.at(decayJets.at(1).second).first+jets_lv.at(decayJets.at(2).second).first;

                // find the deltaR of the constituent particles
				Tprime1_deltaR = t_lv.DeltaR(jets_lv.at(decayJets.at(0).second).first);
				Tprime2_deltaR = jets_lv.at(decayJets.at(1).second).first.DeltaR(jets_lv.at(decayJets.at(2).second).first);
				
				validBDecay = true;
				tagBDecayMode = 6;
				leptonicBprimeJetIdx = jet2_idx;
				hadronicBprimeJetIdxs = {jet1_idx, jet3_idx};
				leptonicBprimeJetIDs = 4; // assign the W with leptonic top
				hadronicBprimeJetIDs = {2,5};      // assign bH hadronic
				Bprime1_lv = t_lv+jets_lv.at(decayJets.at(1).second).first; // decayJets.second gives the jets_lv index to get 4-vec
				Bprime2_lv = jets_lv.at(decayJets.at(0).second).first+jets_lv.at(decayJets.at(2).second).first;
				Bprime1_deltaR = t_lv.DeltaR(jets_lv.at(decayJets.at(1).second).first);
				Bprime2_deltaR = jets_lv.at(decayJets.at(0).second).first.DeltaR(jets_lv.at(decayJets.at(2).second).first);
			
			}
			else if(decayJets.at(0).first==1 && decayJets.at(1).first==2 && decayJets.at(2).first==2)
			{ // TTbar --> tH and tH
				validTDecay = true;
				tagTDecayMode = 3;
				leptonicTprimeJetIDs = 2; // assign an H with leptonic top
				hadronicTprimeJetIDs = {1,2};      // assign tH hadronic
				// options (lepTop + H1) - (T0 + H2) OR (lepTop + H2) - (T0 + H1) checking smallest
				if(massDiff1 < massDiff2)
				{ // (lepTop + H1) wins
					leptonicTprimeJetIdx = jet2_idx;
					hadronicTprimeJetIdxs = {jet1_idx, jet3_idx};
					Tprime1_lv = t_lv+jets_lv.at(decayJets.at(1).second).first;
					Tprime2_lv = jets_lv.at(decayJets.at(0).second).first+jets_lv.at(decayJets.at(2).second).first;
					Tprime1_deltaR = t_lv.DeltaR(jets_lv.at(decayJets.at(1).second).first);
					Tprime2_deltaR = jets_lv.at(decayJets.at(0).second).first.DeltaR(jets_lv.at(decayJets.at(2).second).first);
				}
				else
				{ // (lepTop + H2) wins
					leptonicTprimeJetIdx = jet3_idx;
					hadronicTprimeJetIdxs = {jet1_idx, jet2_idx};
					Tprime1_lv = t_lv+jets_lv.at(decayJets.at(2).second).first;
					Tprime2_lv = jets_lv.at(decayJets.at(0).second).first+jets_lv.at(decayJets.at(1).second).first;
					Tprime1_deltaR = t_lv.DeltaR(jets_lv.at(decayJets.at(2).second).first);
					Tprime2_deltaR = jets_lv.at(decayJets.at(1).second).first.DeltaR(jets_lv.at(decayJets.at(0).second).first);
				}
			}
			else if(decayJets.at(0).first==1 && decayJets.at(1).first==2 && decayJets.at(2).first==3)
			{ // TTbar --> tH and tZ
				validTDecay = true;
				tagTDecayMode = 4;
				// options (lepTop + H1) - (T0 + Z2) OR (lepTop + Z2) - (T0 + H1)
				if(massDiff1 < massDiff2)
				{ // (lepTop + H1) wins
					leptonicTprimeJetIdx = jet2_idx;
					hadronicTprimeJetIdxs = {jet1_idx, jet3_idx};
					leptonicTprimeJetIDs = 2; // tH
					hadronicTprimeJetIDs = {1,3}; // tZ
					Tprime1_lv = t_lv+jets_lv.at(decayJets.at(1).second).first;
					Tprime2_lv = jets_lv.at(decayJets.at(0).second).first+jets_lv.at(decayJets.at(2).second).first;
					Tprime1_deltaR = t_lv.DeltaR(jets_lv.at(decayJets.at(1).second).first);
					Tprime2_deltaR = jets_lv.at(decayJets.at(0).second).first.DeltaR(jets_lv.at(decayJets.at(2).second).first);
				}
				else
				{ // (lepTop + Z2) wins
					leptonicTprimeJetIdx = jet3_idx;
					hadronicTprimeJetIdxs = {jet1_idx, jet2_idx};
					leptonicTprimeJetIDs = 3;
					hadronicTprimeJetIDs = {1,2};
					Tprime1_lv = t_lv+jets_lv.at(decayJets.at(2).second).first;
					Tprime2_lv = jets_lv.at(decayJets.at(0).second).first+jets_lv.at(decayJets.at(1).second).first;
					Tprime1_deltaR = t_lv.DeltaR(jets_lv.at(decayJets.at(2).second).first);
					Tprime2_deltaR = jets_lv.at(decayJets.at(1).second).first.DeltaR(jets_lv.at(decayJets.at(0).second).first);
				}
			}
			else if(decayJets.at(0).first==3 && decayJets.at(1).first==4 && decayJets.at(2).first==5)
			{ // TT -> tZ bW, BB -> tW bZ
				validTDecay = true;
				tagTDecayMode = 5;
				leptonicTprimeJetIdx =jet1_idx;
				hadronicTprimeJetIdxs = {jet2_idx, jet3_idx};
				leptonicTprimeJetIDs = 3; // tZ
				hadronicTprimeJetIDs = {4,5}; // bW
				Tprime1_lv = t_lv+jets_lv.at(decayJets.at(0).second).first;
				Tprime2_lv = jets_lv.at(decayJets.at(1).second).first+jets_lv.at(decayJets.at(2).second).first;
				Tprime1_deltaR = t_lv.DeltaR(jets_lv.at(decayJets.at(0).second).first);
				Tprime2_deltaR = jets_lv.at(decayJets.at(1).second).first.DeltaR(jets_lv.at(decayJets.at(2).second).first);
				
				validBDecay = true;
				tagBDecayMode = 5;
				leptonicBprimeJetIdx = jet2_idx;
				hadronicBprimeJetIdxs = {jet1_idx, jet3_idx};
				leptonicBprimeJetIDs = 4; // assign the W with the leptonic top
				hadronicBprimeJetIDs = {3,5};      // assign the b & Z as hadronic
				Bprime1_lv = t_lv+jets_lv.at(decayJets.at(1).second).first; // decayJets.second gives the jets_lv index to get 4-vec
				Bprime2_lv = jets_lv.at(decayJets.at(0).second).first+jets_lv.at(decayJets.at(2).second).first;
				Bprime1_deltaR = t_lv.DeltaR(jets_lv.at(decayJets.at(1).second).first);
				Bprime2_deltaR = jets_lv.at(decayJets.at(0).second).first.DeltaR(jets_lv.at(decayJets.at(2).second).first);
			}
			else if(decayJets.at(0).first==1 && decayJets.at(1).first==3 && decayJets.at(2).first==3)
			{ // TTbar --> tZ tZ
				validTDecay = true;
				tagTDecayMode = 2;
				leptonicTprimeJetIDs = 3; // tZ
				hadronicTprimeJetIDs = {1,3}; // tZ
				// options (lepTop + Z1) - (T0 + Z2) OR (lepTop + Z2) - (T0 + Z1)
				if(massDiff1 < massDiff2)
				{ // (lepTop + Z1) wins
					leptonicTprimeJetIdx = jet2_idx;
					hadronicTprimeJetIdxs = {jet1_idx, jet3_idx};
					Tprime1_lv = t_lv+jets_lv.at(decayJets.at(1).second).first;
					Tprime2_lv = jets_lv.at(decayJets.at(0).second).first+jets_lv.at(decayJets.at(2).second).first;
					Tprime1_deltaR = t_lv.DeltaR(jets_lv.at(decayJets.at(1).second).first);
					Tprime2_deltaR = jets_lv.at(decayJets.at(0).second).first.DeltaR(jets_lv.at(decayJets.at(2).second).first);
				}
				else
				{ // (lepTop + Z2) wins
					leptonicTprimeJetIdx = jet3_idx;
					hadronicTprimeJetIdxs = {jet1_idx, jet2_idx};
					Tprime1_lv = t_lv+jets_lv.at(decayJets.at(2).second).first;
					Tprime2_lv = jets_lv.at(decayJets.at(0).second).first+jets_lv.at(decayJets.at(1).second).first;
					Tprime1_deltaR = t_lv.DeltaR(jets_lv.at(decayJets.at(2).second).first);
					Tprime2_deltaR = jets_lv.at(decayJets.at(1).second).first.DeltaR(jets_lv.at(decayJets.at(0).second).first);
				}
			}
			else if(decayJets.at(0).first==1 && decayJets.at(1).first==4 && decayJets.at(2).first==4)
			{ // BB/XX -> tW tW, jets t W W
				validBDecay = true;
				tagBDecayMode = 1;
				leptonicBprimeJetIDs = 4; // tW
				hadronicBprimeJetIDs = {1,4}; // tW
				// options (lepTop + W1) - (T0 + W2) OR (lepTop + W2) - (T0 + W1)
				if(massDiff1 < massDiff2)
				{ // (lepTop + W1) wins
					leptonicBprimeJetIdx = jet2_idx;
					hadronicBprimeJetIdxs = {jet1_idx, jet3_idx};
					Bprime1_lv = t_lv+jets_lv.at(decayJets.at(1).second).first;
					Bprime2_lv = jets_lv.at(decayJets.at(0).second).first+jets_lv.at(decayJets.at(2).second).first;
					Bprime1_deltaR = t_lv.DeltaR(jets_lv.at(decayJets.at(1).second).first);
					Bprime2_deltaR = jets_lv.at(decayJets.at(0).second).first.DeltaR(jets_lv.at(decayJets.at(2).second).first);
				}
				else
				{ // (lepTop + W2) wins
					leptonicBprimeJetIdx = jet3_idx;
					hadronicBprimeJetIdxs = {jet1_idx, jet2_idx};
					Bprime1_lv = t_lv+jets_lv.at(decayJets.at(2).second).first;
					Bprime2_lv = jets_lv.at(decayJets.at(0).second).first+jets_lv.at(decayJets.at(1).second).first;
					Bprime1_deltaR = t_lv.DeltaR(jets_lv.at(decayJets.at(2).second).first);
					Bprime2_deltaR = jets_lv.at(decayJets.at(0).second).first.DeltaR(jets_lv.at(decayJets.at(1).second).first);
				}
			}
			
			if(!validTDecay)
			{ // Not a valid T decay combination
				tagTDecayMode = 0;
				if(massDiff3 < massDiff1 and massDiff3 < massDiff2)
				{  // lepTop + 0 is best
					leptonicTprimeJetIdx = jet1_idx;
					hadronicTprimeJetIdxs = {jet2_idx, jet3_idx};
					leptonicTprimeJetIDs = decayJets.at(0).first;
					hadronicTprimeJetIDs = {decayJets.at(1).first, decayJets.at(2).first};
					Tprime1_lv = t_lv+jets_lv.at(decayJets.at(0).second).first;
					Tprime2_lv = jets_lv.at(decayJets.at(1).second).first+jets_lv.at(decayJets.at(2).second).first;
					Tprime1_deltaR = t_lv.DeltaR(jets_lv.at(decayJets.at(0).second).first);
					Tprime2_deltaR = jets_lv.at(decayJets.at(1).second).first.DeltaR(jets_lv.at(decayJets.at(2).second).first);
				}
				else if(massDiff1 < massDiff2 and massDiff1 < massDiff3)
				{ // lepTop + 1 is best
					leptonicTprimeJetIdx = jet2_idx;
					hadronicTprimeJetIdxs = {jet1_idx, jet3_idx};
					leptonicTprimeJetIDs = decayJets.at(1).first;
					hadronicTprimeJetIDs = {decayJets.at(0).first, decayJets.at(2).first};
					Tprime1_lv = t_lv+jets_lv.at(decayJets.at(1).second).first;
					Tprime2_lv = jets_lv.at(decayJets.at(0).second).first+jets_lv.at(decayJets.at(2).second).first;
					Tprime1_deltaR = t_lv.DeltaR(jets_lv.at(decayJets.at(1).second).first);
					Tprime2_deltaR = jets_lv.at(decayJets.at(0).second).first.DeltaR(jets_lv.at(decayJets.at(2).second).first);
				}
				else
				{ // lepTop + 2 is best
					leptonicTprimeJetIdx = jet3_idx;
					hadronicTprimeJetIdxs = {jet1_idx, jet2_idx};
					leptonicTprimeJetIDs = decayJets.at(2).first;
					hadronicTprimeJetIDs = {decayJets.at(0).first, decayJets.at(1).first};
					Tprime1_lv = t_lv+jets_lv.at(decayJets.at(2).second).first;
					Tprime2_lv = jets_lv.at(decayJets.at(0).second).first+jets_lv.at(decayJets.at(1).second).first;
					Tprime1_deltaR = t_lv.DeltaR(jets_lv.at(decayJets.at(2).second).first);
					Tprime2_deltaR = jets_lv.at(decayJets.at(1).second).first.DeltaR(jets_lv.at(decayJets.at(0).second).first);
				}
				if(hadronicTprimeJetIDs[0] == 1 && hadronicTprimeJetIDs[1] == 2) tagTDecayMode = 7;
				if(hadronicTprimeJetIDs[0] == 1 && hadronicTprimeJetIDs[1] == 3) tagTDecayMode = 8;
				if(hadronicTprimeJetIDs[0] == 4 && hadronicTprimeJetIDs[1] == 5) tagTDecayMode = 9;
			}
			if(!validBDecay)
			{ // Not a valid B decay combination
				tagBDecayMode = 0;
				if(massDiff3 < massDiff1 and massDiff3 < massDiff2)
				{  // lepTop + 0 is best
					leptonicBprimeJetIdx = jet1_idx;
					hadronicBprimeJetIdxs = {jet2_idx, jet3_idx};
					leptonicBprimeJetIDs = decayJets.at(0).first;
					hadronicBprimeJetIDs = {decayJets.at(1).first, decayJets.at(2).first};
					Bprime1_lv = t_lv+jets_lv.at(decayJets.at(0).second).first;
					Bprime2_lv = jets_lv.at(decayJets.at(1).second).first+jets_lv.at(decayJets.at(2).second).first;
					Bprime1_deltaR = t_lv.DeltaR(jets_lv.at(decayJets.at(0).second).first);
					Bprime2_deltaR = jets_lv.at(decayJets.at(1).second).first.DeltaR(jets_lv.at(decayJets.at(2).second).first);
				}
				else if(massDiff1 < massDiff2 and massDiff1 < massDiff3)
				{ // lepTop + 1 is best
					leptonicBprimeJetIdx = jet2_idx;
					hadronicBprimeJetIdxs = {jet1_idx, jet3_idx};
					leptonicBprimeJetIDs = decayJets.at(1).first;
					hadronicBprimeJetIDs = {decayJets.at(0).first, decayJets.at(2).first};
					Bprime1_lv = t_lv+jets_lv.at(decayJets.at(1).second).first;
					Bprime2_lv = jets_lv.at(decayJets.at(0).second).first+jets_lv.at(decayJets.at(2).second).first;
					Bprime1_deltaR = t_lv.DeltaR(jets_lv.at(decayJets.at(1).second).first);
					Bprime2_deltaR = jets_lv.at(decayJets.at(0).second).first.DeltaR(jets_lv.at(decayJets.at(2).second).first);
				}
				else
				{ // lepTop + 2 is best
					leptonicBprimeJetIdx = jet3_idx;
					hadronicBprimeJetIdxs = {jet1_idx, jet2_idx};
					leptonicBprimeJetIDs = decayJets.at(2).first;
					hadronicBprimeJetIDs = {decayJets.at(0).first, decayJets.at(1).first};
					Bprime1_lv = t_lv+jets_lv.at(decayJets.at(2).second).first;
					Bprime2_lv = jets_lv.at(decayJets.at(0).second).first+jets_lv.at(decayJets.at(1).second).first;
					Bprime1_deltaR = t_lv.DeltaR(jets_lv.at(decayJets.at(2).second).first);
					Bprime2_deltaR = jets_lv.at(decayJets.at(1).second).first.DeltaR(jets_lv.at(decayJets.at(0).second).first);
				}
				if(hadronicBprimeJetIDs[0] == 2 && hadronicBprimeJetIDs[1] == 5) tagBDecayMode = 7;
				if(hadronicBprimeJetIDs[0] == 3 && hadronicBprimeJetIDs[1] == 5) tagBDecayMode = 8;
				if(hadronicBprimeJetIDs[0] == 1 && hadronicBprimeJetIDs[1] == 4) tagBDecayMode = 9;
			}
		}
		else
		{ // isLeptonic_W
			
		    float massDiff1=(W_lv+jets_lv.at(jet2_idx).first).M()-(jets_lv.at(jet1_idx).first+jets_lv.at(jet3_idx).first).M();
            float massDiff2=(W_lv+jets_lv.at(jet3_idx).first).M()-(jets_lv.at(jet1_idx).first+jets_lv.at(jet2_idx).first).M();
            float massDiff3=(W_lv+jets_lv.at(jet1_idx).first).M()-(jets_lv.at(jet2_idx).first+jets_lv.at(jet3_idx).first).M();

			if(decayJets.at(0).first==4 && decayJets.at(1).first==5 && decayJets.at(2).first==5)
			{ // bW bW
				validTDecay = true;
				tagTDecayMode = 1;
				hadronicTprimeJetIdxs = {};
				leptonicTprimeJetIDs = 5; // bW
				hadronicTprimeJetIDs = {4,5}; // bW
				// options (lepW + b1) - (W0 + b2) OR (lepW + b2) - (W0 + b1)
				if(massDiff1 < massDiff2)
				{ // (lepW + b1) wins
					leptonicTprimeJetIdx = jet2_idx;
					hadronicTprimeJetIdxs = {jet1_idx, jet3_idx};
					Tprime1_lv = W_lv+jets_lv.at(decayJets.at(1).second).first;
					Tprime2_lv = jets_lv.at(decayJets.at(0).second).first+jets_lv.at(decayJets.at(2).second).first;
					Tprime1_deltaR = W_lv.DeltaR(jets_lv.at(decayJets.at(1).second).first);
					Tprime2_deltaR = jets_lv.at(decayJets.at(0).second).first.DeltaR(jets_lv.at(decayJets.at(2).second).first);
				}
				else
				{ // (lepW + b2) wins
					leptonicTprimeJetIdx = jet3_idx;
					hadronicTprimeJetIdxs = {jet1_idx, jet2_idx};
					Tprime1_lv = W_lv+jets_lv.at(decayJets.at(2).second).first;
					Tprime2_lv = jets_lv.at(decayJets.at(0).second).first+jets_lv.at(decayJets.at(1).second).first;
					Tprime1_deltaR = W_lv.DeltaR(jets_lv.at(decayJets.at(2).second).first);
					Tprime2_deltaR = jets_lv.at(decayJets.at(0).second).first.DeltaR(jets_lv.at(decayJets.at(1).second).first);
				}
			}
			else if(decayJets.at(0).first==1 && decayJets.at(1).first==3 && decayJets.at(2).first==5)
			{ // TT -> bW tZ, BB -> tW bZ
				validTDecay = true;
				tagTDecayMode = 5;
				leptonicTprimeJetIdx = jet3_idx;
				hadronicTprimeJetIdxs = {jet1_idx, jet2_idx};
				leptonicTprimeJetIDs = 5; // bW
				hadronicTprimeJetIDs = {1,3}; // tZ
				Tprime1_lv = W_lv+jets_lv.at(decayJets.at(2).second).first;
				Tprime2_lv = jets_lv.at(decayJets.at(0).second).first+jets_lv.at(decayJets.at(1).second).first;
				Tprime1_deltaR = W_lv.DeltaR(jets_lv.at(decayJets.at(2).second).first);
				Tprime2_deltaR = jets_lv.at(decayJets.at(0).second).first.DeltaR(jets_lv.at(decayJets.at(1).second).first);
				
				validBDecay = true;
				tagBDecayMode = 5;
				leptonicBprimeJetIdx = jet1_idx;
				hadronicBprimeJetIdxs = {jet2_idx, jet3_idx};
				leptonicBprimeJetIDs = 1; // tW
				hadronicBprimeJetIDs = {3,5}; // bZ
				Bprime1_lv = W_lv+jets_lv.at(decayJets.at(0).second).first;
				Bprime2_lv = jets_lv.at(decayJets.at(1).second).first+jets_lv.at(decayJets.at(2).second).first;
				Bprime1_deltaR = W_lv.DeltaR(jets_lv.at(decayJets.at(0).second).first);
				Bprime2_deltaR = jets_lv.at(decayJets.at(1).second).first.DeltaR(jets_lv.at(decayJets.at(2).second).first);
			}
			else if(decayJets.at(0).first==1 && decayJets.at(1).first==2 && decayJets.at(2).first==5)
			{ // TT -> bW tH, BB -> tW bH
				validTDecay = true;
				tagTDecayMode = 6;
				leptonicTprimeJetIdx = jet3_idx;
				hadronicTprimeJetIdxs = {jet1_idx, jet2_idx};
				leptonicTprimeJetIDs = 5; // bW
				hadronicTprimeJetIDs = {1,2}; // tH
				Tprime1_lv = W_lv+jets_lv.at(decayJets.at(2).second).first;
				Tprime2_lv = jets_lv.at(decayJets.at(0).second).first+jets_lv.at(decayJets.at(1).second).first;
				Tprime1_deltaR = W_lv.DeltaR(jets_lv.at(decayJets.at(2).second).first);
				Tprime2_deltaR = jets_lv.at(decayJets.at(0).second).first.DeltaR(jets_lv.at(decayJets.at(1).second).first);
				
				validBDecay = true;
				tagBDecayMode = 6;
				leptonicBprimeJetIdx = jet1_idx;
				hadronicBprimeJetIdxs = {jet2_idx, jet3_idx};
				leptonicBprimeJetIDs = 1; // tW
				hadronicBprimeJetIDs = {2,5}; // bH
				Bprime1_lv = W_lv+jets_lv.at(decayJets.at(0).second).first;
				Bprime2_lv = jets_lv.at(decayJets.at(1).second).first+jets_lv.at(decayJets.at(2).second).first;
				Bprime1_deltaR = W_lv.DeltaR(jets_lv.at(decayJets.at(0).second).first);
				Bprime2_deltaR = jets_lv.at(decayJets.at(2).second).first.DeltaR(jets_lv.at(decayJets.at(2).second).first);
			}
			else if(decayJets.at(0).first==1 && decayJets.at(1).first==1 && decayJets.at(2).first==4)
			{ // BB -> tW tW, jets t t W
				validBDecay = true;
				tagBDecayMode = 1;
				leptonicBprimeJetIDs = 1; // tW
				hadronicBprimeJetIDs = {1,4}; // tW
				// options (lepW + t0) - (W2 + t1) OR (lepW + t1) - (W2 + t0)
				if(massDiff3 < massDiff1)
				{ // (lepW + t0) wins
					leptonicBprimeJetIdx = jet1_idx;
					hadronicBprimeJetIdxs = {jet2_idx, jet3_idx};
					Bprime1_lv = W_lv+jets_lv.at(decayJets.at(0).second).first;
					Bprime2_lv = jets_lv.at(decayJets.at(1).second).first+jets_lv.at(decayJets.at(2).second).first;
					Bprime1_deltaR = W_lv.DeltaR(jets_lv.at(decayJets.at(0).second).first);
					Bprime2_deltaR = jets_lv.at(decayJets.at(1).second).first.DeltaR(jets_lv.at(decayJets.at(2).second).first);
				}
				else
				{ // (lepW + t1) wins
					leptonicBprimeJetIdx = jet2_idx;
					hadronicBprimeJetIdxs = {jet1_idx, jet3_idx};
					Bprime1_lv = W_lv+jets_lv.at(decayJets.at(1).second).first;
					Bprime2_lv = jets_lv.at(decayJets.at(0).second).first+jets_lv.at(decayJets.at(2).second).first;
					Bprime1_deltaR = W_lv.DeltaR(jets_lv.at(decayJets.at(1).second).first);
					Bprime2_deltaR = jets_lv.at(decayJets.at(0).second).first.DeltaR(jets_lv.at(decayJets.at(2).second).first);
				}
			}
			if(!validTDecay)
			{ // not a valid grouping
				tagTDecayMode = 0;
				if(massDiff3 < massDiff1 and massDiff3 < massDiff2)
				{ // lepW + 0 wins
					leptonicTprimeJetIdx = jet1_idx;
					hadronicTprimeJetIdxs = {jet2_idx, jet3_idx};
					leptonicTprimeJetIDs = decayJets.at(0).first;
					hadronicTprimeJetIDs = {decayJets.at(1).first, decayJets.at(2).first};
					Tprime1_lv = W_lv+jets_lv.at(decayJets.at(0).second).first;
					Tprime2_lv = jets_lv.at(decayJets.at(1).second).first+jets_lv.at(decayJets.at(2).second).first;
					Tprime1_deltaR = W_lv.DeltaR(jets_lv.at(decayJets.at(0).second).first);
					Tprime2_deltaR = jets_lv.at(decayJets.at(1).second).first.DeltaR(jets_lv.at(decayJets.at(2).second).first);
				}
				else if(massDiff1 < massDiff2 and massDiff1 < massDiff3)
				{ // lepW + 1 wins
					leptonicTprimeJetIdx = jet2_idx;
					hadronicTprimeJetIdxs = {jet1_idx, jet3_idx};
					leptonicTprimeJetIDs = decayJets.at(1).first;
					hadronicTprimeJetIDs = {decayJets.at(0).first, decayJets.at(2).first};
					Tprime1_lv = W_lv+jets_lv.at(decayJets.at(1).second).first;
					Tprime2_lv = jets_lv.at(decayJets.at(0).second).first+jets_lv.at(decayJets.at(2).second).first;
					Tprime1_deltaR = W_lv.DeltaR(jets_lv.at(decayJets.at(1).second).first);
					Tprime2_deltaR = jets_lv.at(decayJets.at(0).second).first.DeltaR(jets_lv.at(decayJets.at(2).second).first);
				}
				else
				{ // lepW + 2 wins
					leptonicTprimeJetIdx = jet3_idx;
					hadronicTprimeJetIdxs = {jet1_idx, jet2_idx};
					leptonicTprimeJetIDs = decayJets.at(2).first;
					hadronicTprimeJetIDs = {decayJets.at(0).first, decayJets.at(1).first};
					Tprime1_lv = W_lv+jets_lv.at(decayJets.at(2).second).first;
					Tprime2_lv = jets_lv.at(decayJets.at(0).second).first+jets_lv.at(decayJets.at(1).second).first;
					Tprime1_deltaR = W_lv.DeltaR(jets_lv.at(decayJets.at(2).second).first);
					Tprime2_deltaR = jets_lv.at(decayJets.at(0).second).first.DeltaR(jets_lv.at(decayJets.at(2).second).first);
				}
				if(hadronicTprimeJetIDs[0] == 1 && hadronicTprimeJetIDs[1] == 2) tagTDecayMode = 7;
				if(hadronicTprimeJetIDs[0] == 1 && hadronicTprimeJetIDs[1] == 3) tagTDecayMode = 8;
				if(hadronicTprimeJetIDs[0] == 4 && hadronicTprimeJetIDs[1] == 5) tagTDecayMode = 9;
			}
			if(!validBDecay)
			{ // not a valid grouping
				tagBDecayMode = 0;
				if(massDiff3 < massDiff1 and massDiff3 < massDiff2)
				{ // lepW + 0 wins
					leptonicBprimeJetIdx = jet1_idx;
					hadronicBprimeJetIdxs = {jet2_idx, jet3_idx};
					leptonicBprimeJetIDs = decayJets.at(0).first;
					hadronicBprimeJetIDs = {decayJets.at(1).first, decayJets.at(2).first};
					Bprime1_lv = W_lv+jets_lv.at(decayJets.at(0).second).first;
					Bprime2_lv = jets_lv.at(decayJets.at(1).second).first+jets_lv.at(decayJets.at(2).second).first;
					Bprime1_deltaR = W_lv.DeltaR(jets_lv.at(decayJets.at(0).second).first);
					Bprime2_deltaR = jets_lv.at(decayJets.at(1).second).first.DeltaR(jets_lv.at(decayJets.at(2).second).first);
				}
				else if(massDiff1 < massDiff2 and massDiff1 < massDiff3)
				{ // lepW + 1 wins
					leptonicBprimeJetIdx = jet2_idx;
					hadronicBprimeJetIdxs = {jet1_idx, jet3_idx};
					leptonicBprimeJetIDs = decayJets.at(1).first;
					hadronicBprimeJetIDs = {decayJets.at(0).first, decayJets.at(2).first};
					Bprime1_lv = W_lv+jets_lv.at(decayJets.at(1).second).first;
					Bprime2_lv = jets_lv.at(decayJets.at(0).second).first+jets_lv.at(decayJets.at(2).second).first;
					Bprime1_deltaR = W_lv.DeltaR(jets_lv.at(decayJets.at(1).second).first);
					Bprime2_deltaR = jets_lv.at(decayJets.at(0).second).first.DeltaR(jets_lv.at(decayJets.at(2).second).first);
				}
				else
				{ // lepW + 2 wins
					leptonicBprimeJetIdx = jet3_idx;
					hadronicBprimeJetIdxs = {jet1_idx, jet2_idx};
					leptonicBprimeJetIDs = decayJets.at(2).first;
					hadronicBprimeJetIDs = {decayJets.at(0).first, decayJets.at(1).first};
					Bprime1_lv = W_lv+jets_lv.at(decayJets.at(2).second).first;
					Bprime2_lv = jets_lv.at(decayJets.at(0).second).first+jets_lv.at(decayJets.at(1).second).first;
					Bprime1_deltaR = W_lv.DeltaR(jets_lv.at(decayJets.at(2).second).first);
					Bprime2_deltaR = jets_lv.at(decayJets.at(0).second).first.DeltaR(jets_lv.at(decayJets.at(2).second).first);
				}
				if(hadronicBprimeJetIDs[0] == 2 && hadronicBprimeJetIDs[1] == 5) tagBDecayMode = 7;
				if(hadronicBprimeJetIDs[0] == 3 && hadronicBprimeJetIDs[1] == 5) tagBDecayMode = 8;
				if(hadronicBprimeJetIDs[0] == 1 && hadronicBprimeJetIDs[1] == 4) tagBDecayMode = 9;
			}
		}

		if(Tprime1_lv.M() != -999)
		{
			Tprime1_Mass = Tprime1_lv.M();
			Tprime2_Mass = Tprime2_lv.M();
			Tprime1_Pt = Tprime1_lv.Pt();
			Tprime2_Pt = Tprime2_lv.Pt();
			Tprime1_Eta = Tprime1_lv.Eta();
			Tprime2_Eta = Tprime2_lv.Eta();
			Tprime1_Phi = Tprime1_lv.Phi();
			Tprime2_Phi = Tprime2_lv.Phi();
		}
		if(Bprime1_lv.M() != -999)
		{
			Bprime1_Mass = Bprime1_lv.M();
			Bprime2_Mass = Bprime2_lv.M();
			Bprime1_Pt = Bprime1_lv.Pt();
			Bprime2_Pt = Bprime2_lv.Pt();
			Bprime1_Eta = Bprime1_lv.Eta();
			Bprime2_Eta = Bprime2_lv.Eta();
			Bprime1_Phi = Bprime1_lv.Phi();
			Bprime2_Phi = Bprime2_lv.Phi();
		}

		// if(validTDecay){
		// 	std::cout << "Top Masses: " << Tprime1_Mass << ", " << Tprime2_Mass << ", " << tagTDecayMode << endl;
		// }
		// if(validBDecay){
		// 	std::cout << "Bottom Masses: " << Bprime1_Mass << ", " << Bprime2_Mass << ", " << tagBDecayMode << endl;
		// }

		//std::cout << "Leptonic jet id: " << leptonicTprimeJetIdx << ", " << "Hadronic jet id: " << hadronicTprimeJetIdxs << std::endl;
	}
	RVec<float> TandBPrimeVec = {tagTDecayMode, tagBDecayMode, Tprime1_Mass,Tprime2_Mass,Tprime1_Pt,Tprime2_Pt,Tprime1_Eta,Tprime2_Eta,Tprime1_Phi,Tprime2_Phi,Tprime1_deltaR,Tprime2_deltaR,Bprime1_Mass,Bprime2_Mass,Bprime1_Pt,Bprime2_Pt,Bprime1_Eta,Bprime2_Eta,Bprime1_Phi,Bprime2_Phi,Bprime1_deltaR,Bprime2_deltaR,leptonicTprimeJetIDs,leptonicBprimeJetIDs,hadronicTprimeJetIDs[0],hadronicTprimeJetIDs[1],hadronicBprimeJetIDs[0],hadronicBprimeJetIDs[1], float(leptonicTprimeJetIdx), float(hadronicTprimeJetIdxs[0]), float(hadronicTprimeJetIdxs[1]), float(leptonicBprimeJetIdx), float(hadronicBprimeJetIdxs[0]), float(hadronicBprimeJetIdxs[1])};
	return TandBPrimeVec;
}
