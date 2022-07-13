import os
import shutil

import SimpleITK as sitk
import numpy as np


# path1 = r'D:\first_set\files\oct_8 Jul 2021 02-12-10_avi_Label.nii.gz'
# path2 = r'D:\first_set\files\oct_8 Jul 2021 02-23-44_avi_Label.nii.gz'


def combine_single_case(path1, path2, name, class_num=5):
    msk1 = sitk.ReadImage(path1)
    mask1 = sitk.GetArrayFromImage(msk1)
    msk2 = sitk.ReadImage(path2)
    mask2 = sitk.GetArrayFromImage(msk2)
    mask = np.empty_like(mask1)
    # mask_temp = np.empty_like(mask1[0])
    print(name)
    for sls in range(mask.shape[0]):
        if mask1[sls].sum() == 0 and mask2[sls].sum() == 0:
            continue
        #print(sls)
        for i in range(1, class_num):
            if mask1[sls].max() < i and mask2[sls].max() < i:
                break
            class_array = np.full_like(mask[0], i)
            #print(mask1[sls].max(), mask2[sls].max())
            msk1 = (mask1[sls] == class_array)
            msk2 = (mask2[sls] == class_array)
            mask_temp = msk1 | msk2
            mask[sls] = mask[sls] + mask_temp * i
            #print(i, mask[sls].max())
            mask[sls][mask[sls] > i] = i
    out = sitk.GetImageFromArray(mask)
    save_path = os.path.join(r'D:\pycharm_project\oct_data\combination\seg_merge1', name)
    sitk.WriteImage(out, save_path)


def combination(dir1, dir2):
    file_list1 = os.listdir(dir1)
    file_list2 = os.listdir(dir2)
    file_list1.sort()
    file_list2.sort()

    f1_difference = set(file_list1).difference(set(file_list2))
    f2_difference = set(file_list2).difference(set(file_list1))
    f_intersaction = set(file_list1).intersection(set(file_list2))

    for difference in f1_difference:
        target_dir = r'D:\pycharm_project\oct_data\combination\seg_merge_1'
        src1 = os.path.join(dir1, difference)
        shutil.copy(src1, target_dir)

    for difference in f2_difference:
        target_dir = r'D:\pycharm_project\oct_data\combination\seg_merge_1'
        src2 = os.path.join(dir2, difference)
        shutil.copy(src2, target_dir)

    for file in f_intersaction:
        path1 = os.path.join(dir1, file)
        path2 = os.path.join(dir2, file)
        combine_single_case(path1, path2, file, class_num=5)


if __name__ == '__main__':
    dir1 = r'D:\pycharm_project\oct_data\combination\long1'
    dir2 = r'D:\pycharm_project\oct_data\combination\song1'
    combination(dir1, dir2)