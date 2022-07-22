import os

import commentjson

# json_path = '/home/sjy/Documents/base_data/json/oct_8-Jul-2021-02-12-10_avi_Label.json'
encoding = 'UTF-8'


# json_file_path = os.path.join(json_dir, json_file)
def annotations_in_json(json_path):
    with open(json_path, encoding='UTF-8') as f:
        info = commentjson.load(f)
        anots = info["Models"]["PolygonModel"]["3"]
        name_without_ext = info["FileName"].rstrip("avi")
    return anots, name_without_ext


if __name__ == '__main__':
    json_dir = '/home/sjy/Documents/base_data/json'
    jsons = os.listdir(json_dir)
    num = 0
    for json in jsons:
        json_path = os.path.join(json_dir, json)
        anots, _ = annotations_in_json(json_path)
        num = num + len(anots)
        print(num)
