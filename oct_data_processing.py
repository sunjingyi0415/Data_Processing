import glob
import os

import SimpleITK as sitk
import h5py
import numpy as np
from PIL import Image

'''
convert slices to 2D h5py
'''

slice_num = 0
image_path = sorted(glob.glob("/nvme/data/raw_ts_png/*.png"))
for case in image_path:
    image = np.array(Image.open(case))
    name = case.split('/')[-1].rsplit('.', 1)[0]
    msk_path = os.path.join("/nvme/data/labels", name + ".nii.gz")  # label路径
    if os.path.exists(msk_path):
        print(msk_path)
        msk_itk = sitk.ReadImage(msk_path)
        mask = sitk.GetArrayFromImage(msk_itk)[0]
        image = image.astype(np.float32)
        image1 = (image - image.min()) / (image.max() - image.min())  # 归一化
        print(image1.shape)
        # mask = mask.astype(np.float32)
        if image1.shape[0] != mask.shape[0]:
            print("Error", mask.shape)
        print(name)

        f = h5py.File('/nvme/data/ts_h5/{}.h5'.format(name), 'w')
        f.create_dataset('image', data=image1[0], compression="gzip")
        f.create_dataset('label', data=mask[0], compression="gzip")
        f.close()
        slice_num += 1

print("Converted all Oct volumes to 2D slices")
print("Total {} slices".format(slice_num))
