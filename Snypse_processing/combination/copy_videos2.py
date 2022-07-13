import os
import shutil

base_dir = r'D:\pycharm_project\oct_data\second_song_25'
dst_dir = r'D:\pycharm_project\oct_data\combination\videos2'

json_dir = r'D:\pycharm_project\oct_data\combination\json_combined_2'

seg_dir = r'D:\pycharm_project\oct_data\combination\seg_merge2'
folders = os.listdir(base_dir)
for folder in folders:
    video_path = os.path.join(base_dir, folder, folder + '.avi')
    dst_path = os.path.join(dst_dir, folder, folder + '.avi')
    folder_path = os.path.join(dst_dir, folder)
    #os.makedirs(folder_path)
    #
    shutil.copyfile(video_path, dst_path)

    json_path = os.path.join(json_dir, folder + '_avi_Label.json')
    dst_json_path = os.path.join(dst_dir, folder, folder + '_avi_Label.json')
    shutil.copyfile(json_path, dst_json_path)

    seg_path = os.path.join(seg_dir, folder + '_avi_Label.nii.gz')
    dst_seg_path = os.path.join(dst_dir, folder, folder + '_avi_Label.nii.gz')
    shutil.copyfile(seg_path, dst_seg_path)
