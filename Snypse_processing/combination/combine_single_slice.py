import os
import shutil

import SimpleITK as sitk
import numpy as np


path1 = r'D:\pycharm_project\oct_data\combination\oct_1 Nov 2021 02-27-52_avi_Label.nii.gz'
path2 = r'D:\pycharm_project\oct_data\combination\oct_9 Jul 2021 04-49-47_avi_Label.nii.gz'


def combine_single_case(path1, path2, class_num=4):
    msk1 = sitk.ReadImage(path1)
    mask1 = sitk.GetArrayFromImage(msk1)
    msk2 = sitk.ReadImage(path2)
    mask2 = sitk.GetArrayFromImage(msk2)
    mask = np.zeros_like(mask1)
    for i in range(1, class_num):
        mask1_bool = (mask1 == i)
        mask2_bool = (mask2 == i)
        msk = np.array(mask1_bool | mask2_bool)
        msk_tmp = msk.astype(np.int)
        mask_temp = msk * i
        mask = mask + mask_temp
    out = sitk.GetImageFromArray(mask)
    sitk.WriteImage(out, r'D:\pycharm_project\data\label_nii\3.nii.gz')


def combination(dir1, dir2):
    file_list1 = os.listdir(dir1)
    file_list2 = os.listdir(dir2)
    file_list1.sort()
    file_list2.sort()

    f1_difference = set(file_list1).difference(set(file_list2))
    f2_difference = set(file_list2).difference(set(file_list1))

    for difference in f1_difference:
        target_dir = r'D:\pycharm_project\oct_data\combination\seg_merge'
        src1 = os.path.join(dir1, difference)
        shutil.copyfile(src1, target_dir)

    for difference in f2_difference:
        target_dir = r'D:\pycharm_project\oct_data\combination\seg_merge'
        src2 = os.path.join(dir2, difference)
        shutil.copyfile(src2, target_dir)


if __name__ == '__main__':
    dir1 = r'D:\pycharm_project\oct_data\combination\long'
    dir2 = r'D:\pycharm_project\oct_data\combination\song'
#    os.makedirs(r'D:\pycharm_project\oct_data\combination\seg_merge', mode=0o777)
 #   combination(dir1, dir2)
    combine_single_case(path1, path2)

    #base_dir = r'D:\pycharm_project\oct_data\combination'