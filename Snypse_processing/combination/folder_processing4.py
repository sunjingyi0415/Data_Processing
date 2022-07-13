import os
import shutil


def make_tars():

    video_dir = r"D:\pycharm_project\oct_data\combination\videos"
    base_dir = r"D:\TransUNet\data\oct\labels\segmentations"

    videos = os.listdir(video_dir)
    for video in videos:
        folder_name = video.split('.')[0]
        video_path = os.path.join(video_dir, video)
        dst_path = os.path.join(base_dir, folder_name, video)

        shutil.copyfile(video_path, dst_path)


if __name__ == "__main__":
    make_tars()






