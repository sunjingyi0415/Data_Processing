import json
import os
import cv2 as cv

test_json = '/home/sjy/Documents/data/label/json/oct_9 Jul 2021 05-01-38_avi_Label.json'
test_video = '/home/sjy/Documents/data/video/oct_9 Jul 2021 05-01-38.avi'
test_out = '/home/sjy/Documents/test/'


def get_labeled_info(jsonfile_name):
    annotation = json.load(open(jsonfile_name))
    slices = annotation["Models"]["PolygonModel"]["3"]
    return slices


def cutvideo(video_path, slices, out_path):
    i = 0
    idx = 0
    video = cv.VideoCapture(video_path)  # 读取视频文件
    while True:
        ret, frame = video.read()
        c = cv.waitKey(50)
        if c == 50:
            break
        for sli in slices:
            if i == sli:
                cv.imwrite(out_path + '_' + str(sli) + '.png', frame, [0])
                idx = idx + 1
        i = i + 1
#        print(idx)
        if i == 500:
            break


las = get_labeled_info(test_json)
print(las,len(las))
cutvideo(test_video,las,test_out)
