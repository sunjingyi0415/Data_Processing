import json

import commentjson
import cv2 as cv


class Convertions():
    video_path = ''
    label_path = ''
    image_path = ''

    def __init__(self):
        self.a = self.a
        self.json_path = ''
        self.video_path = ''

    def annotations_in_json(self):
        with open(self.json_path) as f:
            info = commentjson.load(f)
            anots = info["Models"]["PolygonModel"]["3"]
            name_without_ext = info["FileName"].rstrip("avi")
        return anots, name_without_ext

    def video2pngs(self, annotations):
        idxtr = 0
        idxts = 0
        name = json.split('_avi_Label.json')[0]
        max = int(self.video_path.get(7))
        for i in range(max):
            vid = cv.VideoCapture(self.video_path)
            ret, frames = vid.read()
            if i in annotations:
                cv.imwrite(train_dir + name + '_' + str(idxtr) + '.png', frames, [0])
                idxtr = idxtr + 1
