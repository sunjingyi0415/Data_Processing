import os

import SimpleITK as sitk

from annotations_in_json import annotations_in_json

tr_json_dir = '/nvme/json/train'
ts_json_dir = '/nvme/json/test'
nifti_dir = '/home/sjy/Documents/base_data/nii_croped'
tr_out_dir = '/nvme/nnUNetFrame/DATASET/nnUNet_raw/nnUNet_raw_data/Task505_Oct/labelsTr'
ts_out_dir = '/nvme/nnUNetFrame/DATASET/nnUNet_raw/nnUNet_raw_data/Task505_Oct/labelsTs'


def extract_labeled_slice(nifti_data, anotations, name, out_nii_dir):  # file_name
    for i in anotations:
        file_dir = os.path.join(out_nii_dir, name + str(i) + ".nii.gz")
        label_data_3d = nifti_data[i][None, :, :]
        out = sitk.GetImageFromArray(label_data_3d)
        sitk.WriteImage(out, file_dir)


def read_img(path):
    img = sitk.ReadImage(path)
    data = sitk.GetArrayFromImage(img)
    return data


def converse(json_dir, out_dir):
    jsons = os.listdir(json_dir)
    for json in jsons:
        json_path = os.path.join(json_dir, json)
        anots, name_ = annotations_in_json(json_path)

        nifti_path = os.path.join(nifti_dir, name_ + 'avi_Label.nii.gz')
        nifti_data = read_img(nifti_path)
        extract_labeled_slice(nifti_data, anots, name_, out_dir)


if __name__ == '__main__':
    # converse(tr_json_dir, tr_out_dir)
    converse(ts_json_dir, ts_out_dir)
