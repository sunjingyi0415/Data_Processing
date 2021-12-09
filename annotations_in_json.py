import json

json_path = '/home/sjy/Documents/data/label/json'


# json_file_path = os.path.join(json_path, json_file)
def annotations_in_json(json_path):
    with open(json_path) as f:
        info = json.load(f)
        anots = info["Models"]["PolygonModel"]["3"]
    return anots


if __name__ == '__main__':
    annotations_in_json(json_path)
