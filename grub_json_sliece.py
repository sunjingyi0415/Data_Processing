import json
import os
import cv2 as cv

json_path = '/home/sjy/Documents/data/label/json'

'''
def find_labled_slice(file_path):
    json_files = os.listdir(file_path)
    print(json_files)
    for json_file in json_files:
        info = json.loads('json_file')
        la_idx=info["Models"]["PolygonModel"]["3"]
        print(la_idx)
        
'''

def find_labled_slice(file_path):
    json_files = os.listdir(file_path)
    for json_file in json_files:
        print(json_file)
        json_file_path=os.path.join(json_path,json_file)
        with open(json_file_path) as f:
            info = json.load(f)
        la_idx=info["Models"]["PolygonModel"]["3"]
        print(la_idx)



if __name__ == '__main__':
    find_labled_slice(json_path)
