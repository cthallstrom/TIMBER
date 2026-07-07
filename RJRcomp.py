import ROOT

def reco_split_truth(file_path, tree_name, branch_a, branch_b):
    # Enable multi-threading for faster processing of large HEP datasets
    ROOT.EnableImplicitMT()
    
    print(f"Opening ROOT File: {file_path}")
    print(f"Targeting TTree: {tree_name}")
    
    # 1. Load the Tree into an RDataFrame
    df = ROOT.RDataFrame(tree_name, file_path)
    
    # 3. Book Histograms automatically optimized for the data ranges
    # (Min/Max operations can be used, but ROOT determines a clean bin range automatically here)
    hist_a = df.Filter("decayFinds[0] == 1").Histo1D((f"lepW_{branch_a}", f"reco_{branch_a};{branch_a};Events", 100, 0, 0), branch_a)
    hist_b = df.Filter("decayFinds[0]==2 || decayFinds[0]==3 || decayFinds[0]==4").Histo1D((f"lepT_{branch_b}", f"{branch_a};Value;Events", 100, 0, 0), branch_b)
    
    # 4. Draw and Style the comparison using a TCanvas
    canvas = ROOT.TCanvas("canvas", "W vs. T comparison", 800, 600)
    ROOT.gStyle.SetOptStat(0) # Hide standard stat box for overlay clarity
    
    # Style Branch A (Red)
    hist_a.SetLineColor(ROOT.kRed + 1)
    hist_a.SetLineWidth(3)
    hist_a.Draw("HIST")
    
    # Style Branch B (Blue)
    hist_b.SetLineColor(ROOT.kBlue + 1)
    hist_b.SetLineWidth(2)
    hist_b.Draw("HIST SAME") # 'SAME' overlays it on the previous histogram
    
    # Adjust Y-axis scale so both fits fit nicely
    max_y = max(hist_a.GetMaximum(), hist_b.GetMaximum())
    hist_a.GetYaxis().SetRangeUser(0, max_y * 1.1)

    canvas.Modified()
    canvas.Update()
    
    # Add a Legend
    legend = ROOT.TLegend(0.7, 0.75, 0.9, 0.9)
    legend.AddEntry(hist_a.GetPtr(), f"lepW", "l")
    legend.AddEntry(hist_b.GetPtr(), f"lepT", "l")
    legend.Draw()
    
    # Save the plot comparison as an image
    canvas.SaveAs(f"RJRcomparisons/{branch_a}.png")
    print("\n🟢 Plot saved successfully as 'branch_comparison.png'")

def Wtruth_split_reco(file_path, tree_name, branch_a, branch_b):
    # Enable multi-threading for faster processing of large HEP datasets
    ROOT.EnableImplicitMT()
    
    print(f"Opening ROOT File: {file_path}")
    print(f"Targeting TTree: {tree_name}")
    
    # 1. Load the Tree into an RDataFrame
    df = ROOT.RDataFrame(tree_name, file_path)
    
    # 3. Book Histograms automatically optimized for the data ranges
    # (Min/Max operations can be used, but ROOT determines a clean bin range automatically here)
    hist_a = df.Filter("lepton_source == 0").Histo1D((f"lepW_{branch_a}", f"isW_{branch_a};{branch_a};Events", 100, 0, 0), branch_a)
    hist_b = df.Filter("lepton_source == 0").Histo1D((f"lepT_{branch_b}", f"{branch_b};Value;Events", 100, 0, 0), branch_b)
    
    # 4. Draw and Style the comparison using a TCanvas
    canvas = ROOT.TCanvas("canvas", "W vs. T comparison", 800, 600)
    ROOT.gStyle.SetOptStat(0) # Hide standard stat box for overlay clarity
    
    # Style Branch A (Red)
    hist_a.SetLineColor(ROOT.kRed + 1)
    hist_a.SetLineWidth(3)
    hist_a.Draw("HIST")
    
    # Style Branch B (Blue)
    hist_b.SetLineColor(ROOT.kBlue + 1)
    hist_b.SetLineWidth(2)
    hist_b.Draw("HIST SAME") # 'SAME' overlays it on the previous histogram
    
    # Adjust Y-axis scale so both fits fit nicely
    max_y = max(hist_a.GetMaximum(), hist_b.GetMaximum())
    hist_a.GetYaxis().SetRangeUser(0, max_y * 1.1)

    canvas.Modified()
    canvas.Update()
    
    # Add a Legend
    legend = ROOT.TLegend(0.7, 0.75, 0.9, 0.9)
    legend.AddEntry(hist_a.GetPtr(), f"lepW", "l")
    legend.AddEntry(hist_b.GetPtr(), f"lepT", "l")
    legend.Draw()
    
    # Save the plot comparison as an image
    canvas.SaveAs(f"RJRcomparisons/isW_{branch_a}.png")
    print("\n🟢 Plot saved successfully as 'branch_comparison.png'")

def Ttruth_split_reco(file_path, tree_name, branch_a, branch_b):
    # Enable multi-threading for faster processing of large HEP datasets
    ROOT.EnableImplicitMT()
    
    print(f"Opening ROOT File: {file_path}")
    print(f"Targeting TTree: {tree_name}")
    
    # 1. Load the Tree into an RDataFrame
    df = ROOT.RDataFrame(tree_name, file_path)
    
    # 3. Book Histograms automatically optimized for the data ranges
    # (Min/Max operations can be used, but ROOT determines a clean bin range automatically here)
    hist_a = df.Filter("lepton_source == 1").Histo1D((f"lepW_{branch_a}", f"isT_{branch_a};{branch_a};Events", 100, 0, 0), branch_a)
    hist_b = df.Filter("lepton_source == 1").Histo1D((f"lepT_{branch_b}", f"{branch_b};Value;Events", 100, 0, 0), branch_b)
    
    # 4. Draw and Style the comparison using a TCanvas
    canvas = ROOT.TCanvas("canvas", "W vs. T comparison", 800, 600)
    ROOT.gStyle.SetOptStat(0) # Hide standard stat box for overlay clarity
    
    # Style Branch A (Red)
    hist_a.SetLineColor(ROOT.kRed + 1)
    hist_a.SetLineWidth(3)
    hist_a.Draw("HIST")
    
    # Style Branch B (Blue)
    hist_b.SetLineColor(ROOT.kBlue + 1)
    hist_b.SetLineWidth(2)
    hist_b.Draw("HIST SAME") # 'SAME' overlays it on the previous histogram
    
    # Adjust Y-axis scale so both fits fit nicely
    max_y = max(hist_a.GetMaximum(), hist_b.GetMaximum())
    hist_a.GetYaxis().SetRangeUser(0, max_y * 1.1)

    canvas.Modified()
    canvas.Update()
    
    # Add a Legend
    legend = ROOT.TLegend(0.7, 0.75, 0.9, 0.9)
    legend.AddEntry(hist_a.GetPtr(), f"lepW", "l")
    legend.AddEntry(hist_b.GetPtr(), f"lepT", "l")
    legend.Draw()
    
    # Save the plot comparison as an image
    canvas.SaveAs(f"RJRcomparisons/isT_{branch_a}.png")
    print("\n🟢 Plot saved successfully as 'branch_comparison.png'")


# Three mode options:1, 2, 3
# 1: plots reconstructed as W and T, splitting by isW and isT
# 2: plots isW, splitting by reco W and reco T
# 3: plots isT, splitting by reco W and reco T
mode = 1

if mode == 1:
    file = open("RJR_branches.txt", 'r')
    for line in file: 
        # --- CHANGE THESE STRINGS TO MATCH YOUR ROOT FILE SPECIFICS ---
        FILE_PATH = "RDF_TprimeTprime_Par-M-1700_TuneCP5_13p6TeV_amcatnlo-pythia8_2024_0.root"
        TREE_NAME = "Events_Nominal"
        BRANCH_1 = line.strip()
        BRANCH_2 = line.strip()
        
        try:
            reco_split_truth(FILE_PATH, TREE_NAME, BRANCH_1, BRANCH_2)
        except Exception as e:
            print(f"\nAn error occurred. Check if PyROOT is sourced properly. Error details:\n{e}")

if mode == 2:
    file1 = open("W_RJR_branches.txt", 'r')
    file2 = open("t_RJR_branches.txt", 'r')

    lines1 = []
    lines2 = []

    for line in file1:
        lines1.append(line)
    
    for line in file2:
        lines2.append(line)

    for i in range(len(lines1)): 
        # --- CHANGE THESE STRINGS TO MATCH YOUR ROOT FILE SPECIFICS ---
        FILE_PATH = "RDF_TprimeTprime_Par-M-1700_TuneCP5_13p6TeV_amcatnlo-pythia8_2024_0.root"
        TREE_NAME = "Events_Nominal"
        BRANCH_1 = lines1[i].strip()
        BRANCH_2 = lines2[i].strip()
        
        try:
            Wtruth_split_reco(FILE_PATH, TREE_NAME, BRANCH_1, BRANCH_2)
        except Exception as e:
            print(f"\nAn error occurred. Check if PyROOT is sourced properly. Error details:\n{e}")

if mode == 3:
    file1 = open("W_RJR_branches.txt", 'r')
    file2 = open("t_RJR_branches.txt", 'r')

    lines1 = []
    lines2 = []

    for line in file1:
        lines1.append(line)
    
    for line in file2:
        lines2.append(line)

    for i in range(len(lines1)): 
        # --- CHANGE THESE STRINGS TO MATCH YOUR ROOT FILE SPECIFICS ---
        FILE_PATH = "RDF_TprimeTprime_Par-M-1700_TuneCP5_13p6TeV_amcatnlo-pythia8_2024_0.root"
        TREE_NAME = "Events_Nominal"
        BRANCH_1 = lines1[i].strip()
        BRANCH_2 = lines2[i].strip()
        
        try:
            Ttruth_split_reco(FILE_PATH, TREE_NAME, BRANCH_1, BRANCH_2)
        except Exception as e:
            print(f"\nAn error occurred. Check if PyROOT is sourced properly. Error details:\n{e}")

else:
    print("Invalid mode, try again")