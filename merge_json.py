import os

import commentjson


def merge_json(path_results, path_merges):
    """
    主要功能是实现一个目录下的多个json文件合并为一个json文件。
    :param path_results:
    :param path_merges:
    :return:
    """
    merges_file = os.path.join(path_merges, "train_summary.json")
    num = 0
    with open(merges_file, "w+") as f0:
        for file in os.listdir(path_results):
            with open(os.path.join(path_results, file), 'r', encoding="utf-8") as f1:
                info = commentjson.load(f1)
                new_info = {}
                new_info['FileName'] = info["FileName"]
                new_info['slices'] = info["Models"]["PolygonModel"]["3"]
                new_info['shapes'] = info["Polys"]
                new_info = commentjson.dumps(new_info, indent=2)
                f0.write(new_info)
                print(file, "has been written")
                num = num + 1
        f0.close()
    print(num, "files have been written")


if __name__ == '__main__':
    path_results = r"D:\first_set\json\train"
    path_merges = r"D:\first_set"
    if not os.path.exists(path_merges):  # 如果results目录不存在，新建该目录。
        os.mkdir(path_merges)
    merge_json(path_results, path_merges)
