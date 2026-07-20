#include "include/RestFramesHandler.hh"
#include "TLorentzVector.h"
#include "TVector3.h"
#include "include/RestFrames.hh"
#include <ROOT/RVec.hxx>
#include <algorithm>
#include <iostream>
#include <memory>
#include <mutex>
#include <random>

using namespace RestFrames;
using namespace ROOT::VecOps;

class Tprime_RestFrames_Handler_W : public RestFramesHandler {
private:
  
  // Reconstruction frames
  std::unique_ptr<DecayRecoFrame> TTbar;
  std::unique_ptr<DecayRecoFrame> T;
  std::unique_ptr<VisibleRecoFrame> Tbar;
  
  std::unique_ptr<DecayRecoFrame> W;
  std::unique_ptr<VisibleRecoFrame> b;
  //std::unique_ptr<VisibleRecoFrame> J0;
  //std::unique_ptr<VisibleRecoFrame> J1;
  
  std::unique_ptr<VisibleRecoFrame> l;
  std::unique_ptr<InvisibleRecoFrame> nu;
  
  // Groups
  std::unique_ptr<CombinatoricGroup> JETS;
  
  std::unique_ptr<InvisibleGroup> INV;
  
  // Jigsaws
  std::unique_ptr<SetMassInvJigsaw> NuM;
  std::unique_ptr<SetRapidityInvJigsaw> NuR;
  std::unique_ptr<ContraBoostInvJigsaw> MinContraMt;
  
  //std::unique_ptr<MinMassChi2CombJigsaw> MinChi2;
  //std::unique_ptr<MinMassesCombJigsaw> MinMJets;
  std::unique_ptr<MinMassDiffCombJigsaw> MinDiffJets;
  
  void define_tree() override;
  void define_groups_jigsaws() override;
  
public:
  Tprime_RestFrames_Handler_W();
  RVec<double> calculate_W_doubles(TLorentzVector &lepton, TVector3 &met3, TLorentzVector &jet1, TLorentzVector &jet2, TLorentzVector &jet3);  
};

Tprime_RestFrames_Handler_W::Tprime_RestFrames_Handler_W() {
  initialize();
};

void Tprime_RestFrames_Handler_W::define_tree() {
    LAB.reset(new LabRecoFrame("LAB","LAB"));
    TTbar.reset(new DecayRecoFrame("TTbar", "T#bar{T}"));
    LAB->AddChildFrame(*TTbar);

    // Vector Like T quark particle production
    T.reset(new DecayRecoFrame("T", "T"));
    Tbar.reset(new VisibleRecoFrame("Tbar", "#bar{T}"));
    TTbar->AddChildFrame(*T);
    TTbar->AddChildFrame(*Tbar);
    // T -> W b
    W.reset(new DecayRecoFrame("W","W"));
    b.reset(new VisibleRecoFrame("b", "b"));
    T->AddChildFrame(*W);
    T->AddChildFrame(*b);
    
    // J1.reset(new VisibleRecoFrame("J1", "J1_{AK8}"));
    // J0.reset(new VisibleRecoFrame("J0","J0_{AK8}"));
    // Tbar->AddChildFrame(*J1);
    // Tbar->AddChildFrame(*J0);
    
    // W -> l nu
    l.reset(new VisibleRecoFrame("l", "#it{l}"));
    nu.reset(new InvisibleRecoFrame("nu", "#nu"));
    W->AddChildFrame(*l);
    W->AddChildFrame(*nu);
}

void Tprime_RestFrames_Handler_W::define_groups_jigsaws() {
    // Combinatoric Group for jets
    JETS.reset(new CombinatoricGroup("JETS", "Jet Jigsaws"));
    //JETS->AddFrame(*b);
    JETS->AddFrame(*Tbar);
    //JETS->AddFrame(*J1);
    //JETS->AddFrame(*J0);

    // jet frames must have at least one element
    // JETS->SetNElementsForFrame(*b, 1);
    JETS->SetNElementsForFrame(*Tbar, 2);
    //JETS->SetNElementsForFrame(*J1, 1);
    //JETS->SetNElementsForFrame(*J0, 1);
    
    // Invisible Group for Neutrino
    INV.reset(new InvisibleGroup("INV", "MET Jigsaws"));
    INV->AddFrame(*nu);

    // -------------------- Define Jigsaws for reconstruction trees --------------
    std::string jigsaw_name;

    // 1 Minimize difference Mt jigsaws                not: Minimize equal (vector) top masses neutrino jigsaws
    jigsaw_name = "M_{#nu} = f(m_{b#it{l}J_{0}J_{1}} , m_{b#it{l}} , m_{J_{0}J_{1}})";
    NuM.reset(new SetMassInvJigsaw("NuM", jigsaw_name));
    INV->AddJigsaw(*NuM); 
    
    // 2 
    jigsaw_name = "#eta_{#nu} = #eta_{b #it{l} Tbar}";
    NuR.reset(new SetRapidityInvJigsaw("NuR", jigsaw_name));
    INV->AddJigsaw(*NuR);
    NuR->AddVisibleFrame(*l); 
    NuR->AddVisibleFrame(*b); 
    NuR->AddVisibleFrame(*Tbar); 

    // 3

    jigsaw_name = "min M_{T}, M_{T} = M_{Tbar}";
    MinContraMt.reset(new ContraBoostInvJigsaw("MinContraMt", jigsaw_name));
    INV->AddJigsaw(*MinContraMt);
    MinContraMt->AddVisibleFrames(*l+*b, 0);
    MinContraMt->AddVisibleFrame(*Tbar, 1);
    MinContraMt->AddInvisibleFrame(*nu, 0);

    // MinMassDiffInv was ok, not best
    // jigsaw_name = "min ( M_{T}- M_{Tbar} )^{2}";
    // MinDeltaMt.reset(new MinMassDiffInvJigsaw("MinDeltaMt", jigsaw_name, 2));
    // INV->AddJigsaw(*MinDeltaMt);
    // MinDeltaMt->AddInvisibleFrame(*nu, 0);
    // //MinDeltaMt.AddInvisibleFrame(Nb_R4, 1);
    // MinDeltaMt->AddVisibleFrames(*l+*b, 0);
    // MinDeltaMt->AddVisibleFrame(*Tbar, 1); //OR *J0+*J1, 1) ???
    // MinDeltaMt->AddMassFrame(*T, 0);
    // MinDeltaMt->AddMassFrame(*Tbar, 1);
    // //MinDeltaMt.AddMassFrame(Lb_R4, 1); //???

    // 4 Combinatoric Jigsaws 
    // MinMassesSqCombJigsaw worked but same problem as MinMassesCombJigsaw
    // MinMassDiffCombJigsaw Initialized Analysis but fell into some infinite loop
    // MinMassChi2ComJigsaw works very well
    // jigsaw_name = "Minimize Chi^2";
    // MinChi2.reset(new MinMassChi2CombJigsaw("MinChi2", jigsaw_name, 2, 2));
    // JETS->AddJigsaw(*MinChi2);
    // MinChi2->AddObjectFrame(*l, 0);
    // MinChi2->AddObjectFrame(*b, 0);
    // MinChi2->AddCombFrame(*b, 0);
    // MinChi2->AddObjectFrame(*Tbar, 1);
    // MinChi2->AddCombFrame(*Tbar, 1);
    // MinChi2->SetMass(1435, 0);
    // MinChi2->SetSigma(205.2, 0);
    // MinChi2->SetMass(1456, 1);
    // MinChi2->SetSigma(173.2, 1);

    // MinMassesCombJigsaw, combinatoric jigsaws for everything else...
    // jigsaw_name = "Minimize M(b #it{l} ) , M(Tbar)"; //M(J0 J1 )
    
    // MinMJets.reset(new MinMassesCombJigsaw("MinCombJets", jigsaw_name));
    // JETS->AddJigsaw(*MinMJets);
    // MinMJets->AddFrames(*l+*b+*nu,0);
    // MinMJets->AddFrame(*Tbar,1);

    // MinMassDiffCombJigsaw
    jigsaw_name = "min ( M_{T}- M_{Tbar} )^{2}";
  
    MinDiffJets.reset(new MinMassDiffCombJigsaw("MinDiffJets", jigsaw_name, 2, 1)); // last param is the # of object frames that need to be calculated.  2 doesn't work
    JETS->AddJigsaw(*MinDiffJets);
    MinDiffJets->AddObjectFrames(*l+*b, 0);
    MinDiffJets->AddCombFrame(*b, 0);
    MinDiffJets->AddObjectFrame(*Tbar, 1); 
    MinDiffJets->AddCombFrame(*Tbar, 1);
};

RVec<double> Tprime_RestFrames_Handler_W::calculate_W_doubles(TLorentzVector &lepton, TVector3 &met3, TLorentzVector &jet1, TLorentzVector &jet2, TLorentzVector &jet3) { //, TLorentzVector &jet4) {
    before_analysis();
    
    INV->SetLabFrameThreeVector(met3);	
    l->SetLabFrameFourVector(lepton);
    b->SetLabFrameFourVector(jet1)
    
    std::vector<RFKey> JETS_ID; // ID for tracking jets in tree
    JETS_ID.clear();
    //JETS_ID.push_back(JETS->AddLabFrameFourVector(jet1));
    JETS_ID.push_back(JETS->AddLabFrameFourVector(jet2));
    JETS_ID.push_back(JETS->AddLabFrameFourVector(jet3));

    LAB->AnalyzeEvent(); // analyze the event

    RVec<double> observables;

    observables.push_back(TTbar->GetMass());//................. 0
    observables.push_back(TTbar->GetCosDecayAngle());//........ 1
    observables.push_back(TTbar->GetDeltaPhiDecayAngle());//... 2
    
    observables.push_back(T->GetMass());//..................... 3
    observables.push_back(T->GetCosDecayAngle());//............ 4
    observables.push_back(T->GetDeltaPhiDecayAngle());//....... 5
    observables.push_back(T->GetFourVector().Pt()); //......... 6
    observables.push_back(T->GetFourVector().Eta()); //........ 7
    observables.push_back(T->GetFourVector().Phi()); //........ 8
    
    observables.push_back(Tbar->GetMass()); //................. 9
    observables.push_back(Tbar->GetCosDecayAngle()); //....... 10
    observables.push_back(Tbar->GetFourVector().Pt()); //...... 11
    observables.push_back(Tbar->GetFourVector().Eta()); //..... 12
    observables.push_back(Tbar->GetFourVector().Phi()); //..... 13
    
    observables.push_back(W->GetMass()); //.................... 14
    observables.push_back(W->GetCosDecayAngle()); //........... 15
    observables.push_back(W->GetDeltaPhiDecayAngle());//....... 16
    observables.push_back(W->GetFourVector().Pt()); //......... 17
    observables.push_back(W->GetFourVector().Eta()); //........ 18
    observables.push_back(W->GetFourVector().Phi()); //........ 19

    observables.push_back(b->GetMass());//..................... 20
    observables.push_back(b->GetCosDecayAngle());//............ 21

    observables.push_back(TTbar->GetDeltaPhiVisible());//...... 22
    observables.push_back(TTbar->GetDeltaPhiDecayVisible());//. 23
    observables.push_back(TTbar->GetDeltaPhiBoostVisible());//. 24
    observables.push_back(TTbar->GetVisibleShape());//......... 25

    // Vectors isn't working as a separate function, because they don't operate one after the other on the same event!
    // Returning what I think we need to identify the 3 jets compared to our list.
    observables.push_back(Tbar->GetFourVector().E());//........ 26
    observables.push_back(b->GetFourVector().E());//........... 27

    observables.push_back(-1); // dummy -1 for t mass ......... 28
    observables.push_back(-1); // dummy -1 for t cos decay .... 29
    observables.push_back(-1); // dummy -1 for t del phi decay. 30
    observables.push_back(-1); // dummy -1 for t pt ........... 31
    observables.push_back(-1); // dummy -1 for t eta .......... 32
    observables.push_back(-1); // dummy -1 for t phi .......... 33

    observables.push_back(nu->GetInvisibleFourVector().E());//. 34
    observables.push_back(nu->GetInvisibleFourVector().Pz());// 35

    observables.push_back(b->GetMass());//..................... 36
    observables.push_back(-1);// dummy for minMlb mass ........ 37

    after_analysis();

    return observables;
};


class Tprime_RestFrames_Container_W : public RestFramesContainer {
    public:
        Tprime_RestFrames_Container_W(int num_threads);
        RestFramesHandler *create_handler() override;

        RVec<double> return_W_doubles(int thread_index, float lepton_pt, float lepton_eta, float lepton_phi, float lepton_mass, RVec<float> fatjet_pt, RVec<float> fatjet_eta, RVec<float> fatjet_phi, RVec<float> fatjet_mass, float met_pt, float met_phi);
	
};

Tprime_RestFrames_Container_W::Tprime_RestFrames_Container_W (int num_threads) : RestFramesContainer(num_threads){
    initialize();
};

RestFramesHandler * Tprime_RestFrames_Container_W::create_handler() {
    return new Tprime_RestFrames_Handler_W;
}

// return_doubles() returns all the masses, cos angles, and deltaPhi angles of the frames in the tree
RVec<double> Tprime_RestFrames_Container_W::return_W_doubles(int thread_index, float lepton_pt, float lepton_eta, float lepton_phi, float lepton_mass, RVec<float> fatjet_pt, RVec<float> fatjet_eta, RVec<float> fatjet_phi, RVec<float> fatjet_mass, float met_pt, float met_phi) {

  // This pointer should explicitly not be deleted!
  Tprime_RestFrames_Handler_W *rfhw = static_cast<Tprime_RestFrames_Handler_W *>(get_handler(thread_index));
  
  TLorentzVector fatjet_1;
  TLorentzVector fatjet_2;
  TLorentzVector fatjet_3;
  
  TLorentzVector lepton;
  
  TVector3 met3;
  
  lepton.SetPtEtaPhiM(lepton_pt, lepton_eta, lepton_phi, lepton_mass);
    
  double MET_px  = met_pt*std::cos(met_phi);
  double MET_py  = met_pt*std::sin(met_phi);
  met3  = TVector3(MET_px, MET_py, 0.0);

  RVec<double> observables;
  double minDiffVLQ = 9999;
  
  // for (int i = 0; i < 3; i++) {
  //   fatjet_1.SetPtEtaPhiM(fatjet_pt[(i+0)%3], fatjet_eta[(i+0)%3], fatjet_phi[(i+0)%3], fatjet_mass[(i+0)%3]);
  //   fatjet_2.SetPtEtaPhiM(fatjet_pt[(i+1)%3], fatjet_eta[(i+1)%3], fatjet_phi[(i+1)%3], fatjet_mass[(i+1)%3]);
  //   fatjet_3.SetPtEtaPhiM(fatjet_pt[(i+2)%3], fatjet_eta[(i+2)%3], fatjet_phi[(i+2)%3], fatjet_mass[(i+2)%3]);
    
  //   RVec<double> temp_observables = rfhw->calculate_W_doubles(lepton, met3, fatjet_1, fatjet_2, fatjet_3); //jet_4);
  //   double diffVLQ = abs(temp_observables[3] - temp_observables[6]);
  //   if (diffVLQ < minDiffVLQ) observables = temp_observables;
  // }

  fatjet_1.SetPtEtaPhiM(fatjet_pt[J0_idx],fatjet_eta[J0_idx],fatjet_phi[J0_idx],fatjet_mass[J0_idx]);
  fatjet_2.SetPtEtaPhiM(fatjet_pt[VLQ1_idx],fatjet_eta[VLQ1_idx],fatjet_phi[VLQ1_idx],fatjet_mass[VLQ1_idx]);
  fatjet_3.SetPtEtaPhiM(fatjet_pt[VLQ2_idx],fatjet_eta[VLQ2_idx],fatjet_phi[VLQ2_idx],fatjet_mass[VLQ2_idx]);
  
  RVec<double> temp_observables = rfhw->calculate_w_doubles(lepton, met3, fatjet_1, fatjet_2, fatjet_3);

  
  return observables;
}


