import json

import commentjson


def nifti_json(json_path=None, with_comment=False):
    with open(json_path, encoding='utf-8') as f:
        if with_comment:  # 若*.json中添加了注释，则使用commentjson。若无注释则使用json库也可。
            Anno_Dict = commentjson.load(f)
        else:
            Anno_Dict = json.load(f)

    name = Anno_Dict["FileInfo"]["Name"]
    Results_Dict = Anno_Dict["Polys"]
    Polygon_list = Results_Dict[0]["Shapes"]
    count = []
    frame_idx = []
    label = []

    for p_idx, p_item in enumerate(Polygon_list):
        count.append(p_idx)
        frame_idx.append(p_item["ImageFrame"])
        label.append(p_item["labelType"])

    return name, count, frame_idx, label


if __name__ == '__main__':
    nifti_json(json_path=None, with_comment=False)
