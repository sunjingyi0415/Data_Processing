import os

import SimpleITK as sitk

from get_nonzero_in_column import get_nonzero_in_column


def cropping_nonzero1(image, file_path):
    u, l, d, r = get_nonzero_in_column(file_path)
    print(r - l, d - u)
    crop_img = sitk.Crop(
        image,  # 輸入影像
        [l, u, 0],
        [image.GetWidth() - r, image.GetHeight() - d, 0]  # 下方去除寬度
    )  # 上方去除寬度
    return crop_img


nii_dir = '/home/sjy/Documents/base_data/nii'
niis = os.listdir(nii_dir)
for nii in niis:
    png_name = nii.rstrip("avi_Label.nii.gz")
    png_path = os.path.join('/nvme/raw_png0', png_name + '_0.png')
    nii_path = os.path.join(nii_dir, nii)
    print(png_name)
    itk_img = sitk.ReadImage(nii_path)
    itk_nii = cropping_nonzero1(itk_img, png_path)
    print(itk_nii.GetWidth(), itk_nii.GetHeight())
    sitk.WriteImage(itk_nii, '/home/sjy/Documents/base_data/nii_croped/' + nii)
