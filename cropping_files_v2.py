import os

import cv2 as cv

from get_nonzero_in_column import get_nonzero_in_column

img_dir = '/nvme/raw_png1'
out_dir = '/nvme/cropped_png1/'


def cropping_image_v2(img_path):
    img = cv.imread(img_path)
    u, l, d, r = get_nonzero_in_column(img_path)
    return img[u:d, l:r]


if __name__ == '__main__':
    imgs = os.listdir(img_dir)
    for img in imgs:
        img_path = os.path.join(img_dir, img)
        cropped_img = cropping_image_v2(img_path)
        cv.imwrite(out_dir + img, cropped_img)
