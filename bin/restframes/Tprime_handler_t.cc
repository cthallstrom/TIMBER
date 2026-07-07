#include "include/RestFramesHandler.hh"
#include <typeinfo>
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

class Tprime_RestFrames_Handler_t : public RestFramesHandler {
private:
  //(H/Z)t tree
  // Reconstruction frames
  std::unique_ptr<DecayRecoFrame> TTbar;
  std::unique_ptr<DecayRecoFrame> T;
  std::unique_ptr<VisibleRecoFrame> Tbar;
  
  std::unique_ptr<DecayRecoFrame> t;
  std::unique_ptr<VisibleRecoFrame> J0; // this is the Z/H boson
  
  std::unique_ptr<DecayRecoFrame> W;
  std::unique_ptr<VisibleRecoFrame> b;
  
  std::unique_ptr<VisibleRecoFrame> l;
  std::unique_ptr<InvisibleRecoFrame> nu;
  
  // Groups
  std::unique_ptr<CombinatoricGroup> JETS;
  
  std::unique_ptr<CombinatoricGroup> SMTOP;
  
  std::unique_ptr<InvisibleGroup> INV;
  
  // Jigsaws
  std::unique_ptr<SetMassInvJigsaw> NuM;
  std::unique_ptr<SetRapidityInvJigsaw> NuR;
  std::unique_ptr<ContraBoostInvJigsaw> MinContraMt;
  
  //std::unique_ptr<MinMassesCombJigsaw> MinMJets;
  std::unique_ptr<MinMassDiffCombJigsaw> MinDiffJets;
  
  std::unique_ptr<MinMassChi2CombJigsaw> MinChi2;
  
  void define_tree() override;
  void define_groups_jigsaws() override;
  
public:
  Tprime_RestFrames_Handler_t();
  RVec<double> calculate_t_doubles(TLorentzVector &lepton, TVector3 &met3, TLorentzVector &jet1, TLorentzVector &jet2, TLorentzVector &jet3, RVec<TLorentzVector> &AK4s, TLorentzVector &minMlb_lv);
};

Tprime_RestFrames_Handler_t::Tprime_RestFrames_Handler_t() {
    initialize();
};

void Tprime_RestFrames_Handler_t::define_tree() {
    LAB.reset(new LabRecoFrame("LAB","LAB"));
    TTbar.reset(new DecayRecoFrame("TTbar", "T#bar{T}"));
    LAB->AddChildFrame(*TTbar);

    // Vector Like T quark particle production
    T.reset(new DecayRecoFrame("T", "T"));
    Tbar.reset(new VisibleRecoFrame("Tbar", "#bar{T}"));
    TTbar->AddChildFrame(*T);
    TTbar->AddChildFrame(*Tbar);
    
    // T -> t J0 (Z or H) 
    t.reset(new DecayRecoFrame("t","t"));
    J0.reset(new VisibleRecoFrame("J0", "J0_{AK8}"));
    T->AddChildFrame(*t);
    T->AddChildFrame(*J0);

    // t -> W b 
    W.reset(new DecayRecoFrame("W","W"));
    b.reset(new VisibleRecoFrame("b", "b"));
    t->AddChildFrame(*W);
    t->AddChildFrame(*b);

    // W -> l nu
    l.reset(new VisibleRecoFrame("l", "#it{l}"));
    nu.reset(new InvisibleRecoFrame("nu", "#nu"));
    W->AddChildFrame(*l);
    W->AddChildFrame(*nu);
}

void Tprime_RestFrames_Handler_t::define_groups_jigsaws() {
    // Combinatoric Group for jets
    JETS.reset(new CombinatoricGroup("JETS", "Jet Jigsaws"));
    JETS->AddFrame(*J0);
    JETS->AddFrame(*Tbar);

    // jet frames must have at least one element
    JETS->SetNElementsForFrame(*J0, 1);
    JETS->SetNElementsForFrame(*Tbar, 2);
    
    // Combinatoric Group for SM top quark reconstruction
    // SMTOP.reset(new CombinatoricGroup("SMTOP", "Standard Model top Jigsaw"));
    // SMTOP->AddFrame(*b);
    // SMTOP->SetNElementsForFrame(*b, 1);

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
    jigsaw_name = "#eta_{#nu} = #eta_{J_{0} b #it{l} Tbar}";
    NuR.reset(new SetRapidityInvJigsaw("NuR", jigsaw_name));
    INV->AddJigsaw(*NuR);
    NuR->AddVisibleFrame(*l); 
    NuR->AddVisibleFrame(*b); 
    NuR->AddVisibleFrame(*Tbar); 
    NuR->AddVisibleFrame(*J0);

    // 3

    jigsaw_name = "min M_{T}, M_{T} = M_{Tbar}";
    MinContraMt.reset(new ContraBoostInvJigsaw("MinContraMt", jigsaw_name));
    INV->AddJigsaw(*MinContraMt);
    MinContraMt->AddVisibleFrames(*J0+*l+*b, 0);
    MinContraMt->AddVisibleFrame(*Tbar, 1);
    MinContraMt->AddInvisibleFrame(*nu, 0);

    // MinMassDiffCombJigsaw
    jigsaw_name = "min ( M_{T}- M_{Tbar} )^{2}";
  
    MinDiffJets.reset(new MinMassDiffCombJigsaw("MinDiffJets", jigsaw_name, 2, 1)); // last param is the # of object frames that need to be calculated.  2 doesn't work
    JETS->AddJigsaw(*MinDiffJets);
    MinDiffJets->AddObjectFrames(*J0+*l+*b, 0);
    MinDiffJets->AddCombFrame(*J0, 0);
    MinDiffJets->AddObjectFrame(*Tbar, 1); 
    MinDiffJets->AddCombFrame(*Tbar, 1);
    
    // JET group 2 for SM t quark
    // jigsaw_name = "Minimize Chi^2";
    // MinChi2.reset(new MinMassChi2CombJigsaw("MinChi2", jigsaw_name, 1, 1)); // may need to change second number to 2
    // SMTOP->AddJigsaw(*MinChi2);
    // MinChi2->AddObjectFrames(*l+*b+*nu, 0);
    // //MinChi2->AddObjectFrame(*b, 0);
    // MinChi2->AddCombFrame(*b, 0);
    // MinChi2->SetMass(171.77, 0);
    // MinChi2->SetSigma(0.38, 0);
};

RVec<double> Tprime_RestFrames_Handler_t::calculate_t_doubles(TLorentzVector &lepton, TVector3 &met3, TLorentzVector &jet1, TLorentzVector &jet2, TLorentzVector &jet3, RVec<TLorentzVector> &AK4s,TLorentzVector &minMlb_lv) {
    before_analysis();
    
    INV->SetLabFrameThreeVector(met3);	
    l->SetLabFrameFourVector(lepton);
    LAB->AddFrameParticle(*b, minMlb_lv);
    
    std::vector<RFKey> JETS_ID; // ID for tracking jets in tree
    JETS_ID.clear();
    JETS_ID.push_back(JETS->AddLabFrameFourVector(jet3));
    JETS_ID.push_back(JETS->AddLabFrameFourVector(jet1));
    JETS_ID.push_back(JETS->AddLabFrameFourVector(jet2));
    
    // for (int i = 0; i < AK4s.size(); i++) {
    //   JETS_ID.push_back(SMTOP->AddLabFrameFourVector(AK4s[i]));
    // } // if this loop is skipped that means there were no T -> t -> b W

    LAB->AnalyzeEvent(); // analyze the event


    RVec<double> observables; // = {T_mass, Tbar_mass};

    observables.push_back(TTbar->GetMass()); //................. 0
    observables.push_back(TTbar->GetCosDecayAngle()); //........ 1
    observables.push_back(TTbar->GetDeltaPhiDecayAngle()); //... 2
    
    observables.push_back(T->GetMass()); // .................... 3
    observables.push_back(T->GetCosDecayAngle()); //............ 4
    observables.push_back(T->GetDeltaPhiDecayAngle());//........ 5
    
    observables.push_back(Tbar->GetMass()); //.................. 6
    observables.push_back(Tbar->GetCosDecayAngle()); //......... 7
    
    observables.push_back(W->GetMass()); //..................... 8
    observables.push_back(W->GetCosDecayAngle()); //............ 9
    observables.push_back(W->GetDeltaPhiDecayAngle());//........ 10
    
    observables.push_back(J0->GetMass()); //.................... 11
    observables.push_back(J0->GetCosDecayAngle());//............ 12

    observables.push_back(TTbar->GetDeltaPhiVisible()); //...... 13
    observables.push_back(TTbar->GetDeltaPhiDecayVisible());//.. 14
    observables.push_back(TTbar->GetDeltaPhiBoostVisible());//.. 15
    observables.push_back(TTbar->GetVisibleShape());//.......... 16
    
    // Vectors isn't working as a separate function, because they don't operate one after the other on the same event!
    // Returning what I think we need to identify the 3 jets compared to our list.
    observables.push_back(Tbar->GetFourVector().E()); // ....... 17
    observables.push_back(J0->GetFourVector().E()); // ......... 18

    observables.push_back(t->GetMass()); // .................... 19
    observables.push_back(t->GetCosDecayAngle()); //............ 20
    observables.push_back(t->GetDeltaPhiDecayAngle()); //....... 21

    observables.push_back(nu->GetInvisibleFourVector().E()); //.................. 22
    observables.push_back(nu->GetInvisibleFourVector().Pz());//............ 23
    
    after_analysis();

    return observables;
};


class Tprime_RestFrames_Container_t : public RestFramesContainer {
    public:
        Tprime_RestFrames_Container_t(int num_threads);
        RestFramesHandler *create_handler() override;

        RVec<double> return_t_doubles(int thread_index, float lepton_pt, float lepton_eta, float lepton_phi, float lepton_mass, RVec<float> fatjet_pt, RVec<float> fatjet_eta, RVec<float> fatjet_phi, RVec<float> fatjet_mass, float met_pt, float met_phi, RVec<TLorentzVector> jets);
	
};

Tprime_RestFrames_Container_t::Tprime_RestFrames_Container_t (int num_threads) : RestFramesContainer(num_threads){
    initialize();
};

RestFramesHandler * Tprime_RestFrames_Container_t::create_handler() {
    return new Tprime_RestFrames_Handler_t;
}

// return_doubles() returns all the masses, cos angles, and deltaPhi angles of the frames in the tree
RVec<double> Tprime_RestFrames_Container_t::return_t_doubles(int thread_index, float lepton_pt, float lepton_eta, float lepton_phi, float lepton_mass, RVec<float> fatjet_pt, RVec<float> fatjet_eta, RVec<float> fatjet_phi, RVec<float> fatjet_mass, float met_pt, float met_phi, RVec<TLorentzVector> jets, TLorentzVector minMlb_lv) {

    // This pointer should explicitly not be deleted!
    Tprime_RestFrames_Handler_t *rfht = static_cast<Tprime_RestFrames_Handler_t *>(get_handler(thread_index));

    TLorentzVector fatjet_1;
    TLorentzVector fatjet_2;
    TLorentzVector fatjet_3;

    TLorentzVector lepton;

    TVector3 met3;
    
    lepton.SetPtEtaPhiM(lepton_pt, lepton_eta, lepton_phi, lepton_mass);

    fatjet_1.SetPtEtaPhiM(fatjet_pt[0], fatjet_eta[0], fatjet_phi[0], fatjet_mass[0]);
    fatjet_2.SetPtEtaPhiM(fatjet_pt[1], fatjet_eta[1], fatjet_phi[1], fatjet_mass[1]);
    fatjet_3.SetPtEtaPhiM(fatjet_pt[2], fatjet_eta[2], fatjet_phi[2], fatjet_mass[2]);

    double MET_px  = met_pt*std::cos(met_phi);
    double MET_py  = met_pt*std::sin(met_phi);
    met3  = TVector3(MET_px, MET_py, 0.0);
   
    RVec<double> observables = rfht->calculate_t_doubles(lepton, met3, fatjet_1, fatjet_2, fatjet_3, jets, minMlb_lv); //jet_4);

    return observables;
}


