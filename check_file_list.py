import os

file_path = '/nvme/data/unlabeled_videos'
txt_path = '/nvme/data/videos/unlabeled_list.txt'
labed_tr_path = '/home/sjy/Documents/base_data/video/train'
labed_ts_path = '/home/sjy/Documents/base_data/video/test'


def check_file_list():
    with open(txt_path, 'r') as f_txt:
        unlabeled_list0 = f_txt.read()
        unlabeled_list = unlabeled_list0.replace('\n', ',').split(',')[:-1]
    file_list = os.listdir(file_path)
    intersection = list(set(unlabeled_list) & set(file_list))

    tr = os.listdir(labed_tr_path)
    ts = os.listdir(labed_ts_path)
    tr.extend(ts)

    d = list(set(unlabeled_list).difference(set(file_list)))
    repeat = list(set(file_list).difference(set(unlabeled_list)))

    la_re = list(set(tr) & (set(file_list)))
    print(len(file_list))
    print(len(intersection))
    print(len(tr))

    print(d, len(d))
    repeat.sort()
    print(repeat, len(repeat))
    print(la_re, len(la_re))


if __name__ == '__main__':
    check_file_list()
