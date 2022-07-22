import os

import cv2 as cv

video_dir = '/home/sjy/Documents/raw_data1'
output_dir = '/nvme/raw_png1/'


# video_dir = '/nvme/video'
# output_dir = '/nvme/raw_png0/'


def get_images_from_oct2(file_path):
    video = cv.VideoCapture(file_path)
    max = int(video.get(7))
    file_name = os.path.split(file_path)[-1].strip('.avi')
    for i in range(max):
        ret, frames = video.read()
        cv.imwrite(output_dir + file_name + '_' + str(i) + '.png', frames, [0])


if __name__ == '__main__':
    videos = os.listdir(video_dir)
    for vid in videos:
        video_path = os.path.join(video_dir, vid)
        get_images_from_oct2(video_path)
