import os
import shutil

import numpy as np

raw_test_path = '/home/sjy/Documents/base_data/raw_test/'
test_path = '/home/sjy/Documents/base_data/test/'

files = os.listdir(raw_test_path)
print(len(files))
ran = np.random.randint(0, 1480, size=370)
for i in ran:
    old = os.path.join(raw_test_path, files[i])
    new = os.path.join(test_path, files[i])
    shutil.copyfile(old, new)
