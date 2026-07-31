# Status Post Summer 2026
This file represents the status of the analysis as of July 31st 2026. It details where everything is, and the state of each task. Please reach out to Cai Hallstrom or Hannah Larson with any questions

## Tagging Choices
After comparing GloParT, GloparT (mass decorrelated), and Particle Net, we settled on Particle Net as our tagger of choice. It produced better confusion matrices and efficiency plots. (INSERT PERCENTAGES HERE) In particular, it was better at differentiating Z and H. Some small gains were also seen in top and W tagging. Efficiency plots and confusion matrices can be found in the following slides:

https://docs.google.com/presentation/d/1mkyUKc2I7PPUdAj0iE9kDBNA6DQcaAXOhFlHIOU379c/edit?slide=id.g3f6109fab66_0_15#slide=id.g3f6109fab66_0_15

Additional confusion matrices can be found at /uscms_data/d1/cai/run3VLQ/TIMBER/cMatrices

## Confusion Matrix Scripts
The cMatrices folder contains several python scripts designed to generate confusion matrices for different purposes. 

confusionPlots.py is the most basic. It compares the tags from a neural network to the truth, which are obtained using the functions in TIMBER/TIMBER/framework/Tprim1lep/StandardTT_fatjet_matching.cc

decayModeConMats.py and RJRdecayModeConMats.py are for comparing reconstructed decay modes to the true decay modes. True decay modes are determined using the newDecayModeSelection function in Standard_TTBBdecayModeFinder.cc. 

abcTesting.py was used for optimizing GloParT. Congqiao suggested weighting each ratio in order to account for discrepancies in training volume. This script iterates over values of a, b, and c, creating a confusion matrix for each one and taking the off diagonal Frobenius norm as a measure of how "good" the matrix is. The best weights are then saved and used to produce a final confusion matrix.

PNWMtesting.py and truthComp.py are left over from when we compared our code with that of a grad student. truthComp.py compares our respective truth findings, while PNWMtesting.py compares our Particle Net tags.

## Efficiency Plots
BattleOfTaggers/BOTPlots.py will need to be edited by hand if we need to rerun it. You can do either efficiency of taggers at a certain mass (mass) or effeciency of one tagger at all masses (algo). This can be changed by hand. Also there are two functions, one to generate the root files(creatRootFiles), and one to create the plots(plotEff). If you have the root files, you dont need to create them new everytime, you can just run the plotting script. 

## Reconstructions
Over the summer, we worked on three separate methods of reconstructing the events.

### Manual Reconstruction
The manual reconstruction functions are found in eventReco.cc. Do not confuse this with manualreco.cc. That is a file from an older analysis, and it will not work. This reconstruction is running quite smoothly, and shouldn't require any work. There are two things to take note of: First, rather than using pdg Ids, the manual reco recasts them to 0-5 in this order: J, t, H, Z, W, b. This makes the code much simpler. Second, the manual reco returns the full and partial T prime decay modes as 0-9 in this order: bWbW, tZtZ, tHtH, tZtH, tZbW, tHbW, tZ, tH, bW. The same order is used for their Bprime analogs.

### Recursive Jigsaw Reconstruction (RJR)
Firstly, RJR_decayModes (in TIMBER/TIMBER/bin/restframes/helper.cc) currently DOES NOT WORK. It runs quietly, but every decay gets assigned to -1. Someone will need to go in and fix this at some point.

RJR reconstruction has had some issues. Currently there are 6 different TIMBER/bin/restframes/Tprime_handler functions, split evenly between t and W decay modes. Currently the Tprime_handler_(t/W).cc works, and should be regarded as the working function. It had plotted a nice peak, but a couples changes happened before we caught that the peak had shifted from the right side of the curve to the left side. The commit that induced these changes was when we added four vector information about the t and W quarks to the return statement. I'm not sure why or how this happened, but it might be worth trying to implement the four vector information again to see if/how it changes the plotting again. 

The other functions currently cannot be evaluated, as they were based off of the script that produced shifted plots. Grace Cummings suggested taking the idx for J0, VLQ1, and VLQ2 produced by the manual reconstruction, and feeding those into the RJR script to replace the combinatorics group in RJR. Tprime_handler_(t/W)man.cc was supposed to accomplish this. Tprime_handler(t/W)_noComb.cc was supposed to test if RJR was even using the cambanatorics group. When we ran plain RJR, we found that the order we passed the jets into the function mattered in terms of which AK8 jet was assigned to J0. This is odd, as RJR is supposed to be looping over the jets to find which combination makes the best fit. Because of the 'hard coding', I believe the combanatorics group and/or the jets jigsaw isn't working correctly, and I think it would be worth testing out an RJR that doesnt use them, btu everything else is the same. We still manually check for the min VLQ mass difference, we still have the jigsaws in place for the invisible group, but test it without any JETS rules. I think this is worth checking if there is time.

### SPANet
Reconstruction using SPANet is still in the early stages. The example github and paper are linked here, along with a helpful online h5 viewer:

https://github.com/Alexanders101/SPANet/blob/master/README.md

https://arxiv.org/pdf/2106.03898

https://myhdf5.hdfgroup.org/

A clone of this github with some preliminary work for our analysis can be found at uscms_data/d1/cai/run3VLQ/SPANetTesting/SPANet. It keeps their examples intact and contains the necessary setup for our analysis, labeled as single_lepton_VLQ. Our git repo contains Tprime1lepSPANet.py, a slimmed TIMBER script, and h5Builder.py. These two scripts create a ROOT file and then convert it to the h5 format required by SPANet. They use slightly modified functions found in SPANet_functions.cc.

Currently, when attempting to train SPANet on one of our created h5 files, it crashes with a collision error. This supposedly occurs because two targets are trying to claim the same jet, or because of some issue with how the input file is formatted. We have not been successful in solving it.

## Elastic Analysis Facility
In order to efficiently train SPANet, GPU access is required. Instructions for accessing the EAF can be found at this link:

https://eafdocs.fnal.gov/master/03_proxy.html

Once starting your server, select the CMS option to ensure that your files are accessible.
