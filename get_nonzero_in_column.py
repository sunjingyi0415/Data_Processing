import cv2


# file_path = '/nvme/raw_png1/oct_1 Nov 2021 02-27-52_0.png'


def get_nonzero_in_column(path):
    img = cv2.imread(path)
    column = img[:, 1]
    for i in range(len(column)):
        a = column[i + 1] - column[i]
        if a.any() != 0:
            crop_down = i + 1
            break
    crop_left = int((img.shape[1] - crop_down + 1) / 2)
    crop_up = 1
    crop_right = crop_left + crop_down
    return crop_up, crop_left, crop_down, crop_right


if __name__ == '__main__':
    a, b, c, d = get_nonzero_in_column(file_path)
