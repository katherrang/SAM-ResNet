# NOTE: runs SAM ResNet algorithm then sorts output
# RUN THIS CODE IN ANACONDA ENVIRONMENT 'sam_environment':
# conda activate sam_environment
# cd C:/FULL-PATH-TO-WHERE-THIS-FILE-IS-LOCATED
# python runSAM.py

# SAM ResNet setup for windows: https://github.com/katherrang/SAM-ResNet-for-Dummies 
# SAM ResNet setup for mac: https://www.dropbox.com/scl/fi/9nek2ybdhdic6fdzfu0dm/SAM-Algorithm-Download-for-Mac.docx?dl=0&rlkey=siw197lspo3akb7ouolexksmf 

import os
import shutil
import glob

img_folder = "C:/FULL-PATH-TO-THE-FOLDER-WHERE-THE-IMAGES-TO-RUN-ARE-LOCATED"   # NOTE: this folder should only contain images
output_folder = 'example'   # NOTE: this will be the name of the subfolder where the images will be stored

# navigate to SAM folder
SAM_path = 'C:/toolkits.win/sam'    # NOTE: path where the SAM-ResNet algorithm is located
os.chdir(SAM_path)
print('Navigate to ' + os.getcwd())

# run SAM algorithm
os.system("python main.py test " + img_folder + "/")

# sort output
if not os.path.exists('predictions/'+output_folder):
    os.makedirs('predictions/'+output_folder)
else: # clear old files for clarity
    for f in glob.glob('predictions/'+output_folder+'/*'):
        os.remove(f)

img_filename = os.listdir(img_folder)
for f in img_filename: # move file to catagory folder
    shutil.move('predictions/'+f,'predictions/'+output_folder+'/'+f)

# save output to analysis folder
analysis_path = 'C:/Users/kchan/Documents/CCLAB/SAM'

if not os.path.exists(analysis_path + '/raw_output/' + output_folder):
    os.makedirs(analysis_path + '/raw_output/' + output_folder)
else: # clear old files for clarity
    for f in glob.glob(analysis_path + '/raw_output/' + output_folder+'/*'):
        os.remove(f)

for f in img_filename:
    shutil.copy('predictions/'+output_folder+'/'+f, analysis_path+'/raw_output/'+output_folder+'/'+f)

# save original image to analysis folder for reference
if not os.path.exists(analysis_path + '/original/' + output_folder):
    os.makedirs(analysis_path + '/original/' + output_folder)
else: # clear old files for clarity
    for f in glob.glob(analysis_path + '/original/' + output_folder+'/*'):
        os.remove(f)
for f in img_filename:
    shutil.copy(img_folder+'/'+f, analysis_path+'/original/'+output_folder+'/'+f)