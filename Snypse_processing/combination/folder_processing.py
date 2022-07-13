import glob
import tarfile
import os


def un_tar(file_name, target_path):
    tar = tarfile.open(file_name)
    names = tar.getnames()
    for name in names:
        tar.extract(name, target_path)
    tar.close()


def batch_un_tar(dir, target_path):
    sub_dir_list = os.listdir(dir)
    for sub_dir in sub_dir_list:
        tar_path = os.path.join(dir, sub_dir, sub_dir + '_avi_Label.tar')
        un_tar(tar_path, target_path)


if __name__ == '__main__':
    #  un_tar(r'D:\pycharm_project\oct_data\second_long_20\oct_1 Nov 2021 02-27-52\oct_1 Nov 2021 02-27-52_avi_Label.tar', r'D:\pycharm_project\oct_data\combination\song')
    base_dir = r'D:\pycharm_project\oct_data'
    dir = os.path.join(base_dir, r'first_song_45')
    target_path = os.path.join(base_dir, r'combination', r'song1')
        # r'D:\pycharm_project\oct_data\combination\song'

    batch_un_tar(dir, target_path)
