import os 

class sample:
    def __init__(self, prefix, xsec, year, textlist, samplename): #, color
        self.prefix = prefix
        self.year = year
        self.textlist = textlist
        self.samplename = samplename
        self.xsec = xsec # in pb

################################################
###                                          ###
###                SIGNALS                   ###
###                                          ###
################################################

BpBp_M1200_2024 = sample("BpBp_M1200_2024", 1.0, "2024", "BpBp_M1200_2024NanoList.txt", "/BprimeBprime_Par-M-1200_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
BpBp_M1400_2024 = sample("BpBp_M1400_2024", 1.0, "2024", "BpBp_M1400_2024NanoList.txt", "/BprimeBprime_Par-M-1400_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
BpBp_M1500_2024 = sample("BpBp_M1500_2024", 1.0, "2024", "BpBp_M1500_2024NanoList.txt", "/BprimeBprime_Par-M-1500_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
BpBp_M1600_2024 = sample("BpBp_M1600_2024", 1.0, "2024", "BpBp_M1600_2024NanoList.txt", "/BprimeBprime_Par-M-1600_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
BpBp_M1700_2024 = sample("BpBp_M1700_2024", 1.0, "2024", "BpBp_M1700_2024NanoList.txt", "/BprimeBprime_Par-M-1700_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
BpBp_M1800_2024 = sample("BpBp_M1800_2024", 1.0, "2024", "BpBp_M1800_2024NanoList.txt", "/BprimeBprime_Par-M-1800_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
BpBp_M1900_2024 = sample("BpBp_M1900_2024", 1.0, "2024", "BpBp_M1900_2024NanoList.txt", "/BprimeBprime_Par-M-1900_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
BpBp_M2000_2024 = sample("BpBp_M2000_2024", 1.0, "2024", "BpBp_M2000_2024NanoList.txt", "/BprimeBprime_Par-M-2000_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
BpBp_M2100_2024 = sample("BpBp_M2100_2024", 1.0, "2024", "BpBp_M2100_2024NanoList.txt", "/BprimeBprime_Par-M-2100_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
BpBp_M2200_2024 = sample("BpBp_M2200_2024", 1.0, "2024", "BpBp_M2200_2024NanoList.txt", "/BprimeBprime_Par-M-2200_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
TpTp_M1200_2024 = sample("TpTp_M1200_2024", 1.0, "2024", "TpTp_M1200_2024NanoList.txt", "/TprimeTprime_Par-M-1200_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
TpTp_M1300_2024 = sample("TpTp_M1300_2024", 1.0, "2024", "TpTp_M1300_2024NanoList.txt", "/TprimeTprime_Par-M-1300_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
TpTp_M1400_2024 = sample("TpTp_M1400_2024", 1.0, "2024", "TpTp_M1400_2024NanoList.txt", "/TprimeTprime_Par-M-1400_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
TpTp_M1600_2024 = sample("TpTp_M1600_2024", 1.0, "2024", "TpTp_M1600_2024NanoList.txt", "/TprimeTprime_Par-M-1600_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
TpTp_M1700_2024 = sample("TpTp_M1700_2024", 1.0, "2024", "TpTp_M1700_2024NanoList.txt", "/TprimeTprime_Par-M-1700_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
TpTp_M1800_2024 = sample("TpTp_M1800_2024", 1.0, "2024", "TpTp_M1800_2024NanoList.txt", "/TprimeTprime_Par-M-1800_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
TpTp_M1900_2024 = sample("TpTp_M1900_2024", 1.0, "2024", "TpTp_M1900_2024NanoList.txt", "/TprimeTprime_Par-M-1900_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
TpTp_M2000_2024 = sample("TpTp_M2000_2024", 1.0, "2024", "TpTp_M2000_2024NanoList.txt", "/TprimeTprime_Par-M-2000_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
TpTp_M2100_2024 = sample("TpTp_M2100_2024", 1.0, "2024", "TpTp_M2100_2024NanoList.txt", "/TprimeTprime_Par-M-2100_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
TpTp_M2200_2024 = sample("TpTp_M2200_2024", 1.0, "2024", "TpTp_M2200_2024NanoList.txt", "/TprimeTprime_Par-M-2200_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")

#####INCORRECT 2025 SIGNAL BELOW -> ACTUALLY 2024 SIG BEIGN USED FOR 2025
BpBp_M1200_2025 = sample("BpBp_M1200_2024", 1.0, "2025", "BpBp_M1200_2024NanoList.txt", "/BprimeBprime_Par-M-1200_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
BpBp_M1400_2025 = sample("BpBp_M1400_2024", 1.0, "2025", "BpBp_M1400_2024NanoList.txt", "/BprimeBprime_Par-M-1400_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
BpBp_M1500_2025 = sample("BpBp_M1500_2024", 1.0, "2025", "BpBp_M1500_2024NanoList.txt", "/BprimeBprime_Par-M-1500_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
BpBp_M1600_2025 = sample("BpBp_M1600_2024", 1.0, "2025", "BpBp_M1600_2024NanoList.txt", "/BprimeBprime_Par-M-1600_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
BpBp_M1700_2025 = sample("BpBp_M1700_2024", 1.0, "2025", "BpBp_M1700_2024NanoList.txt", "/BprimeBprime_Par-M-1700_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
BpBp_M1800_2025 = sample("BpBp_M1800_2024", 1.0, "2025", "BpBp_M1800_2024NanoList.txt", "/BprimeBprime_Par-M-1800_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
BpBp_M1900_2025 = sample("BpBp_M1900_2024", 1.0, "2025", "BpBp_M1900_2024NanoList.txt", "/BprimeBprime_Par-M-1900_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
BpBp_M2000_2025 = sample("BpBp_M2000_2024", 1.0, "2025", "BpBp_M2000_2024NanoList.txt", "/BprimeBprime_Par-M-2000_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
BpBp_M2100_2025 = sample("BpBp_M2100_2024", 1.0, "2025", "BpBp_M2100_2024NanoList.txt", "/BprimeBprime_Par-M-2100_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
BpBp_M2200_2025 = sample("BpBp_M2200_2024", 1.0, "2025", "BpBp_M2200_2024NanoList.txt", "/BprimeBprime_Par-M-2200_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
TpTp_M1200_2025 = sample("TpTp_M1200_2024", 1.0, "2025", "TpTp_M1200_2024NanoList.txt", "/TprimeTprime_Par-M-1200_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
TpTp_M1300_2025 = sample("TpTp_M1300_2024", 1.0, "2025", "TpTp_M1300_2024NanoList.txt", "/TprimeTprime_Par-M-1300_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
TpTp_M1400_2025 = sample("TpTp_M1400_2024", 1.0, "2025", "TpTp_M1400_2024NanoList.txt", "/TprimeTprime_Par-M-1400_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
TpTp_M1600_2025 = sample("TpTp_M1600_2024", 1.0, "2025", "TpTp_M1600_2024NanoList.txt", "/TprimeTprime_Par-M-1600_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
TpTp_M1700_2025 = sample("TpTp_M1700_2024", 1.0, "2025", "TpTp_M1700_2024NanoList.txt", "/TprimeTprime_Par-M-1700_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
TpTp_M1800_2025 = sample("TpTp_M1800_2024", 1.0, "2025", "TpTp_M1800_2024NanoList.txt", "/TprimeTprime_Par-M-1800_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
TpTp_M1900_2025 = sample("TpTp_M1900_2024", 1.0, "2025", "TpTp_M1900_2024NanoList.txt", "/TprimeTprime_Par-M-1900_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
TpTp_M2000_2025 = sample("TpTp_M2000_2024", 1.0, "2025", "TpTp_M2000_2024NanoList.txt", "/TprimeTprime_Par-M-2000_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
TpTp_M2100_2025 = sample("TpTp_M2100_2024", 1.0, "2025", "TpTp_M2100_2024NanoList.txt", "/TprimeTprime_Par-M-2100_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
TpTp_M2200_2025 = sample("TpTp_M2200_2024", 1.0, "2025", "TpTp_M2200_2024NanoList.txt", "/TprimeTprime_Par-M-2200_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")

######## END OF INCORRECT 2025 SAMPLES


Bprime_M1000_2022 = sample("Bprime_M1000_2022", 1.0, "2022", "Bprime_M1000_2022NanoList.txt", "/BprimeBprimeto2B4Tau_MB-1000_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
Bprime_M1000_2022EE = sample("Bprime_M1000_2022EE", 1.0, "2022EE", "Bprime_M1000_2022EENanoList.txt", "/BprimeBprimeto2B4Tau_MB-1000_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
Bprime_M1000_2023 = sample("Bprime_M1000_2023", 1.0, "2023", "Bprime_M1000_2023NanoList.txt", "/BprimeBprimeto2B4Tau_MB-1000_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
Bprime_M1000_2023BPix = sample("Bprime_M1000_2023BPix", 1.0, "2023BPix", "Bprime_M1000_2023BPixNanoList.txt", "/BprimeBprimeto2B4Tau_MB-1000_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
Bprime_M1300_2022 = sample("Bprime_M1300_2022", 1.0, "2022", "Bprime_M1300_2022NanoList.txt", "/BprimeBprimeto2B4Tau_MB-1300_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
Bprime_M1300_2022EE = sample("Bprime_M1300_2022EE", 1.0, "2022EE", "Bprime_M1300_2022EENanoList.txt", "/BprimeBprimeto2B4Tau_MB-1300_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
Bprime_M1300_2023 = sample("Bprime_M1300_2023", 1.0, "2023", "Bprime_M1300_2023NanoList.txt", "/BprimeBprimeto2B4Tau_MB-1300_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
Bprime_M1300_2023BPix = sample("Bprime_M1300_2023BPix", 1.0, "2023BPix", "Bprime_M1300_2023BPixNanoList.txt", "/BprimeBprimeto2B4Tau_MB-1300_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
Bprime_M1600_2022 = sample("Bprime_M1600_2022", 1.0, "2022", "Bprime_M1600_2022NanoList.txt", "/BprimeBprimeto2B4Tau_MB-1600_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
Bprime_M1600_2022EE = sample("Bprime_M1600_2022EE", 1.0, "2022EE", "Bprime_M1600_2022EENanoList.txt", "/BprimeBprimeto2B4Tau_MB-1600_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
Bprime_M1600_2023 = sample("Bprime_M1600_2023", 1.0, "2023", "Bprime_M1600_2023NanoList.txt", "/BprimeBprimeto2B4Tau_MB-1600_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
Bprime_M1600_2023BPix = sample("Bprime_M1600_2023BPix", 1.0, "2023BPix", "Bprime_M1600_2023BPixNanoList.txt", "/BprimeBprimeto2B4Tau_MB-1600_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
Bprime_M700_2022 = sample("Bprime_M700_2022", 1.0, "2022", "Bprime_M700_2022NanoList.txt", "/BprimeBprimeto2B4Tau_MB-700_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
Bprime_M700_2022EE = sample("Bprime_M700_2022EE", 1.0, "2022EE", "Bprime_M700_2022EENanoList.txt", "/BprimeBprimeto2B4Tau_MB-700_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
Bprime_M700_2023 = sample("Bprime_M700_2023", 1.0, "2023", "Bprime_M700_2023NanoList.txt", "/BprimeBprimeto2B4Tau_MB-700_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
Bprime_M700_2023BPix = sample("Bprime_M700_2023BPix", 1.0, "2023BPix", "Bprime_M700_2023BPixNanoList.txt", "/BprimeBprimeto2B4Tau_MB-700_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
Bprime_M400_2022 = sample("Bprime_M400_2022", 1.0, "2022", "Bprime_M400_2022NanoList.txt", "/BprimeBprimeto2B4Tau_MB-400_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
Bprime_M400_2022EE = sample("Bprime_M400_2022EE", 1.0, "2022EE", "Bprime_M400_2022EENanoList.txt", "/BprimeBprimeto2B4Tau_MB-400_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
Bprime_M400_2023 = sample("Bprime_M400_2023", 1.0, "2023", "Bprime_M400_2023NanoList.txt", "/BprimeBprimeto2B4Tau_MB-400_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
Bprime_M400_2023BPix = sample("Bprime_M400_2023BPix", 1.0, "2023BPix", "Bprime_M400_2023BPixNanoList.txt", "/BprimeBprimeto2B4Tau_MB-400_MXi-2000_TuneCP5_13p6TeV-madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
Bprime_M1000_2024 = sample("Bprime_M1000_2024", 1.0, "2024", "Bprime_M1000_2024NanoList.txt", "/BprimeBprimeToB2Tau_Par-MB-1000-MXi-2000_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
Bprime_M1300_2024 = sample("Bprime_M1300_2024", 1.0, "2024", "Bprime_M1300_2024NanoList.txt", "/BprimeBprimeToB2Tau_Par-MB-1300-MXi-2000_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
Bprime_M1600_2024 = sample("Bprime_M1600_2024", 1.0, "2024", "Bprime_M1600_2024NanoList.txt", "/BprimeBprimeToB2Tau_Par-MB-1600-MXi-2000_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
Bprime_M400_2024 = sample("Bprime_M400_2024", 1.0, "2024", "Bprime_M400_2024NanoList.txt", "/BprimeBprimeToB2Tau_Par-MB-400-MXi-2000_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
Bprime_M700_2024 = sample("Bprime_M700_2024", 1.0, "2024", "Bprime_M700_2024NanoList.txt", "/BprimeBprimeToB2Tau_Par-MB-700-MXi-2000_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")

################################################
###                                          ###
###                  DATA                    ###
###                                          ###
################################################

SingleElecRun2022C = sample("SingleElecRun2022C", 1.0, "2022", "SingleElecRun2022CNanoList.txt", "/EGamma/Run2022C-NanoAODv15-v1/NANOAOD")
SingleElecRun2022D = sample("SingleElecRun2022D", 1.0, "2022", "SingleElecRun2022DNanoList.txt", "/EGamma/Run2022D-NanoAODv15-v1/NANOAOD")
SingleElecRun2022EEE  = sample("SingleElecRun2022EEE", 1.0, "2022EE", "SingleElecRun2022EEENanoList.txt", "/EGamma/Run2022E-NanoAODv15-v1/NANOAOD")
SingleElecRun2022EEF  = sample("SingleElecRun2022EEF", 1.0, "2022EE", "SingleElecRun2022EEFNanoList.txt", "/EGamma/Run2022F-NanoAODv15-v1/NANOAOD")
SingleElecRun2022EEG  = sample("SingleElecRun2022EEG", 1.0, "2022EE", "SingleElecRun2022EEGNanoList.txt", "/EGamma/Run2022G-NanoAODv15-v1/NANOAOD")
SingleElecRun2023C01  = sample("SingleElecRun2023C01", 1.0, "2023", "SingleElecRun2023C01NanoList.txt", "/EGamma0/Run2023C-NanoAODv15_v1/NANOAOD")
SingleElecRun2023C02  = sample("SingleElecRun2023C02", 1.0, "2023", "SingleElecRun2023C02NanoList.txt", "/EGamma0/Run2023C-NanoAODv15_v2-v1/NANOAOD")
SingleElecRun2023C03  = sample("SingleElecRun2023C03", 1.0, "2023", "SingleElecRun2023C03NanoList.txt", "/EGamma0/Run2023C-NanoAODv15_v3-v1/NANOAOD")
SingleElecRun2023C04  = sample("SingleElecRun2023C04", 1.0, "2023", "SingleElecRun2023C04NanoList.txt", "/EGamma0/Run2023C-NanoAODv15_v4-v1/NANOAOD")
SingleElecRun2023C11  = sample("SingleElecRun2023C11", 1.0, "2023", "SingleElecRun2023C11NanoList.txt", "/EGamma1/Run2023C-NanoAODv15_v1/NANOAOD")
SingleElecRun2023C12  = sample("SingleElecRun2023C12", 1.0, "2023", "SingleElecRun2023C12NanoList.txt", "/EGamma1/Run2023C-NanoAODv15_v2-v1/NANOAOD")
SingleElecRun2023C13  = sample("SingleElecRun2023C13", 1.0, "2023", "SingleElecRun2023C13NanoList.txt", "/EGamma1/Run2023C-NanoAODv15_v3-v1/NANOAOD")
SingleElecRun2023C14  = sample("SingleElecRun2023C14", 1.0, "2023", "SingleElecRun2023C14NanoList.txt", "/EGamma1/Run2023C-NanoAODv15_v4-v1/NANOAOD")
SingleElecRun2023BPixD01  = sample("SingleElecRun2023BPixD01", 1.0, "2023BPix", "SingleElecRun2023BPixD01NanoList.txt", "/EGamma0/Run2023D-NanoAODv15_v1/NANOAOD")
SingleElecRun2023BPixD02  = sample("SingleElecRun2023BPixD02", 1.0, "2023BPix", "SingleElecRun2023BPixD02NanoList.txt", "/EGamma0/Run2023D-NanoAODv15_v2-v1/NANOAOD")
SingleElecRun2023BPixD11  = sample("SingleElecRun2023BPixD11", 1.0, "2023BPix", "SingleElecRun2023BPixD11NanoList.txt", "/EGamma1/Run2023D-NanoAODv15_v1/NANOAOD")
SingleElecRun2023BPixD12  = sample("SingleElecRun2023BPixD12", 1.0, "2023BPix", "SingleElecRun2023BPixD12NanoList.txt", "/EGamma1/Run2023D-NanoAODv15_v2-v1/NANOAOD")
SingleElecRun2024C0 = sample("SingleElecRun2024C0", 1.0, "2024", "SingleElecRun2024C0NanoList.txt","/EGamma0/Run2024C-MINIv6NANOv15-v1/NANOAOD")
SingleElecRun2024D0 = sample("SingleElecRun2024D0", 1.0, "2024", "SingleElecRun2024D0NanoList.txt","/EGamma0/Run2024D-MINIv6NANOv15-v1/NANOAOD")
SingleElecRun2024E0 = sample("SingleElecRun2024E0", 1.0, "2024", "SingleElecRun2024E0NanoList.txt","/EGamma0/Run2024E-MINIv6NANOv15-v1/NANOAOD")
SingleElecRun2024F0 = sample("SingleElecRun2024F0", 1.0, "2024", "SingleElecRun2024F0NanoList.txt","/EGamma0/Run2024F-MINIv6NANOv15-v1/NANOAOD")
SingleElecRun2024G0 = sample("SingleElecRun2024G0", 1.0, "2024", "SingleElecRun2024G0NanoList.txt","/EGamma0/Run2024G-MINIv6NANOv15-v2/NANOAOD")
SingleElecRun2024H0 = sample("SingleElecRun2024H0", 1.0, "2024", "SingleElecRun2024H0NanoList.txt","/EGamma0/Run2024H-MINIv6NANOv15-v2/NANOAOD")
SingleElecRun2024I01 = sample("SingleElecRun2024I01", 1.0, "2024", "SingleElecRun2024I01NanoList.txt","/EGamma0/Run2024I-MINIv6NANOv15-v1/NANOAOD")
SingleElecRun2024I02 = sample("SingleElecRun2024I02", 1.0, "2024", "SingleElecRun2024I02NanoList.txt","/EGamma0/Run2024I-MINIv6NANOv15_v2-v1/NANOAOD")
SingleElecRun2024C1 = sample("SingleElecRun2024C1", 1.0, "2024", "SingleElecRun2024C1NanoList.txt","/EGamma1/Run2024C-MINIv6NANOv15-v1/NANOAOD")
SingleElecRun2024D1 = sample("SingleElecRun2024D1", 1.0, "2024", "SingleElecRun2024D1NanoList.txt","/EGamma1/Run2024D-MINIv6NANOv15-v1/NANOAOD")
SingleElecRun2024E1 = sample("SingleElecRun2024E1", 1.0, "2024", "SingleElecRun2024E1NanoList.txt","/EGamma1/Run2024E-MINIv6NANOv15-v1/NANOAOD")
SingleElecRun2024F1 = sample("SingleElecRun2024F1", 1.0, "2024", "SingleElecRun2024F1NanoList.txt","/EGamma1/Run2024F-MINIv6NANOv15-v1/NANOAOD")
SingleElecRun2024G1 = sample("SingleElecRun2024G1", 1.0, "2024", "SingleElecRun2024G1NanoList.txt","/EGamma1/Run2024G-MINIv6NANOv15-v2/NANOAOD")
SingleElecRun2024H1 = sample("SingleElecRun2024H1", 1.0, "2024", "SingleElecRun2024H1NanoList.txt","/EGamma1/Run2024H-MINIv6NANOv15-v1/NANOAOD")
SingleElecRun2024I11 = sample("SingleElecRun2024I11", 1.0, "2024", "SingleElecRun2024I11NanoList.txt","/EGamma1/Run2024I-MINIv6NANOv15-v1/NANOAOD")
SingleElecRun2024I12 = sample("SingleElecRun2024I12", 1.0, "2024", "SingleElecRun2024I12NanoList.txt","/EGamma1/Run2024I-MINIv6NANOv15_v2-v1/NANOAOD")
SingleElecRun2025B0  = sample("SingleElecRun2025B0" , 1.0, "2025", "SingleElecRun2025B0NanoList.txt" ,"/EGamma0/Run2025B-PromptReco-v1/NANOAOD")
SingleElecRun2025C01 = sample("SingleElecRun2025C01", 1.0, "2025", "SingleElecRun2025C01NanoList.txt","/EGamma0/Run2025C-PromptReco-v1/NANOAOD")
SingleElecRun2025C02 = sample("SingleElecRun2025C02", 1.0, "2025", "SingleElecRun2025C02NanoList.txt","/EGamma0/Run2025C-PromptReco-v2/NANOAOD")
SingleElecRun2025D0  = sample("SingleElecRun2025D0" , 1.0, "2025", "SingleElecRun2025D0NanoList.txt" ,"/EGamma0/Run2025D-PromptReco-v1/NANOAOD")
SingleElecRun2025E0  = sample("SingleElecRun2025E0" , 1.0, "2025", "SingleElecRun2025E0NanoList.txt" ,"/EGamma0/Run2025E-PromptReco-v1/NANOAOD")
SingleElecRun2025F01 = sample("SingleElecRun2025F01", 1.0, "2025", "SingleElecRun2025F01NanoList.txt","/EGamma0/Run2025F-PromptReco-v1/NANOAOD")
SingleElecRun2025F02 = sample("SingleElecRun2025F02", 1.0, "2025", "SingleElecRun2025F02NanoList.txt","/EGamma0/Run2025F-PromptReco-v2/NANOAOD")
SingleElecRun2025G0  = sample("SingleElecRun2025G0" , 1.0, "2025", "SingleElecRun2025G0NanoList.txt" ,"/EGamma0/Run2025G-PromptReco-v1/NANOAOD")
SingleElecRun2025B1  = sample("SingleElecRun2025B1" , 1.0, "2025", "SingleElecRun2025B1NanoList.txt" ,"/EGamma1/Run2025B-PromptReco-v1/NANOAOD")
SingleElecRun2025C11 = sample("SingleElecRun2025C11", 1.0, "2025", "SingleElecRun2025C11NanoList.txt","/EGamma1/Run2025C-PromptReco-v1/NANOAOD")
SingleElecRun2025C12 = sample("SingleElecRun2025C12", 1.0, "2025", "SingleElecRun2025C12NanoList.txt","/EGamma1/Run2025C-PromptReco-v2/NANOAOD")
SingleElecRun2025D1  = sample("SingleElecRun2025D1" , 1.0, "2025", "SingleElecRun2025D1NanoList.txt" ,"/EGamma1/Run2025D-PromptReco-v1/NANOAOD")
SingleElecRun2025E1  = sample("SingleElecRun2025E1" , 1.0, "2025", "SingleElecRun2025E1NanoList.txt" ,"/EGamma1/Run2025E-PromptReco-v1/NANOAOD")
SingleElecRun2025F11 = sample("SingleElecRun2025F11", 1.0, "2025", "SingleElecRun2025F11NanoList.txt","/EGamma1/Run2025F-PromptReco-v1/NANOAOD")
SingleElecRun2025F12 = sample("SingleElecRun2025F12", 1.0, "2025", "SingleElecRun2025F12NanoList.txt","/EGamma1/Run2025F-PromptReco-v2/NANOAOD")
SingleElecRun2025G1  = sample("SingleElecRun2025G1" , 1.0, "2025", "SingleElecRun2025G1NanoList.txt" ,"/EGamma1/Run2025G-PromptReco-v1/NANOAOD")
SingleElecRun2025B2  = sample("SingleElecRun2025B2" , 1.0, "2025", "SingleElecRun2025B2NanoList.txt" ,"/EGamma2/Run2025B-PromptReco-v1/NANOAOD")
SingleElecRun2025C21 = sample("SingleElecRun2025C21", 1.0, "2025", "SingleElecRun2025C21NanoList.txt","/EGamma2/Run2025C-PromptReco-v1/NANOAOD")
SingleElecRun2025C22 = sample("SingleElecRun2025C22", 1.0, "2025", "SingleElecRun2025C22NanoList.txt","/EGamma2/Run2025C-PromptReco-v2/NANOAOD")
SingleElecRun2025D2  = sample("SingleElecRun2025D2" , 1.0, "2025", "SingleElecRun2025D2NanoList.txt" ,"/EGamma2/Run2025D-PromptReco-v1/NANOAOD")
SingleElecRun2025E2  = sample("SingleElecRun2025E2" , 1.0, "2025", "SingleElecRun2025E2NanoList.txt" ,"/EGamma2/Run2025E-PromptReco-v1/NANOAOD")
SingleElecRun2025F21 = sample("SingleElecRun2025F21", 1.0, "2025", "SingleElecRun2025F21NanoList.txt","/EGamma2/Run2025F-PromptReco-v1/NANOAOD")
SingleElecRun2025F22 = sample("SingleElecRun2025F22", 1.0, "2025", "SingleElecRun2025F22NanoList.txt","/EGamma2/Run2025F-PromptReco-v2/NANOAOD")
SingleElecRun2025G2  = sample("SingleElecRun2025G2" , 1.0, "2025", "SingleElecRun2025G2NanoList.txt" ,"/EGamma2/Run2025G-PromptReco-v1/NANOAOD")
SingleElecRun2025B3  = sample("SingleElecRun2025B3" , 1.0, "2025", "SingleElecRun2025B3NanoList.txt" ,"/EGamma3/Run2025B-PromptReco-v1/NANOAOD")
SingleElecRun2025C31 = sample("SingleElecRun2025C31", 1.0, "2025", "SingleElecRun2025C31NanoList.txt","/EGamma3/Run2025C-PromptReco-v1/NANOAOD")
SingleElecRun2025C32 = sample("SingleElecRun2025C32", 1.0, "2025", "SingleElecRun2025C32NanoList.txt","/EGamma3/Run2025C-PromptReco-v2/NANOAOD")
SingleElecRun2025D3  = sample("SingleElecRun2025D3" , 1.0, "2025", "SingleElecRun2025D3NanoList.txt" ,"/EGamma3/Run2025D-PromptReco-v1/NANOAOD")
SingleElecRun2025E3  = sample("SingleElecRun2025E3" , 1.0, "2025", "SingleElecRun2025E3NanoList.txt" ,"/EGamma3/Run2025E-PromptReco-v1/NANOAOD")
SingleElecRun2025F31 = sample("SingleElecRun2025F31", 1.0, "2025", "SingleElecRun2025F31NanoList.txt","/EGamma3/Run2025F-PromptReco-v1/NANOAOD")
SingleElecRun2025F32 = sample("SingleElecRun2025F32", 1.0, "2025", "SingleElecRun2025F32NanoList.txt","/EGamma3/Run2025F-PromptReco-v2/NANOAOD")
SingleElecRun2025G3  = sample("SingleElecRun2025G3" , 1.0, "2025", "SingleElecRun2025G3NanoList.txt" ,"/EGamma3/Run2025G-PromptReco-v1/NANOAOD")

SingleMuonRun2022C = sample("SingleMuonRun2022C", 1.0, "2022", "SingleMuonRun2022CNanoList.txt", "/Muon/Run2022C-NanoAODv15-v1/NANOAOD")
SingleMuonRun2022D = sample("SingleMuonRun2022D", 1.0, "2022", "SingleMuonRun2022DNanoList.txt", "/Muon/Run2022D-NanoAODv15-v1/NANOAOD")
SingleMuonRun2022EEE  = sample("SingleMuonRun2022EEE", 1.0, "2022EE", "SingleMuonRun2022EEENanoList.txt", "/Muon/Run2022E-NanoAODv15-v1/NANOAOD")
SingleMuonRun2022EEF  = sample("SingleMuonRun2022EEF", 1.0, "2022EE", "SingleMuonRun2022EEFNanoList.txt", "/Muon/Run2022F-NanoAODv15-v1/NANOAOD")
SingleMuonRun2022EEG  = sample("SingleMuonRun2022EEG", 1.0, "2022EE", "SingleMuonRun2022EEGNanoList.txt", "/Muon/Run2022G-NanoAODv15-v1/NANOAOD")
SingleMuonRun2023C01  = sample("SingleMuonRun2023C01", 1.0, "2023", "SingleMuonRun2023C01NanoList.txt", "/Muon0/Run2023C-NanoAODv15_v1/NANOAOD")
SingleMuonRun2023C02  = sample("SingleMuonRun2023C02", 1.0, "2023", "SingleMuonRun2023C02NanoList.txt", "/Muon0/Run2023C-NanoAODv15_v2-v1/NANOAOD")
SingleMuonRun2023C03  = sample("SingleMuonRun2023C03", 1.0, "2023", "SingleMuonRun2023C03NanoList.txt", "/Muon0/Run2023C-NanoAODv15_v3-v1/NANOAOD")
SingleMuonRun2023C04  = sample("SingleMuonRun2023C04", 1.0, "2023", "SingleMuonRun2023C04NanoList.txt", "/Muon0/Run2023C-NanoAODv15_v4-v1/NANOAOD")
SingleMuonRun2023C11  = sample("SingleMuonRun2023C11", 1.0, "2023", "SingleMuonRun2023C11NanoList.txt", "/Muon1/Run2023C-NanoAODv15_v1/NANOAOD")
SingleMuonRun2023C12  = sample("SingleMuonRun2023C12", 1.0, "2023", "SingleMuonRun2023C12NanoList.txt", "/Muon1/Run2023C-NanoAODv15_v2-v1/NANOAOD")
SingleMuonRun2023C13  = sample("SingleMuonRun2023C13", 1.0, "2023", "SingleMuonRun2023C13NanoList.txt", "/Muon1/Run2023C-NanoAODv15_v3-v1/NANOAOD")
SingleMuonRun2023C14  = sample("SingleMuonRun2023C14", 1.0, "2023", "SingleMuonRun2023C14NanoList.txt", "/Muon1/Run2023C-NanoAODv15_v4-v1/NANOAOD")
SingleMuonRun2023BPixD01  = sample("SingleMuonRun2023BPixD01", 1.0, "2023BPix", "SingleMuonRun2023BPixD01NanoList.txt", "/Muon0/Run2023D-NanoAODv15_v1/NANOAOD")
SingleMuonRun2023BPixD02  = sample("SingleMuonRun2023BPixD02", 1.0, "2023BPix", "SingleMuonRun2023BPixD02NanoList.txt", "/Muon0/Run2023D-NanoAODv15_v2-v1/NANOAOD")
SingleMuonRun2023BPixD11  = sample("SingleMuonRun2023BPixD11", 1.0, "2023BPix", "SingleMuonRun2023BPixD11NanoList.txt", "/Muon1/Run2023D-NanoAODv15_v1/NANOAOD")
SingleMuonRun2023BPixD12  = sample("SingleMuonRun2023BPixD12", 1.0, "2023BPix", "SingleMuonRun2023BPixD12NanoList.txt", "/Muon1/Run2023D-NanoAODv15_v2-v1/NANOAOD")
SingleMuonRun2024C0 = sample("SingleMuonRun2024C0", 1.0, "2024", "SingleMuonRun2024C0NanoList.txt","/Muon0/Run2024C-MINIv6NANOv15-v1/NANOAOD")
SingleMuonRun2024D0 = sample("SingleMuonRun2024D0", 1.0, "2024", "SingleMuonRun2024D0NanoList.txt","/Muon0/Run2024D-MINIv6NANOv15-v1/NANOAOD")
SingleMuonRun2024E0 = sample("SingleMuonRun2024E0", 1.0, "2024", "SingleMuonRun2024E0NanoList.txt","/Muon0/Run2024E-MINIv6NANOv15-v1/NANOAOD")
SingleMuonRun2024F0 = sample("SingleMuonRun2024F0", 1.0, "2024", "SingleMuonRun2024F0NanoList.txt","/Muon0/Run2024F-MINIv6NANOv15-v1/NANOAOD")
SingleMuonRun2024G0 = sample("SingleMuonRun2024G0", 1.0, "2024", "SingleMuonRun2024G0NanoList.txt","/Muon0/Run2024G-MINIv6NANOv15-v1/NANOAOD")
SingleMuonRun2024H0 = sample("SingleMuonRun2024H0", 1.0, "2024", "SingleMuonRun2024H0NanoList.txt","/Muon0/Run2024H-MINIv6NANOv15-v1/NANOAOD")
SingleMuonRun2024I01 = sample("SingleMuonRun2024I01", 1.0, "2024", "SingleMuonRun2024I01NanoList.txt","/Muon0/Run2024I-MINIv6NANOv15-v1/NANOAOD")
SingleMuonRun2024I02 = sample("SingleMuonRun2024I02", 1.0, "2024", "SingleMuonRun2024I02NanoList.txt","/Muon0/Run2024I-MINIv6NANOv15_v2-v1/NANOAOD")
SingleMuonRun2024C1 = sample("SingleMuonRun2024C1", 1.0, "2024", "SingleMuonRun2024C1NanoList.txt","/Muon1/Run2024C-MINIv6NANOv15-v1/NANOAOD")
SingleMuonRun2024D1 = sample("SingleMuonRun2024D1", 1.0, "2024", "SingleMuonRun2024D1NanoList.txt","/Muon1/Run2024D-MINIv6NANOv15-v1/NANOAOD")
SingleMuonRun2024E1 = sample("SingleMuonRun2024E1", 1.0, "2024", "SingleMuonRun2024E1NanoList.txt","/Muon1/Run2024E-MINIv6NANOv15-v1/NANOAOD")
SingleMuonRun2024F1 = sample("SingleMuonRun2024F1", 1.0, "2024", "SingleMuonRun2024F1NanoList.txt","/Muon1/Run2024F-MINIv6NANOv15-v1/NANOAOD")
SingleMuonRun2024G1 = sample("SingleMuonRun2024G1", 1.0, "2024", "SingleMuonRun2024G1NanoList.txt","/Muon1/Run2024G-MINIv6NANOv15-v2/NANOAOD")
SingleMuonRun2024H1 = sample("SingleMuonRun2024H1", 1.0, "2024", "SingleMuonRun2024H1NanoList.txt","/Muon1/Run2024H-MINIv6NANOv15-v2/NANOAOD")
SingleMuonRun2024I11 = sample("SingleMuonRun2024I11", 1.0, "2024", "SingleMuonRun2024I11NanoList.txt","/Muon1/Run2024I-MINIv6NANOv15-v1/NANOAOD")
SingleMuonRun2024I12 = sample("SingleMuonRun2024I12", 1.0, "2024", "SingleMuonRun2024I12NanoList.txt","/Muon1/Run2024I-MINIv6NANOv15_v2-v1/NANOAOD")
SingleMuonRun2025B0  = sample("SingleMuonRun2025B0" , 1.0, "2025", "SingleMuonRun2025B0NanoList.txt" ,"/Muon0/Run2025B-PromptReco-v1/NANOAOD")
SingleMuonRun2025C01 = sample("SingleMuonRun2025C01", 1.0, "2025", "SingleMuonRun2025C01NanoList.txt","/Muon0/Run2025C-PromptReco-v1/NANOAOD")
SingleMuonRun2025C02 = sample("SingleMuonRun2025C02", 1.0, "2025", "SingleMuonRun2025C02NanoList.txt","/Muon0/Run2025C-PromptReco-v2/NANOAOD")
SingleMuonRun2025D0  = sample("SingleMuonRun2025D0" , 1.0, "2025", "SingleMuonRun2025D0NanoList.txt" ,"/Muon0/Run2025D-PromptReco-v1/NANOAOD")
SingleMuonRun2025E0  = sample("SingleMuonRun2025E0" , 1.0, "2025", "SingleMuonRun2025E0NanoList.txt" ,"/Muon0/Run2025E-PromptReco-v1/NANOAOD")
SingleMuonRun2025F01 = sample("SingleMuonRun2025F01", 1.0, "2025", "SingleMuonRun2025F01NanoList.txt","/Muon0/Run2025F-PromptReco-v1/NANOAOD")
SingleMuonRun2025F02 = sample("SingleMuonRun2025F02", 1.0, "2025", "SingleMuonRun2025F02NanoList.txt","/Muon0/Run2025F-PromptReco-v2/NANOAOD")
SingleMuonRun2025G0  = sample("SingleMuonRun2025G0" , 1.0, "2025", "SingleMuonRun2025G0NanoList.txt" ,"/Muon0/Run2025G-PromptReco-v1/NANOAOD")
SingleMuonRun2025B1  = sample("SingleMuonRun2025B1" , 1.0, "2025", "SingleMuonRun2025B1NanoList.txt" ,"/Muon1/Run2025B-PromptReco-v1/NANOAOD")
SingleMuonRun2025C11 = sample("SingleMuonRun2025C11", 1.0, "2025", "SingleMuonRun2025C11NanoList.txt","/Muon1/Run2025C-PromptReco-v1/NANOAOD")
SingleMuonRun2025C12 = sample("SingleMuonRun2025C12", 1.0, "2025", "SingleMuonRun2025C12NanoList.txt","/Muon1/Run2025C-PromptReco-v2/NANOAOD")
SingleMuonRun2025D1  = sample("SingleMuonRun2025D1" , 1.0, "2025", "SingleMuonRun2025D1NanoList.txt" ,"/Muon1/Run2025D-PromptReco-v1/NANOAOD")
SingleMuonRun2025E1  = sample("SingleMuonRun2025E1" , 1.0, "2025", "SingleMuonRun2025E1NanoList.txt" ,"/Muon1/Run2025E-PromptReco-v1/NANOAOD")
SingleMuonRun2025F11 = sample("SingleMuonRun2025F11", 1.0, "2025", "SingleMuonRun2025F11NanoList.txt","/Muon1/Run2025F-PromptReco-v1/NANOAOD")
SingleMuonRun2025F12 = sample("SingleMuonRun2025F12", 1.0, "2025", "SingleMuonRun2025F12NanoList.txt","/Muon1/Run2025F-PromptReco-v2/NANOAOD")
SingleMuonRun2025G1  = sample("SingleMuonRun2025G1" , 1.0, "2025", "SingleMuonRun2025G1NanoList.txt" ,"/Muon1/Run2025G-PromptReco-v1/NANOAOD")

MuonEGRun2022C = sample("MuonEGRun2022C", 1.0, "2022", "MuonEGRun2022CNanoList.txt", "/MuonEG/Run2022C-22Sep2023-v1/NANOAOD")
MuonEGRun2022D = sample("MuonEGRun2022D", 1.0, "2022", "MuonEGRun2022DNanoList.txt", "/MuonEG/Run2022D-22Sep2023-v1/NANOAOD")
MuonEGRun2022EEE  = sample("MuonEGRun2022EEE", 1.0, "2022EE", "MuonEGRun2022EEENanoList.txt", "/MuonEG/Run2022E-22Sep2023-v1/NANOAOD")
MuonEGRun2022EEF  = sample("MuonEGRun2022EEF", 1.0, "2022EE", "MuonEGRun2022EEFNanoList.txt", "/MuonEG/Run2022F-22Sep2023-v1/NANOAOD")
MuonEGRun2022EEG  = sample("MuonEGRun2022EEG", 1.0, "2022EE", "MuonEGRun2022EEGNanoList.txt", "/MuonEG/Run2022G-22Sep2023-v1/NANOAOD")
MuonEGRun2023C1  = sample("MuonEGRun2023C1", 1.0, "2023", "MuonEGRun2023C1NanoList.txt", "/MuonEG/Run2023C-22Sep2023_v1-v1/NANOAOD")
MuonEGRun2023C2  = sample("MuonEGRun2023C2", 1.0, "2023", "MuonEGRun2023C2NanoList.txt", "/MuonEG/Run2023C-22Sep2023_v2-v1/NANOAOD")
MuonEGRun2023C3  = sample("MuonEGRun2023C3", 1.0, "2023", "MuonEGRun2023C3NanoList.txt", "/MuonEG/Run2023C-22Sep2023_v3-v1/NANOAOD")
MuonEGRun2023C4  = sample("MuonEGRun2023C4", 1.0, "2023", "MuonEGRun2023C4NanoList.txt", "/MuonEG/Run2023C-22Sep2023_v4-v1/NANOAOD")
MuonEGRun2023BPixD1  = sample("MuonEGRun2023BPixD1", 1.0, "2023BPix", "MuonEGRun2023BPixD1NanoList.txt", "/MuonEG/Run2023D-22Sep2023_v1-v1/NANOAOD")
MuonEGRun2023BPixD2  = sample("MuonEGRun2023BPixD2", 1.0, "2023BPix", "MuonEGRun2023BPixD2NanoList.txt", "/MuonEG/Run2023D-22Sep2023_v2-v1/NANOAOD")
MuonEGRun2024C = sample("MuonEGRun2024C", 1.0, "2024", "MuonEGRun2024CNanoList.txt","/MuonEG/Run2024C-MINIv6NANOv15-v1/NANOAOD")
MuonEGRun2024D = sample("MuonEGRun2024D", 1.0, "2024", "MuonEGRun2024DNanoList.txt","/MuonEG/Run2024D-MINIv6NANOv15-v1/NANOAOD")
MuonEGRun2024E = sample("MuonEGRun2024E", 1.0, "2024", "MuonEGRun2024ENanoList.txt","/MuonEG/Run2024E-MINIv6NANOv15-v1/NANOAOD")
MuonEGRun2024F = sample("MuonEGRun2024F", 1.0, "2024", "MuonEGRun2024FNanoList.txt","/MuonEG/Run2024F-MINIv6NANOv15-v2/NANOAOD")
MuonEGRun2024G = sample("MuonEGRun2024G", 1.0, "2024", "MuonEGRun2024GNanoList.txt","/MuonEG/Run2024G-MINIv6NANOv15-v3/NANOAOD")
MuonEGRun2024H = sample("MuonEGRun2024H", 1.0, "2024", "MuonEGRun2024HNanoList.txt","/MuonEG/Run2024H-MINIv6NANOv15-v2/NANOAOD")
MuonEGRun2024I1 = sample("MuonEGRun2024I1", 1.0, "2024", "MuonEGRun2024I1NanoList.txt","/MuonEG/Run2024I-MINIv6NANOv15-v2/NANOAOD")
MuonEGRun2024I2 = sample("MuonEGRun2024I2", 1.0, "2024", "MuonEGRun2024I2NanoList.txt","/MuonEG/Run2024I-MINIv6NANOv15_v2-v2/NANOAOD")
MuonEGRun2025B  = sample("MuonEGRun2025B" , 1.0, "2025", "MuonEGRun2025BNanoList.txt" ,"/MuonEG/Run2025B-PromptReco-v1/NANOAOD")
MuonEGRun2025C1 = sample("MuonEGRun2025C1", 1.0, "2025", "MuonEGRun2025C1NanoList.txt","/MuonEG/Run2025C-PromptReco-v1/NANOAOD")
MuonEGRun2025C2 = sample("MuonEGRun2025C2", 1.0, "2025", "MuonEGRun2025C2NanoList.txt","/MuonEG/Run2025C-PromptReco-v2/NANOAOD")
MuonEGRun2025D  = sample("MuonEGRun2025D" , 1.0, "2025", "MuonEGRun2025DNanoList.txt" ,"/MuonEG/Run2025D-PromptReco-v1/NANOAOD")
MuonEGRun2025E  = sample("MuonEGRun2025E" , 1.0, "2025", "MuonEGRun2025ENanoList.txt" ,"/MuonEG/Run2025E-PromptReco-v1/NANOAOD")
MuonEGRun2025F1 = sample("MuonEGRun2025F1", 1.0, "2025", "MuonEGRun2025F1NanoList.txt","/MuonEG/Run2025F-PromptReco-v1/NANOAOD")
MuonEGRun2025F2 = sample("MuonEGRun2025F2", 1.0, "2025", "MuonEGRun2025F2NanoList.txt","/MuonEG/Run2025F-PromptReco-v2/NANOAOD")
MuonEGRun2025G  = sample("MuonEGRun2025G" , 1.0, "2025", "MuonEGRun2025GNanoList.txt" ,"/MuonEG/Run2025G-PromptReco-v1/NANOAOD")

TauRun2022C = sample("TauRun2022C", 1.0, "2022", "TauRun2022CNanoList.txt", "/Tau/Run2022C-22Sep2023-v1/NANOAOD")
TauRun2022D = sample("TauRun2022D", 1.0, "2022", "TauRun2022DNanoList.txt", "/Tau/Run2022D-22Sep2023-v1/NANOAOD")
TauRun2022EEE  = sample("TauRun2022EEE", 1.0, "2022EE", "TauRun2022EEENanoList.txt", "/Tau/Run2022E-22Sep2023-v1/NANOAOD")
TauRun2022EEF  = sample("TauRun2022EEF", 1.0, "2022EE", "TauRun2022EEFNanoList.txt", "/Tau/Run2022F-22Sep2023-v1/NANOAOD")
TauRun2022EEG  = sample("TauRun2022EEG", 1.0, "2022EE", "TauRun2022EEGNanoList.txt", "/Tau/Run2022G-22Sep2023-v1/NANOAOD")
TauRun2023C1  = sample("TauRun2023C1", 1.0, "2023", "TauRun2023C1NanoList.txt", "/Tau/Run2023C-22Sep2023_v1-v2/NANOAOD")
TauRun2023C2  = sample("TauRun2023C2", 1.0, "2023", "TauRun2023C2NanoList.txt", "/Tau/Run2023C-22Sep2023_v2-v1/NANOAOD")
TauRun2023C3  = sample("TauRun2023C3", 1.0, "2023", "TauRun2023C3NanoList.txt", "/Tau/Run2023C-22Sep2023_v3-v1/NANOAOD")
TauRun2023C4  = sample("TauRun2023C4", 1.0, "2023", "TauRun2023C4NanoList.txt", "/Tau/Run2023C-22Sep2023_v4-v1/NANOAOD")
TauRun2023BPixD1  = sample("TauRun2023BPixD1", 1.0, "2023BPix", "TauRun2023BPixD1NanoList.txt", "/Tau/Run2023D-22Sep2023_v1-v1/NANOAOD")
TauRun2023BPixD2  = sample("TauRun2023BPixD2", 1.0, "2023BPix", "TauRun2023BPixD2NanoList.txt", "/Tau/Run2023D-22Sep2023_v2-v1/NANOAOD")
TauRun2024C = sample("TauRun2024C", 1.0, "2024", "TauRun2024CNanoList.txt","/Tau/Run2024C-MINIv6NANOv15-v1/NANOAOD")
TauRun2024D = sample("TauRun2024D", 1.0, "2024", "TauRun2024DNanoList.txt","/Tau/Run2024D-MINIv6NANOv15-v1/NANOAOD")
TauRun2024E = sample("TauRun2024E", 1.0, "2024", "TauRun2024ENanoList.txt","/Tau/Run2024E-MINIv6NANOv15-v1/NANOAOD")
TauRun2024F = sample("TauRun2024F", 1.0, "2024", "TauRun2024FNanoList.txt","/Tau/Run2024F-MINIv6NANOv15-v1/NANOAOD")
TauRun2024G = sample("TauRun2024G", 1.0, "2024", "TauRun2024GNanoList.txt","/Tau/Run2024G-MINIv6NANOv15-v1/NANOAOD")
TauRun2024H = sample("TauRun2024H", 1.0, "2024", "TauRun2024HNanoList.txt","/Tau/Run2024H-MINIv6NANOv15-v1/NANOAOD")
TauRun2024I1 = sample("TauRun2024I1", 1.0, "2024", "TauRun2024I1NanoList.txt","/Tau/Run2024I-MINIv6NANOv15-v1/NANOAOD")
TauRun2024I2 = sample("TauRun2024I2", 1.0, "2024", "TauRun2024I2NanoList.txt","/Tau/Run2024I-MINIv6NANOv15_v2-v1/NANOAOD")
TauRun2025B  = sample("TauRun2025B" , 1.0, "2025", "TauRun2025BNanoList.txt" ,"/Tau/Run2025B-PromptReco-v1/NANOAOD")
TauRun2025C1 = sample("TauRun2025C1", 1.0, "2025", "TauRun2025C1NanoList.txt","/Tau/Run2025C-PromptReco-v1/NANOAOD")
TauRun2025C2 = sample("TauRun2025C2", 1.0, "2025", "TauRun2025C2NanoList.txt","/Tau/Run2025C-PromptReco-v2/NANOAOD")
TauRun2025D  = sample("TauRun2025D" , 1.0, "2025", "TauRun2025DNanoList.txt" ,"/Tau/Run2025D-PromptReco-v1/NANOAOD")
TauRun2025E  = sample("TauRun2025E" , 1.0, "2025", "TauRun2025ENanoList.txt" ,"/Tau/Run2025E-PromptReco-v1/NANOAOD")
TauRun2025F1 = sample("TauRun2025F1", 1.0, "2025", "TauRun2025F1NanoList.txt","/Tau/Run2025F-PromptReco-v1/NANOAOD")
TauRun2025F2 = sample("TauRun2025F2", 1.0, "2025", "TauRun2025F2NanoList.txt","/Tau/Run2025F-PromptReco-v2/NANOAOD")
TauRun2025G  = sample("TauRun2025G" , 1.0, "2025", "TauRun2025GNanoList.txt" ,"/Tau/Run2025G-PromptReco-v1/NANOAOD")

NonpromptSingleElecRun2022C = sample("NonpromptSingleElecRun2022C", 1.0, "2022", "SingleElecRun2022CNanoList.txt", "/EGamma/Run2022C-NanoAODv15-v1/NANOAOD")
NonpromptSingleElecRun2022D = sample("NonpromptSingleElecRun2022D", 1.0, "2022", "SingleElecRun2022DNanoList.txt", "/EGamma/Run2022D-NanoAODv15-v1/NANOAOD")
NonpromptSingleElecRun2022EEE  = sample("NonpromptSingleElecRun2022EEE", 1.0, "2022EE", "SingleElecRun2022EEENanoList.txt", "/EGamma/Run2022E-NanoAODv15-v1/NANOAOD")
NonpromptSingleElecRun2022EEF  = sample("NonpromptSingleElecRun2022EEF", 1.0, "2022EE", "SingleElecRun2022EEFNanoList.txt", "/EGamma/Run2022F-NanoAODv15-v1/NANOAOD")
NonpromptSingleElecRun2022EEG  = sample("NonpromptSingleElecRun2022EEG", 1.0, "2022EE", "SingleElecRun2022EEGNanoList.txt", "/EGamma/Run2022G-NanoAODv15-v1/NANOAOD")
NonpromptSingleElecRun2023C01  = sample("NonpromptSingleElecRun2023C01", 1.0, "2023", "SingleElecRun2023C01NanoList.txt", "/EGamma0/Run2023C-NanoAODv15_v1/NANOAOD")
NonpromptSingleElecRun2023C02  = sample("NonpromptSingleElecRun2023C02", 1.0, "2023", "SingleElecRun2023C02NanoList.txt", "/EGamma0/Run2023C-NanoAODv15_v2-v1/NANOAOD")
NonpromptSingleElecRun2023C03  = sample("NonpromptSingleElecRun2023C03", 1.0, "2023", "SingleElecRun2023C03NanoList.txt", "/EGamma0/Run2023C-NanoAODv15_v3-v1/NANOAOD")
NonpromptSingleElecRun2023C04  = sample("NonpromptSingleElecRun2023C04", 1.0, "2023", "SingleElecRun2023C04NanoList.txt", "/EGamma0/Run2023C-NanoAODv15_v4-v1/NANOAOD")
NonpromptSingleElecRun2023C11  = sample("NonpromptSingleElecRun2023C11", 1.0, "2023", "SingleElecRun2023C11NanoList.txt", "/EGamma1/Run2023C-NanoAODv15_v1/NANOAOD")
NonpromptSingleElecRun2023C12  = sample("NonpromptSingleElecRun2023C12", 1.0, "2023", "SingleElecRun2023C12NanoList.txt", "/EGamma1/Run2023C-NanoAODv15_v2-v1/NANOAOD")
NonpromptSingleElecRun2023C13  = sample("NonpromptSingleElecRun2023C13", 1.0, "2023", "SingleElecRun2023C13NanoList.txt", "/EGamma1/Run2023C-NanoAODv15_v3-v1/NANOAOD")
NonpromptSingleElecRun2023C14  = sample("NonpromptSingleElecRun2023C14", 1.0, "2023", "SingleElecRun2023C14NanoList.txt", "/EGamma1/Run2023C-NanoAODv15_v4-v1/NANOAOD")
NonpromptSingleElecRun2023BPixD01  = sample("NonpromptSingleElecRun2023BPixD01", 1.0, "2023BPix", "SingleElecRun2023BPixD01NanoList.txt", "/EGamma0/Run2023D-NanoAODv15_v1/NANOAOD")
NonpromptSingleElecRun2023BPixD02  = sample("NonpromptSingleElecRun2023BPixD02", 1.0, "2023BPix", "SingleElecRun2023BPixD02NanoList.txt", "/EGamma0/Run2023D-NanoAODv15_v2-v1/NANOAOD")
NonpromptSingleElecRun2023BPixD11  = sample("NonpromptSingleElecRun2023BPixD11", 1.0, "2023BPix", "SingleElecRun2023BPixD11NanoList.txt", "/EGamma1/Run2023D-NanoAODv15_v1/NANOAOD")
NonpromptSingleElecRun2023BPixD12  = sample("NonpromptSingleElecRun2023BPixD12", 1.0, "2023BPix", "SingleElecRun2023BPixD12NanoList.txt", "/EGamma1/Run2023D-NanoAODv15_v2-v1/NANOAOD")
NonpromptSingleElecRun2024C0 = sample("NonpromptSingleElecRun2024C0", 1.0, "2024", "NonpromptSingleElecRun2024C0NanoList.txt","/EGamma0/Run2024C-MINIv6NANOv15-v1/NANOAOD")
NonpromptSingleElecRun2024D0 = sample("NonpromptSingleElecRun2024D0", 1.0, "2024", "NonpromptSingleElecRun2024D0NanoList.txt","/EGamma0/Run2024D-MINIv6NANOv15-v1/NANOAOD")
NonpromptSingleElecRun2024E0 = sample("NonpromptSingleElecRun2024E0", 1.0, "2024", "NonpromptSingleElecRun2024E0NanoList.txt","/EGamma0/Run2024E-MINIv6NANOv15-v1/NANOAOD")
NonpromptSingleElecRun2024F0 = sample("NonpromptSingleElecRun2024F0", 1.0, "2024", "NonpromptSingleElecRun2024F0NanoList.txt","/EGamma0/Run2024F-MINIv6NANOv15-v1/NANOAOD")
NonpromptSingleElecRun2024G0 = sample("NonpromptSingleElecRun2024G0", 1.0, "2024", "NonpromptSingleElecRun2024G0NanoList.txt","/EGamma0/Run2024G-MINIv6NANOv15-v2/NANOAOD")
NonpromptSingleElecRun2024H0 = sample("NonpromptSingleElecRun2024H0", 1.0, "2024", "NonpromptSingleElecRun2024H0NanoList.txt","/EGamma0/Run2024H-MINIv6NANOv15-v2/NANOAOD")
NonpromptSingleElecRun2024I01 = sample("NonpromptSingleElecRun2024I01", 1.0, "2024", "NonpromptSingleElecRun2024I01NanoList.txt","/EGamma0/Run2024I-MINIv6NANOv15-v1/NANOAOD")
NonpromptSingleElecRun2024I02 = sample("NonpromptSingleElecRun2024I02", 1.0, "2024", "NonpromptSingleElecRun2024I02NanoList.txt","/EGamma0/Run2024I-MINIv6NANOv15_v2-v1/NANOAOD")
NonpromptSingleElecRun2024C1 = sample("NonpromptSingleElecRun2024C1", 1.0, "2024", "NonpromptSingleElecRun2024C1NanoList.txt","/EGamma1/Run2024C-MINIv6NANOv15-v1/NANOAOD")
NonpromptSingleElecRun2024D1 = sample("NonpromptSingleElecRun2024D1", 1.0, "2024", "NonpromptSingleElecRun2024D1NanoList.txt","/EGamma1/Run2024D-MINIv6NANOv15-v1/NANOAOD")
NonpromptSingleElecRun2024E1 = sample("NonpromptSingleElecRun2024E1", 1.0, "2024", "NonpromptSingleElecRun2024E1NanoList.txt","/EGamma1/Run2024E-MINIv6NANOv15-v1/NANOAOD")
NonpromptSingleElecRun2024F1 = sample("NonpromptSingleElecRun2024F1", 1.0, "2024", "NonpromptSingleElecRun2024F1NanoList.txt","/EGamma1/Run2024F-MINIv6NANOv15-v1/NANOAOD")
NonpromptSingleElecRun2024G1 = sample("NonpromptSingleElecRun2024G1", 1.0, "2024", "NonpromptSingleElecRun2024G1NanoList.txt","/EGamma1/Run2024G-MINIv6NANOv15-v2/NANOAOD")
NonpromptSingleElecRun2024H1 = sample("NonpromptSingleElecRun2024H1", 1.0, "2024", "NonpromptSingleElecRun2024H1NanoList.txt","/EGamma1/Run2024H-MINIv6NANOv15-v1/NANOAOD")
NonpromptSingleElecRun2024I11 = sample("NonpromptSingleElecRun2024I11", 1.0, "2024", "NonpromptSingleElecRun2024I11NanoList.txt","/EGamma1/Run2024I-MINIv6NANOv15-v1/NANOAOD")
NonpromptSingleElecRun2024I12 = sample("NonpromptSingleElecRun2024I12", 1.0, "2024", "NonpromptSingleElecRun2024I12NanoList.txt","/EGamma1/Run2024I-MINIv6NANOv15_v2-v1/NANOAOD")
NonpromptSingleElecRun2025B0  = sample("NonpromptSingleElecRun2025B0" , 1.0, "2025", "NonpromptSingleElecRun2025B0NanoList.txt" ,"/EGamma0/Run2025B-PromptReco-v1/NANOAOD")
NonpromptSingleElecRun2025C01 = sample("NonpromptSingleElecRun2025C01", 1.0, "2025", "NonpromptSingleElecRun2025C01NanoList.txt","/EGamma0/Run2025C-PromptReco-v1/NANOAOD")
NonpromptSingleElecRun2025C02 = sample("NonpromptSingleElecRun2025C02", 1.0, "2025", "NonpromptSingleElecRun2025C02NanoList.txt","/EGamma0/Run2025C-PromptReco-v2/NANOAOD")
NonpromptSingleElecRun2025D0  = sample("NonpromptSingleElecRun2025D0" , 1.0, "2025", "NonpromptSingleElecRun2025D0NanoList.txt" ,"/EGamma0/Run2025D-PromptReco-v1/NANOAOD")
NonpromptSingleElecRun2025E0  = sample("NonpromptSingleElecRun2025E0" , 1.0, "2025", "NonpromptSingleElecRun2025E0NanoList.txt" ,"/EGamma0/Run2025E-PromptReco-v1/NANOAOD")
NonpromptSingleElecRun2025F01 = sample("NonpromptSingleElecRun2025F01", 1.0, "2025", "NonpromptSingleElecRun2025F01NanoList.txt","/EGamma0/Run2025F-PromptReco-v1/NANOAOD")
NonpromptSingleElecRun2025F02 = sample("NonpromptSingleElecRun2025F02", 1.0, "2025", "NonpromptSingleElecRun2025F02NanoList.txt","/EGamma0/Run2025F-PromptReco-v2/NANOAOD")
NonpromptSingleElecRun2025G0  = sample("NonpromptSingleElecRun2025G0" , 1.0, "2025", "NonpromptSingleElecRun2025G0NanoList.txt" ,"/EGamma0/Run2025G-PromptReco-v1/NANOAOD")
NonpromptSingleElecRun2025B1  = sample("NonpromptSingleElecRun2025B1" , 1.0, "2025", "NonpromptSingleElecRun2025B1NanoList.txt" ,"/EGamma1/Run2025B-PromptReco-v1/NANOAOD")
NonpromptSingleElecRun2025C11 = sample("NonpromptSingleElecRun2025C11", 1.0, "2025", "NonpromptSingleElecRun2025C11NanoList.txt","/EGamma1/Run2025C-PromptReco-v1/NANOAOD")
NonpromptSingleElecRun2025C12 = sample("NonpromptSingleElecRun2025C12", 1.0, "2025", "NonpromptSingleElecRun2025C12NanoList.txt","/EGamma1/Run2025C-PromptReco-v2/NANOAOD")
NonpromptSingleElecRun2025D1  = sample("NonpromptSingleElecRun2025D1" , 1.0, "2025", "NonpromptSingleElecRun2025D1NanoList.txt" ,"/EGamma1/Run2025D-PromptReco-v1/NANOAOD")
NonpromptSingleElecRun2025E1  = sample("NonpromptSingleElecRun2025E1" , 1.0, "2025", "NonpromptSingleElecRun2025E1NanoList.txt" ,"/EGamma1/Run2025E-PromptReco-v1/NANOAOD")
NonpromptSingleElecRun2025F11 = sample("NonpromptSingleElecRun2025F11", 1.0, "2025", "NonpromptSingleElecRun2025F11NanoList.txt","/EGamma1/Run2025F-PromptReco-v1/NANOAOD")
NonpromptSingleElecRun2025F12 = sample("NonpromptSingleElecRun2025F12", 1.0, "2025", "NonpromptSingleElecRun2025F12NanoList.txt","/EGamma1/Run2025F-PromptReco-v2/NANOAOD")
NonpromptSingleElecRun2025G1  = sample("NonpromptSingleElecRun2025G1" , 1.0, "2025", "NonpromptSingleElecRun2025G1NanoList.txt" ,"/EGamma1/Run2025G-PromptReco-v1/NANOAOD")
NonpromptSingleElecRun2025B2  = sample("NonpromptSingleElecRun2025B2" , 1.0, "2025", "NonpromptSingleElecRun2025B2NanoList.txt" ,"/EGamma2/Run2025B-PromptReco-v1/NANOAOD")
NonpromptSingleElecRun2025C21 = sample("NonpromptSingleElecRun2025C21", 1.0, "2025", "NonpromptSingleElecRun2025C21NanoList.txt","/EGamma2/Run2025C-PromptReco-v1/NANOAOD")
NonpromptSingleElecRun2025C22 = sample("NonpromptSingleElecRun2025C22", 1.0, "2025", "NonpromptSingleElecRun2025C22NanoList.txt","/EGamma2/Run2025C-PromptReco-v2/NANOAOD")
NonpromptSingleElecRun2025D2  = sample("NonpromptSingleElecRun2025D2" , 1.0, "2025", "NonpromptSingleElecRun2025D2NanoList.txt" ,"/EGamma2/Run2025D-PromptReco-v1/NANOAOD")
NonpromptSingleElecRun2025E2  = sample("NonpromptSingleElecRun2025E2" , 1.0, "2025", "NonpromptSingleElecRun2025E2NanoList.txt" ,"/EGamma2/Run2025E-PromptReco-v1/NANOAOD")
NonpromptSingleElecRun2025F21 = sample("NonpromptSingleElecRun2025F21", 1.0, "2025", "NonpromptSingleElecRun2025F21NanoList.txt","/EGamma2/Run2025F-PromptReco-v1/NANOAOD")
NonpromptSingleElecRun2025F22 = sample("NonpromptSingleElecRun2025F22", 1.0, "2025", "NonpromptSingleElecRun2025F22NanoList.txt","/EGamma2/Run2025F-PromptReco-v2/NANOAOD")
NonpromptSingleElecRun2025G2  = sample("NonpromptSingleElecRun2025G2" , 1.0, "2025", "NonpromptSingleElecRun2025G2NanoList.txt" ,"/EGamma2/Run2025G-PromptReco-v1/NANOAOD")
NonpromptSingleElecRun2025B3  = sample("NonpromptSingleElecRun2025B3" , 1.0, "2025", "NonpromptSingleElecRun2025B3NanoList.txt" ,"/EGamma3/Run2025B-PromptReco-v1/NANOAOD")
NonpromptSingleElecRun2025C31 = sample("NonpromptSingleElecRun2025C31", 1.0, "2025", "NonpromptSingleElecRun2025C31NanoList.txt","/EGamma3/Run2025C-PromptReco-v1/NANOAOD")
NonpromptSingleElecRun2025C32 = sample("NonpromptSingleElecRun2025C32", 1.0, "2025", "NonpromptSingleElecRun2025C32NanoList.txt","/EGamma3/Run2025C-PromptReco-v2/NANOAOD")
NonpromptSingleElecRun2025D3  = sample("NonpromptSingleElecRun2025D3" , 1.0, "2025", "NonpromptSingleElecRun2025D3NanoList.txt" ,"/EGamma3/Run2025D-PromptReco-v1/NANOAOD")
NonpromptSingleElecRun2025E3  = sample("NonpromptSingleElecRun2025E3" , 1.0, "2025", "NonpromptSingleElecRun2025E3NanoList.txt" ,"/EGamma3/Run2025E-PromptReco-v1/NANOAOD")
NonpromptSingleElecRun2025F31 = sample("NonpromptSingleElecRun2025F31", 1.0, "2025", "NonpromptSingleElecRun2025F31NanoList.txt","/EGamma3/Run2025F-PromptReco-v1/NANOAOD")
NonpromptSingleElecRun2025F32 = sample("NonpromptSingleElecRun2025F32", 1.0, "2025", "NonpromptSingleElecRun2025F32NanoList.txt","/EGamma3/Run2025F-PromptReco-v2/NANOAOD")
NonpromptSingleElecRun2025G3  = sample("NonpromptSingleElecRun2025G3" , 1.0, "2025", "NonpromptSingleElecRun2025G3NanoList.txt" ,"/EGamma3/Run2025G-PromptReco-v1/NANOAOD")

NonpromptSingleMuonRun2022C = sample("NonpromptSingleMuonRun2022C", 1.0, "2022", "SingleMuonRun2022CNanoList.txt", "/Muon/Run2022C-NanoAODv15-v1/NANOAOD")
NonpromptSingleMuonRun2022D = sample("NonpromptSingleMuonRun2022D", 1.0, "2022", "SingleMuonRun2022DNanoList.txt", "/Muon/Run2022D-NanoAODv15-v1/NANOAOD")
NonpromptSingleMuonRun2022EEE  = sample("NonpromptSingleMuonRun2022EEE", 1.0, "2022EE", "SingleMuonRun2022EEENanoList.txt", "/Muon/Run2022E-NanoAODv15-v1/NANOAOD")
NonpromptSingleMuonRun2022EEF  = sample("NonpromptSingleMuonRun2022EEF", 1.0, "2022EE", "SingleMuonRun2022EEFNanoList.txt", "/Muon/Run2022F-NanoAODv15-v1/NANOAOD")
NonpromptSingleMuonRun2022EEG  = sample("NonpromptSingleMuonRun2022EEG", 1.0, "2022EE", "SingleMuonRun2022EEGNanoList.txt", "/Muon/Run2022G-NanoAODv15-v1/NANOAOD")
NonpromptSingleMuonRun2023C01  = sample("NonpromptSingleMuonRun2023C01", 1.0, "2023", "SingleMuonRun2023C01NanoList.txt", "/Muon0/Run2023C-NanoAODv15_v1/NANOAOD")
NonpromptSingleMuonRun2023C02  = sample("NonpromptSingleMuonRun2023C02", 1.0, "2023", "SingleMuonRun2023C02NanoList.txt", "/Muon0/Run2023C-NanoAODv15_v2-v1/NANOAOD")
NonpromptSingleMuonRun2023C03  = sample("NonpromptSingleMuonRun2023C03", 1.0, "2023", "SingleMuonRun2023C03NanoList.txt", "/Muon0/Run2023C-NanoAODv15_v3-v1/NANOAOD")
NonpromptSingleMuonRun2023C04  = sample("NonpromptSingleMuonRun2023C04", 1.0, "2023", "SingleMuonRun2023C04NanoList.txt", "/Muon0/Run2023C-NanoAODv15_v4-v1/NANOAOD")
NonpromptSingleMuonRun2023C11  = sample("NonpromptSingleMuonRun2023C11", 1.0, "2023", "SingleMuonRun2023C11NanoList.txt", "/Muon1/Run2023C-NanoAODv15_v1/NANOAOD")
NonpromptSingleMuonRun2023C12  = sample("NonpromptSingleMuonRun2023C12", 1.0, "2023", "SingleMuonRun2023C12NanoList.txt", "/Muon1/Run2023C-NanoAODv15_v2-v1/NANOAOD")
NonpromptSingleMuonRun2023C13  = sample("NonpromptSingleMuonRun2023C13", 1.0, "2023", "SingleMuonRun2023C13NanoList.txt", "/Muon1/Run2023C-NanoAODv15_v3-v1/NANOAOD")
NonpromptSingleMuonRun2023C14  = sample("NonpromptSingleMuonRun2023C14", 1.0, "2023", "SingleMuonRun2023C14NanoList.txt", "/Muon1/Run2023C-NanoAODv15_v4-v2/NANOAOD")
NonpromptSingleMuonRun2023BPixD01  = sample("NonpromptSingleMuonRun2023BPixD01", 1.0, "2023BPix", "SingleMuonRun2023BPixD01NanoList.txt", "/Muon0/Run2023D-NanoAODv15_v1/NANOAOD")
NonpromptSingleMuonRun2023BPixD02  = sample("NonpromptSingleMuonRun2023BPixD02", 1.0, "2023BPix", "SingleMuonRun2023BPixD02NanoList.txt", "/Muon0/Run2023D-NanoAODv15_v2-v1/NANOAOD")
NonpromptSingleMuonRun2023BPixD11  = sample("NonpromptSingleMuonRun2023BPixD11", 1.0, "2023BPix", "SingleMuonRun2023BPixD11NanoList.txt", "/Muon1/Run2023D-NanoAODv15_v1/NANOAOD")
NonpromptSingleMuonRun2023BPixD12  = sample("NonpromptSingleMuonRun2023BPixD12", 1.0, "2023BPix", "SingleMuonRun2023BPixD12NanoList.txt", "/Muon1/Run2023D-NanoAODv15_v2-v1/NANOAOD")
NonpromptSingleMuonRun2024C0 = sample("NonpromptSingleMuonRun2024C0", 1.0, "2024", "NonpromptSingleMuonRun2024C0NanoList.txt","/Muon0/Run2024C-MINIv6NANOv15-v1/NANOAOD")
NonpromptSingleMuonRun2024D0 = sample("NonpromptSingleMuonRun2024D0", 1.0, "2024", "NonpromptSingleMuonRun2024D0NanoList.txt","/Muon0/Run2024D-MINIv6NANOv15-v1/NANOAOD")
NonpromptSingleMuonRun2024E0 = sample("NonpromptSingleMuonRun2024E0", 1.0, "2024", "NonpromptSingleMuonRun2024E0NanoList.txt","/Muon0/Run2024E-MINIv6NANOv15-v1/NANOAOD")
NonpromptSingleMuonRun2024F0 = sample("NonpromptSingleMuonRun2024F0", 1.0, "2024", "NonpromptSingleMuonRun2024F0NanoList.txt","/Muon0/Run2024F-MINIv6NANOv15-v1/NANOAOD")
NonpromptSingleMuonRun2024G0 = sample("NonpromptSingleMuonRun2024G0", 1.0, "2024", "NonpromptSingleMuonRun2024G0NanoList.txt","/Muon0/Run2024G-MINIv6NANOv15-v1/NANOAOD")
NonpromptSingleMuonRun2024H0 = sample("NonpromptSingleMuonRun2024H0", 1.0, "2024", "NonpromptSingleMuonRun2024H0NanoList.txt","/Muon0/Run2024H-MINIv6NANOv15-v1/NANOAOD")
NonpromptSingleMuonRun2024I01 = sample("NonpromptSingleMuonRun2024I01", 1.0, "2024", "NonpromptSingleMuonRun2024I01NanoList.txt","/Muon0/Run2024I-MINIv6NANOv15-v1/NANOAOD")
NonpromptSingleMuonRun2024I02 = sample("NonpromptSingleMuonRun2024I02", 1.0, "2024", "NonpromptSingleMuonRun2024I02NanoList.txt","/Muon0/Run2024I-MINIv6NANOv15_v2-v1/NANOAOD")
NonpromptSingleMuonRun2024C1 = sample("NonpromptSingleMuonRun2024C1", 1.0, "2024", "NonpromptSingleMuonRun2024C1NanoList.txt","/Muon1/Run2024C-MINIv6NANOv15-v1/NANOAOD")
NonpromptSingleMuonRun2024D1 = sample("NonpromptSingleMuonRun2024D1", 1.0, "2024", "NonpromptSingleMuonRun2024D1NanoList.txt","/Muon1/Run2024D-MINIv6NANOv15-v1/NANOAOD")
NonpromptSingleMuonRun2024E1 = sample("NonpromptSingleMuonRun2024E1", 1.0, "2024", "NonpromptSingleMuonRun2024E1NanoList.txt","/Muon1/Run2024E-MINIv6NANOv15-v1/NANOAOD")
NonpromptSingleMuonRun2024F1 = sample("NonpromptSingleMuonRun2024F1", 1.0, "2024", "NonpromptSingleMuonRun2024F1NanoList.txt","/Muon1/Run2024F-MINIv6NANOv15-v1/NANOAOD")
NonpromptSingleMuonRun2024G1 = sample("NonpromptSingleMuonRun2024G1", 1.0, "2024", "NonpromptSingleMuonRun2024G1NanoList.txt","/Muon1/Run2024G-MINIv6NANOv15-v2/NANOAOD")
NonpromptSingleMuonRun2024H1 = sample("NonpromptSingleMuonRun2024H1", 1.0, "2024", "NonpromptSingleMuonRun2024H1NanoList.txt","/Muon1/Run2024H-MINIv6NANOv15-v2/NANOAOD")
NonpromptSingleMuonRun2024I11 = sample("NonpromptSingleMuonRun2024I11", 1.0, "2024", "NonpromptSingleMuonRun2024I11NanoList.txt","/Muon1/Run2024I-MINIv6NANOv15-v1/NANOAOD")
NonpromptSingleMuonRun2024I12 = sample("NonpromptSingleMuonRun2024I12", 1.0, "2024", "NonpromptSingleMuonRun2024I12NanoList.txt","/Muon1/Run2024I-MINIv6NANOv15_v2-v1/NANOAOD")
NonpromptSingleMuonRun2025B0  = sample("NonpromptSingleMuonRun2025B0" , 1.0, "2025", "NonpromptSingleMuonRun2025B0NanoList.txt" ,"/Muon0/Run2025B-PromptReco-v1/NANOAOD")
NonpromptSingleMuonRun2025C01 = sample("NonpromptSingleMuonRun2025C01", 1.0, "2025", "NonpromptSingleMuonRun2025C01NanoList.txt","/Muon0/Run2025C-PromptReco-v1/NANOAOD")
NonpromptSingleMuonRun2025C02 = sample("NonpromptSingleMuonRun2025C02", 1.0, "2025", "NonpromptSingleMuonRun2025C02NanoList.txt","/Muon0/Run2025C-PromptReco-v2/NANOAOD")
NonpromptSingleMuonRun2025D0  = sample("NonpromptSingleMuonRun2025D0" , 1.0, "2025", "NonpromptSingleMuonRun2025D0NanoList.txt" ,"/Muon0/Run2025D-PromptReco-v1/NANOAOD")
NonpromptSingleMuonRun2025E0  = sample("NonpromptSingleMuonRun2025E0" , 1.0, "2025", "NonpromptSingleMuonRun2025E0NanoList.txt" ,"/Muon0/Run2025E-PromptReco-v1/NANOAOD")
NonpromptSingleMuonRun2025F01 = sample("NonpromptSingleMuonRun2025F01", 1.0, "2025", "NonpromptSingleMuonRun2025F01NanoList.txt","/Muon0/Run2025F-PromptReco-v1/NANOAOD")
NonpromptSingleMuonRun2025F02 = sample("NonpromptSingleMuonRun2025F02", 1.0, "2025", "NonpromptSingleMuonRun2025F02NanoList.txt","/Muon0/Run2025F-PromptReco-v2/NANOAOD")
NonpromptSingleMuonRun2025G0  = sample("NonpromptSingleMuonRun2025G0" , 1.0, "2025", "NonpromptSingleMuonRun2025G0NanoList.txt" ,"/Muon0/Run2025G-PromptReco-v1/NANOAOD")
NonpromptSingleMuonRun2025B1  = sample("NonpromptSingleMuonRun2025B1" , 1.0, "2025", "NonpromptSingleMuonRun2025B1NanoList.txt" ,"/Muon1/Run2025B-PromptReco-v1/NANOAOD")
NonpromptSingleMuonRun2025C11 = sample("NonpromptSingleMuonRun2025C11", 1.0, "2025", "NonpromptSingleMuonRun2025C11NanoList.txt","/Muon1/Run2025C-PromptReco-v1/NANOAOD")
NonpromptSingleMuonRun2025C12 = sample("NonpromptSingleMuonRun2025C12", 1.0, "2025", "NonpromptSingleMuonRun2025C12NanoList.txt","/Muon1/Run2025C-PromptReco-v2/NANOAOD")
NonpromptSingleMuonRun2025D1  = sample("NonpromptSingleMuonRun2025D1" , 1.0, "2025", "NonpromptSingleMuonRun2025D1NanoList.txt" ,"/Muon1/Run2025D-PromptReco-v1/NANOAOD")
NonpromptSingleMuonRun2025E1  = sample("NonpromptSingleMuonRun2025E1" , 1.0, "2025", "NonpromptSingleMuonRun2025E1NanoList.txt" ,"/Muon1/Run2025E-PromptReco-v1/NANOAOD")
NonpromptSingleMuonRun2025F11 = sample("NonpromptSingleMuonRun2025F11", 1.0, "2025", "NonpromptSingleMuonRun2025F11NanoList.txt","/Muon1/Run2025F-PromptReco-v1/NANOAOD")
NonpromptSingleMuonRun2025F12 = sample("NonpromptSingleMuonRun2025F12", 1.0, "2025", "NonpromptSingleMuonRun2025F12NanoList.txt","/Muon1/Run2025F-PromptReco-v2/NANOAOD")
NonpromptSingleMuonRun2025G1  = sample("NonpromptSingleMuonRun2025G1" , 1.0, "2025", "NonpromptSingleMuonRun2025G1NanoList.txt" ,"/Muon1/Run2025G-PromptReco-v1/NANOAOD")

NonpromptMuonEGRun2022C = sample("NonpromptMuonEGRun2022C", 1.0, "2022", "MuonEGRun2022CNanoList.txt", "/MuonEG/Run2022C-22Sep2023-v1/NANOAOD")
NonpromptMuonEGRun2022D = sample("NonpromptMuonEGRun2022D", 1.0, "2022", "MuonEGRun2022DNanoList.txt", "/MuonEG/Run2022D-22Sep2023-v1/NANOAOD")
NonpromptMuonEGRun2022EEE  = sample("NonpromptMuonEGRun2022EEE", 1.0, "2022EE", "MuonEGRun2022EEENanoList.txt", "/MuonEG/Run2022E-22Sep2023-v1/NANOAOD")
NonpromptMuonEGRun2022EEF  = sample("NonpromptMuonEGRun2022EEF", 1.0, "2022EE", "MuonEGRun2022EEFNanoList.txt", "/MuonEG/Run2022F-22Sep2023-v1/NANOAOD")
NonpromptMuonEGRun2022EEG  = sample("NonpromptMuonEGRun2022EEG", 1.0, "2022EE", "MuonEGRun2022EEGNanoList.txt", "/MuonEG/Run2022G-22Sep2023-v1/NANOAOD")
NonpromptMuonEGRun2023C1  = sample("NonpromptMuonEGRun2023C1", 1.0, "2023", "MuonEGRun2023C1NanoList.txt", "/MuonEG/Run2023C-22Sep2023_v1-v1/NANOAOD")
NonpromptMuonEGRun2023C2  = sample("NonpromptMuonEGRun2023C2", 1.0, "2023", "MuonEGRun2023C2NanoList.txt", "/MuonEG/Run2023C-22Sep2023_v2-v1/NANOAOD")
NonpromptMuonEGRun2023C3  = sample("NonpromptMuonEGRun2023C3", 1.0, "2023", "MuonEGRun2023C3NanoList.txt", "/MuonEG/Run2023C-22Sep2023_v3-v1/NANOAOD")
NonpromptMuonEGRun2023C4  = sample("NonpromptMuonEGRun2023C4", 1.0, "2023", "MuonEGRun2023C4NanoList.txt", "/MuonEG/Run2023C-22Sep2023_v4-v1/NANOAOD")
NonpromptMuonEGRun2023BPixD1  = sample("NonpromptMuonEGRun2023BPixD1", 1.0, "2023BPix", "MuonEGRun2023BPixD1NanoList.txt", "/MuonEG/Run2023D-22Sep2023_v1-v1/NANOAOD")
NonpromptMuonEGRun2023BPixD2  = sample("NonpromptMuonEGRun2023BPixD2", 1.0, "2023BPix", "MuonEGRun2023BPixD2NanoList.txt", "/MuonEG/Run2023D-22Sep2023_v2-v1/NANOAOD")
NonpromptMuonEGRun2024C = sample("NonpromptMuonEGRun2024C", 1.0, "2024", "NonpromptMuonEGRun2024CNanoList.txt","/MuonEG/Run2024C-MINIv6NANOv15-v1/NANOAOD")
NonpromptMuonEGRun2024D = sample("NonpromptMuonEGRun2024D", 1.0, "2024", "NonpromptMuonEGRun2024DNanoList.txt","/MuonEG/Run2024D-MINIv6NANOv15-v1/NANOAOD")
NonpromptMuonEGRun2024E = sample("NonpromptMuonEGRun2024E", 1.0, "2024", "NonpromptMuonEGRun2024ENanoList.txt","/MuonEG/Run2024E-MINIv6NANOv15-v1/NANOAOD")
NonpromptMuonEGRun2024F = sample("NonpromptMuonEGRun2024F", 1.0, "2024", "NonpromptMuonEGRun2024FNanoList.txt","/MuonEG/Run2024F-MINIv6NANOv15-v1/NANOAOD")
NonpromptMuonEGRun2024G = sample("NonpromptMuonEGRun2024G", 1.0, "2024", "NonpromptMuonEGRun2024GNanoList.txt","/MuonEG/Run2024G-MINIv6NANOv15-v3/NANOAOD")
NonpromptMuonEGRun2024H = sample("NonpromptMuonEGRun2024H", 1.0, "2024", "NonpromptMuonEGRun2024HNanoList.txt","/MuonEG/Run2024H-MINIv6NANOv15-v1/NANOAOD")
NonpromptMuonEGRun2024I1 = sample("NonpromptMuonEGRun2024I1", 1.0, "2024", "NonpromptMuonEGRun2024I1NanoList.txt","/MuonEG/Run2024I-MINIv6NANOv15-v1/NANOAOD")
NonpromptMuonEGRun2024I2 = sample("NonpromptMuonEGRun2024I2", 1.0, "2024", "NonpromptMuonEGRun2024I2NanoList.txt","/MuonEG/Run2024I-MINIv6NANOv15_v2-v2/NANOAOD")
NonpromptMuonEGRun2025B  = sample("NonpromptMuonEGRun2025B" , 1.0, "2025", "NonpromptMuonEGRun2025BNanoList.txt" ,"/MuonEG/Run2025B-PromptReco-v1/NANOAOD")
NonpromptMuonEGRun2025C1 = sample("NonpromptMuonEGRun2025C1", 1.0, "2025", "NonpromptMuonEGRun2025C1NanoList.txt","/MuonEG/Run2025C-PromptReco-v1/NANOAOD")
NonpromptMuonEGRun2025C2 = sample("NonpromptMuonEGRun2025C2", 1.0, "2025", "NonpromptMuonEGRun2025C2NanoList.txt","/MuonEG/Run2025C-PromptReco-v2/NANOAOD")
NonpromptMuonEGRun2025D  = sample("NonpromptMuonEGRun2025D" , 1.0, "2025", "NonpromptMuonEGRun2025DNanoList.txt" ,"/MuonEG/Run2025D-PromptReco-v1/NANOAOD")
NonpromptMuonEGRun2025E  = sample("NonpromptMuonEGRun2025E" , 1.0, "2025", "NonpromptMuonEGRun2025ENanoList.txt" ,"/MuonEG/Run2025E-PromptReco-v1/NANOAOD")
NonpromptMuonEGRun2025F1 = sample("NonpromptMuonEGRun2025F1", 1.0, "2025", "NonpromptMuonEGRun2025F1NanoList.txt","/MuonEG/Run2025F-PromptReco-v1/NANOAOD")
NonpromptMuonEGRun2025F2 = sample("NonpromptMuonEGRun2025F2", 1.0, "2025", "NonpromptMuonEGRun2025F2NanoList.txt","/MuonEG/Run2025F-PromptReco-v2/NANOAOD")
NonpromptMuonEGRun2025G  = sample("NonpromptMuonEGRun2025G" , 1.0, "2025", "NonpromptMuonEGRun2025GNanoList.txt" ,"/MuonEG/Run2025G-PromptReco-v1/NANOAOD")

NonpromptTauRun2022C = sample("NonpromptTauRun2022C", 1.0, "2022", "TauRun2022CNanoList.txt", "/Tau/Run2022C-22Sep2023-v1/NANOAOD")
NonpromptTauRun2022D = sample("NonpromptTauRun2022D", 1.0, "2022", "TauRun2022DNanoList.txt", "/Tau/Run2022D-22Sep2023-v1/NANOAOD")
NonpromptTauRun2022EEE  = sample("NonpromptTauRun2022EEE", 1.0, "2022EE", "TauRun2022EEENanoList.txt", "/Tau/Run2022E-22Sep2023-v1/NANOAOD")
NonpromptTauRun2022EEF  = sample("NonpromptTauRun2022EEF", 1.0, "2022EE", "TauRun2022EEFNanoList.txt", "/Tau/Run2022F-22Sep2023-v1/NANOAOD")
NonpromptTauRun2022EEG  = sample("NonpromptTauRun2022EEG", 1.0, "2022EE", "TauRun2022EEGNanoList.txt", "/Tau/Run2022G-22Sep2023-v1/NANOAOD")
NonpromptTauRun2023C1  = sample("NonpromptTauRun2023C1", 1.0, "2023", "TauRun2023C1NanoList.txt", "/Tau/Run2023C-22Sep2023_v1-v2/NANOAOD")
NonpromptTauRun2023C2  = sample("NonpromptTauRun2023C2", 1.0, "2023", "TauRun2023C2NanoList.txt", "/Tau/Run2023C-22Sep2023_v2-v1/NANOAOD")
NonpromptTauRun2023C3  = sample("NonpromptTauRun2023C3", 1.0, "2023", "TauRun2023C3NanoList.txt", "/Tau/Run2023C-22Sep2023_v3-v1/NANOAOD")
NonpromptTauRun2023C4  = sample("NonpromptTauRun2023C4", 1.0, "2023", "TauRun2023C4NanoList.txt", "/Tau/Run2023C-22Sep2023_v4-v1/NANOAOD")
NonpromptTauRun2023BPixD1  = sample("NonpromptTauRun2023BPixD1", 1.0, "2023BPix", "TauRun2023BPixD12023BPixNanoList.txt", "/Tau/Run2023D-22Sep2023_v1-v1/NANOAOD")
NonpromptTauRun2023BPixD2  = sample("NonpromptTauRun2023BPixD2", 1.0, "2023BPix", "TauRun2023BPixD22023BPixNanoList.txt", "/Tau/Run2023D-22Sep2023_v2-v1/NANOAOD")
NonpromptTauRun2024C = sample("NonpromptTauRun2024C", 1.0, "2024", "NonpromptTauRun2024CNanoList.txt","/Tau/Run2024C-MINIv6NANOv15-v1/NANOAOD")
NonpromptTauRun2024D = sample("NonpromptTauRun2024D", 1.0, "2024", "NonpromptTauRun2024DNanoList.txt","/Tau/Run2024D-MINIv6NANOv15-v1/NANOAOD")
NonpromptTauRun2024E = sample("NonpromptTauRun2024E", 1.0, "2024", "NonpromptTauRun2024ENanoList.txt","/Tau/Run2024E-MINIv6NANOv15-v1/NANOAOD")
NonpromptTauRun2024F = sample("NonpromptTauRun2024F", 1.0, "2024", "NonpromptTauRun2024FNanoList.txt","/Tau/Run2024F-MINIv6NANOv15-v1/NANOAOD")
NonpromptTauRun2024G = sample("NonpromptTauRun2024G", 1.0, "2024", "NonpromptTauRun2024GNanoList.txt","/Tau/Run2024G-MINIv6NANOv15-v1/NANOAOD")
NonpromptTauRun2024H = sample("NonpromptTauRun2024H", 1.0, "2024", "NonpromptTauRun2024HNanoList.txt","/Tau/Run2024H-MINIv6NANOv15-v1/NANOAOD")
NonpromptTauRun2024I1 = sample("NonpromptTauRun2024I1", 1.0, "2024", "NonpromptTauRun2024I1NanoList.txt","/Tau/Run2024I-MINIv6NANOv15-v1/NANOAOD")
NonpromptTauRun2024I2 = sample("NonpromptTauRun2024I2", 1.0, "2024", "NonpromptTauRun2024I2NanoList.txt","/Tau/Run2024I-MINIv6NANOv15_v2-v1/NANOAOD")
NonpromptTauRun2025B  = sample("NonpromptTauRun2025B" , 1.0, "2025", "NonpromptTauRun2025BNanoList.txt" ,"/Tau/Run2025B-PromptReco-v1/NANOAOD")
NonpromptTauRun2025C1 = sample("NonpromptTauRun2025C1", 1.0, "2025", "NonpromptTauRun2025C1NanoList.txt","/Tau/Run2025C-PromptReco-v1/NANOAOD")
NonpromptTauRun2025C2 = sample("NonpromptTauRun2025C2", 1.0, "2025", "NonpromptTauRun2025C2NanoList.txt","/Tau/Run2025C-PromptReco-v2/NANOAOD")
NonpromptTauRun2025D  = sample("NonpromptTauRun2025D" , 1.0, "2025", "NonpromptTauRun2025DNanoList.txt" ,"/Tau/Run2025D-PromptReco-v1/NANOAOD")
NonpromptTauRun2025E  = sample("NonpromptTauRun2025E" , 1.0, "2025", "NonpromptTauRun2025ENanoList.txt" ,"/Tau/Run2025E-PromptReco-v1/NANOAOD")
NonpromptTauRun2025F1 = sample("NonpromptTauRun2025F1", 1.0, "2025", "NonpromptTauRun2025F1NanoList.txt","/Tau/Run2025F-PromptReco-v1/NANOAOD")
NonpromptTauRun2025F2 = sample("NonpromptTauRun2025F2", 1.0, "2025", "NonpromptTauRun2025F2NanoList.txt","/Tau/Run2025F-PromptReco-v2/NANOAOD")
NonpromptTauRun2025G  = sample("NonpromptTauRun2025G" , 1.0, "2025", "NonpromptTauRun2025GNanoList.txt" ,"/Tau/Run2025G-PromptReco-v1/NANOAOD")

################################################
###                                          ###
###    BACKGROUNDS MOSTLY FOR EXOTIC TAUS    ###
###                                          ###
################################################

# diboson 3L and 4L
WZ3L2022 = sample("WZ3L2022", 4.924, "2022", "WZ3L2022NanoList.txt", "/WZto3LNu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WZ3L2022ext = sample("WZ3L2022ext", 4.924, "2022", "WZ3L2022extNanoList.txt", "/WZto3LNu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v3/NANOAODSIM")
WZ3L2022EE = sample("WZ3L2022EE", 4.924, "2022EE", "WZ3L2022EENanoList.txt", "/WZto3LNu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WZ3L2022EEext = sample("WZ3L2022EEext", 4.924, "2022EE", "WZ3L2022EEextNanoList.txt", "/WZto3LNu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM")
WZ3L2023 = sample("WZ3L2023", 4.924, "2023", "WZ3L2023NanoList.txt", "/WZto3LNu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
WZ3L2023ext = sample("WZ3L2023ext", 4.924, "2023", "WZ3L2023extNanoList.txt", "/WZto3LNu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15_ext1-v2/NANOAODSIM")
WZ3L2023BPix = sample("WZ3L2023BPix", 4.924, "2023BPix", "WZ3L2023BPixNanoList.txt", "/WZto3LNu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM")
WZ3L2023BPixext = sample("WZ3L2023BPixext", 4.924, "2023BPix", "WZ3L2023BPixextNanoList.txt", "/WZto3LNu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6_ext1-v2/NANOAODSIM")
WZ3L2024 = sample("WZ3L2024", 4.924, "2024", "WZ3L2024NanoList.txt", "/WZtoL3Nu_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
#/WZJJto3LNu-EWK-QCD_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM

ZZ4L2022 = sample("ZZ4L2022", 1.39, "2022", "ZZ4L2022NanoList.txt", "/ZZto4L_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
ZZ4L2022ext = sample("ZZ4L2022ext", 1.39, "2022", "ZZ4L2022extNanoList.txt", "/ZZto4L_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM")
ZZ4L2022EE = sample("ZZ4L2022EE", 1.39, "2022EE", "ZZ4L2022EENanoList.txt", "/ZZto4L_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
ZZ4L2022EEext = sample("ZZ4L2022EEext", 1.39, "2022EE", "ZZ4L2022EEextNanoList.txt", "/ZZto4L_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM")
ZZ4L2023 = sample("ZZ4L2023", 1.39, "2023", "ZZ4L2023NanoList.txt", "/ZZto4L_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM")
ZZ4L2023BPix = sample("ZZ4L2023BPix", 1.39, "2023BPix", "ZZ4L2023BPixNanoList.txt", "/ZZto4L_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM")
ZZ4L2024 = sample("ZZ4L2024", 1.39, "2024", "ZZ4L2024NanoList.txt", "/ZZto4L_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")

# xsec from H+ -> WA preapp
VHnonbb2022     = sample("VHnonbb2022", 1.0132, "2022", "VHnonbb2022.txt", "/VH_HtoNonbb_M-125_TuneCP5_13p6TeV_amcatnloFXFX-madspin-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM")
VHnonbb2022EE   = sample("VHnonbb2022EE", 1.0132, "2022EE", "VHnonbb2022EE.txt", "/VH_HtoNonbb_M-125_TuneCP5_13p6TeV_amcatnloFXFX-madspin-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM")
VHnonbb2023     = sample("VHnonbb2023", 1.0132, "2023", "VHnonbb2023.txt", "/VH_HtoNonbb_M-125_TuneCP5_13p6TeV_amcatnloFXFX-madspin-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
VHnonbb2023BPix = sample("VHnonbb2023BPix", 1.0132, "2023BPix", "VHnonbb2023BPix.txt", "/VH_HtoNonbb_M-125_TuneCP5_13p6TeV_amcatnloFXFX-madspin-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
ZHnonbb2024     = sample("ZHnonbb2024", 0.9014, "2024", "ZHnonbb2024.txt", "/ZH-HtoNon2B_Par-M-125_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
WmHnonbb2024     = sample("WmHnonbb2024", 0.6409, "2024", "WmHnonbb2024.txt", "/WminusH-HtoNon2B_Par-M-125_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
WpHnonbb2024     = sample("WpHnonbb2024", 1.024, "2024", "WpHnonbb2024.txt", "/WplusH-HtoNon2B_Par-M-125_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")

# triboson
WWW2022     = sample("WWW2022", 0.2328, "2022", "WWW2022.txt", "/WWW_4F_TuneCP5_13p6TeV_amcatnlo-madspin-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WWW2022EE   = sample("WWW2022EE", 0.2328, "2022EE", "WWW2022EE.txt", "/WWW_4F_TuneCP5_13p6TeV_amcatnlo-madspin-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WWW2023     = sample("WWW2023", 0.2328, "2023", "WWW2023.txt", "/WWW_4F_TuneCP5_13p6TeV_amcatnlo-madspin-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
WWW2023BPix = sample("WWW2023BPix", 0.2328, "2023BPix", "WWW2023BPix.txt", "/WWW_4F_TuneCP5_13p6TeV_amcatnlo-madspin-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM")
WWW2024     = sample("WWW2024", 0.2328, "2024", "WWW2024.txt", "/WWW-4F_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")

WWZ2022     = sample("WWZ2022", 0.1851, "2022", "WWZ2022.txt", "/WWZ_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WWZ2022EE   = sample("WWZ2022EE", 0.1851, "2022EE", "WWZ2022EE.txt", "/WWZ_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WWZ2023     = sample("WWZ2023", 0.1851, "2023", "WWZ2023.txt", "/WWZ_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
WWZ2023BPix = sample("WWZ2023BPix", 0.1851, "2023BPix", "WWZ2023BPix.txt", "/WWZ_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM")
WWZ2024     = sample("WWZ2024", 0.1851, "2024", "WWZ2024.txt", "/WWZ-4F_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")

WWZ4L2022     = sample("WWZ4L2022", 0.002244, "2022", "WWZ4L2022.txt", "/WWZto4L2Nu_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WWZ4L2022EE   = sample("WWZ4L2022EE", 0.002244, "2022EE", "WWZ4L2022EE.txt", "/WWZto4L2Nu_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WWZ4L2023     = sample("WWZ4L2023", 0.002244, "2023", "WWZ4L2023.txt", "/WWZto4L2Nu_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
WWZ4L2023BPix = sample("WWZ4L2023BPix", 0.002244, "2023BPix", "WWZ4L2023BPix.txt", "/WWZto4L2Nu_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")

WZZ2022     = sample("WZZ2022", 0.06206, "2022", "WZZ2022.txt", "/WZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WZZ2022EE   = sample("WZZ2022EE", 0.06206, "2022EE", "WZZ2022EE.txt", "/WZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WZZ2023     = sample("WZZ2023", 0.06206, "2023", "WZZ2023.txt", "/WZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
WZZ2023BPix = sample("WZZ2023BPix", 0.06206, "2023BPix", "WZZ2023BPix.txt", "/WZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM")
WZZ2024     = sample("WZZ2024", 0.06206, "2024", "WZZ2024.txt", "/WZZ-5F_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")

ZZZ2022     = sample("ZZZ2022", 0.01591, "2022", "ZZZ2022.txt", "/ZZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
ZZZ2022EE   = sample("ZZZ2022EE", 0.01591, "2022EE", "ZZZ2022EE.txt", "/ZZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
ZZZ2023     = sample("ZZZ2023", 0.01591, "2023", "ZZZ2023.txt", "/ZZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
ZZZ2023BPix = sample("ZZZ2023BPix", 0.01591, "2023BPix", "ZZZ2023BPix.txt", "/ZZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM")
ZZZ2024     = sample("ZZZ2024", 0.01591, "2024", "ZZZ2024.txt", "/ZZZ-5F_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")

# 4 bosons
WWZZ3L2022     = sample("WWZZ3L2022", 0.0004888, "2022", "WWZZ3L2022NanoList.txt", "/WWZZ_3L_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WWZZ3L2022EE   = sample("WWZZ3L2022EE", 0.0004888, "2022EE", "WWZZ3L2022EENanoList.txt", "/WWZZ_3L_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WWZZ3L2023     = sample("WWZZ3L2023", 0.0004888, "2023", "WWZZ3L2023NanoList.txt", "/WWZZ_3L_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
WWZZ3L2023BPix = sample("WWZZ3L2023BPix", 0.0004888, "2023BPix", "WWZZ3L2023BPixNanoList.txt", "/WWZZ_3L_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")

WWZZ4L2022     = sample("WWZZ4L2022", 0.0004888, "2022", "WWZZ4L2022NanoList.txt", "/WWZZ_4Lplus_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
WWZZ4L2022EE   = sample("WWZZ4L2022EE", 0.0004888, "2022EE", "WWZZ4L2022EENanoList.txt", "/WWZZ_4Lplus_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
WWZZ4L2023     = sample("WWZZ4L2023", 0.0004888, "2023", "WWZZ4L2023NanoList.txt", "/WWZZ_4Lplus_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
WWZZ4L2023BPix = sample("WWZZ4L2023BPix", 0.0004888, "2023BPix", "WWZZ4L2023BPixNanoList.txt", "/WWZZ_4Lplus_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")

# Photon conversions

#/WZGtoLNuZG_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM
#/ZZG-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM

ZG2J2022     = sample("ZG2J2022", 0.1136, "2022", "ZG2J2022NanoList.txt", "/ZG2JtoG2L2J_EWK_MLL-50_MJJ-120_TuneCP5_withDipoleRecoil_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
ZG2J2022EE   = sample("ZG2J2022EE", 0.1136, "2022EE", "ZG2J2022EENanoList.txt", "/ZG2JtoG2L2J_EWK_MLL-50_MJJ-120_TuneCP5_withDipoleRecoil_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM")
ZG2J2023     = sample("ZG2J2023", 0.1136, "2023", "ZG2J2023NanoList.txt", "/ZG2JtoG2L2J_EWK_MLL-50_MJJ-120_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
ZG2J2023BPix = sample("ZG2J2023BPix", 0.1136, "2023BPix", "ZG2J2023BPixNanoList.txt", "/ZG2JtoG2L2J_EWK_MLL-50_MJJ-120_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
ZGG2024     = sample("ZGG2024", 0.1068, "2024", "ZGG2024NanoList.txt", "/ZGG_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")

TTG1Jpt102022     = sample("TTG1Jpt102022", 4.216, "2022", "TTG1Jpt102022NanoList.txt", "/TTG-1Jets_PTG-10to100_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM")
TTG1Jpt102022EE   = sample("TTG1Jpt102022EE", 4.216, "2022EE", "TTG1Jpt102022EENanoList.txt", "/TTG-1Jets_PTG-10to100_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v4/NANOAODSIM")
TTG1Jpt102023     = sample("TTG1Jpt102023", 4.216, "2023", "TTG1Jpt102023NanoList.txt", "/TTG-1Jets_PTG-10to100_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
TTG1Jpt102023BPix = sample("TTG1Jpt102023BPix", 4.216, "2023BPix", "TTG1Jpt102023BPixNanoList.txt", "/TTG-1Jets_PTG-10to100_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
TTG1Jpt1002022     = sample("TTG1Jpt1002022", 0.4114, "2022", "TTG1Jpt1002022NanoList.txt", "/TTG-1Jets_PTG-100to200_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM")
TTG1Jpt1002022EE   = sample("TTG1Jpt1002022EE", 0.4114, "2022EE", "TTG1Jpt1002022EENanoList.txt", "/TTG-1Jets_PTG-100to200_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM")
TTG1Jpt1002023     = sample("TTG1Jpt1002023", 0.4114, "2023", "TTG1Jpt1002023NanoList.txt", "/TTG-1Jets_PTG-100to200_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
TTG1Jpt1002023BPix = sample("TTG1Jpt1002023BPix", 0.4114, "2023BPix", "TTG1Jpt1002023BPixNanoList.txt", "/TTG-1Jets_PTG-100to200_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
TTG1Jpt2002022     = sample("TTG1Jpt2002022", 0.1284, "2022", "TTG1Jpt2002022NanoList.txt", "/TTG-1Jets_PTG-200_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM")
TTG1Jpt2002022EE   = sample("TTG1Jpt2002022EE", 0.1284, "2022EE", "TTG1Jpt2002022EENanoList.txt", "/TTG-1Jets_PTG-200_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM")
TTG1Jpt2002023     = sample("TTG1Jpt2002023", 0.1284, "2023", "TTG1Jpt2002023NanoList.txt", "/TTG-1Jets_PTG-200_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
TTG1Jpt2002023BPix = sample("TTG1Jpt2002023BPix", 0.1284, "2023BPix", "TTG1Jpt2002023BPixNanoList.txt", "/TTG-1Jets_PTG-200_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
TTG1Jpt1002024     = sample("TTG1Jpt1002024", 0.4114, "2024", "TTG1Jpt1002024NanoList.txt", "/TTG-1Jets_Bin-PTG-100_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
TTG1Jpt2002024     = sample("TTG1Jpt2002024", 0.1284, "2024", "TTG1Jpt2002024NanoList.txt", "/TTG-1Jets_Bin-PTG-200_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM")
#/TTGG_TuneCP5_13p6TeV_madgraph-madspin-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM

# t+Z/y
TZQB2022     = sample("TZQB2022", 0.07968, "2022", "TZQB2022NanoList.txt", "/TZQB-Zto2L-4FS_MLL-30_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
TZQB2022EE   = sample("TZQB2022EE", 0.07968, "2022EE", "TZQB2022EENanoList.txt", "/TZQB-Zto2L-4FS_MLL-30_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
TZQB2023     = sample("TZQB2023", 0.07968, "2023", "TZQB2023NanoList.txt", "/TZQB-Zto2L-4FS_MLL-30_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
TZQB2023BPix = sample("TZQB2023BPix", 0.07968, "2023BPix", "TZQB2023BPixNanoList.txt", "/TZQB-Zto2L-4FS_MLL-30_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v3/NANOAODSIM")
TZQB2024     = sample("TZQB2024", 0.07968, "2024", "TZQB2024NanoList.txt", "/TZQB-Zto2L-4FS_Bin-MLL-30_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-Madgraph_2_6_5_150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")

TGQB2022     = sample("TGQB2022", 0.07968, "2022", "TGQB2022NanoList.txt", "/TGQB-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
TGQB2022EE   = sample("TGQB2022EE", 0.07968, "2022EE", "TGQB2022EENanoList.txt", "/TGQB-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
TGQB2023     = sample("TGQB2023", 0.07968, "2023", "TGQB2023NanoList.txt", "/TGQB-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
TGQB2023BPix = sample("TGQB2023BPix", 0.07968, "2023BPix", "TGQB2023BPixNanoList.txt", "/TGQB-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
TGQB2024     = sample("TGQB2024", 0.07968, "2024", "TGQB2024NanoList.txt", "/TGQB-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")

# tt+X
TTHnonB2022 = sample("TTHnonB2022", 0.570*(1.0-0.5824), "2022", "TTHnonB2022NanoList.txt", "/TTHtoNon2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v4/NANOAODSIM")
TTHnonB2022EE = sample("TTHnonB2022EE", 0.570*(1.0-0.05824), "2022EE", "TTHnonB2022EENanoList.txt", "/TTHtoNon2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
TTHnonB2023 = sample("TTHnonB2023", 0.570*(1.0-0.05824), "2023", "TTHnonB2023NanoList.txt", "/TTHtoNon2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM")
TTHnonB2023BPix = sample("TTHnonB2023BPix", 0.570*(1.0-0.05824), "2023BPix", "TTHnonB2023BPixNanoList.txt", "/TTHtoNon2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM")
TTHnonB2024 = sample("TTHnonB2024", 0.570*(1.0-0.05824), "2024", "TTHnonB2024NanoList.txt", "/TTH-HtoNon2B_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")

TTWl2022 = sample("TTWl2022", 0.2505, "2022", "TTWl2022NanoList.txt", "/TTLNu-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-mg35x_130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
TTWl2022EE = sample("TTWl2022EE", 0.2505, "2022EE", "TTWl2022EENanoList.txt", "/TTLNu-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-mg35x_130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
TTWl2023 = sample("TTWl2023", 0.2505, "2023", "TTWl2023NanoList.txt", "/TTLNu-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-mg35x_130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
TTWl2023BPix = sample("TTWl2023BPix", 0.2505, "2023BPix", "TTWl2023BPixNanoList.txt", "/TTLNu-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-mg35x_130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
TTWl2024 = sample("TTWl2024", 0.2505, "2024", "TTWl2024NanoList.txt", "/TTLNu-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-mg35x_150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")

TTZM42022 = sample("TTZM42022", 0.03949, "2022", "TTZM42022NanoList.txt", "/TTLL_MLL-4to50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
TTZM42022EE = sample("TTZM42022EE", 0.03949, "2022EE", "TTZM42022EENanoList.txt", "/TTLL_MLL-4to50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
TTZM42023 = sample("TTZM42023",  0.03949,"2023", "TTZM42023NanoList.txt", "/TTLL_MLL-4to50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
TTZM42023BPix = sample("TTZM42023BPix", 0.03949, "2023BPix", "TTZM42023BPixNanoList.txt", "/TTLL_MLL-4to50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
TTZM42024 = sample("TTZM42024",  0.03949,"2024", "TTZM42024NanoList.txt", "/TTLL_Bin-MLL-4to50_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")

TTZM502022 = sample("TTZM502022", 0.08646, "2022", "TTZM502022NanoList.txt", "/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
TTZM502022EE = sample("TTZM502022EE", 0.08646, "2022EE", "TTZM502022EENanoList.txt", "/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
TTZM502023 = sample("TTZM502023", 0.08646, "2023", "TTZM502023NanoList.txt", "/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
TTZM502023BPix = sample("TTZM502023BPix", 0.08646, "2023BPix", "TTZM502023BPixNanoList.txt", "/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
TTZM502022ext = sample("TTZM502022ext", 0.08646, "2022", "TTZM502022extNanoList.txt", "/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v3/NANOAODSIM")
TTZM502022EEext = sample("TTZM502022EEext", 0.08646, "2022EE", "TTZM502022EEextNanoList.txt", "/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM")
TTZM502023ext = sample("TTZM502023ext", 0.08646, "2023", "TTZM502023extNanoList.txt", "/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15_ext1-v2/NANOAODSIM")
TTZM502023BPixext = sample("TTZM502023BPixext", 0.08646, "2023BPix", "TTZM502023BPixextNanoList.txt", "/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6_ext1-v2/NANOAODSIM")
TTZM502024 = sample("TTZM502024", 0.08646, "2024", "TTZM502024NanoList.txt", "/TTLL_Bin-MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")

# tt + XX

TTWH2022     = sample("TTWH2022", 0.001252, "2022", "TTWH2022.txt", "/TTWH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
TTWH2022EE   = sample("TTWH2022EE", 0.001252, "2022EE", "TTWH2022EE.txt", "/TTWH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
TTWH2023     = sample("TTWH2023", 0.001252, "2023", "TTWH2023.txt", "/TTWH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM")
TTWH2023BPix = sample("TTWH2023BPix", 0.001252, "2023BPix", "TTWH2023BPix.txt", "/TTWH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
TTWH2024     = sample("TTWH2024", 0.001252, "2024", "TTWH2024.txt", "/TTWH_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")

TTWW2022     = sample("TTWW2022", 0.008203, "2022", "TTWW2022.txt", "/TTWW_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
TTWW2022EE   = sample("TTWW2022EE", 0.008203, "2022EE", "TTWW2022EE.txt", "/TTWW_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
TTWW2023     = sample("TTWW2023", 0.008203, "2023", "TTWW2023.txt", "/TTWW_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
TTWW2023BPix = sample("TTWW2023BPix", 0.008203, "2023BPix", "TTWW2023BPix.txt", "/TTWW_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
TTWW2024     = sample("TTWW2024", 0.008203, "2024", "TTWW2024.txt", "/TTWW_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")

TTWZ2022     = sample("TTWZ2022", 0.002715, "2022", "TTWZ2022.txt", "/TTWZ_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
TTWZ2022EE   = sample("TTWZ2022EE", 0.002715, "2022EE", "TTWZ2022EE.txt", "/TTWZ_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM")
TTWZ2023     = sample("TTWZ2023", 0.002715, "2023", "TTWZ2023.txt", "/TTWZ_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
TTWZ2023BPix = sample("TTWZ2023BPix", 0.002715, "2023BPix", "TTWZ2023BPix.txt", "/TTWZ_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
TTWZ2024     = sample("TTWZ2024", 0.002715, "2024", "TTWZ2024.txt", "/TTWZ_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")

TTZH2022     = sample("TTZH2022", 0.001288, "2022", "TTZH2022.txt", "/TTZH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
TTZH2022EE   = sample("TTZH2022EE", 0.001288, "2022EE", "TTZH2022EE.txt", "/TTZH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM")
TTZH2023     = sample("TTZH2023", 0.001288, "2023", "TTZH2023.txt", "/TTZH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM")
TTZH2023BPix = sample("TTZH2023BPix", 0.001288, "2023BPix", "TTZH2023BPix.txt", "/TTZH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
TTZH2024     = sample("TTZH2024", 0.001288, "2024", "TTZH2024.txt", "/TTZH-ZHto4B_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")

TTZZ2022     = sample("TTZZ2022", 0.001579, "2022", "TTZZ2022NanoList.txt", "/TTZZ_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
TTZZ2022EE   = sample("TTZZ2022EE", 0.001579, "2022EE", "TTZZ2022EENanoList.txt", "/TTZZ_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM")
TTZZ2023     = sample("TTZZ2023", 0.001579, "2023", "TTZZ2023NanoList.txt", "/TTZZ_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM")
TTZZ2023BPix = sample("TTZZ2023BPix", 0.001579, "2023BPix", "TTZZ2023BPixNanoList.txt", "/TTZZ_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
TTZZ2024     = sample("TTZZ2024", 0.001579, "2024", "TTZZ2024NanoList.txt", "/TTZZ_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")

TTTT2022     = sample("TTTT2022", 0.009652, "2022", "TTTT2022NanoList.txt", "/TTTT_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM")
TTTT2022EE   = sample("TTTT2022EE", 0.009652, "2022EE", "TTTT2022EENanoList.txt", "/TTTT_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM")
TTTT2023     = sample("TTTT2023", 0.009652, "2023", "TTTT2023NanoList.txt", "/TTTT_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM")
TTTT2023BPix = sample("TTTT2023BPix", 0.009652, "2023BPix", "TTTT2023BPixNanoList.txt", "/TTTT_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM")
TTTT2024     = sample("TTTT2024", 0.009652, "2024", "TTTT2024NanoList.txt", "/TTTT_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")

#/TTHH-TTto2L2Nu-HHto2B2Tau_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM
#/TTHH-TTto2L2Nu-HHto2B2W_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM
#/TTHH-TTto2L2Nu-HHto2B2Z_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM
#/TTHH-TTtoLNu2Q-HHto2B2Tau_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM
#/TTHH-TTtoLNu2Q-HHto2B2W_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM
#/TTHH-TTtoLNu2Q-HHto2B2Z_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM

################################################
###                                          ###
###    BACKGROUNDS MOSTLY FOR STANDARD       ###
###                                          ###
################################################

# top quark production
TT2L2024 = sample("TT2L2024",923.6*0.105,"2024","TT2L2024NanoList.txt","/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM")
TT0L2024 = sample("TT0L2024",923.6*0.457,"2024","TT0L2024NanoList.txt","/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
TT1L2024 = sample("TT1L2024",923.6*0.438,"2024","TT1L2024NanoList.txt","/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")

# single top production
STtWm2L2024 = sample("STtWm2L2024",43.95*0.105,"2024","STtWm2LNanoList.txt","/TWminusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
STtWm0L2024 = sample("STtWm0L2024",43.95*0.457,"2024","STtWm0LNanoList.txt","/TWminusto4Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
STtWm1L2024 = sample("STtWm1L2024",43.95*0.438,"2024","STtWm1LNanoList.txt","/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
STtbWp2L2024 = sample("STtbWp2L2024",43.95*0.105,"2024","STtbWp2LNanoList.txt","/TbarWplusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
STtbWp0L2024 = sample("STtbWp0L2024",43.95*0.457,"2024","STtbWp0LNanoList.txt","/TbarWplusto4Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
STtbWp1L2024 = sample("STtbWp1L2024",43.95*0.438,"2024","STtbWp1LNanoList.txt","/TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
STtTch0L2024 = sample("STtTch0L2024",145.*0.6732,"2024","STtTch0LNanoList.txt","/TBbarQto2Q-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
STtTch1L2024 = sample("STtTch1L2024",145.*0.3268,"2024","STtTch1LNanoList.txt","/TBbarQtoLNu-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
STtbTch0L2024 = sample("STtbTch0L2024",87.2*0.6732,"2024","STtbTch0LNanoList.txt","/TbarBQto2Q-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
STtbTch1L2024 = sample("STtbTch1L2024",87.2*0.3268,"2024","STtbTch1LNanoList.txt","/TbarBQtoLNu-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
STtSch0L2024 = sample("STtSch0L2024",7.244*0.6732,"2024","STtSch0LNanoList.txt","/TBbarto2Q-s-channel_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
STtSch1L2024 = sample("STtSch1L2024",7.244*0.3268,"2024","STtSch1LNanoList.txt","/TBbartoLNu-s-channel_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
STtbSch0L2024 = sample("STtbSch0L2024",4.534*0.6732,"2024","STtbSch0LNanoList.txt","/TbarBto2Q-s-channel_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
STtbSch1L2024 = sample("STtbSch1L2024",4.534*0.3268,"2024","STtbSch1LNanoList.txt","/TbarBtoLNu-s-channel_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")

# W boson production
WHT400M02024 = sample("WHT400M02024",59.99,"2024","WHT400M02024NanoList.txt","/WtoLNu-4Jets_Bin-HT-400to800-MLNu-0to120_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
WHT800M02024 = sample("WHT800M02024",6.23,"2024","WHT800M02024NanoList.txt","/WtoLNu-4Jets_Bin-HT-800to1500-MLNu-0to120_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
WHT1500M02024 = sample("WHT1500M02024",0.4477,"2024","WHT1500M02024NanoList.txt","/WtoLNu-4Jets_Bin-HT-1500to2500-MLNu-0to120_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
WHT2500M02024 = sample("WHT2500M02024",0.03075,"2024","WHT2500M02024NanoList.txt","/WtoLNu-4Jets_Bin-HT-2500-MLNu-0to120_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")

WHT400M1202024 = sample("WHT400M1202024",0.5239,"2024","WHT400M1202024NanoList.txt","/WtoLNu-4Jets_Bin-HT-400to800-MLNu-120_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
WHT800M1202024 = sample("WHT800M1202024",0.06255,"2024","WHT800M1202024NanoList.txt","/WtoLNu-4Jets_Bin-HT-800to1500-MLNu-120_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
WHT1500M1202024 = sample("WHT1500M1202024",0.005066,"2024","WHT1500M1202024NanoList.txt","/WtoLNu-4Jets_Bin-HT-1500to2500-MLNu-120_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
WHT2500M1202024 = sample("WHT2500M1202024",0.0003788,"2024","WHT2500M1202024NanoList.txt","/WtoLNu-4Jets_Bin-HT-2500-MLNu-120_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")

# Z boson production
DYHT400M42024 = sample("DYHT400M42024",5.649,"2024","DYHT400M42024NanoList.txt","/DYto2L-4Jets_Bin-HT-400to800-MLL-4to50_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
DYHT800M42024 = sample("DYHT800M42024",0.4204,"2024","DYHT800M42024NanoList.txt","/DYto2L-4Jets_Bin-HT-800to1500-MLL-4to50_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v4/NANOAODSIM")
DYHT1500M42024 = sample("DYHT1500M42024",0.02079,"2024","DYHT1500M42024NanoList.txt","/DYto2L-4Jets_Bin-HT-1500to2500-MLL-4to50_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v4/NANOAODSIM")
DYHT2500M42024 = sample("DYHT2500M42024",0.00107,"2024","DYHT2500M42024NanoList.txt","/DYto2L-4Jets_Bin-HT-2500-MLL-4to50_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v4/NANOAODSIM")
DYHT400M502024 = sample("DYHT400M502024",6.742,"2024","DYHT400M502024NanoList.txt","/DYto2L-4Jets_Bin-HT-400to800-MLL-50to120_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v5/NANOAODSIM")
DYHT800M502024 = sample("DYHT800M502024",0.693,"2024","DYHT800M502024NanoList.txt","/DYto2L-4Jets_Bin-HT-800to1500-MLL-50to120_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v5/NANOAODSIM")
DYHT1500M502024 = sample("DYHT1500M502024",0.05047,"2024","DYHT1500M502024NanoList.txt","/DYto2L-4Jets_Bin-HT-1500to2500-MLL-50to120_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v4/NANOAODSIM")
DYHT2500M502024 = sample("DYHT2500M502024",0.00346,"2024","DYHT2500M502024NanoList.txt","/DYto2L-4Jets_Bin-HT-2500-MLL-50to120_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v4/NANOAODSIM")
DYHT400M1202024 = sample("DYHT400M1202024",0.1757,"2024","DYHT400M1202024NanoList.txt","/DYto2L-4Jets_Bin-HT-400to800-MLL-120_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v4/NANOAODSIM")
DYHT800M1202024 = sample("DYHT800M1202024",0.02089,"2024","DYHT800M1202024NanoList.txt","/DYto2L-4Jets_Bin-HT-800to1500-MLL-120_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v4/NANOAODSIM")
DYHT1500M1202024 = sample("DYHT1500M1202024",0.001697,"2024","DYHT1500M1202024NanoList.txt","/DYto2L-4Jets_Bin-HT-1500to2500-MLL-120_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v4/NANOAODSIM")
DYHT2500M1202024 = sample("DYHT2500M1202024",0.0001247,"2024","DYHT2500M1202024NanoList.txt","/DYto2L-4Jets_Bin-HT-2500-MLL-120_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v4/NANOAODSIM")

DYeeM102024 = sample("DYeeM102024",17230.,"2024","DYeeM102024NanoList.txt","/DYto2E-4Jets_Bin-MLL-10to50_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
DYeeM502024 = sample("DYeeM502024",5481.,"2024","DYeeM502024NanoList.txt","/DYto2E-4Jets_Bin-MLL-50_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM")
DYmmM102024 = sample("DYmmM102024",17410.,"2024","DYmmM102024NanoList.txt","/DYto2Mu-4Jets_Bin-MLL-10to50_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
DYmmM502024 = sample("DYmmM502024",5447.,"2024","DYmmM502024NanoList.txt","/DYto2Mu-4Jets_Bin-MLL-50_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM")
DYttM102024 = sample("DYttM102024",17420.,"2024","DYttM102024NanoList.txt","/DYto2Tau-4Jets_Bin-MLL-10to50_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
DYttM502024 = sample("DYttM502024",5448.,"2024","DYttM502024NanoList.txt","/DYto2Tau-4Jets_Bin-MLL-50_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v5/NANOAODSIM")

# QCD
QCDePT802024 = sample("QCDePT802024",391400.,"2024","QCDePT802024NanoList.txt","/QCD_Bin-PT-80to120_Fil-EMEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
QCDmPT802024 = sample("QCDmPT802024",96070.0,"2024","QCDmPT802024NanoList.txt","/QCD_Bin-PT-80to120_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
QCDePT1202024 = sample("QCDePT1202024",391400.,"2024","QCDePT1202024NanoList.txt","/QCD_Bin-PT-120to170_Fil-EMEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
QCDmPT1202024 = sample("QCDmPT1202024",23140.0,"2024","QCDmPT1202024NanoList.txt","/QCD_Bin-PT-120to170_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
QCDePT1702024 = sample("QCDePT1702024",18010.,"2024","QCDePT1702024NanoList.txt","/QCD_Bin-PT-170to300_Fil-EMEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
QCDmPT1702024 = sample("QCDmPT1702024",7754.0,"2024","QCDmPT1702024NanoList.txt","/QCD_Bin-PT-170to300_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
QCDePT3002024 = sample("QCDePT3002024",1116.,"2024","QCDePT3002024NanoList.txt","/QCD_Bin-PT-300to470_Fil-EMEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
QCDmPT3002024 = sample("QCDmPT3002024",699.6,"2024","QCDmPT3002024NanoList.txt","/QCD_Bin-PT-300to470_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
QCDePT4702024 = sample("QCDePT4702024",82.76,"2024","QCDePT4702024NanoList.txt","/QCD_Bin-PT-470to600_Fil-EMEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
QCDmPT4702024 = sample("QCDmPT4702024",67.67,"2024","QCDmPT4702024NanoList.txt","/QCD_Bin-PT-470to600_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
QCDePT6002024 = sample("QCDePT6002024",21.62,"2024","QCDePT6002024NanoList.txt","/QCD_Bin-PT-600to800_Fil-EMEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
QCDmPT6002024 = sample("QCDmPT6002024",21.27,"2024","QCDmPT6002024NanoList.txt","/QCD_Bin-PT-600to800_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
QCDePT8002024 = sample("QCDePT8002024",3.361,"2024","QCDePT8002024NanoList.txt","/QCD_Bin-PT-800to1000_Fil-EMEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
QCDmPT8002024 = sample("QCDmPT8002024",3.89,"2024","QCDmPT8002024NanoList.txt","/QCD_Bin-PT-800to1000_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
QCDPT10002024 = sample("QCDPT10002024",9.306,"2024","QCDPT10002024NanoList.txt","/QCD_Bin-PT-1000to1500_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
QCDPT15002024 = sample("QCDPT15002024",0.5015,"2024","QCDPT15002024NanoList.txt","/QCD_Bin-PT-1500to2000_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
QCDPT20002024 = sample("QCDPT20002024",0.04264,"2024","QCDPT20002024NanoList.txt","/QCD_Bin-PT-2000to2500_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
QCDPT25002024 = sample("QCDPT25002024",0.004454,"2024","QCDPT25002024NanoList.txt","/QCD_Bin-PT-2500to3000_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
QCDPT30002024 = sample("QCDPT30002024",0.0005539,"2024","QCDPT30002024NanoList.txt","/QCD_Bin-PT-3000_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")

## Diboson and ttHbb
# Electing not to run the versions without any prompt leptons. 3-4 leptons are above
WW1L2024 = sample("WW1L2024", 48.94, "2024", "WW1L2024NanoList.txt", "/WWtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
WW2L2024 = sample("WW2L2024", 11.79, "2024", "WW2L2024NanoList.txt", "/WWto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
WZ1L2Q2024 = sample("WZ1L2Q2024", 15.87, "2024", "WZ1L2Q2024NanoList.txt", "/WZtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
WZ1L3Nu2024 = sample("WZ1L3Nu2024", 3.077, "2024", "WZ1L3Nu2024NanoList.txt", "/WZtoL3Nu_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
WZ2L2024 = sample("WZ2L2024", 7.568, "2024", "WZ2L2024NanoList.txt", "/WZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
ZZ2L2Q2024 = sample("ZZ2L2Q2024", 6.788, "2024", "ZZ2L2Q2024NanoList.txt", "/ZZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
ZZ2L2Nu2024 = sample("ZZ2L2Nu2024", 1.031, "2024", "ZZ2L2Nu2024NanoList.txt", "/ZZto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")
TTH2B2024 = sample("TTH2B2024", 0.5742, "2024", "TTH2B2024NanoList.txt", "/TTH-Hto2B_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM")

sample_test = {
    "SingleElecRun2022C":      SingleElecRun2022C,
}

samples_data = {
    "SingleElecRun2022C":      SingleElecRun2022C,      
    "SingleElecRun2022D":      SingleElecRun2022D,      
    "SingleElecRun2022EEE":    SingleElecRun2022EEE,    
    "SingleElecRun2022EEF":    SingleElecRun2022EEF,    
    "SingleElecRun2022EEG":    SingleElecRun2022EEG,    
    "SingleElecRun2023C01":    SingleElecRun2023C01,    
    "SingleElecRun2023C02":    SingleElecRun2023C02,    
    "SingleElecRun2023C03":    SingleElecRun2023C03,    
    "SingleElecRun2023C04":    SingleElecRun2023C04,    
    "SingleElecRun2023C11":    SingleElecRun2023C11,    
    "SingleElecRun2023C12":    SingleElecRun2023C12,    
    "SingleElecRun2023C13":    SingleElecRun2023C13,    
    "SingleElecRun2023C14":    SingleElecRun2023C14,    
    "SingleElecRun2023BPixD01":SingleElecRun2023BPixD01,
    "SingleElecRun2023BPixD02":SingleElecRun2023BPixD02,
    "SingleElecRun2023BPixD11":SingleElecRun2023BPixD11,
    "SingleElecRun2023BPixD12":SingleElecRun2023BPixD12,
    "SingleElecRun2024C0" : SingleElecRun2024C0 ,
    "SingleElecRun2024D0" : SingleElecRun2024D0 ,
    "SingleElecRun2024E0" : SingleElecRun2024E0 ,
    "SingleElecRun2024F0" : SingleElecRun2024F0 ,
    "SingleElecRun2024G0" : SingleElecRun2024G0 ,
    "SingleElecRun2024H0" : SingleElecRun2024H0 ,
    "SingleElecRun2024I01": SingleElecRun2024I01,
    "SingleElecRun2024I02": SingleElecRun2024I02,
    "SingleElecRun2024C1" : SingleElecRun2024C1 ,
    "SingleElecRun2024D1" : SingleElecRun2024D1 ,
    "SingleElecRun2024E1" : SingleElecRun2024E1 ,
    "SingleElecRun2024F1" : SingleElecRun2024F1 ,
    "SingleElecRun2024G1" : SingleElecRun2024G1 ,
    "SingleElecRun2024H1" : SingleElecRun2024H1 ,
    "SingleElecRun2024I11": SingleElecRun2024I11,
    "SingleElecRun2024I12": SingleElecRun2024I12,
    "SingleElecRun2025B0" : SingleElecRun2025B0 ,
    "SingleElecRun2025C01": SingleElecRun2025C01,
    "SingleElecRun2025C02": SingleElecRun2025C02,
    "SingleElecRun2025D0" : SingleElecRun2025D0 ,
    "SingleElecRun2025E0" : SingleElecRun2025E0 ,
    "SingleElecRun2025F01": SingleElecRun2025F01,
    "SingleElecRun2025F02": SingleElecRun2025F02,
    "SingleElecRun2025G0" : SingleElecRun2025G0 ,
    "SingleElecRun2025B1" : SingleElecRun2025B1 ,
    "SingleElecRun2025C11": SingleElecRun2025C11,
    "SingleElecRun2025C12": SingleElecRun2025C12,
    "SingleElecRun2025D1" : SingleElecRun2025D1 ,
    "SingleElecRun2025E1" : SingleElecRun2025E1 ,
    "SingleElecRun2025F11": SingleElecRun2025F11,
    "SingleElecRun2025F12": SingleElecRun2025F12,
    "SingleElecRun2025G1" : SingleElecRun2025G1 ,
    "SingleElecRun2025B2" : SingleElecRun2025B2 ,
    "SingleElecRun2025C21": SingleElecRun2025C21,
    "SingleElecRun2025C22": SingleElecRun2025C22,
    "SingleElecRun2025D2" : SingleElecRun2025D2 ,
    "SingleElecRun2025E2" : SingleElecRun2025E2 ,
    "SingleElecRun2025F21": SingleElecRun2025F21,
    "SingleElecRun2025F22": SingleElecRun2025F22,
    "SingleElecRun2025G2" : SingleElecRun2025G2 ,
    "SingleElecRun2025B3" : SingleElecRun2025B3 ,
    "SingleElecRun2025C31": SingleElecRun2025C31,
    "SingleElecRun2025C32": SingleElecRun2025C32,
    "SingleElecRun2025D3" : SingleElecRun2025D3 ,
    "SingleElecRun2025E3" : SingleElecRun2025E3 ,
    "SingleElecRun2025F31": SingleElecRun2025F31,
    "SingleElecRun2025F32": SingleElecRun2025F32,
    "SingleElecRun2025G3" : SingleElecRun2025G3 ,
                      
    "SingleMuonRun2022C":      SingleMuonRun2022C,      
    "SingleMuonRun2022D":      SingleMuonRun2022D,      
    "SingleMuonRun2022EEE":    SingleMuonRun2022EEE,    
    "SingleMuonRun2022EEF":    SingleMuonRun2022EEF,    
    "SingleMuonRun2022EEG":    SingleMuonRun2022EEG,    
    "SingleMuonRun2023C01":    SingleMuonRun2023C01,    
    "SingleMuonRun2023C02":    SingleMuonRun2023C02,    
    "SingleMuonRun2023C03":    SingleMuonRun2023C03,    
    "SingleMuonRun2023C04":    SingleMuonRun2023C04,    
    "SingleMuonRun2023C11":    SingleMuonRun2023C11,    
    "SingleMuonRun2023C12":    SingleMuonRun2023C12,    
    "SingleMuonRun2023C13":    SingleMuonRun2023C13,    
    "SingleMuonRun2023C14":    SingleMuonRun2023C14,    
    "SingleMuonRun2023BPixD01":SingleMuonRun2023BPixD01,
    "SingleMuonRun2023BPixD02":SingleMuonRun2023BPixD02,
    "SingleMuonRun2023BPixD11":SingleMuonRun2023BPixD11,
    "SingleMuonRun2023BPixD12":SingleMuonRun2023BPixD12,
    "SingleMuonRun2024C0" : SingleMuonRun2024C0,
    "SingleMuonRun2024D0" : SingleMuonRun2024D0,
    "SingleMuonRun2024E0" : SingleMuonRun2024E0,
    "SingleMuonRun2024F0" : SingleMuonRun2024F0,
    "SingleMuonRun2024G0" : SingleMuonRun2024G0,
    "SingleMuonRun2024H0" : SingleMuonRun2024H0,
    "SingleMuonRun2024I01": SingleMuonRun2024I01,
    "SingleMuonRun2024I02": SingleMuonRun2024I02,
    "SingleMuonRun2024C1" : SingleMuonRun2024C1,
    "SingleMuonRun2024D1" : SingleMuonRun2024D1,
    "SingleMuonRun2024E1" : SingleMuonRun2024E1,
    "SingleMuonRun2024F1" : SingleMuonRun2024F1,
    "SingleMuonRun2024G1" : SingleMuonRun2024G1,
    "SingleMuonRun2024H1" : SingleMuonRun2024H1,
    "SingleMuonRun2024I11": SingleMuonRun2024I11,
    "SingleMuonRun2024I12": SingleMuonRun2024I12,
    "SingleMuonRun2025B0" : SingleMuonRun2025B0,
    "SingleMuonRun2025C01": SingleMuonRun2025C01,
    "SingleMuonRun2025C02": SingleMuonRun2025C02,
    "SingleMuonRun2025D0" : SingleMuonRun2025D0,
    "SingleMuonRun2025E0" : SingleMuonRun2025E0,
    "SingleMuonRun2025F01": SingleMuonRun2025F01,
    "SingleMuonRun2025F02": SingleMuonRun2025F02,
    "SingleMuonRun2025G0" : SingleMuonRun2025G0,
    "SingleMuonRun2025B1" : SingleMuonRun2025B1,
    "SingleMuonRun2025C11": SingleMuonRun2025C11,
    "SingleMuonRun2025C12": SingleMuonRun2025C12,
    "SingleMuonRun2025D1" : SingleMuonRun2025D1,
    "SingleMuonRun2025E1" : SingleMuonRun2025E1,
    "SingleMuonRun2025F11": SingleMuonRun2025F11,
    "SingleMuonRun2025F12": SingleMuonRun2025F12,
    "SingleMuonRun2025G1" : SingleMuonRun2025G1,

    "MuonEGRun2022C":     MuonEGRun2022C,
    "MuonEGRun2022D":     MuonEGRun2022D,
    "MuonEGRun2022EEE":   MuonEGRun2022EEE,
    "MuonEGRun2022EEF":   MuonEGRun2022EEF,
    "MuonEGRun2022EEG":   MuonEGRun2022EEG,
    "MuonEGRun2023C1":    MuonEGRun2023C1,
    "MuonEGRun2023C2":    MuonEGRun2023C2,
    "MuonEGRun2023C3":    MuonEGRun2023C3,
    "MuonEGRun2023C4":    MuonEGRun2023C4,
    "MuonEGRun2023BPixD1":MuonEGRun2023BPixD1,
    "MuonEGRun2023BPixD2":MuonEGRun2023BPixD2,
    "MuonEGRun2024C"  :    MuonEGRun2024C ,
    "MuonEGRun2024D"  :    MuonEGRun2024D ,
    "MuonEGRun2024E"  :    MuonEGRun2024E ,
    "MuonEGRun2024F"  :    MuonEGRun2024F ,
    "MuonEGRun2024G"  :    MuonEGRun2024G ,
    "MuonEGRun2024H"  :    MuonEGRun2024H ,
    "MuonEGRun2024I1" :    MuonEGRun2024I1,
    "MuonEGRun2024I2" :    MuonEGRun2024I2,
    "MuonEGRun2025B"  :    MuonEGRun2025B ,
    "MuonEGRun2025C1" :    MuonEGRun2025C1,
    "MuonEGRun2025C2" :    MuonEGRun2025C2,
    "MuonEGRun2025D"  :    MuonEGRun2025D ,
    "MuonEGRun2025E"  :    MuonEGRun2025E ,
    "MuonEGRun2025F1" :    MuonEGRun2025F1,
    "MuonEGRun2025F2" :    MuonEGRun2025F2,
    "MuonEGRun2025G"  :    MuonEGRun2025G ,
                                      
    "TauRun2022C":      TauRun2022C,  
    "TauRun2022D":      TauRun2022D,
    "TauRun2022EEE":    TauRun2022EEE,
    "TauRun2022EEF":    TauRun2022EEF,
    "TauRun2022EEG":    TauRun2022EEG,
    "TauRun2023C1":    TauRun2023C1,
    "TauRun2023C2":    TauRun2023C2,
    "TauRun2023C3":    TauRun2023C3,
    "TauRun2023C4":    TauRun2023C4,
    "TauRun2023BPixD1":TauRun2023BPixD1,
    "TauRun2023BPixD2":TauRun2023BPixD2,
    "TauRun2024C" : TauRun2024C  ,
    "TauRun2024D" : TauRun2024D  ,
    "TauRun2024E" : TauRun2024E  ,
    "TauRun2024F" : TauRun2024F  ,
    "TauRun2024G" : TauRun2024G  ,
    "TauRun2024H" : TauRun2024H  ,
    "TauRun2024I1": TauRun2024I1 ,
    "TauRun2024I2": TauRun2024I2 ,
    "TauRun2025B" : TauRun2025B  ,
    "TauRun2025C1": TauRun2025C1 ,
    "TauRun2025C2": TauRun2025C2 ,
    "TauRun2025D" : TauRun2025D  ,
    "TauRun2025E" : TauRun2025E  ,
    "TauRun2025F1": TauRun2025F1 , 
    "TauRun2025F2": TauRun2025F2 ,
    "TauRun2025G" : TauRun2025G  ,
}                            

samples_nonprompt = {
    "NonpromptSingleElecRun2022C":      NonpromptSingleElecRun2022C,      
    "NonpromptSingleElecRun2022D":      NonpromptSingleElecRun2022D,      
    "NonpromptSingleElecRun2022EEE":    NonpromptSingleElecRun2022EEE,    
    "NonpromptSingleElecRun2022EEF":    NonpromptSingleElecRun2022EEF,    
    "NonpromptSingleElecRun2022EEG":    NonpromptSingleElecRun2022EEG,    
    "NonpromptSingleElecRun2023C01":    NonpromptSingleElecRun2023C01,    
    "NonpromptSingleElecRun2023C02":    NonpromptSingleElecRun2023C02,    
    "NonpromptSingleElecRun2023C03":    NonpromptSingleElecRun2023C03,    
    "NonpromptSingleElecRun2023C04":    NonpromptSingleElecRun2023C04,    
    "NonpromptSingleElecRun2023C11":    NonpromptSingleElecRun2023C11,    
    "NonpromptSingleElecRun2023C12":    NonpromptSingleElecRun2023C12,    
    "NonpromptSingleElecRun2023C13":    NonpromptSingleElecRun2023C13,    
    "NonpromptSingleElecRun2023C14":    NonpromptSingleElecRun2023C14,    
    "NonpromptSingleElecRun2023BPixD01":NonpromptSingleElecRun2023BPixD01,
    "NonpromptSingleElecRun2023BPixD02":NonpromptSingleElecRun2023BPixD02,
    "NonpromptSingleElecRun2023BPixD11":NonpromptSingleElecRun2023BPixD11,
    "NonpromptSingleElecRun2023BPixD12":NonpromptSingleElecRun2023BPixD12,
    "NonpromptSingleMuonRun2022C":      NonpromptSingleMuonRun2022C,      
    "NonpromptSingleMuonRun2022D":      NonpromptSingleMuonRun2022D,      
    "NonpromptSingleMuonRun2022EEE":    NonpromptSingleMuonRun2022EEE,    
    "NonpromptSingleMuonRun2022EEF":    NonpromptSingleMuonRun2022EEF,    
    "NonpromptSingleMuonRun2022EEG":    NonpromptSingleMuonRun2022EEG,    
    "NonpromptSingleMuonRun2023C01":    NonpromptSingleMuonRun2023C01,    
    "NonpromptSingleMuonRun2023C02":    NonpromptSingleMuonRun2023C02,    
    "NonpromptSingleMuonRun2023C03":    NonpromptSingleMuonRun2023C03,    
    "NonpromptSingleMuonRun2023C04":    NonpromptSingleMuonRun2023C04,    
    "NonpromptSingleMuonRun2023C11":    NonpromptSingleMuonRun2023C11,    
    "NonpromptSingleMuonRun2023C12":    NonpromptSingleMuonRun2023C12,    
    "NonpromptSingleMuonRun2023C13":    NonpromptSingleMuonRun2023C13,    
    "NonpromptSingleMuonRun2023C14":    NonpromptSingleMuonRun2023C14,    
    "NonpromptSingleMuonRun2023BPixD01":NonpromptSingleMuonRun2023BPixD01,
    "NonpromptSingleMuonRun2023BPixD02":NonpromptSingleMuonRun2023BPixD02,
    "NonpromptSingleMuonRun2023BPixD11":NonpromptSingleMuonRun2023BPixD11,
    "NonpromptSingleMuonRun2023BPixD12":NonpromptSingleMuonRun2023BPixD12,
    "NonpromptMuonEGRun2022C":      NonpromptMuonEGRun2022C,
    "NonpromptMuonEGRun2022D":      NonpromptMuonEGRun2022D,
    "NonpromptMuonEGRun2022EEE":    NonpromptMuonEGRun2022EEE,
    "NonpromptMuonEGRun2022EEF":    NonpromptMuonEGRun2022EEF,
    "NonpromptMuonEGRun2022EEG":    NonpromptMuonEGRun2022EEG,
    "NonpromptMuonEGRun2023C1":    NonpromptMuonEGRun2023C1,
    "NonpromptMuonEGRun2023C2":    NonpromptMuonEGRun2023C2,
    "NonpromptMuonEGRun2023C3":    NonpromptMuonEGRun2023C3,
    "NonpromptMuonEGRun2023C4":    NonpromptMuonEGRun2023C4,
    "NonpromptMuonEGRun2023BPixD1":NonpromptMuonEGRun2023BPixD1,
    "NonpromptMuonEGRun2023BPixD2":NonpromptMuonEGRun2023BPixD2,
    "NonpromptTauRun2022C":      NonpromptTauRun2022C,
    "NonpromptTauRun2022D":      NonpromptTauRun2022D,
    "NonpromptTauRun2022EEE":    NonpromptTauRun2022EEE,
    "NonpromptTauRun2022EEF":    NonpromptTauRun2022EEF,
    "NonpromptTauRun2022EEG":    NonpromptTauRun2022EEG,
    "NonpromptTauRun2023C1":    NonpromptTauRun2023C1,
    "NonpromptTauRun2023C2":    NonpromptTauRun2023C2,
    "NonpromptTauRun2023C3":    NonpromptTauRun2023C3,
    "NonpromptTauRun2023C4":    NonpromptTauRun2023C4,
    "NonpromptTauRun2023BPixD1":NonpromptTauRun2023BPixD1,
    "NonpromptTauRun2023BPixD2":NonpromptTauRun2023BPixD2,
}

samples_signal={
    "Bprime_M1000_2022":    Bprime_M1000_2022,    
    "Bprime_M1000_2022EE":  Bprime_M1000_2022EE,  
    "Bprime_M1000_2023":    Bprime_M1000_2023,    
    "Bprime_M1000_2023BPix":Bprime_M1000_2023BPix,
    "Bprime_M1000_2024":Bprime_M1000_2024,
    "Bprime_M1300_2022":    Bprime_M1300_2022,    
    "Bprime_M1300_2022EE":  Bprime_M1300_2022EE,  
    "Bprime_M1300_2023":    Bprime_M1300_2023,    
    "Bprime_M1300_2023BPix":Bprime_M1300_2023BPix,
    "Bprime_M1300_2024":Bprime_M1300_2024,
    "Bprime_M1600_2022":    Bprime_M1600_2022,    
    "Bprime_M1600_2022EE":  Bprime_M1600_2022EE,  
    "Bprime_M1600_2023":    Bprime_M1600_2023,    
    "Bprime_M1600_2023BPix":Bprime_M1600_2023BPix,
    "Bprime_M1600_2024":Bprime_M1600_2024,
    "Bprime_M700_2022":    Bprime_M700_2022,    
    "Bprime_M700_2022EE":  Bprime_M700_2022EE,  
    "Bprime_M700_2023":    Bprime_M700_2023,    
    "Bprime_M700_2023BPix":Bprime_M700_2023BPix,
    "Bprime_M700_2024":Bprime_M700_2024,
    "Bprime_M400_2022":     Bprime_M400_2022,
    "Bprime_M400_2022EE":   Bprime_M400_2022EE,
    "Bprime_M400_2023":     Bprime_M400_2023,
    "Bprime_M400_2023BPix": Bprime_M400_2023BPix,
    "Bprime_M400_2024": Bprime_M400_2024,
}

samples_mc = {
    "Bprime_M1000_2022":    Bprime_M1000_2022,    
    "Bprime_M1000_2022EE":  Bprime_M1000_2022EE,  
    "Bprime_M1000_2023":    Bprime_M1000_2023,    
    "Bprime_M1000_2023BPix":Bprime_M1000_2023BPix,
    "Bprime_M1300_2022":    Bprime_M1300_2022,    
    "Bprime_M1300_2022EE":  Bprime_M1300_2022EE,  
    "Bprime_M1300_2023":    Bprime_M1300_2023,    
    "Bprime_M1300_2023BPix":Bprime_M1300_2023BPix,
    "Bprime_M1600_2022":    Bprime_M1600_2022,    
    "Bprime_M1600_2022EE":  Bprime_M1600_2022EE,  
    "Bprime_M1600_2023":    Bprime_M1600_2023,    
    "Bprime_M1600_2023BPix":Bprime_M1600_2023BPix,
    "Bprime_M700_2022":    Bprime_M700_2022,    
    "Bprime_M700_2022EE":  Bprime_M700_2022EE,  
    "Bprime_M700_2023":    Bprime_M700_2023,    
    "Bprime_M700_2023BPix":Bprime_M700_2023BPix,
    "Bprime_M400_2022":     Bprime_M400_2022,
    "Bprime_M400_2022EE":   Bprime_M400_2022EE,
    "Bprime_M400_2023":     Bprime_M400_2023,
    "Bprime_M400_2023BPix": Bprime_M400_2023BPix,
    "WZ3L2022":       WZ3L2022,
    "WZ3L2022ext":    WZ3L2022ext,
    "WZ3L2022EE":     WZ3L2022EE,
    "WZ3L2022EEext":  WZ3L2022EEext,
    "WZ3L2023":       WZ3L2023,
    "WZ3L2023ext":    WZ3L2023ext,
    "WZ3L2023BPix":   WZ3L2023BPix,
    "WZ3L2023BPixext":WZ3L2023BPixext,
    "ZZ4L2022":       ZZ4L2022,
    "ZZ4L2022ext":    ZZ4L2022ext,
    "ZZ4L2022EE":     ZZ4L2022EE,
    "ZZ4L2022EEext":  ZZ4L2022EEext,
    "ZZ4L2023":       ZZ4L2023,
    "ZZ4L2023BPix":   ZZ4L2023BPix,
    "WWW2022"     :     WWW2022     ,
    "WWW2022EE"   :     WWW2022EE   ,
    "WWW2023"     :     WWW2023     ,
    "WWW2023BPix" :     WWW2023BPix ,
    "WWZ2022"     :     WWZ2022     ,
    "WWZ2022EE"   :     WWZ2022EE   ,
    "WWZ2023"     :     WWZ2023     ,
    "WWZ2023BPix" :     WWZ2023BPix ,
    "WZZ2022"     :     WZZ2022     ,
    "WZZ2022EE"   :     WZZ2022EE   ,
    "WZZ2023"     :     WZZ2023     ,
    "WZZ2023BPix" :     WZZ2023BPix ,
    "ZZZ2022"     :     ZZZ2022     ,
    "ZZZ2022EE"   :     ZZZ2022EE   ,
    "ZZZ2023"     :     ZZZ2023     ,
    "ZZZ2023BPix" :     ZZZ2023BPix ,
    "WWZZ4L2022":     WWZZ4L2022,
    "WWZZ4L2022EE":   WWZZ4L2022EE,
    "WWZZ4L2023":     WWZZ4L2023,
    "WWZZ4L2023BPix": WWZZ4L2023BPix,
    "VHnonbb2022": VHnonbb2022,
    "VHnonbb2022EE": VHnonbb2022EE,
    "VHnonbb2023": VHnonbb2023,
    "VHnonbb2023BPix": VHnonbb2023BPix,
    "ZG2J2022"           : ZG2J2022,
    "ZG2J2022EE"         : ZG2J2022EE,
    "ZG2J2023"           : ZG2J2023,
    "ZG2J2023BPix"       : ZG2J2023BPix,
    "TTG1Jpt102022"      : TTG1Jpt102022,
    "TTG1Jpt102022EE"    : TTG1Jpt102022EE,   
    "TTG1Jpt102023"      : TTG1Jpt102023, 
    "TTG1Jpt102023BPix"  : TTG1Jpt102023BPix, 
    "TTG1Jpt1002022"     : TTG1Jpt1002022,
    "TTG1Jpt1002022EE"   : TTG1Jpt1002022EE, 
    "TTG1Jpt1002023"     : TTG1Jpt1002023,
    "TTG1Jpt1002023BPix" : TTG1Jpt1002023BPix, 
    "TTG1Jpt2002022"     : TTG1Jpt2002022,
    "TTG1Jpt2002022EE"   : TTG1Jpt2002022EE, 
    "TTG1Jpt2002023"     : TTG1Jpt2002023,
    "TTG1Jpt2002023BPix" : TTG1Jpt2002023BPix, 
    "TTHnonB2022":    TTHnonB2022,    
    "TTHnonB2022EE":  TTHnonB2022EE,  
    "TTHnonB2023":    TTHnonB2023,    
    "TTHnonB2023BPix":TTHnonB2023BPix,
    "TTWl2022":         TTWl2022,         
    "TTWl2022EE":       TTWl2022EE,       
    "TTWl2023":         TTWl2023,         
    "TTWl2023BPix":     TTWl2023BPix,     
    "TTZM42022":       TTZM42022,       
    "TTZM42022EE":     TTZM42022EE,     
    "TTZM42023":       TTZM42023,       
    "TTZM42023BPix":   TTZM42023BPix,   
    "TTZM502022":    TTZM502022,    
    "TTZM502022EE":  TTZM502022EE,  
    "TTZM502023":    TTZM502023,    
    "TTZM502023BPix":TTZM502023BPix,
    "TTZM502022ext":    TTZM502022ext,  
    "TTZM502022EEext":  TTZM502022EEext,
    "TTZM502023ext":    TTZM502023ext,
    "TTZM502023BPixext":TTZM502023BPixext,
    "TTWH2022"     : TTWH2022     ,
    "TTWH2022EE"   : TTWH2022EE  ,
    "TTWH2023"     : TTWH2023    ,
    "TTWH2023BPix" : TTWH2023BPix,
    "TTWW2022"     : TTWW2022    ,
    "TTWW2022EE"   : TTWW2022EE  ,
    "TTWW2023"     : TTWW2023    ,
    "TTWW2023BPix" : TTWW2023BPix,
    "TTWZ2022"     : TTWZ2022    ,
    "TTWZ2022EE"   : TTWZ2022EE  ,
    "TTWZ2023"     : TTWZ2023    ,
    "TTWZ2023BPix" : TTWZ2023BPix,
    "TTZH2022"     : TTZH2022    ,
    "TTZH2022EE"   : TTZH2022EE  ,
    "TTZH2023"     : TTZH2023    ,
    "TTZH2023BPix" : TTZH2023BPix,
    "TTZZ2022"     : TTZZ2022    ,
    "TTZZ2022EE"   : TTZZ2022EE  ,
    "TTZZ2023"     : TTZZ2023    ,
    "TTZZ2023BPix" : TTZZ2023BPix,
    "TTTT2022"     : TTTT2022    ,
    "TTTT2022EE"   : TTTT2022EE  ,
    "TTTT2023"     : TTTT2023    ,
    "TTTT2023BPix" : TTTT2023BPix,
    "TZQB2022" : TZQB2022,
    "TZQB2022EE" : TZQB2022EE,
    "TZQB2023" : TZQB2023,
    "TZQB2023BPix" : TZQB2023BPix,
    "TGQB2022" : TGQB2022,
    "TGQB2022EE" : TGQB2022EE,
    "TGQB2023" : TGQB2023,
    "TGQB2023BPix" : TGQB2023BPix,
}

samples_mc_standard = {
    "BpBp_M1200_2024": BpBp_M1200_2024 ,
    "BpBp_M1400_2024": BpBp_M1400_2024 ,
    "BpBp_M1500_2024": BpBp_M1500_2024 ,
    "BpBp_M1600_2024": BpBp_M1600_2024 ,
    "BpBp_M1700_2024": BpBp_M1700_2024 ,
    "BpBp_M1800_2024": BpBp_M1800_2024 ,
    "BpBp_M1900_2024": BpBp_M1900_2024 ,
    "BpBp_M2000_2024": BpBp_M2000_2024 ,
    "BpBp_M2100_2024": BpBp_M2100_2024 ,
    "BpBp_M2200_2024": BpBp_M2200_2024 ,
    "TpTp_M1200_2024": TpTp_M1200_2024 ,
    "TpTp_M1300_2024": TpTp_M1300_2024 ,
    "TpTp_M1400_2024": TpTp_M1400_2024 ,
    "TpTp_M1600_2024": TpTp_M1600_2024 ,
    "TpTp_M1700_2024": TpTp_M1700_2024 ,
    "TpTp_M1800_2024": TpTp_M1800_2024 ,
    "TpTp_M1900_2024": TpTp_M1900_2024 ,
    "TpTp_M2000_2024": TpTp_M2000_2024 ,
    "TpTp_M2100_2024": TpTp_M2100_2024 ,
    "TpTp_M2200_2024": TpTp_M2200_2024 ,

    #tt+X
    "TTHnonB2024" : TTHnonB2024,
    "TTWl2024" : TTWl2024,
    "TTZM42024" : TTZM42024,
    "TTZM502024" : TTZM502024, 
    "TTZM502024" : TTZM502024,
    
    #tz + qb
    "TZQB2024" : TZQB2024,

    # top quark
    "TT2L2024":TT2L2024,
    "TT0L2024":TT0L2024,
    "TT1L2024":TT1L2024,
                     
    # single top    
    "STtWm2L2024"    :STtWm2L2024  ,
    "STtWm0L2024"    :STtWm0L2024  ,
    "STtWm1L2024"    :STtWm1L2024  ,
    "STtbWp2L2024"   :STtbWp2L2024 ,
    "STtbWp0L2024"   :STtbWp0L2024 ,
    "STtbWp1L2024"   :STtbWp1L2024 ,
    "STtTch0L2024"   :STtTch0L2024 ,
    "STtTch1L2024"   :STtTch1L2024 ,
    "STtbTch0L2024"  :STtbTch0L2024,
    "STtbTch1L2024"  :STtbTch1L2024,
    "STtSch0L2024"   :STtSch0L2024 ,
    "STtSch1L2024"   :STtSch1L2024 ,
    "STtbSch0L2024"  :STtbSch0L2024,
    "STtbSch1L2024"  :STtbSch1L2024,
                                   
    # W boson                      
    "WHT400M02024"   :WHT400M02024 ,
    "WHT800M02024"   :WHT800M02024 ,
    "WHT1500M02024"  :WHT1500M02024,
    "WHT2500M02024"  :WHT2500M02024,
                     
    "WHT400M1202024" :WHT400M1202024  ,
    "WHT800M1202024" :WHT800M1202024  ,
    "WHT1500M1202024":WHT1500M1202024 ,
    "WHT2500M1202024":WHT2500M1202024 ,
                                      
    # Z boson                         
    "DYHT400M42024"  : DYHT400M42024  ,
    "DYHT800M42024"  : DYHT800M42024  ,
    "DYHT1500M42024" : DYHT1500M42024 ,
    "DYHT2500M42024" : DYHT2500M42024 ,
    "DYHT400M502024" : DYHT400M502024 ,
    "DYHT800M502024" : DYHT800M502024 ,
    "DYHT1500M502024": DYHT1500M502024,
    "DYHT2500M502024": DYHT2500M502024,
    "DYHT400M1202024": DYHT400M1202024,
    "DYHT800M1202024": DYHT800M1202024,
    "DYHT1500M1202024":DYHT1500M1202024,
    "DYHT2500M1202024":DYHT2500M1202024,
                                      
    "DYeeM102024"  :DYeeM102024  ,
    "DYeeM502024"  :DYeeM502024  ,
    "DYmmM102024"  :DYmmM102024  ,
    "DYmmM502024"  :DYmmM502024  ,
    "DYttM102024"  :DYttM102024  ,
    "DYttM502024"  :DYttM502024  ,
                                 
    # QCD                        
    "QCDePT802024" :QCDePT802024 ,
    "QCDmPT802024" :QCDmPT802024 ,
    "QCDePT1202024":QCDePT1202024,
    "QCDmPT1202024":QCDmPT1202024,
    "QCDePT1702024":QCDePT1702024,
    "QCDmPT1702024":QCDmPT1702024,
    "QCDePT3002024":QCDePT3002024,
    "QCDmPT3002024":QCDmPT3002024,
    "QCDePT4702024":QCDePT4702024,
    "QCDmPT4702024":QCDmPT4702024,
    "QCDePT6002024":QCDePT6002024,
    "QCDmPT6002024":QCDmPT6002024,
    "QCDePT8002024":QCDePT8002024,
    "QCDmPT8002024":QCDmPT8002024,
    "QCDPT10002024":QCDPT10002024,
    "QCDPT15002024":QCDPT15002024,
    "QCDPT20002024":QCDPT20002024,
    "QCDPT25002024":QCDPT25002024,
    "QCDPT30002024":QCDPT30002024,

    # Diboson and ttHbb
    "WW1L2024"     :WW1L2024     ,
    "WW2L2024"     :WW2L2024     ,
    "WZ1L2Q2024"   :WZ1L2Q2024   ,
    "WZ1L3Nu2024"  :WZ1L3Nu2024  ,
    "WZ2L2024"     :WZ2L2024     ,
    "ZZ2L2Q2024"   :ZZ2L2Q2024   ,
    "ZZ2L2Nu2024"  :ZZ2L2Nu2024  ,
    "TTH2B2024"    :TTH2B2024    ,
}

# samples_pfmc = {
#     "TTToSemiLeptonic2022":     TTToSemiLeptonic2022,
#     "TTToSemiLeptonic2022ext":  TTToSemiLeptonic2022ext,
#     "TTToSemiLeptonic2022EE":   TTToSemiLeptonic2022EE,
#     "TTToSemiLeptonic2022EEext":TTToSemiLeptonic2022EEext,
#     "TTToSemiLeptonic2023":     TTToSemiLeptonic2023,
#     "TTToSemiLeptonic2023BPix": TTToSemiLeptonic2023BPix,
#     "DYPT402022":     DYPT402022,
#     "DYPT402022EE":   DYPT402022EE,
#     "DYPT402023":     DYPT402023,
#     "DYPT402023BPix": DYPT402023BPix,
#     "DYPT1002022":    DYPT1002022,
#     "DYPT1002022EE":  DYPT1002022EE,
#     "DYPT1002023":    DYPT1002023,
#     "DYPT1002023BPix":DYPT1002023BPix,
#     "DYPT2002022":    DYPT2002022,
#     "DYPT2002022EE":  DYPT2002022EE,
#     "DYPT2002023":    DYPT2002023,
#     "DYPT2002023BPix":DYPT2002023BPix,
#     "DYPT4002022":    DYPT4002022,
#     "DYPT4002022EE":  DYPT4002022EE,
#     "DYPT4002023":    DYPT4002023,
#     "DYPT4002023BPix":DYPT4002023BPix,
#     "DYPT6002022":    DYPT6002022,
#     "DYPT6002022EE":  DYPT6002022EE,
#     "DYPT6002023":    DYPT6002023,
#     "DYPT6002023BPix":DYPT6002023BPix,
#     # Add 2024 MC in here for the same samples
# }    

# samples_pfdata = {
#     "SingleElecRun2022C":      SingleElecRun2022C,
#     "SingleElecRun2022D":      SingleElecRun2022D,
#     "SingleElecRun2022EEE":    SingleElecRun2022EEE,
#     "SingleElecRun2022EEF":    SingleElecRun2022EEF,
#     "SingleElecRun2022EEG":    SingleElecRun2022EEG,
#     "SingleElecRun2023C01":    SingleElecRun2023C01,
#     "SingleElecRun2023C02":    SingleElecRun2023C02,
#     "SingleElecRun2023C03":    SingleElecRun2023C03,
#     "SingleElecRun2023C04":    SingleElecRun2023C04,
#     "SingleElecRun2023C11":    SingleElecRun2023C11,
#     "SingleElecRun2023C12":    SingleElecRun2023C12,
#     "SingleElecRun2023C13":    SingleElecRun2023C13,
#     "SingleElecRun2023C14":    SingleElecRun2023C14,
#     "SingleElecRun2023BPixD01":SingleElecRun2023BPixD01,
#     "SingleElecRun2023BPixD02":SingleElecRun2023BPixD02,
#     "SingleElecRun2023BPixD11":SingleElecRun2023BPixD11,
#     "SingleElecRun2023BPixD12":SingleElecRun2023BPixD12,
#     "SingleMuonRun2022C":      SingleMuonRun2022C,
#     "SingleMuonRun2022D":      SingleMuonRun2022D,
#     "SingleMuonRun2022EEE":    SingleMuonRun2022EEE,
#     "SingleMuonRun2022EEF":    SingleMuonRun2022EEF,
#     "SingleMuonRun2022EEG":    SingleMuonRun2022EEG,
#     "SingleMuonRun2023C01":    SingleMuonRun2023C01,
#     "SingleMuonRun2023C02":    SingleMuonRun2023C02,
#     "SingleMuonRun2023C03":    SingleMuonRun2023C03,
#     "SingleMuonRun2023C04":    SingleMuonRun2023C04,
#     "SingleMuonRun2023C11":    SingleMuonRun2023C11,
#     "SingleMuonRun2023C12":    SingleMuonRun2023C12,
#     "SingleMuonRun2023C13":    SingleMuonRun2023C13,
#     "SingleMuonRun2023C14":    SingleMuonRun2023C14,
#     "SingleMuonRun2023BPixD01":SingleMuonRun2023BPixD01,
#     "SingleMuonRun2023BPixD02":SingleMuonRun2023BPixD02,
#     "SingleMuonRun2023BPixD11":SingleMuonRun2023BPixD11,
#     "SingleMuonRun2023BPixD12":SingleMuonRun2023BPixD12,
#     # Add 2024 and 2025 data in here
# }

samples_mc_test = {
    "BpBp_M1200_2024": BpBp_M1200_2024 ,
    "BpBp_M1400_2024": BpBp_M1400_2024 ,
    "BpBp_M1500_2024": BpBp_M1500_2024 ,
    "BpBp_M1600_2024": BpBp_M1600_2024 ,
    "BpBp_M1700_2024": BpBp_M1700_2024 ,
    "BpBp_M1800_2024": BpBp_M1800_2024 ,
    "BpBp_M1900_2024": BpBp_M1900_2024 ,
    "BpBp_M2000_2024": BpBp_M2000_2024 ,
    "BpBp_M2100_2024": BpBp_M2100_2024 ,
    "BpBp_M2200_2024": BpBp_M2200_2024 ,

    "TpTp_M1200_2024": TpTp_M1200_2024 ,
    "TpTp_M1300_2024": TpTp_M1300_2024 ,
    "TpTp_M1400_2024": TpTp_M1400_2024 ,
    "TpTp_M1600_2024": TpTp_M1600_2024 ,
    "TpTp_M1700_2024": TpTp_M1700_2024 ,
    "TpTp_M1800_2024": TpTp_M1800_2024 ,
    "TpTp_M1900_2024": TpTp_M1900_2024 ,
    "TpTp_M2000_2024": TpTp_M2000_2024 ,
    "TpTp_M2100_2024": TpTp_M2100_2024 ,
    "TpTp_M2200_2024": TpTp_M2200_2024 ,
}

samples_mc_standard_22_23 = {
    

    }
