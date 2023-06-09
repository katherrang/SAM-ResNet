# SAM-ResNet

FOLDERS -------------------------------:

original - contains folders containing the original images

raw_output - contains folders containing the SAM-ResNet raw output for each images

overlay - contains folders containing the heatmap visualization of the SAM-ResNet output over the original images

summary - contains folders containing the summary figure for each image containing: (1) the original image, (2) the raw SAM-ResNet output, and (3) the overlay visualization


SCRIPTS -------------------------------:

runSAM.py - runs SAM algorithm, sorts SAM raw outputs, copies original img to 'original/output_folder' and raw outputs to 'raw_output/output_folder'. RUN FIRST 

generateHeatmap.m - generates heatmap overlay img to 'overlay/output_folder' and summary img to 'summary/output_folder'


RUNNING ORDER -------------------------:
1. runSAM.py
2. generateHeatmap.m

NOTE: make sure that output_folder name is consistent for both scripts

OTHER HELPFUL LINKS -------------------:

SAM ResNet setup for windows: https://github.com/katherrang/SAM-ResNet-for-Dummies 
SAM ResNet setup for mac: https://www.dropbox.com/scl/fi/9nek2ybdhdic6fdzfu0dm/SAM-Algorithm-Download-for-Mac.docx?dl=0&rlkey=siw197lspo3akb7ouolexksmf 
