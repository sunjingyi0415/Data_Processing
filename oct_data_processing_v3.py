import glob
import os

import h5py
import numpy as np


def concatenate(slice_names_to_concatenate, patient0):
    entry_key = 'image'  # where the data is inside of the source files.
    entry_key1 = 'label'
    # entry_key2 = 'name'
    sh = h5py.File(slice_names_to_concatenate[0], 'r')[entry_key].shape  # get the first ones shape.
    layout = h5py.VirtualLayout(shape=(len(slice_names_to_concatenate),) + sh,
                                dtype=np.float32)
    layout1 = h5py.VirtualLayout(shape=(len(slice_names_to_concatenate),) + sh,
                                 dtype=int)
    with h5py.File("/nvme/data/ts_vol_h5/{}.h5".format(patient0), 'w', libver='latest') as f:
        for i, filename in enumerate(slice_names_to_concatenate):
            vsource = h5py.VirtualSource(filename, entry_key, shape=sh)
            vsource1 = h5py.VirtualSource(filename, entry_key1, shape=sh)
            layout[i, :, :] = vsource
            layout1[i, :, :] = vsource1

        # slice_names_to_concatenate = np.string_(slice_names_to_concatenate)
        # dt = h5py.string_dtype(encoding='ascii')

        f.create_virtual_dataset(entry_key, layout, fillvalue=0)
        f.create_virtual_dataset(entry_key1, layout1, fillvalue=0)
        # f.create_dataset(entry_key2, data=slice_names_to_concatenate, dtype=dt)
        print("image shape", f['image'].shape)


def read_patients_list(txt_dir):
    with open(txt_dir, 'r') as f:
        sampled_list = f.read().rstrip('\n').split(',')
    return sampled_list


def repeat_list(single_list):
    length = 80
    item = []
    single_list_len = len(single_list)
    rpt_frequency = length // single_list_len
    if rpt_frequency:
        item = rpt_frequency * single_list
    rest = length % single_list_len
    if rest:
        for i in range(rest):
            item.append(item[i])
    return item


if __name__ == '__main__':
    patients = os.listdir("/nvme/data/video_45/test")
    for patient in patients:
        patient_name = patient.rstrip('.avi')
        group = glob.glob('/nvme/data/ts_h5/' + patient_name + '*' + '.h5')
        group = sorted(group)
        concatenate(group, patient)
        # repeat_group = repeat_list(group)
        # if len(repeat_group) == 80:
        #    concatenate(repeat_group, patient)
        # else:
        #    print("repeat list length error", patient)
        # print(patient)
