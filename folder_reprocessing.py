import os
import shutil
import tarfile

song_path = "D:\\first_set\\song"
files_path = "D:\\first_set\\files"
train_txt = "D:\\first_set\\train.txt"
test_txt = "D:\\first_set\\test.txt"
videos_path = "D:\\first_set\\videos"


def folder_copy(source_path):
    for filepath, dirnames, filenames in os.walk(source_path):
        for filename in filenames:
            if filename[-4:] == '.avi':
                video_full_path = os.path.join(filepath, filename)
                shutil.copy(video_full_path, videos_path)
            else:
                tar_full_path = os.path.join(filepath, filename)
                t = tarfile.open(tar_full_path, "r:")
                t.extractall(files_path)
                t.close()


if __name__ == "__main__":
    folder_copy(song_path)
