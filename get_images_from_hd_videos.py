import os
import cv2 as cv
from annotations_in_json import annotations_in_json
import SimpleITK as sitk
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
jsons_dir = '/nvme/data/first_set/song_json/'
video_tr_dir = '/nvme/data/video_45/train_with_low_resolution/'
video_ts_dir = '/nvme/data/video_45/test/'
test_dir = '/nvme/data/song_ts_png/'
train_dir = '/nvme/data/song_tr_png/'
label_dir = "/nvme/data/first_set/song_label"
label_tr_dir = "/nvme/data/song_tr_label/"
label_ts_dir = "/nvme/data/song_ts_label/"


def video2pngs(annotations, file_name, video_path, save_dir):
    idx = 0
    video = cv.VideoCapture(video_path)
    _, frm = video.read()
    u, l, d, r = get_nonzero_area(frm)
    video.release()

    video = cv.VideoCapture(video_path)
    max = int(video.get(7))
    for i in range(max):
        ret, frame = video.read()
        if i in annotations:
            cropped_frame = frame[u:d, l:r]
            cv.imwrite(save_dir + file_name + str(i) + '.png', cropped_frame)
            idx = idx + 1
    print("{} labeled images in {}".format(idx, video_path))
    return u, l, d, r


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


def get_files_from_videos(source_dir, target_dir, save_label_dir):
    num = 0
    for file in os.listdir(source_dir):
        json_name = file.replace('.avi', '_avi_Label.json')
        json_path = os.path.join(jsons_dir, json_name)
        video_path = os.path.join(source_dir, file)
        anots, name = annotations_in_json(json_path)
        num = num + len(anots)
        u, l, d, r = video2pngs(anots, name, video_path, target_dir)
        get_slices_from_volumes(file, anots, save_label_dir, u, l, d, r)
    print("\ngot {} images from {}".format(num, json_name))


def get_slices_from_volumes(file, anots, save_label_dir, u, l, d, r):
    label_name = file.replace('.avi', '_avi_Label.nii.gz')
    label_path = os.path.join(label_dir, label_name)
    label = sitk.ReadImage(label_path)
    lab = sitk.GetArrayFromImage(label)
    name = file.rstrip('.avi')
    for i in anots:
        file_path = os.path.join(save_label_dir, name + '_' + str(i) + ".nii.gz")
        label_data = lab[i][None, :, :]
        cropped_label_data = label_data[u - 1:d, l - 1:r]
        out = sitk.GetImageFromArray(cropped_label_data)
        sitk.WriteImage(out, file_path)


if __name__ == '__main__':
    get_files_from_videos(video_tr_dir, train_dir, label_tr_dir)
    get_files_from_videos(video_ts_dir, test_dir, label_ts_dir)
