auto newDecayModeSelection(unsigned int nGenPart, ROOT::VecOps::RVec<int>& GenPart_pdgId, ROOT::VecOps::RVec<float>& GenPart_mass, ROOT::VecOps::RVec<float>& GenPart_pt, ROOT::VecOps::RVec<float>& GenPart_phi, ROOT::VecOps::RVec<float>& GenPart_eta, ROOT::VecOps::RVec<short>& GenPart_genPartIdxMother, ROOT::VecOps::RVec<int>& GenPart_status, ROOT::VecOps::RVec<short> GenPart_statusFlags)
{
	RVec<int> decayMode;
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
	int mode = 0;

	// Assign TTbar decay mode
	if(abs(GenPart_pdgId[primes[0]]) == 6000006 && abs(GenPart_pdgId[primes[1]]) == 6000006){
		if(nb == 2 && nW == 2) mode = 1;
		else if(nt == 2 && nZ == 2) mode = 2;
		else if(nt == 2 && nH == 2) mode = 3;
		else if(nt == 2 && nH == 1 && nZ == 1) mode = 4;
		else if(nt == 1 && nZ == 1 && nb == 1 && nW == 1) mode = 5;
		else if(nt == 1 && nH == 1 && nb == 1 && nW == 1) mode = 6;
		else mode = -1;
	}

	// Assign BBbar decay mode
	if(abs(GenPart_pdgId[primes[0]]) == 6000007 && abs(GenPart_pdgId[primes[1]]) == 6000007){
		if(nt == 2 && nW == 2) mode = 7;
		else if(nb == 2 && nZ == 2) mode = 8;
		else if(nb == 2 && nH == 2) mode = 9;
		else if(nb == 2 && nH == 1 && nZ == 1) mode = 10;
		else if(nb == 1 && nZ == 1 && nt == 1 && nW == 1) mode = 11;
		else if(nb == 1 && nH == 1 && nt == 1 && nW == 1) mode = 12;
		else mode = -1;
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
					mode += 100;
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
					mode += 1000;
					break;
				} else { break; } // non-leptonic decay
			}
		}
	}

	decayMode.push_back(mode);

	return decayMode;
}

int nicolasDecayModeSelection(unsigned int nGenPart, ROOT::VecOps::RVec<int>& GenPart_pdgId, ROOT::VecOps::RVec<float>& GenPart_mass, ROOT::VecOps::RVec<float>& GenPart_pt, ROOT::VecOps::RVec<float>& GenPart_phi, ROOT::VecOps::RVec<float>& GenPart_eta, ROOT::VecOps::RVec<short>& GenPart_genPartIdxMother, ROOT::VecOps::RVec<int>& GenPart_status)
{
  //  std::cout << "Hello! Made it to decayModeSelection!" << std::endl;
  std::vector<int> tPrimeID;
  std::vector<int> bPrimeID;
  std::vector<int> listofQuarkIDs;
  std::vector<int> listofBosonIDs;
  std::vector<unsigned int> quarks;
  std::vector<unsigned int> bosons;
  RVec<int> wIDs;
  RVec<int> tIDs;

  bool isBWBW = false;
  bool isTZTZ = false;
  bool isTHTH = false;
  bool isTZTH = false;
  bool isTZBW = false;
  bool isTHBW = false;
  
  bool isTWTW = false;
  bool isBZBZ = false;
  bool isBHBH = false;
  bool isBZBH = false;
  bool isBZTW = false;
  bool isBHTW = false;
  
  int decayMode = 0;
  
  tPrimeID.clear();
  bPrimeID.clear();
  listofQuarkIDs.clear();
  listofBosonIDs.clear();
  quarks.clear();
  bosons.clear();
  wIDs.clear();
  tIDs.clear();

  // format of decayMode: [0-2 leptonic t's] [0-2 leptonic W's] [0-11 Bprime and Tprime decay modes]

  for(unsigned int p = 0; p < nGenPart; p++)
    {
      int id=GenPart_pdgId[p];
      // find T' and B' particles
      if(abs(id) != 6000006 && abs(id) != 6000007){continue;}
      
      bool hasTdaughter = false;
      vector<unsigned int> daughters;
      daughters.clear();
      for(unsigned int  dau = 0; dau < nGenPart; dau++)
  	{
  	if(GenPart_genPartIdxMother[dau]!=p){continue;}
  	daughters.push_back(dau);
  	if(abs(id) == 6000006 && abs(GenPart_pdgId[dau]) == 6000006){hasTdaughter = true;}
  	if(abs(id) == 6000007 && abs(GenPart_pdgId[dau]) == 6000007){hasTdaughter = true;}
  	}
      if(hasTdaughter){continue;}
      int mother = GenPart_genPartIdxMother[p];
      int mother_id = GenPart_pdgId[mother];
      if(abs(id) == 6000006)
  	{
  	if(abs(mother_id) == 6000006){tPrimeID.push_back(GenPart_pdgId[mother]);}
  	else{tPrimeID.push_back(GenPart_pdgId[p]);}
  	}
      if(abs(id) == 6000007)
  	{
  	if(abs(mother_id) == 6000007){bPrimeID.push_back(GenPart_pdgId[mother]);}
  	else{bPrimeID.push_back(GenPart_pdgId[p]);}
  	}
      for(unsigned int j = 0; j < daughters.size(); j++)
  	{
  	unsigned int d = daughters.at(j);
  	int dauId = GenPart_pdgId[d];
  	if(abs(dauId) == 5 || abs(dauId) == 6)
  	  {
  	    quarks.push_back(d);
  	    listofQuarkIDs.push_back(dauId);
  	  }
  	else if(abs(dauId) > 22 && abs(dauId) < 26)
  	  {
  	    bosons.push_back(d);
  	    listofBosonIDs.push_back(dauId);
  	  }
  	else{continue;}
  	}
    }
  
  if(tPrimeID.size() > 0 && bPrimeID.size() > 0) {std::cout << "Found both T' and B' " << std::endl;}
  if(listofQuarkIDs.size() != 0 && listofQuarkIDs.size() != 2)
    {
      std::cout << "More/less than 2 quarks stored: " << listofQuarkIDs.size() << std::endl;
      for(unsigned int i = 0; i < listofQuarkIDs.size(); i++){std::cout << "quark " << i << " = " << listofQuarkIDs.at(i) << std::endl;}
      int test = listofQuarkIDs.at(0)*listofQuarkIDs.at(1);
      int sign = -1;
      if(test > 0){sign = 1;}
      if(sign > 0)
  	{
  	if(listofQuarkIDs.size() == 4)
  	  {
  	    std::swap(listofQuarkIDs.at(2),listofQuarkIDs.at(3));
  	    std::swap(quarks.at(2),quarks.at(3));
  	  }
  	std::swap(listofQuarkIDs.at(1),listofQuarkIDs.at(2));
  	std::swap(quarks.at(1),quarks.at(2));
  	test = listofQuarkIDs.at(0)*listofQuarkIDs.at(1);
  	sign = -1;
  	if(test > 0){sign = 1;}
  	if(sign < 0){std::cout << "Signs are fixed!" << std::endl;}
  	}
      if(listofQuarkIDs.size() > 3 && abs(listofQuarkIDs.at(3)) == 6)
  	{
  	std::swap(listofQuarkIDs.at(2),listofQuarkIDs.at(3));
  	std::swap(quarks.at(2),quarks.at(3));
  	}
      if(listofQuarkIDs.size() > 2 && abs(listofQuarkIDs.at(2)) == 6)
  	{
  	std::swap(listofQuarkIDs.at(1),listofQuarkIDs.at(2));
  	std::swap(quarks.at(1),quarks.at(2));
  	}
    }
  if(listofBosonIDs.size() != 0 && listofBosonIDs.size() != 2)
    {
      std::cout << "More/less than 2 bosons stored: " << listofBosonIDs.size() << std::endl;
    }
  // tag the decay chains according to ID'd quarks and bosons.
  
  // TPrime Decay Mode Selector
  if(tPrimeID.size() > 1 && bPrimeID.size() == 0)
    {
      if(abs(listofQuarkIDs.at(0)) == 5 && abs(listofQuarkIDs.at(1)) == 5)
  	{
  	if(abs(listofBosonIDs.at(0)) == 24 && abs(listofBosonIDs.at(1)) == 24)
  	  {
  	    isBWBW = true;
  	    decayMode = 1; // BWBW ID!
	    wIDs.push_back(bosons.at(0));
	    wIDs.push_back(bosons.at(1));
  	  }
  	}
      // 2 t quarks, check for Z's and H's
      else if(abs(listofQuarkIDs.at(0)) == 6 && abs(listofQuarkIDs.at(1)) == 6)
  	{
	tIDs.push_back(quarks.at(0));
	tIDs.push_back(quarks.at(1));
  	if(listofBosonIDs.at(0) == 23 && listofBosonIDs.at(1) == 23)
  	  {
  	    isTZTZ = true;
  	    decayMode = 2; // TZTZ ID!
  	  }
  	else if(listofBosonIDs.at(0) == 25 && listofBosonIDs.at(1) == 25)
  	  {
  	    isTHTH = true;
  	    decayMode = 3; // THTH ID!
  	  }
  	else if(listofBosonIDs.at(0) == 25 && listofBosonIDs.at(1) == 23)
  	  {
  	    isTZTH = true;
  	    decayMode = 4; //TZTH ID!
  	  }
  	else if(listofBosonIDs.at(0) == 23 && listofBosonIDs.at(1) == 25)
  	  {
  	    isTZTH = true;
  	    decayMode = 4; // TZTH ID!
  	  }
  	else
  	  {
  	    std::cout << "2 t daughters didn't match tZtZ, tHtH, or tZtH" << listofBosonIDs.at(0) << ", " << listofBosonIDs.at(1) << std::endl;
  	  }
  	}
      // t-b pairs, check for correlating bosons in the right spots
      else if(abs(listofQuarkIDs.at(0)) == 6 && abs(listofQuarkIDs.at(1)) == 5)
  	{
	tIDs.push_back(quarks.at(0));
  	if(listofBosonIDs.at(0) == 23 && abs(listofBosonIDs.at(1)) == 24)
  	  {
  	    isTZBW = true;
  	    decayMode = 5; // TZBW ID!
	    wIDs.push_back(bosons.at(1));
  	  }
  	else if(listofBosonIDs.at(0) == 25 && abs(listofBosonIDs.at(1)) == 24)
  	  {
  	    isTHBW = true;
  	    decayMode = 6; // THBW ID!
	    wIDs.push_back(bosons.at(1));
  	  }
  	else{std::cout<< "t - b pair didn't match Z/H - W pair" << listofBosonIDs.at(0)<<", "<<listofBosonIDs.at(1) << std::endl;}
  	}
      // b-t pairs, check for correlating bosons in the right spots
      else if(abs(listofQuarkIDs.at(1)) == 6 && abs(listofQuarkIDs.at(0)) == 5)
  	{
	tIDs.push_back(quarks.at(1));
  	if(listofBosonIDs.at(1) == 23 && abs(listofBosonIDs.at(0)) == 24)
  	  {
  	    isTZBW = true;
  	    decayMode = 5; // TZBW ID!
	    wIDs.push_back(bosons.at(0));
  	  }
  	else if(listofBosonIDs.at(1) == 25 && abs(listofBosonIDs.at(0)) == 24)
  	  {
  	    isTHBW = true;
  	    decayMode = 6; //THBW ID!
	    wIDs.push_back(bosons.at(0));
  	  }
  	else{std::cout<< "b - t pair didn't match W - Z/H pair" << listofBosonIDs.at(0)<<", "<<listofBosonIDs.at(1) << std::endl;}
  	}
      // error messages if we found something else entirely
      else
  	{
  	std::cout << "T' daughters didn't match a recognized pattern" << std::endl;
  	for(size_t i = 0; i < listofQuarkIDs.size(); i++)
  	  {
  	    std::cout << "quark " << i << " = " << listofQuarkIDs.at(i) << std::endl;
  	  }
  	for(size_t i = 0; i < listofBosonIDs.size(); i++)
  	  {
  	    std::cout << "boson " << i << " = " << listofBosonIDs.at(i) << std::endl;
  	  }
  	decayMode = -1;
  	}
    }
  // BPrime Decay Mode Selector
  if(bPrimeID.size() > 1 && tPrimeID.size() == 0)
    {
      // 2 t quarks, check for matching W's
      if(abs(listofQuarkIDs.at(0)) == 6 && abs(listofQuarkIDs.at(1)) == 6)
  	{
	tIDs.push_back(quarks.at(0));
	tIDs.push_back(quarks.at(1));
  	if(abs(listofBosonIDs.at(0)) == 24 && abs(listofBosonIDs.at(1)) == 24)
  	  {
  	    isTWTW = true;
  	    decayMode = 7; // TWTW ID!
	    wIDs.push_back(bosons.at(0));
	    wIDs.push_back(bosons.at(1));
  	  }
  	else{std::cout<< "2 t daughters didn't match tWtW: " <<listofBosonIDs.at(0)<<", "<<listofBosonIDs.at(1) << std::endl;}
  	}
      // 2 b quarks, check for Z's and H's
      else if(abs(listofQuarkIDs.at(0)) == 5 && abs(listofQuarkIDs.at(1)) == 5)
  	{
  	if(listofBosonIDs.at(0) == 23 && listofBosonIDs.at(1) == 23)
  	  {
  	    isBZBZ = true;
  	    decayMode = 8; // BZBZ ID!
  	  }
  	else if(listofBosonIDs.at(0) == 25 && listofBosonIDs.at(1) == 25)
  	  {
  	    isBHBH = true;
  	    decayMode = 9; // BHBH ID!
  	  }
  	else if(listofBosonIDs.at(0) == 25 && listofBosonIDs.at(1) == 23)
  	  {
  	    isBZBH = true;
  	    decayMode = 10; // BZBH ID!
  	  }
  	else if(listofBosonIDs.at(0) == 23 && listofBosonIDs.at(1) == 25)
  	  {
  	    isBZBH = true;
  	    decayMode = 10; //BZBH ID!
  	  }
  	else
  	  {
  	    std::cout << "2 b daughters didn't match bZbZ, bHbH, or bZbH" << listofBosonIDs.at(0) << ", " << listofBosonIDs.at(1) << std::endl;
  	  }
  	}
      // b-t pairs, check for correlating bosons in the right spots
      else if(abs(listofQuarkIDs.at(0)) == 5 && abs(listofQuarkIDs.at(1)) == 6)
  	{
	tIDs.push_back(quarks.at(1));
  	if(listofBosonIDs.at(0) == 23 && abs(listofBosonIDs.at(1)) == 24)
  	  {
  	    isBZTW = true;
  	    decayMode = 11; // BZTW ID!
	    wIDs.push_back(bosons.at(1));
  	  }
  	else if(listofBosonIDs.at(0) == 25 && abs(listofBosonIDs.at(1)) == 24)
  	  {
  	    isBHTW = true;
  	    decayMode = 12; // BHTW ID!
	    wIDs.push_back(bosons.at(1));
  	  }
  	else{std::cout<< "b - t pair didn't match Z/H - W pair" << listofBosonIDs.at(0)<<", "<<listofBosonIDs.at(1) << std::endl;}
  	}
      // t-b pairs, check for correlating bosons in the right spots
      else if(abs(listofQuarkIDs.at(1)) == 5 && abs(listofQuarkIDs.at(0)) == 6)
  	{
	tIDs.push_back(quarks.at(0));
  	if(listofBosonIDs.at(1) == 23 && abs(listofBosonIDs.at(0)) == 24)
  	  {
  	    isBZTW = true;
  	    decayMode = 11; // BZTW ID!
	    wIDs.push_back(bosons.at(0));
  	  }
  	else if(listofBosonIDs.at(1) == 25 && abs(listofBosonIDs.at(0)) == 24)
  	  {
  	    isBHTW = true;
  	    decayMode = 12; // BHTW ID!
	    wIDs.push_back(bosons.at(0));
  	  }
  	else{std::cout<< "t - b pair didn't match W - Z/H pair" << listofBosonIDs.at(0)<<", "<<listofBosonIDs.at(1) << std::endl;}
      }
      // error messages if we found something else entirely
      else
      {
  	std::cout << "B' daughters didn't match a recognized pattern" << std::endl;
  	for(size_t i = 0; i < listofQuarkIDs.size(); i++)
  	  {
  	    std::cout << "quark " << i << " = " << listofQuarkIDs.at(i) << std::endl;
  	  }
  	for(size_t i = 0; i < listofBosonIDs.size(); i++)
  	  {
  	    std::cout << "boson " << i << " = " << listofBosonIDs.at(i) << std::endl;
  	  }
  	decayMode = -1;
     }
  }

  if (decayMode < 0) { return decayMode; }
  
  //std::cout << "# of Ws, # of ts" << wIDs << ", " << tIDs << std::endl;
  // Look for leptons from W's and t's
  int index, prev, child;
  // W's
  for (int i = 0; i < wIDs.size(); i++) {
    index = prev = wIDs.at(i);
    
    for (++index;index < nGenPart; index++) {
      if (GenPart_genPartIdxMother[index] == prev) { // Found a child of W!
        child = abs(GenPart_pdgId[index]);

	if (child == 24) { // it's a W
	  prev = index;
	} else if (11 <= child && child <= 16) { // it's a lepton!
          decayMode += 100;
	  break;
	} else { break; } // non-leptonic decay
      }
    }
  }

  // t's
  for (int i = 0; i < tIDs.size(); i++) {
    index = prev = tIDs.at(i);
    
    for (++index; index < nGenPart; index++) {
      if (GenPart_genPartIdxMother[index] == prev) { // Found a child of t!
        child = abs(GenPart_pdgId[index]);

	if (child == 6) { // it's a t
	  prev = index;
	} else if (child == 24) { // it's a W
	  prev = index;
	} else if (11 <= child && child <= 16) { // it's a lepton!
          decayMode += 1000;
	  break;
	} else { break; } // non-leptonic decay
      }
    }
  }

  //  std::cout << "Returning decayMode = " << decayMode << std::endl;
  return decayMode;
}

#include <fstream>

RVec<int> decayModeSelection(unsigned int nGenPart,ROOT::VecOps::RVec<int>& GenPart_pdgId, ROOT::VecOps::RVec<float>& GenPart_mass, ROOT::VecOps::RVec<float>& GenPart_pt, ROOT::VecOps::RVec<float>& GenPart_phi, ROOT::VecOps::RVec<float>& GenPart_eta, ROOT::VecOps::RVec<short>& GenPart_genPartIdxMother, ROOT::VecOps::RVec<int>& GenPart_status)
{

	std::vector<int> tPrimeID;
	std::vector<int> bPrimeID;
	std::vector<int> listofQuarkIDs;
	std::vector<int> listofBosonIDs;
	std::vector<unsigned int> quarks;
	std::vector<unsigned int> bosons;
	
	bool isBWBW = false;
	bool isTZTZ = false;
	bool isTHTH = false;
	bool isTZTH = false;
	bool isTZBW = false;
	bool isTHBW = false;
	
	bool isTWTW = false;
	bool isBZBZ = false;
	bool isBHBH = false;
	bool isBZBH = false;
	bool isBZTW = false;
	bool isBHTW = false;
	
	int decayMode = 0;
	
	tPrimeID.clear();
	bPrimeID.clear();
	listofQuarkIDs.clear();
	listofBosonIDs.clear();
	quarks.clear();
	bosons.clear();
	
	// ofstream decayFile;
	// decayFile.open("decayOutput.txt", std::ios_base::app);

	for(unsigned int p = 0; p < nGenPart; p++)
	{
		int id=GenPart_pdgId[p];
		//find T' and B' particles
		if(abs(id) != 6000006 && abs(id) != 6000007){continue;}
		bool hasTdaughter = false;
		vector<unsigned int> daughters;
		daughters.clear();
		for(unsigned int  dau = 0; dau < nGenPart; dau++)
		{
			if(GenPart_genPartIdxMother[dau]!=p ){continue;}
			daughters.push_back(dau);
			if(abs(id) == 6000006 && abs(GenPart_pdgId[dau]) == 6000006){hasTdaughter = true;}
			if(abs(id) == 6000007 && abs(GenPart_pdgId[dau]) == 6000007){hasTdaughter = true;}
		}
		if(hasTdaughter){continue;}
		int mother = GenPart_genPartIdxMother[p];
		int mother_id = GenPart_pdgId[mother];
		if(abs(id) == 6000006)
		{
			//std::cout << "\t Found a T'!" << std::endl;
			if(abs(mother_id) == 6000006){
				tPrimeID.push_back(GenPart_pdgId[mother]);
			}
			else{tPrimeID.push_back(GenPart_pdgId[p]);}
		}
		if(abs(id) == 6000007)
		{
			if(abs(mother_id) == 6000007){bPrimeID.push_back(GenPart_pdgId[mother]);}
			else{bPrimeID.push_back(GenPart_pdgId[p]);}
		}
		//std::cout << "\t \t Number of daughters is: " << daughters.size() << std::endl;
		//std::cout << "\t \t Daughters are: " << GenPart_pdgId[daughters.at(0)] << ", " << GenPart_pdgId[daughters.at(1)] << std::endl;
		for(unsigned int j = 0; j < daughters.size(); j++)
		{
			//std::cout << "\t Made it into the quark for loop" << std::endl;
			unsigned int d = daughters.at(j);
			int dauId = GenPart_pdgId[d];
			if(abs(dauId) == 5 || abs(dauId) == 6)
			{
				quarks.push_back(d);
				listofQuarkIDs.push_back(dauId);
				//std::cout << "\t \t Quarks: Pushed back a: " << dauId << std::endl;
			}
			else if(abs(dauId) > 22 && abs(dauId) < 26)
			{
				bosons.push_back(d);
				listofBosonIDs.push_back(dauId);
				//std::cout << "\t \t Bosons: Pushed back a: "<< dauId << std::endl;
			}
			else{std::cout << "SOMETHING WEIRD HAS HAPPENED IN FINDING DECAY PRODUCTS" << std::endl; continue;}
		}
	}
	// std::cout << "Quark length, Boson length: " << quarks.size() << ", " << bosons.size() << std::endl;
	//if(tPrimeID.size() > 0) {std::cout << "Entering Swaps" << std::endl;}
	if(listofQuarkIDs.size() != 0 && listofQuarkIDs.size() != 2)
	{
		// std::cout << "More/less than 2 quarks stored: " << listofQuarkIDs.size() << std::endl;
		int test = listofQuarkIDs.at(0)*listofQuarkIDs.at(1);
		int sign = -1;
		if(test > 0){sign = 1;} // Cai: Why do we bother with sign? just see if test > 0
		if(sign > 0)
		{
			if(listofQuarkIDs.size() == 4)
			{
				std::swap(listofQuarkIDs.at(2),listofQuarkIDs.at(3));
				std::swap(quarks.at(2),quarks.at(3));
			}
			std::swap(listofQuarkIDs.at(1),listofQuarkIDs.at(2));
			std::swap(quarks.at(1),quarks.at(2));
			test = listofQuarkIDs.at(0)*listofQuarkIDs.at(1);
			sign = -1;
			if(test > 0){sign = 1;}
		}
		if(listofQuarkIDs.size() > 3 && abs(listofQuarkIDs.at(3)) == 6)
		{
			std::swap(listofQuarkIDs.at(2),listofQuarkIDs.at(3));
			std::swap(quarks.at(2),quarks.at(3));
		}
		if(listofQuarkIDs.size() > 2 && abs(listofQuarkIDs.at(2)) == 6)
		{
			std::swap(listofQuarkIDs.at(1),listofQuarkIDs.at(2));
			std::swap(quarks.at(1),quarks.at(2));
		}
	}
	if(listofBosonIDs.size() != 0 && listofBosonIDs.size() != 2)
	{
		// std::cout << "More/less than 2 bosons stored: " << listofBosonIDs.size() << std::endl;
	}
	
	// ----------------------------------------------------------
	// tag the decay chains according to ID'd quarks and bosons.
	// -----------------------------------------------------------
	
	// TPrime Decay Mode Selector
	if(tPrimeID.size() > 1 && bPrimeID.size() == 0)
	// std::cout << "Made it to Decay mode selector" << std::endl;
	{
		if(abs(listofQuarkIDs.at(0)) == 5 && abs(listofQuarkIDs.at(1)) == 5)
		{
			if(abs(listofBosonIDs.at(0)) == 24 && abs(listofBosonIDs.at(1)) == 24)
			{
				isBWBW = true;
				decayMode = 1; // BWBW ID!
			}
		}
		// 2 t quarks, check for Z's and H's
		else if(abs(listofQuarkIDs.at(0)) == 6 && abs(listofQuarkIDs.at(1)) == 6)
		{
			if(listofBosonIDs.at(0) == 23 && listofBosonIDs.at(1) == 23)
			{
				isTZTZ = true;
				decayMode = 2; // TZTZ ID!
			}
			else if(listofBosonIDs.at(0) == 25 && listofBosonIDs.at(1) == 25)
			{
				isTHTH = true;
				decayMode = 3; // THTH ID!
			}
			else if(listofBosonIDs.at(0) == 25 && listofBosonIDs.at(1) == 23)
			{
				isTZTH = true;
				decayMode = 4; //TZTH ID!
			}
			else if(listofBosonIDs.at(0) == 23 && listofBosonIDs.at(1) == 25)
			{
				isTZTH = true;
				decayMode = 4; // TZTH ID!
			}
		}
		// t-b pairs, check for correlating bosons in the right spots
		else if(abs(listofQuarkIDs.at(0)) == 6 && abs(listofQuarkIDs.at(1)) == 5)
		{		  
		        if(listofBosonIDs.at(0) == 23 && abs(listofBosonIDs.at(1)) == 24)
			{
				isTZBW = true;
				decayMode = 5; // TZBW ID!
				
			}
			else if(listofBosonIDs.at(0) == 25 && abs(listofBosonIDs.at(1)) == 24)
			{
				isTHBW = true;
				decayMode = 6; // THBW ID!
			}
		}
		// b-t pairs, check for correlating bosons in the right spots
		else if(abs(listofQuarkIDs.at(1)) == 6 && abs(listofQuarkIDs.at(0)) == 5)
		{		  
			if(listofBosonIDs.at(1) == 23 && abs(listofBosonIDs.at(0)) == 24)
			{
				isTZBW = true;
				decayMode = 5; // TZBW ID!
			}
			else if(listofBosonIDs.at(1) == 25 && abs(listofBosonIDs.at(0)) == 24)
			{
				isTHBW = true;
				decayMode = 6; //THBW ID!
			}
		}
		// error messages if we found something else entirely
		else
		{
			decayMode = -1;
		}
		// std::cout << decayMode << std::endl;
		// decayFile  << decayMode << "\n";
	}
	// BPrime Decay Mode Selector
	if(bPrimeID.size() > 1 && tPrimeID.size() == 0)
	{
		// 2 t quarks, check for matching W's
		if(abs(listofQuarkIDs.at(0)) == 6 && abs(listofQuarkIDs.at(1)) == 6)
		{ 
			if(abs(listofBosonIDs.at(0)) == 24 && abs(listofBosonIDs.at(1)) == 24)
			{
				isTWTW = true;
				decayMode = 1; // TWTW ID!
			}
		}
		// 2 b quarks, check for Z's and H's
		else if(abs(listofQuarkIDs.at(0)) == 5 && abs(listofQuarkIDs.at(1)) == 5)
		{
			if(listofBosonIDs.at(0) == 23 && listofBosonIDs.at(1) == 23)
			{
				isBZBZ = true;
				decayMode = 2; // BZBZ ID!
			}
			else if(listofBosonIDs.at(0) == 25 && listofBosonIDs.at(1) == 25)
			{
				isBHBH = true;
				decayMode = 3; // BHBH ID!
			}
			else if(listofBosonIDs.at(0) == 25 && listofBosonIDs.at(1) == 23)
			{
				isBZBH = true;
				decayMode = 4; // BZBH ID!
			}
			else if(listofBosonIDs.at(0) == 23 && listofBosonIDs.at(1) == 25)
			{
				isBZBH = true;
				decayMode = 4; //BZBH ID!
			}
		}
		// b-t pairs, check for correlating bosons in the right spots
		else if(abs(listofQuarkIDs.at(0)) == 5 && abs(listofQuarkIDs.at(1)) == 6)
		{
		        if(listofBosonIDs.at(0) == 23 && abs(listofBosonIDs.at(1)) == 24)
			{
				isBZTW = true;
				decayMode = 5; // BZTW ID!
			}
			else if(listofBosonIDs.at(0) == 25 && abs(listofBosonIDs.at(1)) == 24)
			{
				isBHTW = true;
				decayMode = 6; // BHTW ID!
			}
		}
		// t-b pairs, check for correlating bosons in the right spots
		else if(abs(listofQuarkIDs.at(1)) == 5 && abs(listofQuarkIDs.at(0)) == 6)
		{
		        if(listofBosonIDs.at(1) == 23 && abs(listofBosonIDs.at(0)) == 24)
			{
				isBZTW = true;
				decayMode = 5; // BZTW ID!
			}
			else if(listofBosonIDs.at(1) == 25 && abs(listofBosonIDs.at(0)) == 24)
			{
				isBHTW = true;
				decayMode = 6; // BHTW ID!
			}
		}
		// error messages if we found something else entirely
		else
		{
			decayMode = -1;
		}
	}
	//decayFile.close();
	RVec<int> decayModes;
	decayModes.push_back(decayMode);

	return decayModes;
};

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
