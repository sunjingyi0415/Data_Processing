import json
import os

import cv2 as cv

from annotations_in_json import annotations_in_json

jsons_dir = '/home/sjy/Documents/base_data/json/'
video_dir = '/home/sjy/Documents/base_data/video/'
test_dir = '/home/sjy/Documents/base_data/raw_test/'
train_dir = '/home/sjy/Documents/base_data/train/'


def video2pngs(annotations, frames):
    idxtr = 0
    idxts = 0
    name = json.split('_avi_Label.json')[0]
    max = int(video.get(7))
    for i in range(max):
        if i in annotations:
            cv.imwrite(train_dir + name + '_' + str(idxtr) + '.png', frames, [0])
            idxtr = idxtr + 1
        else:
            cv.imwrite(test_dir + name + '_' + str(idxts) + '.png', frames, [0])
            idxts = idxts + 1


if __name__ == '__main__':
    for json in os.listdir(jsons_dir):
        json_path = os.path.join(jsons_dir, json)
        video_path = os.path.join(video_dir, json.replace('_avi_Label.json', '.avi'))

        anots = annotations_in_json(json_path)
        video = cv.VideoCapture(video_path)
        ret, frame = video.read()
        video2pngs(anots, frame)
'''
    i = 0
    idx = 0
    video = cv.VideoCapture(video_path)  # 读取视频文件
    ret, frame = video.read()
    for sli in slices:
        if i == sli:
        cv.imwrite(out_path + '_'+str(idx) + '.png', frame, [0])
                idx = idx+1
        i = i + 1
        print(idx)
        if i == 800:
            break
    cv.destroyAllWindows()
'''
