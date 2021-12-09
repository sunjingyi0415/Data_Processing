import os
import shutil

import numpy as np

labels_dir = '/nvme/nnUNetFrame/DATASET/nnUNet_raw/nnUNet_raw_data/Task504_Oct/labels/'


def select_testcase(lab_dir):
    np.random.seed(3)
    ran = np.random.choice(1478, 300, replace=False)
    labels = os.listdir(lab_dir)
    labels.sort()
    for i in range(1479):
        source_lab = os.path.join(lab_dir, labels[i])
        ts_lab = source_lab.replace('labels', 'labelsTs')
        tr_lab = source_lab.replace('labels', 'labelsTr')

        if i in ran:
            shutil.copy(source_lab, ts_lab)
            a = 1
        else:
            shutil.copy(source_lab, tr_lab)
            a = 0

        for k in range(3):
            source_img = os.path.join(source_lab.split('.')[0].replace('labels', 'images')
                                      + '_000' + str(k) + '.nii.gz')
            ts_img = source_img.replace('images', 'imagesTs')
            tr_img = source_img.replace('images', 'imagesTr')
            if i in ran:
                shutil.copy(source_img, ts_img)
            else:
                shutil.copy(source_img, tr_img)

        '''
        for k in range(3):
            old = os.path.join(img_dir, images[3 * i + k])
            new = old.replace('imagesTr', 'imagesTs')
            shutil.move(old, new)
        image = os.path.join(img_dir, images[3 * i])
        old1 = image.replace('_0000', '').replace('imagesTr', 'labelsTr')
        new1 = old1.replace('labelsTr', 'labelsTs')
        shutil.move(old1, new1)
'''


if __name__ == '__main__':
    select_testcase(labels_dir)
