import os

import SimpleITK as sitk
import cv2 as cv
import numpy as np


def video2pngs(videos_dir, save_dir):
    videos = os.listdir(videos_dir)
    for video in videos:

        video_path = os.path.join(videos_dir, video)
        vid = cv.VideoCapture(video_path)
        max = int(vid.get(7))
        h = int(vid.get(4))
        w = int(vid.get(3))
        video_name = video.rsplit('.', 1)[0]
        video_p_dir = os.path.join(save_dir, video_name)
        if not os.path.exists(video_p_dir):
            os.makedirs(video_p_dir)

        video_np = np.zeros((max, h, w))

        i = 0
        vid = cv.VideoCapture(video_path)
        while i < max:
            ret, frames = vid.read()
            cv.imwrite(os.path.join(video_p_dir, video_name + '_' + str(i + 1) + '.png'), frames, [0])
            nii_pic = cv.cvtColor(frames, cv.COLOR_BGR2GRAY)
            video_np[i] = nii_pic
            i = i + 1
            if ret is False:
                break

        video_nii = sitk.GetImageFromArray(video_np)
        output_path = os.path.join(save_dir, "nifti", video_name + ".nii.gz")
        sitk.WriteImage(video_nii, output_path)
        print(video)


if __name__ == "__main__":
    v_dir = r"D:\pycharm_project\oct_data\combination\videos"
    s_dir = r"D:\pycharm_project\oct_data\combination\videos_pictures"
    video2pngs(v_dir, s_dir)
