import json
import os.path


def combine_json(name):
    path1 = os.path.join(r"D:\pycharm_project\oct_data\combination\song_json", name)
    path2 = os.path.join(r"D:\pycharm_project\oct_data\combination\long_json", name)
    path = os.path.join(r"D:\pycharm_project\oct_data\combination\json_combined_2", name)
    with open(path1, 'r', encoding='utf8') as f1:
        file1 = json.load(f1)
        slice1 = file1["Models"]["PolygonModel"]["3"]
        f1.close()

    if os.path.exists(path2):
        with open(path2, 'r', encoding='utf8') as f2:
            file2 = json.load(f2)
            slice2 = file2["Models"]["PolygonModel"]["3"]
            f2.close()
        slice_combined = list(set(slice1 + slice2))
        slice_combined = sorted(slice_combined)

        file1["Models"]["PolygonModel"]["3"] = slice_combined

    data = json.dumps(file1, indent=1)

    with open(path, 'w', newline='\n') as f:
        f.write(data)
        f.close()


if __name__ == "__main__":
    names_dir = r"D:\pycharm_project\oct_data\combination\song_json"
    names = os.listdir(names_dir)
    num = 0
    for name in names:
        num = num + 1
        combine_json(name)
        print(name, num)