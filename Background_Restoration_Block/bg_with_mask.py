import cv2
import pdb
import os
import shutil
 


def bg_extract(img, label):
    for i in range(len(label)):
        for j in range(len(label[0])):
            if label[i][j] > 100:   #The masks in the Drive dataset are not strictly 255.
                img[i][j] = [255,255,255]
    return img



base_path = r'./train_input'
base_label_path = r'./train_label'
target_path = r'./background_with_mask/'
files = os.listdir(base_path)

for path in files:
    full_path = os.path.join(base_path, path)
    full_path_label = os.path.join(base_label_path, path)
    print(full_path, full_path_label)
    img = cv2.imread(full_path, 1)
    label = cv2.imread(full_path_label, 0)
    bg = bg_extract(img, label)
    print(target_path+path)
    cv2.imwrite(target_path+path, bg)
