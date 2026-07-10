// Methods in this file:  		There are several corrlib functions and some non corrlib functions.
// goldenjson() pufunc() jetidfunc() fatjetidfunc recofunc() idfunc() isofunc() metfunc() hltfunc() jetvetofunc() 
// additionally, elrecofunc(), elidfunc(), muidfunc(), muisofunc(), tauefunc(), taumufunc(), taujetfunc(), btagshapefunc(), METptfunc(), METphifunc()

using namespace ROOT::VecOps;
using namespace std;

// Make sure the run passes the json? //TODO better explanation
bool goldenjson(lumiMask myLumiMask, const unsigned int &run, const unsigned int &luminosityBlock)
{
  return myLumiMask.accept(run, luminosityBlock);
}; 

// ------------ the order is nom/f, up, down for the scale factors--------------

// Pile Up Function
RVec<double> pufunc(correction::Correction::Ref& pileupcorr, const float &numTrueInt) {
  RVec<double> pu = {pileupcorr->evaluate({numTrueInt, "nominal"}), pileupcorr->evaluate({numTrueInt, "up"}), pileupcorr->evaluate({numTrueInt, "down"})};
  return pu;
};

//JetID Function 0: ~T ~TL, 2: T ~TL, 6: T TL
RVec<float> jetidfunc(correction::Correction::Ref& tightcorr,correction::Correction::Ref& tightlepcorr,const RVec<float>& eta,const RVec<float>& chHEF,const RVec<float>& neHEF,const RVec<float>& chEmEF,const RVec<float>& neEmEF,const RVec<float>& muEF,const RVec<unsigned char>& chMultiplicity,const RVec<unsigned char>& neMultiplicity){
  RVec<float> TorTLvec;

  for(unsigned int ijet = 0; ijet < eta.size(); ijet++){
    float TorTL = -1.0;
    int mult = int(chMultiplicity.at(ijet)) + int(neMultiplicity.at(ijet));

    float jetidTL = tightlepcorr->evaluate({eta.at(ijet),chHEF.at(ijet),neHEF.at(ijet),chEmEF.at(ijet),neEmEF.at(ijet),muEF.at(ijet),int(chMultiplicity.at(ijet)),int(neMultiplicity.at(ijet)),mult});

    if(jetidTL == 1) {
      TorTL = 6;
    }else{
      float jetidT = tightcorr->evaluate({abs(eta.at(ijet)),chHEF.at(ijet),neHEF.at(ijet),chEmEF.at(ijet),neEmEF.at(ijet),muEF.at(ijet),int(chMultiplicity.at(ijet)),int(neMultiplicity.at(ijet)),mult});
      if(jetidT == 1){
	TorTL = 2;
      }else{
	TorTL = 0;
      }
    }
    TorTLvec.push_back(TorTL);
  }

  return TorTLvec;
};

//FatJetID Function 0: ~T ~TL, 2: T ~TL, 6: T TL
RVec<double> fatjetidfunc(correction::Correction::Ref& tightcorr,correction::Correction::Ref& tightlepcorr,RVec<float>& eta, RVec<float>& chHEF,RVec<float>& neHEF,RVec<float>& chEmEF,RVec<float>& neEmEF,RVec<float>& muEF,RVec<short>& chMultiplicity,RVec<short>& neMultiplicity){
  RVec<float> TorTLvec;
  
  for(unsigned int ijet = 0; ijet < eta.size(); ijet++){
    float TorTL = -1.0;
    int mult = int(chMultiplicity.at(ijet)) + int(neMultiplicity.at(ijet));
    
    float jetidTL = tightlepcorr->evaluate({eta.at(ijet),chHEF.at(ijet),neHEF.at(ijet),chEmEF.at(ijet),neEmEF.at(ijet),muEF.at(ijet),int(chMultiplicity.at(ijet)),int(neMultiplicity.at(ijet)),mult});

    if(jetidTL == 1) {
      TorTL = 6;
    }else{
      float jetidT = tightcorr->evaluate({abs(eta.at(ijet)),chHEF.at(ijet),neHEF.at(ijet),chEmEF.at(ijet),neEmEF.at(ijet),muEF.at(ijet),int(chMultiplicity.at(ijet)),int(neMultiplicity.at(ijet)),mult});
      if(jetidT == 1){
	TorTL = 2;
      }else{
	TorTL = 0;
      }
    }
    TorTLvec.push_back(TorTL);
  }

  return TorTLvec;
};

//MET pt function
RVec<float> METptfunc(correction::Correction::Ref& METcorr, string METyr, bool isMC, const float pt, const float phi, float npv) {
	RVec<float> ptVec = {1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0};
	string DtMc;
	if (isMC) DtMc = "MC";
	else DtMc = "DATA";

	ptVec[0] = METcorr->evaluate({"pt", "PuppiMET", METyr, DtMc, "nom", pt, phi, npv});
	ptVec[1] = METcorr->evaluate({"pt", "PuppiMET", METyr, DtMc, "pu_up", pt, phi, npv});
	ptVec[2] = METcorr->evaluate({"pt", "PuppiMET", METyr, DtMc, "pu_dn", pt, phi, npv});
	ptVec[3] = METcorr->evaluate({"pt_stat_xup", "PuppiMET", METyr, DtMc, "nom", pt, phi, npv});
	ptVec[4] = METcorr->evaluate({"pt_stat_xdn", "PuppiMET", METyr, DtMc, "nom", pt, phi, npv});
	ptVec[5] = METcorr->evaluate({"pt_stat_yup", "PuppiMET", METyr, DtMc, "nom", pt, phi, npv});
	ptVec[6] = METcorr->evaluate({"pt_stat_ydn", "PuppiMET", METyr, DtMc, "nom", pt, phi, npv});
	
	return ptVec;

}

//MET phi function
RVec<float> METphifunc(correction::Correction::Ref& METcorr, string METyr, bool isMC, const float pt, const float phi, float npv) {
	RVec<float> phiVec = {1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0};
	string DtMc;
	if (isMC) DtMc = "MC";
	else DtMc = "DATA";
		
	phiVec[0] = METcorr->evaluate({"phi", "PuppiMET", METyr, DtMc, "nom", pt, phi, npv});
	phiVec[1] = METcorr->evaluate({"phi", "PuppiMET", METyr, DtMc, "pu_up", pt, phi, npv});
	phiVec[2] = METcorr->evaluate({"phi", "PuppiMET", METyr, DtMc, "pu_dn", pt, phi, npv});
	phiVec[3] = METcorr->evaluate({"phi_stat_xup", "PuppiMET", METyr, DtMc, "nom", pt, phi, npv});
	phiVec[4] = METcorr->evaluate({"phi_stat_xdn", "PuppiMET", METyr, DtMc, "nom", pt, phi, npv});
	phiVec[5] = METcorr->evaluate({"phi_stat_yup", "PuppiMET", METyr, DtMc, "nom", pt, phi, npv});
	phiVec[6] = METcorr->evaluate({"phi_stat_ydn", "PuppiMET", METyr, DtMc, "nom", pt, phi, npv});
	
	return phiVec;
}


//Electron Reco Function
RVec<float> elrecofunc(correction::Correction::Ref& electroncorr, string elecyr, RVec<float> &pt, RVec<float> &eta, RVec<float> &phi, RVec<int> &ID) {
	RVec<float> el = {1.0, 1.0, 1.0};
	string reco;
	for(int i = 0; i < pt.size(); i++) {
		float eval_pt = pt[i]; // Create a copy of the pT to safely modify for evaluation
		if (pt[i] < 20) {
		  if (elecyr == "2025Prompt") {reco = "Reco20to75"; eval_pt = 20.01;}    //2025 does not have RecoBelow20
		  else {reco = "RecoBelow20";}
		} 
		else if (pt[i] >= 20 && pt[i] <= 75) {reco = "Reco20to75";} 
		else if (pt[i] > 75) {reco = "RecoAbove75";}
		
		if (ID[i] != 11) {continue;} //skip muons and taus
		if (i > 3) {continue;} //skip leptons past the first 4 for mass reco
	
		if (elecyr == "2022Re-recoBCD" || elecyr == "2022Re-recoE+PromptFG" || elecyr == "2024Prompt"|| elecyr == "2025Prompt") {
			el[0] *= electroncorr->evaluate({elecyr, "sf", reco, eta[i], eval_pt}); 
			el[1] *= electroncorr->evaluate({elecyr, "sfup", reco, eta[i], eval_pt}); 
			el[2] *= electroncorr->evaluate({elecyr, "sfdown", reco, eta[i], eval_pt});
		}
		else {
			el[0] *= electroncorr->evaluate({elecyr, "sf", reco, eta[i], eval_pt, phi[i]}); 
			el[1] *= electroncorr->evaluate({elecyr, "sfup", reco, eta[i], eval_pt, phi[i]}); 
			el[2] *= electroncorr->evaluate({elecyr, "sfdown", reco, eta[i], eval_pt, phi[i]});
		}
	}
	
	return el;	
}

//Overloaded Electron Reconstruction Function
RVec<float> elrecofunc(correction::Correction::Ref& electroncorr,string elecyr,float pt,float eta,float phi,int ID) {
  RVec<float> Vpt = {pt};
  RVec<float> Veta = {eta};
  RVec<float> Vphi = {phi};
  RVec<int> VID = {ID};
  return elrecofunc(electroncorr,elecyr,Vpt,Veta,Vphi,VID);
}


//Electron ID Function (wp80iso)
RVec<float> elidfunc(correction::Correction::Ref& electroncorr, string elecyr, string elecidWP, RVec<float> &pt, RVec<float> &eta, RVec<float> &phi, RVec<int> &ID) {
	RVec<float> el = {1.0, 1.0, 1.0};
	for(int i = 0; i < pt.size(); i++) {
		if (ID[i] != 11) {continue;} //skip muons and taus
		if (i > 3) {continue;} //skip leptons past the first 4 for mass reco
		
		if (elecyr == "2022Re-recoBCD" || elecyr == "2022Re-recoE+PromptFG" || elecyr == "2024Prompt"|| elecyr == "2025Prompt") {
			el[0] *= electroncorr->evaluate({elecyr, "sf", elecidWP, eta[i], pt[i]}); 
			el[1] *= electroncorr->evaluate({elecyr, "sfup", elecidWP, eta[i], pt[i]}); 
			el[2] *= electroncorr->evaluate({elecyr, "sfdown", elecidWP, eta[i], pt[i]});
		}
		else {
			el[0] *= electroncorr->evaluate({elecyr, "sf", elecidWP, eta[i], pt[i], phi[i]}); 
			el[1] *= electroncorr->evaluate({elecyr, "sfup", elecidWP, eta[i], pt[i], phi[i]}); 
			el[2] *= electroncorr->evaluate({elecyr, "sfdown", elecidWP, eta[i], pt[i], phi[i]});
		}
	}		
	
	return el;	
}

//Overloaded Electron ID Function
RVec<float> elidfunc(correction::Correction::Ref& electroncorr,string elecyr,string elecidWP,float pt,float eta,float phi,int ID) {
  RVec<float> Vpt = {pt};
  RVec<float> Veta = {eta};
  RVec<float> Vphi = {phi};
  RVec<int> VID = {ID};
  return elidfunc(electroncorr, elecyr, elecidWP,Vpt,Veta,Vphi,VID);
}


  
//Muon Id Function 
RVec<float> muidfunc(correction::Correction::Ref& muonidcorr, RVec<float> &pt, RVec<float> &eta, RVec<int> &ID) {
	RVec<float> mu = {1.0, 1.0, 1.0};
	for(int i = 0; i < pt.size(); i++) {
		if (ID[i] != 13) {continue;} //skip elecs and taus
		if (i > 3) {continue;} //skip leptons past the first 4 for mass reco
	
		mu[0] *= muonidcorr->evaluate({eta[i], pt[i], "nominal"});
		mu[1] *= muonidcorr->evaluate({eta[i], pt[i], "systup"});
		mu[2] *= muonidcorr->evaluate({eta[i], pt[i], "systdown"});
			
	}
	
	return mu;	
}

//Overloaded Muon Id Function 
RVec<float> muidfunc(correction::Correction::Ref& muonidcorr,float pt,float eta,int ID) {
  RVec<float> Vpt = {pt};
  RVec<float> Veta = {eta};
  RVec<int> VID = {ID};
  return muidfunc(muonidcorr,Vpt,Veta,VID);
}

//Muon Iso Function
RVec<float> muisofunc(correction::Correction::Ref& muonisocorr, RVec<float> &pt, RVec<float> &eta, RVec<int> &ID) {
	RVec<float> mu = {1.0, 1.0, 1.0};
	for(int i = 0; i < pt.size(); i++) {
		if (ID[i] != 13) {continue;} //skip elecs and taus
		if (i > 3) {continue;} //skip leptons past the first 4 for mass reco
	
		mu[0] *= muonisocorr->evaluate({eta[i], pt[i], "nominal"});
		mu[1] *= muonisocorr->evaluate({eta[i], pt[i], "systup"});
		mu[2] *= muonisocorr->evaluate({eta[i], pt[i], "systdown"});
	}
	
	return mu;	
}

//Overloaded Muon Iso Function
RVec<float> muisofunc(correction::Correction::Ref& muonisocorr,float pt,float eta,int ID) {
  RVec<float> Vpt = {pt};
  RVec<float> Veta = {eta};
  RVec<int> VID = {ID};
  return muisofunc(muonisocorr,Vpt,Veta,VID);
}

//Tau Id vs e Function (VVLoose)
RVec<float> tauefunc(correction::Correction::Ref& tauidVSecorr, RVec<float> &eta, RVec<int> &dm, RVec<int> &gmatch, RVec<int> &ID) {
	RVec<float> taue = {1.0, 1.0, 1.0};
	for(int i = 0; i < eta.size(); i++) {
		if (ID[i] != 15) {continue;} //skip elecs and muons
		if (i > 3) {continue;} //skip leptons past the first 4 for mass reco
		if (gmatch[i] != 0 || gmatch[i] != 1) {continue;}

		taue[0] *= tauidVSecorr->evaluate({eta[i], dm[i], gmatch[i], "VVLoose", "nom"});
		taue[1] *= tauidVSecorr->evaluate({eta[i], dm[i], gmatch[i], "VVLoose", "up"});
		taue[2] *= tauidVSecorr->evaluate({eta[i], dm[i], gmatch[i], "VVLoose", "down"});
	}	
	
	return taue;	
}


//Tau Id vs muon Function (VLoose)
RVec<float> taumufunc(correction::Correction::Ref& tauidVSmucorr, RVec<float> &eta, RVec<int> &gmatch, RVec<int> &ID) {
	RVec<float> taumu = {1.0, 1.0, 1.0};
	for(int i = 0; i < eta.size(); i++) {
		if (ID[i] != 15) {continue;} //skip elecs and muons
		if (i > 3) {continue;} //skip leptons past the first 4 for mass reco
		if (gmatch[i] != 0 || gmatch[i] != 2) {continue;}

		taumu[0] *= tauidVSmucorr->evaluate({eta[i], gmatch[i], "VLoose", "nom"});
		taumu[1] *= tauidVSmucorr->evaluate({eta[i], gmatch[i], "VLoose", "up"});
		taumu[2] *= tauidVSmucorr->evaluate({eta[i], gmatch[i], "VLoose", "down"});
	}

	return taumu;	
}

//Tau Id vs jet Function (currently VVLoose)
RVec<float> taujetfunc(correction::Correction::Ref& tauidVSjetcorr, RVec<float> &pt, RVec<int> &dm, RVec<int> &gmatch, RVec<int> &ID) {
	RVec<float> taujet = {1.0, 1.0, 1.0};
	/*for(int i = 0; i < pt.size(); i++) {
		if (ID[i] != 15) {continue;} //skip elecs and muons
		if (i > 3) {continue;} //skip leptons past the first 4 for mass reco
	
		taujet[0] *= tauidVSjetcorr->evaluate({pt[i], dm[i], gmatch[i], "VVLoose", "VVLoose", "nom", "dm"}); 
		taujet[1] *= tauidVSjetcorr->evaluate({pt[i], dm[i], gmatch[i], "VVLoose", "VVLoose", "up", "dm"}); 
		taujet[2] *= tauidVSjetcorr->evaluate({pt[i], dm[i], gmatch[i], "VVLoose", "VVLoose", "down", "dm"});
	}*/

	taujet = {1.0, 1.06, 0.94};

	return taujet;	
}

// Jet veto function
RVec<double> jetvetofunc(correction::Correction::Ref& jetvetocorr, const RVec<float> &eta, const RVec<float> &phi){
  RVec<double> map;
  for(unsigned int ijet = 0; ijet < eta.size(); ijet++){
    float phitemp = phi.at(ijet);
    if(phitemp < -3.14159) phitemp = -3.14159;
    else if(phitemp > 3.14159) phitemp = 3.14159;
    map.push_back(jetvetocorr->evaluate({"jetvetomap",eta.at(ijet),phitemp}));
  }
  return map;
};


// Reconstruct the lepton?
RVec<double> recofunc(correction::Correction::Ref& electroncorr, correction::Correction::Ref& muoncorr, string yrstr, const float &pt, const float &eta, const bool &isEl)
{
  RVec<double> reco;
  if(isEl == 0) { 
    reco = {muoncorr->evaluate({yrstr+"_UL",abs(eta),pt,"sf"}), 
      muoncorr->evaluate({yrstr+"_UL",abs(eta),pt,"systup"}), 
      muoncorr->evaluate({yrstr+"_UL",abs(eta),pt,"systdown"})};
  }else{
    reco = {electroncorr->evaluate({yrstr,"sf","RecoAbove20",eta,pt}), 
      electroncorr->evaluate({yrstr,"sfup","RecoAbove20",eta,pt}), 
      electroncorr->evaluate({yrstr,"sfdown","RecoAbove20",eta,pt})};
  }
  return reco;
}; 

// Get the ID of leptons?
RVec<float> idfunc(correction::Correction::Ref& muonidcorr, vector<float> &elid_pts, vector<float> &elid_etas, vector<vector<float>> &elecidsfs, vector<vector<float>> &elecidsfuncs, string &yrstr, const float &pt, const float &eta, const bool &isEl)
{
  RVec<float> id;
  if(isEl > 0){
    int ptbin = (std::upper_bound(elid_pts.begin(), elid_pts.end(), pt) - elid_pts.begin())-1;
    int etabin = (std::upper_bound(elid_etas.begin(), elid_etas.end(), eta) - elid_etas.begin())-1;
    
    id = {elecidsfs[ptbin][etabin], elecidsfuncs[ptbin][etabin]}; //PTL
     
  }else{  
    id = {static_cast<float>(muonidcorr->evaluate({yrstr+"_UL",abs(eta),pt,"sf"})), 
      static_cast<float>(muonidcorr->evaluate({yrstr+"_UL",abs(eta),pt,"systup"})), 
      static_cast<float>(muonidcorr->evaluate({yrstr+"_UL",abs(eta),pt,"systdown"}))};
  }
  return id;
}; 

// iso function
RVec<double> isofunc(vector<float> muiso_pts, vector<float> muiso_etas, vector<vector<float>> muonisosfs, float muonisosfunc, vector<float> elid_pts, vector<float> elid_etas, vector<vector<float>> elecisosfs, float elecisosfunc, const float &pt, const float &eta, const bool &isEl)
{
  RVec<double> iso;
  if(isEl > 0){
    int ptbin = (std::upper_bound(elid_pts.begin(), elid_pts.end(), pt) - elid_pts.begin())-1;
    int etabin = (std::upper_bound(elid_etas.begin(), elid_etas.end(), eta) - elid_etas.begin())-1;
    iso = {elecisosfs[ptbin][etabin], elecisosfunc};
  }else{
    int ptbin = (std::upper_bound(muiso_pts.begin(), muiso_pts.end(), pt) - muiso_pts.begin())-1;
    int etabin = (std::upper_bound(muiso_etas.begin(), muiso_etas.end(), abs(eta)) - muiso_etas.begin())-1;
    iso = {muonisosfs[ptbin][etabin], muonisosfunc};
  }
  return iso;
};

// What is MET? = missing transverse energy = neutrinos. It returns the corrections for met's transverse momentum and phi angle. 
RVec<float> metfunc(correction::Correction::Ref& metptcorr, correction::Correction::Ref& metphicorr, const float &met, const float &phi, const int &npvs, const unsigned int &run)
//assigned types as per BtoTW git analyzer_RDF.cc
{
   float floatrun = run;
   float floatnpvs = npvs;
   float tmpmet = met;
      if(tmpmet > 6500) tmpmet = 6499;
         RVec<float> corrmet = {static_cast<float>(metptcorr->evaluate({tmpmet, phi, floatnpvs, floatrun})), static_cast<float>(metphicorr->evaluate({tmpmet, phi, floatnpvs, floatrun}))};
  return corrmet;
};

// IDK what this function does. What's HLT? seems to be calling a bunch of variables under HLT 
// (electrons? and a muon correction)
RVec<double> hltfunc(correction::Correction::Ref& muonhltcorr, vector<float> &elhlt_pts, vector<float> &elhlt_etas, vector<vector<float>> &elechltsfs, vector<vector<float>> &elechltuncs, string &yrstr, const float &pt, const float &eta, const bool &isEl)
// I assumed hltfunc is a double type vector because of the definition of its return value below.
{
    RVec<double> hlt;
    if(isEl > 0){
      int ptbin = (std::upper_bound(elhlt_pts.begin(), elhlt_pts.end(), pt) - elhlt_pts.begin())-1;
      int etabin = (std::upper_bound(elhlt_etas.begin(), elhlt_etas.end(), 
	            abs(eta)) - elhlt_etas.begin())-1;
      hlt = {elechltsfs[ptbin][etabin], elechltuncs[ptbin][etabin]};
    }
    else {
      //we have lookup tables we might put it into correction format.	      
      
      hlt = {1,1,1};  
      /*hlt = {muonhltcorr->evaluate({yrstr+"_UL",abs(eta),pt,"sf"}), 
	     muonhltcorr->evaluate({yrstr+"_UL",abs(eta),pt,"systup"}), 
	     muonhltcorr->evaluate({yrstr+"_UL",abs(eta),pt,"systdown"})};*/
    }
    return hlt;
 }; 

// WORK ON THIS JULIE
RVec<float> btagshapefunc(string WP, string year, string jesvar, correction::Correction::Ref& btagwpbccorr, correction::Correction::Ref& btagwplcorr, std::vector<int> btagpts, std::vector<std::vector<float>> btageffs, float deepjetL, const RVec<float> &pt, const RVec<float> &eta, const RVec<float> &disc, const RVec<unsigned char> &flav) {

   std::string nominal = "central";
   if(jesvar == "JECup") nominal = "up_jes";
   else if (jesvar == "JECdn") nominal = "down_jes";

   RVec<float> weights(9, 1.0); // collect product of SFs over jets
   for(unsigned int ijet = 0; ijet < eta.size(); ijet++){
       
       int ptbin = (std::upper_bound(btagpts.begin(), btagpts.end(), pt.at(ijet)) - btagpts.begin())-1;
       correction::Correction::Ref wpcorr;
       float eff;
       string downcorrelated = "down_correlated"; string upcorrelated = "up_correlated";
       std::vector<int> shift = {0,4};
       
       if(flav.at(ijet) < 4){wpcorr = btagwplcorr; eff = btageffs[2][ptbin]; shift = {4,0}; downcorrelated = "down"; upcorrelated = "up";}
       else if(flav.at(ijet) == 4){wpcorr = btagwpbccorr; eff = btageffs[1][ptbin];}
       else{wpcorr = btagwpbccorr; eff = btageffs[0][ptbin];}

       if(disc.at(ijet) > deepjetL){
		weights[0] *= wpcorr->evaluate({"central",WP,flav.at(ijet),abs(eta.at(ijet)), pt.at(ijet)}); // seemed like P(Data)/P(MC) reduces to SF
 		weights[1+shift[0]] *= wpcorr->evaluate({upcorrelated,WP,flav.at(ijet),abs(eta.at(ijet)), pt.at(ijet)}); 
 		weights[2+shift[0]] *= wpcorr->evaluate({downcorrelated,WP,flav.at(ijet),abs(eta.at(ijet)), pt.at(ijet)});
 		
		if(year == "2023" or year == "2023BPix"){
 	  		weights[3+shift[0]] *= wpcorr->evaluate({"up_uncorrelated",WP,flav.at(ijet),abs(eta.at(ijet)), pt.at(ijet)});
 	  		weights[4+shift[0]] *= wpcorr->evaluate({"down_uncorrelated",WP,flav.at(ijet),abs(eta.at(ijet)), pt.at(ijet)});
 		}
		
 		weights[1+shift[1]] *= wpcorr->evaluate({"central",WP,flav.at(ijet),abs(eta.at(ijet)), pt.at(ijet)});
 		weights[2+shift[1]] *= wpcorr->evaluate({"central",WP,flav.at(ijet),abs(eta.at(ijet)), pt.at(ijet)});
 		weights[3+shift[1]] *= wpcorr->evaluate({"central",WP,flav.at(ijet),abs(eta.at(ijet)), pt.at(ijet)});
 		weights[4+shift[1]] *= wpcorr->evaluate({"central",WP,flav.at(ijet),abs(eta.at(ijet)), pt.at(ijet)});
       
       }else{
 		weights[0] *= (1.0-eff*wpcorr->evaluate({"central",WP,flav.at(ijet),abs(eta.at(ijet)), pt.at(ijet)}))/(1.0-eff);
 		weights[1+shift[0]] *= (1.0-eff*wpcorr->evaluate({upcorrelated,WP,flav.at(ijet),abs(eta.at(ijet)), pt.at(ijet)}))/(1.0-eff);
		weights[2+shift[0]] *= (1.0-eff*wpcorr->evaluate({downcorrelated,WP,flav.at(ijet),abs(eta.at(ijet)), pt.at(ijet)}))/(1.0-eff);
 		
		if(year == "2023" or year == "2023BPix"){
 	  		weights[3+shift[0]] *= (1.0-eff*wpcorr->evaluate({"up_uncorrelated",WP,flav.at(ijet),abs(eta.at(ijet)), pt.at(ijet)}))/(1.0-eff);
 	  		weights[4+shift[0]] *= (1.0-eff*wpcorr->evaluate({"down_uncorrelated",WP,flav.at(ijet),abs(eta.at(ijet)), pt.at(ijet)}))/(1.0-eff);
 		}
 	
		weights[1+shift[1]] *= (1.0-eff*wpcorr->evaluate({"central",WP,flav.at(ijet),abs(eta.at(ijet)), pt.at(ijet)}))/(1.0-eff);
 		weights[2+shift[1]] *= (1.0-eff*wpcorr->evaluate({"central",WP,flav.at(ijet),abs(eta.at(ijet)), pt.at(ijet)}))/(1.0-eff);
 		weights[3+shift[1]] *= (1.0-eff*wpcorr->evaluate({"central",WP,flav.at(ijet),abs(eta.at(ijet)), pt.at(ijet)}))/(1.0-eff);
 		weights[4+shift[1]] *= (1.0-eff*wpcorr->evaluate({"central",WP,flav.at(ijet),abs(eta.at(ijet)), pt.at(ijet)}))/(1.0-eff);
      }
   }
     
   return weights; 

};
