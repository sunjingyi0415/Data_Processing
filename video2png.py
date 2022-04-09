import os

import cv2 as cv

# video_path1 = '/home/sjy/Documents/testdata/video/oct_8 Jul 2021 02-12-10.avi'
# png_path1 = '/home/sjy/Documents/Task500/png'

slices1=[23, 24, 27, 77, 80, 94, 108, 151, 169, 174, 245, 247, 355]
#videos_path = '/home/sjy/Documents/data/video/'
#png_out_dir = '/home/sjy/Documents/Task500/image/'

# 截图图像
def cutVideo(video_path, slices, out_path):
    i = 0
    idx = 0
    video = cv.VideoCapture(video_path)  # 读取视频文件
    while (True):
        ret, frame = video.read()
        c = cv.waitKey(50)
        if c == 27:
            break
        for sli in slices:
            if i == sli:
                cv.imwrite(out_path + '_'+str(idx) + '.png', frame, [0])
                idx = idx+1
        i = i + 1
        print(idx)
        if i == 800:
            break
    cv.destroyAllWindows()

def cutVideo4test(video_path, slices, out_path):
    i = 0
    idx = 0
    video = cv.VideoCapture(video_path)  # 读取视频文件
    while (True):
        ret, frame = video.read()
        if ret:
            max = len(frame[0])
            c = cv.waitKey(50)
            if c == 27:
                break
            for sli in slices:
                if i != sli:
                    cv.imwrite(out_path + '_' + str(idx) + '.png', frame, [0])
                    idx = idx + 1
                i = i + 1
                #            print(idx)
                if i == max:
                    break


    cv.destroyAllWindows()