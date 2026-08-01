auto newDecayModeSelection(unsigned int nGenPart, ROOT::VecOps::RVec<int>& GenPart_pdgId, ROOT::VecOps::RVec<float>& GenPart_mass, ROOT::VecOps::RVec<float>& GenPart_pt, ROOT::VecOps::RVec<float>& GenPart_phi, ROOT::VecOps::RVec<float>& GenPart_eta, ROOT::VecOps::RVec<short>& GenPart_genPartIdxMother, ROOT::VecOps::RVec<int>& GenPart_status, ROOT::VecOps::RVec<short> GenPart_statusFlags)
{
	RVec<int> TdecayMode;
	RVec<int> BdecayMode;
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
	for (int i = 0; i < Ws.size(); i++) {
		index = prev = Ws.at(i);
		
		for (++index;index < nGenPart; index++) {
			if (GenPart_genPartIdxMother[index] == prev) { // Found a child of W!
				child = abs(GenPart_pdgId[index]);

				if (child == 24) { // it's a W
				prev = index;
				} else if (11 <= child && child <= 16) { // it's a lepton!
					Tmode += 100;
					Bmode += 100;
					break;
				} else { break; } // non-leptonic decay
			}
		}
	}

	// t's
	for (int i = 0; i < ts.size(); i++) {
		index = prev = ts.at(i);
		
		for (++index; index < nGenPart; index++) {
			if (GenPart_genPartIdxMother[index] == prev) { // Found a child of t!
				child = abs(GenPart_pdgId[index]);

			if (child == 6) { // it's a t
				prev = index;
				} else if (child == 24) { // it's a W
				prev = index;
				} else if (11 <= child && child <= 16) { // it's a lepton!
					Tmode += 1000;
					Bmode += 1000;
					break;
				} else { break; } // non-leptonic decay
			}
		}
	}

	TdecayMode.push_back(Tmode);
	BdecayMode.push_back(Bmode);

	RVec<RVec<int>> decayModes;
	decayModes.push_back(TdecayMode);
	decayModes.push_back(BdecayMode);

	return decayModes;
}

int genTTbarMassCalc(unsigned int nGenPart, ROOT::VecOps::RVec<int>& GenPart_pdgId, ROOT::VecOps::RVec<float>& GenPart_mass, ROOT::VecOps::RVec<float>& GenPart_pt, ROOT::VecOps::RVec<float>& GenPart_phi, ROOT::VecOps::RVec<float>& GenPart_eta, ROOT::VecOps::RVec<int>& GenPart_genPartIdxMother, ROOT::VecOps::RVec<int>& GenPart_status)
{
	int genTTbarMass = -999;
	double topPtWeight = 1.0;
	TLorentzVector top, antitop;
	bool gottop = false;
	bool gotantitop = false;
	bool gottoppt = false;
	bool gotantitoppt = false;
	float toppt, antitoppt;
	for(unsigned int p = 0; p < nGenPart; p++)
	{
		int id = GenPart_pdgId[p];
		if (abs(id) != 6){continue;}
		if (GenPart_mass[p] < 10){continue;}
		int motherid = GenPart_pdgId[GenPart_genPartIdxMother[p]];
		if(abs(motherid) != 6)
		{
			if (!gottop && id == 6)
			{
				top.SetPtEtaPhiM(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], GenPart_mass[p]);
				gottop = true;
			}
			if (!gotantitop && id == -6)
			{
				antitop.SetPtEtaPhiM(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], GenPart_mass[p]);
				gotantitop = true;
			}
		}
		
		if(GenPart_status[p] == 62)
		{
			if (!gottoppt && id == 6)
			{
				toppt = GenPart_pt[p];
				gottoppt = true;
			}
			if (!gotantitoppt && id == -6)
			{
				antitoppt = GenPart_pt[p];
				gotantitoppt = true;
			}
		}
	}
	if(gottop && gotantitop){genTTbarMass = (top+antitop).M();}
	if(gottoppt && gotantitoppt)
	{
		float SFtop = TMath::Exp(0.0615-0.0005*toppt);
		float SFantitop = TMath::Exp(0.0615-0.0005*antitoppt);
		topPtWeight = TMath::Sqrt(SFtop*SFantitop);
	}
	return genTTbarMass;
//	}
//	return returnVar;
};
