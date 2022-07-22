import os
import shutil

from annotations_in_json import annotations_in_json

tr_json_dir = '/nvme/json/train'
tr_png_path = '/nvme/cropped_png'
tr_out_path = '/nvme/seg_trainset/'

ts_json_dir = '/nvme/json/test'
ts_png_path = '/nvme/cropped_png'
ts_out_path = '/nvme/seg_testset/'


def select_labeled_png(json_dir, png_path, out_path):
    jsons = os.listdir(json_dir)
    for json in jsons:
        file_name = json.rstrip('avi_Label.json')
        json_path = os.path.join(json_dir, json)
        anots, a = annotations_in_json(json_path)
        for anot in anots:
            src_path = os.path.join(png_path, file_name + '_' + str(anot) + '.png')
            print(os.path.exists(src_path))
            shutil.copy(src_path, out_path)


if __name__ == '__main__':
    select_labeled_png(ts_json_dir, ts_png_path, ts_out_path)
    select_labeled_png(tr_json_dir, tr_png_path, tr_out_path)
