import commentjson
import json
import SimpleITK as sitk
import numpy as np


def delete34(nii_path):
    labs = sitk.ReadImage(nii_path)
    labs_array = sitk.GetArrayFromImage(labs)
    labs_array[labs_array == 3] = 0
    labs_array[labs_array == 4] = 0
    labsa = sitk.GetImageFromArray(labs_array)
    sitk.WriteImage(labsa, r'D:\pycharm_project\oct_data\combination\segmentation_25\oct_1 Nov 2021 02-27-52\oct_1 Nov 2021 02-27-52_avi_Label1.nii.gz')

    tag_list = []
    for i in range(labs_array.shape[0]):
        k = len(np.unique(labs_array[i, :, :]))
        if k > 1:
            tag_list.append(i)

    json_path = nii_path.replace('.nii.gz', '.json')
    path1 =  r'D:\pycharm_project\oct_data\combination\segmentation_25\oct_1 Nov 2021 02-27-52\oct_1 Nov 2021 02-27-52_avi_Label1.nii.gz'
    with open(path1, 'w+', encoding='utf8') as f:
        data = json.load(f)
        data["Models"]["PolygonModel"]["3"] = tag_list
        json.dumps(data, f)
        f.close()


if __name__ == "__main__":
    path = r'D:\pycharm_project\oct_data\combination\segmentation_25\oct_1 Nov 2021 02-27-52\oct_1 Nov 2021 02-27-52_avi_Label.nii.gz'
    delete34(path)