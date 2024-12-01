import cv2
import pdb
import os
import shutil
import numpy as np
base_path = r'./background_with_mask/'
target_path = r'./background/'
files = os.listdir(base_path)

def bg_inpainting(img):
    iter = 0
    for i in range(len(img)):
        for j in range(len(img[0])):
            #import pdb;pdb.set_trace()
            if min(img[i,j,:]) > 240:
                flag = 51
                for m in range(max(0, i-9), min(len(img), i+9)):
                    for n in range(max(0, j-9), min(len(img), j+9)):
                        if min(img[m,n,:]) < 240:
                            img[i,j,:] = img[m,n,:]
                            break
    iter += 1
    cv2.imwrite(target_path+'test_' + str(iter) + '.jpg', img)
    img = cv2.imread(target_path+'test_' + str(iter) + '.jpg', 1)
    for i in range(len(img)):
        for j in range(len(img[0])):
            if min(img[i,j,:]) > 240:
                flag = 51
                for m in range(max(0, i-9), min(len(img), i+9)):
                    for n in range(max(0, j-9), min(len(img), j+9)):
                        if min(img[m,n,:]) < 240:
                            img[i,j,:] = img[m,n,:]
                            break
    iter += 1
    cv2.imwrite(target_path+'test_' + str(iter) + '.jpg', img)
    img = cv2.imread(target_path+'test_' + str(iter) + '.jpg', 1)
    for i in range(len(img)):
        for j in range(len(img[0])):
            if min(img[i,j,:]) > 240:
                flag = 51
                for m in range(max(0, i-9), min(len(img), i+9)):
                    for n in range(max(0, j-9), min(len(img), j+9)):
                        if min(img[m,n,:]) < 240:
                            img[i,j,:] = img[m,n,:]
                            break
    iter += 1
    cv2.imwrite(target_path+'test_' + str(iter) + '.jpg', img)
    return img





for path in files:
    full_path = os.path.join(base_path, path)
    print(full_path)
    img = cv2.imread(full_path, 1)
    erode_size = int(2*np.floor(np.log2(min(len(img), len(img[0])))) + 1)
    print((len(img), len(img[0]), erode_size))
    img = cv2.medianBlur(img, 2*erode_size - 1)
    img = cv2.erode(img, (erode_size,erode_size))
    img = cv2.erode(img, (erode_size,erode_size))
    img = cv2.erode(img, (erode_size,erode_size))
    img = cv2.medianBlur(img, 2*erode_size - 1)
    bg = bg_inpainting(img)
    blurred_bg = cv2.medianBlur(bg, 2*erode_size - 1)
    inpainted_bg = cv2.blur(blurred_bg, (erode_size,erode_size))
    print(target_path+path)
    cv2.imwrite(target_path+path[:-4]+'_inpainted.jpg', inpainted_bg)