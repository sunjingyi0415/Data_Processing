import os

import SimpleITK as sitk
import cv2 as cv
import numpy as np
from scipy.ndimage import zoom


def creat_npz(image_dir, label_dir, save_dir):
    image_names = os.listdir(image_dir)
    num = 0
    for image_name in image_names:
        name = image_name.rstrip('.png')
        label_name = name + '.nii.gz'
        image_path = os.path.join(image_dir, image_name)
        label_path = os.path.join(label_dir, label_name)
        target_name = name + '.npz'
        save_path = os.path.join(save_dir, target_name)

        label_nii = sitk.ReadImage(label_path)
        label = sitk.GetArrayFromImage(label_nii).astype(np.int8)
        label[label == 4] = 0
        if label.sum() != 0:
            image = cv.imread(image_path)
            image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
            h, w = label.shape[0], label.shape[1]
            if label.shape != image.shape:
                label = zoom(label, (image.shape[0] / h, image.shape[1] / w), order=0)
            num = num + 1
            np.savez(save_path, image=image, label=label)
        print(name)
    print(num)


if __name__ == "__main__":
    tr_image_d = r"D:\first_set\tr_image"
    tr_label_d = r"D:\first_set\tr_label"
    save_dir = r"D:\TransUNet\data\oct\train_npz"

    ts_image_d = r"D:\first_set\ts_image"
    ts_label_d = r"D:\first_set\ts_label"
    save_dir = r"D:\TransUNet\data\oct\test_vol_h5"

    creat_npz(ts_image_d, ts_label_d, save_dir)
    # creat_npz(tr_image_d, tr_label_d, save_dir)
