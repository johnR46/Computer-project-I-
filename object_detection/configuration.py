'''
Object Detection        https://github.com/tensorflow/models/tree/master/research/object_detection
Protocol Buffers        https://github.com/google/protobuf/releases
Microsoft Visual C++    https://www.microsoft.com/en-US/download/details.aspx?id=52685
Sentdex                 https://pythonprogramming.net/introduction-use-tensorflow-object-detection-api-tutorial

beginners               https://www.datacamp.com/community/tutorials/tensorflow-tutorial
build Tools             http://landinghub.visualstudio.com/visual-cpp-build-tools


"C:/Users/THID/cep3/bin/protoc" object_detection/protos/*.proto --python_out=.
export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim

pip install pyqt5
cd labelImg
pyrcc5 -o resources.py resources.qrc
python labelImg.py

'''

import os
import shutil
import zipfile

# list of needed zip files.
exited_zips = {
    'object_detection.zip' : False,
    'protoc-3.5.0-win32.zip' : False,
    'ssd_mobilenet_v1_coco_2017_11_17.zip' : False
}
# check needed zip files.
for key, value in exited_zips.items() :
    exited_zips[key] = os.path.isfile(key)
# if needed zip files exited then extract needed zip files.
if all(exited_zips.values()) :
    for key, value in exited_zips.items():
        if key.endswith('zip') :
            zip = zipfile.ZipFile(key)  
            zip.extractall()
            zip.close()
            os.remove(key)

# list of needed directories.
excited_directories = {
    'modification/outputed_pictures' : False,
    'modification/outputed_videos' : False,
    'modification/zoo' : False,
}
# if needed directories exited then delate it and creact it else creact.
for key, value in excited_directories.items() :
    if os.path.isdir(key) :
        shutil.rmtree(key)
        os.makedirs(key)
    else:
        os.makedirs(key)

# delet unuse files or unuse directories
unuse_files = []
unuse_directories = []
for value in unuse_files:
    os.remove(value)
for value in unuse_directories:
    shutil.rmtree(value)

# move directory 
# shutil.move('current_dir', 'new_dir')
shutil.move('modification/inputed_pictures', 'object_detection/inputed_pictures')
shutil.move('modification/inputed_videos', 'object_detection/inputed_videos')
shutil.move('modification/outputed_pictures', 'object_detection/outputed_pictures')
shutil.move('modification/outputed_videos', 'object_detection/outputed_videos')
shutil.move('modification/zoo', 'object_detection/zoo')
shutil.move('ssd_mobilenet_v1_coco_2017_11_17', 'object_detection/zoo/ssd_mobilenet_v1_coco_2017_11_17')
shutil.move('modification/label_map_util.py', 'object_detection/utils/label_map_util.py')

shutil.move('modification/od_picture.py', 'object_detection/od_picture.py')
shutil.move('modification/od_video.py', 'object_detection/od_video.py')
shutil.move('modification/visualization_utils.py', 'object_detection/utils/visualization_utils.py')

# delete directores and files.
try:
    shutil.rmtree('modification')
    os.remove('readme.txt')
    os.remove('object_detection/object_detection_tutorial.ipynb')
except OSError:
    pass