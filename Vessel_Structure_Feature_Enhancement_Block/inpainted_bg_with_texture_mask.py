import cv2
import pdb
import os
import shutil
 


def bg_extract(img, label, texture):
    for i in range(len(label)):
        for j in range(len(label[0])):
            if label[i][j] > 100: #The masks in the Drive dataset are not strictly 255.
                img[i][j]=[192 + int(texture[i][j]/4), 192 + int(texture[i][j]/4), 192 + int(texture[i][j]/4)]
    return img



base_path = r'./background'
target_path = r'./inpainted_background_with_texture_mask/'
label_path = r'./train_label'
gt_path = r'./train_input'
files = os.listdir(base_path)

for path in files:
    full_path = os.path.join(base_path, path)
    full_path_label = os.path.join(label_path, path[:-13]+'.jpg')
    full_path_gt = os.path.join(gt_path, path[:-13]+'.jpg')
    print(full_path, full_path_label, full_path_gt)
    img = cv2.imread(full_path, 1)
    label = cv2.imread(full_path_label, 0)
    gt = cv2.imread(full_path_gt, 0)
    texture = cv2.Canny(gt, threshold1=1, threshold2=50)
    bg = bg_extract(img, label, texture)
    cv2.imwrite(target_path+path[:-13]+'.jpg', bg)
