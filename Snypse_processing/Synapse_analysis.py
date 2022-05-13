import os

path1 = r'D:\pycharm_project\TransUNet\data\averaged-training-images'
path2 = r'D:\pycharm_project\data\project_transunet\project_TransUNet\data\Synapse\train_npz'


def case_statistic(path):
    cases_slices = os.listdir(path)
    case_list = []
    num = 0
    for case_slices in cases_slices:
        case = case_slices[4:8]
        if case not in case_list:
            case_list.append(case)
            num = num + 1
    print(case_list, '\n', num)


if __name__ == '__main__':
    case_statistic(path1)
    case_statistic(path2)

