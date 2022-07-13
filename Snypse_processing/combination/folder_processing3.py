import os
import shutil
import tarfile


def make_tars():
    tar_dir = r"D:\pycharm_project\oct_data\combination\tar1"
    first_set_dir = r"D:\pycharm_project\oct_data\combination\first_song_45"

    tars = os.listdir(tar_dir)
    for tar in tars:
        name = tar.split('.')[0]
        tar_path = os.path.join(tar_dir, tar)
        fst_path = os.path.join(first_set_dir, name, name + "_avi_Label.tar")
        shutil.copyfile(tar_path, fst_path)


if __name__ == "__main__":
    make_tars()





