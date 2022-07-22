encoding = 'UTF-8'
import os

import SimpleITK as sitk
import cv2 as cv

from annotations_in_json import annotations_in_json

'''
jsons_dir = '/home/sjy/Documents/base_data/json/'
video_tr_dir = '/nvme/data/video_45/train_with_low_resolution/'
video_ts_dir = '/nvme/data/video_45/test/'
test_dir = '/nvme/data/raw_ts_png/'
train_dir = '/nvme/data/raw_tr_png/'
'''
jsons_dir = r'D:\first_set\files'
video_tr_dir = r'D:\first_set\videos\train'
video_ts_dir = r'D:\first_set\videos\test'
test_dir = "D:\\first_set\\ts_image\\"
train_dir = "D:\\first_set\\tr_image\\"
label_dir = "D:\\first_set\\files\\"
label_tr_dir = "D:\\first_set\\tr_label\\"
label_ts_dir = "D:\\first_set\\ts_label\\"


def video2pngs(annotations, file_name, video_path, save_dir):
    idx = 0
    video = cv.VideoCapture(video_path)

    max = int(video.get(7))
    for i in range(max):
        ret, frame = video.read()
        size = frame.shape[:2]
        if i in annotations:
            u, l, d, r = get_nonzero_area(frame)
            cropped_frame = frame[u:d, l:r]
            cv.imwrite(save_dir + file_name + str(i) + '.png', cropped_frame)
            idx = idx + 1
    print("{} labeled images in {}".format(idx, video_path))
    return u, l, d, r, size


def get_nonzero_area(img):
    column = img[:, 0]
    for i in range(len(column)):
        a = column[i + 1] - column[i]
        if a.any() != 0:
            crop_down = i + 1
            break
    crop_left = int((img.shape[1] - crop_down + 1) / 2)
    crop_up = 1
    crop_right = crop_left + crop_down
    return crop_up, crop_left, crop_down, crop_right


def get_images_from_videos(source_dir, target_dir, save_label_dir):
    num = 0
    num_v = 0
    for file in os.listdir(source_dir):
        json_name = file.replace('.avi', '_avi_Label.json')
        json_path = os.path.join(jsons_dir, json_name)
        video_path = os.path.join(source_dir, file)
        anots, name = annotations_in_json(json_path)
        num = num + len(anots)
        num_v = num_v + 1
        u, l, d, r, size = video2pngs(anots, name, video_path, target_dir)
        get_slices_from_volumes(file, anots, save_label_dir, u, l, d, r, size)
    print("\n {} images converted".format(num))


def get_slices_from_volumes(file, anots, save_label_dir, u, l, d, r, size_2d):
    label_name = file.replace('.avi', '_avi_Label.nii.gz')
    label_path = os.path.join(label_dir, label_name)
    label = sitk.ReadImage(label_path)
    lab = sitk.GetArrayFromImage(label)
    name = file.rstrip('.avi')
    for i in anots:
        file_path = os.path.join(save_label_dir, name + '_' + str(i) + ".nii.gz")
        label_data = lab[i, :, :]
        h, w = label_data.shape
        if (h, w) != size_2d:
            h, w = size_2d
            label_data = cv.resize(label_data, (w, h), interpolation=cv.INTER_NEAREST)
        cropped_label_data = label_data[u:d, l:r]
        if cropped_label_data.sum() == 0:
            print(name, 'error')
        out = sitk.GetImageFromArray(cropped_label_data)
        sitk.WriteImage(out, file_path)


if __name__ == '__main__':
    get_images_from_videos(video_tr_dir, train_dir, label_tr_dir)
    # get_images_from_videos(video_ts_dir, test_dir, label_ts_dir)
