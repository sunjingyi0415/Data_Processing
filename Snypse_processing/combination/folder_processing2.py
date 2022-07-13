import os
import shutil
import tarfile


def make_dirs():
    seg_dir = r"D:\pycharm_project\oct_data\combination\seg_merge1"
    json_dir = r"D:\pycharm_project\oct_data\combination\json_combined_1"
    dir = r"D:\pycharm_project\oct_data\combination\segmentation_1"
    if not os.path.exists(dir):
        os.makedirs(dir)

    segs = os.listdir(seg_dir)
    for seg in segs:
        name = seg.rsplit('_', 2)[0]

        dst_dir = os.path.join(dir, name)
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir, mode=0o777)

        source_seg_path = os.path.join(seg_dir, seg)
        dst_path = os.path.join(dst_dir, seg)
        shutil.copyfile(source_seg_path, dst_path)

        source_path = os.path.join(json_dir, name + "_avi_Label.json")
        dst_json = os.path.join(dst_dir, name + "_avi_Label.json")
        shutil.copyfile(source_path, dst_json)


if __name__ == "__main__":
    make_dirs()





