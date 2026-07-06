using namespace std;
using namespace ROOT::VecOps;
#include <vector>
#include <cmath> // for std::abs
#include <utility> // for std::pair
#include <algorithm>

struct GenSubjetMatch {
    int gen;
    int subjet; // Using -1 instead of None if no subjet matches
};

float deltaR(float eta1, float phi1, float eta2, float phi2) {
    float deta = eta1 - eta2;
    float dphi = phi1 - phi2;
    while (dphi >  M_PI) dphi -= 2 * M_PI;
    while (dphi < -M_PI) dphi += 2 * M_PI;
    return std::sqrt(deta * deta + dphi * dphi);
}

auto get_lastcopy_tprimes(
    RVec<Int_t>& GenPart_pdgId,
    RVec<UShort_t>& GenPart_statusFlags,
    RVec<Float_t>& GenPart_pt) 
{
    RVec<int> tprimes;
    std::vector<float> tprimes_pt;

    for (size_t i = 0; i < GenPart_pdgId.size(); ++i) {
        if (std::abs(GenPart_pdgId[i]) == 6000006) {
            
            // Check the 13th bit of the status flag (isLastCopy)
            bool isLastCopy = (GenPart_statusFlags[i] >> 13) & 1;

            if (isLastCopy) {
                tprimes.push_back(i);
                tprimes_pt.push_back(GenPart_pt[i]);
            }
        }
    }

    return tprimes;
}

#include <vector>
#include <cmath> // for std::abs

auto get_tprime_daughters(
    RVec<int>& tprimes, // Passed from the previous function
    RVec<int>& GenPart_pdgId,
    RVec<Short_t>& GenPart_genPartIdxMother) 
{
    // Initialize a vector containing two empty vectors for the daughters
    std::vector<std::vector<int>> daughters(2, std::vector<int>());

    // Safety check: ensure we actually found at least 2 T' mothers
    if (tprimes.size() < 2) {
        return daughters; // Return empty daughter collections
    }

    for (size_t i = 0; i < GenPart_pdgId.size(); ++i) {
        int mother = GenPart_genPartIdxMother[i];

        // Skip particles with no valid mother (e.g., incoming beams)
        if (mother < 0) {
            continue;
        }

        int pdg = std::abs(GenPart_pdgId[i]);

        // Filter for allowed decay products: W (24), Z (23), H (25), t (6), b (5)
        if (pdg != 24 && pdg != 23 && pdg != 25 && pdg != 6 && pdg != 5) {
            continue;
        }

        // Match daughters to their specific T' mother
        if (mother == tprimes[0]) {
            daughters[0].push_back(i);
        }
        else if (mother == tprimes[1]) {
            daughters[1].push_back(i);
        }
    }

    return daughters;
}

#include <vector>
#include <cmath>
#include <ROOT/RVec.hxx>

// Assuming deltaR is defined elsewhere in your environment
// float deltaR(float eta1, float phi1, float eta2, float phi2);

std::vector<std::vector<int>> tag_ak8jets_with_genquarks(
    const std::vector<std::vector<int>>& daughters, // from get_tprime_daughters
    const ROOT::VecOps::RVec<float>& GenPart_eta,
    const ROOT::VecOps::RVec<float>& GenPart_phi,
    const ROOT::VecOps::RVec<int>& GenPart_pdgId,   // Added PDG ID branch
    const ROOT::VecOps::RVec<TLorentzVector>& ak8jets) 
{
    const float DR_MAX = 0.8;
    // Flatten daughters[0] + daughters[1] into gen_quarks indices
    std::vector<int> gen_quarks;
    if (daughters.size() > 0) gen_quarks.insert(gen_quarks.end(), daughters[0].begin(), daughters[0].end());
    if (daughters.size() > 1) gen_quarks.insert(gen_quarks.end(), daughters[1].begin(), daughters[1].end());

    size_t nJets = ak8jets.size();
    std::vector<std::vector<int>> jet_matches(nJets);

    // -------------------------------
    // STEP 1: basic AK8 matching
    // -------------------------------
    for (int iGen : gen_quarks) {
        float eta = GenPart_eta[iGen];
        float phi = GenPart_phi[iGen];

        int best = -1;
        float bestdr = 999.0f;

        for (size_t iJet = 0; iJet < nJets; ++iJet) {
            // Unpacking eta and phi from your jet structure
            float jeta = ak8jets[iJet].Eta(); 
            float jphi = ak8jets[iJet].Phi(); 

            float dr = deltaR(jeta, jphi, eta, phi);

            if (dr < DR_MAX && dr < bestdr) {
                best = iJet;
                bestdr = dr;
            }
        }

        if (best >= 0) {
            // Look up the PDG ID using the index, and store the ID instead!
            int pdgId = GenPart_pdgId[iGen];
            jet_matches[best].push_back(pdgId);   
        }
    } 

    return jet_matches;
}