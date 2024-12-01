import cv2
import pdb
import os
import shutil
import random
import numpy as np
from PIL import Image
 
def BGR_to_RGB(cvimg):
    pilimg = cvimg.copy()
    pilimg[:, :, 0] = cvimg[:, :, 2]
    pilimg[:, :, 2] = cvimg[:, :, 0]
    return pilimg


def bg_extract(img, label):
    #pdb.set_trace()
    for i in range(len(label)):
        for j in range(len(label[0])):
            if label[i][j] == 255:
                #pdb.set_trace()
                img[i][j] = [0,0,0]
                # img[i][j][0]= sum(sum(img[i-4:i+5,j-4:j+5,0]))/10
                # img[i][j][1]= sum(sum(img[i-4:i+5,j-4:j+5,1]))/10
                # img[i][j][2]= sum(sum(img[i-4:i+5,j-4:j+5,2]))/10
    return img

def gamma(img, G = 1.0):        #G小于1，变暗；大于1，变亮。
    labe = []
    G = 1.0 / G
    for i in range(256):
        labe.append(((i / 255) ** G) * 255)
    labe = np.array(labe).astype('uint8')
    img = cv2.LUT(img, labe)
    return img


bg_path = r'./background/'
input_path = r'./train_input/'
label_path = r'./train_label/'
target_input_path = r'./train_input_expand/'
target_label_path = r'./train_label_expand/'
bg_files = []
gt_files = []
label_files = []
for filename in os.listdir(bg_path):
    if filename[-13:-4] == 'inpainted':
        bg_files.append(filename)
for filename in os.listdir(input_path):
        gt_files.append(filename)
for filename in os.listdir(label_path):
        label_files.append(filename)
for i in range(len(bg_files)):
    bg_files1 = bg_files[:i] + bg_files[i+1:]
    gt_files1 = gt_files[:i] + gt_files[i+1:]
    label_files1 = label_files[:i] + label_files[i+1:]
    bg_num = bg_files[i][6:9]
    slice = random.sample(range(len(bg_files1)),2)
    for label in slice:
        bg_full_path = os.path.join(bg_path, bg_files[i])
        gt_full_path = os.path.join(input_path, gt_files1[label])
        label_full_path = os.path.join(label_path, label_files1[label])
        print(bg_full_path, gt_full_path, label_full_path)
        target_gt_full_path = os.path.join(target_input_path, bg_files[i][:-15]+'_'+gt_files1[label][:-4]+'.jpg')
        target_label_full_path = os.path.join(target_label_path, bg_files[i][:-15]+'_'+gt_files1[label][:-4]+'.jpg')
        print(target_gt_full_path, target_label_full_path)
        gt = Image.open(gt_full_path)
        gt = np.array(gt)
        gt = BGR_to_RGB(gt)
        bg = cv2.imread(bg_full_path, 1)
        label = cv2.imread(label_full_path, 0)



        ga1 = random.random()/2.5+0.8
        ga2 = random.random()/2.5+0.8
        gt = gamma(gt, ga1)
        bg = gamma(bg, ga2)
        angle1 = random.sample(range(0, 360),1)[0]
        angle2 = random.sample(range(0, 360),1)[0]
        scale1 = random.random()/10 + 0.9
        scale2 = random.random()*(1-scale1) + scale1
        M1 = cv2.getRotationMatrix2D((len(label[0])/2, len(label)/2), angle1, scale1)
        gt = cv2.warpAffine(gt, M1, (len(label[0]), len(label)))
        label = cv2.warpAffine(label, M1, (len(label[0]), len(label)))

        M2 = cv2.getRotationMatrix2D((len(label[0])/2, len(label)/2), angle2, scale2)
        bg = cv2.warpAffine(bg, M2, (len(bg[0]), len(bg)))
        bg1 = np.copy(bg)

        erode_k = random.sample([1,3],1)[0]
        kernel = np.ones((erode_k,erode_k),np.uint8)

        texture = cv2.Canny(gt, threshold1=1, threshold2=50)
        
        for m in range(len(bg)):
            for n in range(len(bg[0])):
                if min(bg[m,n,:]) > 250: #Vessel mask not been inpainted.
                    label[m][n] = 255
                if label[m][n] > 100: #The masks in the Drive dataset are not strictly 255.
                    bg[m,n,:] = [192 + int(texture[m][n]/4), 192 + int(texture[m][n]/4), 192 + int(texture[m][n]/4)]
        cv2.imwrite(target_gt_full_path, bg)
        cv2.imwrite(target_label_full_path, label)