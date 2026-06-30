
// ------------------------------------------------------------------------------------------
// 		DEACY/GENTTBAR CALCULATOR:
// 		- Fxn to determine either deacy mode or genTTbarMass depending on file type
// ------------------------------------------------------------------------------------------
//int decayModeSelection_genTTbarMassCalc(unsigned int nGenPart, ROOT::VecOps::RVec<int>& GenPart_pdgId, ROOT::VecOps::RVec<float>& GenPart_mass, ROOT::VecOps::RVec<float>& GenPart_pt, ROOT::VecOps::RVec<float>& GenPart_phi, ROOT::VecOps::RVec<float>& GenPart_eta, ROOT::VecOps::RVec<int>& GenPart_genPartIdxMother, ROOT::VecOps::RVec<int>& GenPart_status)
//{
//	auto lamb = [](TString region)
//	{
//		if(isSig == true){region = "Signal";} // TPrimeTPrime or BPrimeBPrime
//		else if(isTT == true){region = "TTToSemiLeptonic";} // TTToSemiLeptonic
//		return region;
//	};
//	auto decayMode_genTTbarMass_map = ROOT::VecOps::Map(nGenPart, GenPart_pdgId, GenPart_mass, GenPart_pt, GenPart_phi, GenPart_eta, GenPart_genPartIdxMother, GenPart_status, lamb);
//	return decayMode_genTTbarMass_map;
//};
//
//auto decayMode_genTTbarMass_map()
//	int returnVar = 0;
//	if(region == "Signal")
//	{

#include <fstream>

RVec<int> decayModeSelection(unsigned int nGenPart,ROOT::VecOps::RVec<int>& GenPart_pdgId, ROOT::VecOps::RVec<float>& GenPart_mass, ROOT::VecOps::RVec<float>& GenPart_pt, ROOT::VecOps::RVec<float>& GenPart_phi, ROOT::VecOps::RVec<float>& GenPart_eta, ROOT::VecOps::RVec<short>& GenPart_genPartIdxMother, ROOT::VecOps::RVec<int>& GenPart_status)
{
//	int returnVar = 0;
//	if(region == "Signal")
//	{
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
	int VLQ1toT = -99;
	
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
		        VLQ1toT = 1;
		  
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
		        VLQ1toT = 0;
		  
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
		        VLQ1toT = 0;

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
		        VLQ1toT = 1;

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
	decayModes.push_back(VLQ1toT);

	return decayModes;
};

//	else if(region == "TTToSemiLeptonic")
//	{


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
