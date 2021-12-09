import os

import SimpleITK as sitk

# image1 = '/home/sjy/nnUNetFrame/DATASET/nnUNet_raw/nnUNet_raw_data/Task500_Oct/imagesTr/oct_8 Jul 2021 02-12-10_0_0000.nii.gz'
# outpath = '/home/sjy/Documents/test/'
# image = sitk.ReadImage(image1)

image_path = '/home/sjy/Documents/data/imagesTr'
label_path = '/home/sjy/Documents/data/labelsTr'
image_out_path = '/nvme/nnUNetFrame/DATASET/nnUNet_raw/nnUNet_raw_data/Task504_Oct/imagesTr/'
label_out_path = '/nvme/nnUNetFrame/DATASET/nnUNet_raw/nnUNet_raw_data/Task504_Oct/labelsTr/'


def cropping_image(img):
    print(img.GetWidth())
    crop_img = sitk.RegionOfInterest(
        img,  # 輸入影像
        [int(0.317 * img.GetWidth()), int(0.317 * img.GetWidth()), 1],
        [int(0.341 * img.GetWidth()), 1, 0]
    )

    crop_img.SetSpacing((1, 1, 2))
    crop_img.SetOrigin((int(0.5 * img.GetWidth()), 0, 0))

    return crop_img


if __name__ == '__main__':

    for one_image in os.listdir(image_path):
        print(one_image)
        one_image_path = os.path.join(image_path, one_image)
        image = sitk.ReadImage(one_image_path)
        out_image = cropping_image(image)
        sitk.WriteImage(out_image, image_out_path + one_image)

    for one_label in os.listdir(label_path):
        print(one_label)
        one_label_path = os.path.join(label_path, one_label)
        label = sitk.ReadImage(one_label_path)
        out_label = cropping_image(label)
        sitk.WriteImage(out_label, label_out_path + one_label)
