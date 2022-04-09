import json
import os
import cv2 as cv
import SimpleITK as sitk

from video2png import cutVideo, cutVideo4test

data_dir = "/home/sjy/Documents/data/"
json_dir = '/home/sjy/Documents/data/label/json/'
image_dir = '/home/sjy/Documents/data/png/'
videos_dir = '/home/sjy/Documents/data/video/'
label_dir = '/home/sjy/Documents/data/label/nifti/'
test_dir = '/home/sjy/Documents/data/video/test/'

out_nii_dir = '/home/sjy/nnUNetFrame/DATASET/nnUNet_raw/nnUNet_raw_data/Task500_pngtest/labelsTr/'

def get_labeled_info(jsonfile_name):
    annotation = json.load(open(jsonfile_name))
    slices = annotation["Models"]["PolygonModel"]["3"]
    return slices


def read_img(path):
    img = sitk.ReadImage(path)
    data = sitk.GetArrayFromImage(img)
    return data

def extract_labeled_slice(nifti_data, jsonfile, nifti_file_name):#file_name
    idx = 0
    for i in jsonfile:
        file_dir = os.path.join(out_nii_dir, nifti_file_name + '_' + str(idx) + ".nii.gz")
        label_data_3d = nifti_data[i][None, :, :]
        out = sitk.GetImageFromArray(label_data_3d)
        sitk.WriteImage(out, file_dir)
        idx = idx + 1


json_files = os.listdir(json_dir)
print(json_files)

for json_file in json_files:
    json_file_path = os.path.join(json_dir, json_file)
    la_idx = get_labeled_info(json_file_path)
    json_file_name = os.path.splitext(json_file)[0]
    file_name = json_file_name.rsplit('_', 2)[0]

    test_path = os.path.join(test_dir, file_name)



    video_path = os.path.join(videos_dir, file_name) + '.avi'
#    cutVideo4test(video_path, la_idx, test_path)
#    print(len(la_idx))
#    nifti_path = os.path.join(label_dir, file_name) + '_avi_Label.nii'
 #   nifti_data = read_img(nifti_path)
 #   extract_labeled_slice(nifti_data, la_idx, file_name)
'''
a = 0
for json_file in json_files:
    json_file_path = os.path.join(json_dir, json_file)
    la_idx = get_labeled_info(json_file_path)
    l=len(la_idx)
    a = a + l
print(a)
print(len(json_files))
'''