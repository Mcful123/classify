# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 15:42:38 2021

@author: chomi
"""

import cv2 as cv
import os

path = 'images/'

def image_resize(image, width = None, height = None, inter = cv.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))
    resized = cv.resize(image, dim, interpolation = inter)
    return resized


for filename in os.listdir(path):
    flag = 1
    if(filename.endswith(".png")):
        img = cv.imread(path + filename)
        copy = img.copy()
        copy = image_resize(copy, width = 800)
        cv.imshow('quick', copy)
        while(flag == 1):
            key = cv.waitKey(0)
            if(key == ord('0')):
                print(filename, " Saved as:  0")
                cv.imwrite('images/0/' + filename, copy)
                cv.imwrite('images/sorted/' + filename, img)
                os.remove(path + filename)
                flag = 0
            elif(key == ord('1')):
                print(filename, " Saved as:  1")
                cv.imwrite('images/1/' + filename, copy)
                cv.imwrite('images/sorted/' + filename, img)
                os.remove(path + filename)
                flag = 0
            elif(key == ord('2')):
                print(filename, " Saved as:  2")
                cv.imwrite('images/2/' + filename, copy)
                cv.imwrite('images/sorted/' + filename, img)
                os.remove(path + filename)
                flag = 0
            elif(key == ord('3')):
                print(filename, " Saved as:  3")
                cv.imwrite('images/3/' + filename, copy)
                cv.imwrite('images/sorted/' + filename, img)
                os.remove(path + filename)
                flag = 0
            elif(key == ord('4')):
                print(filename, " Saved as:  4")
                cv.imwrite('images/40/' + filename, copy)
                cv.imwrite('images/sorted/' + filename, img)
                os.remove(path + filename)
                flag = 0
            elif(key == ord('l')):
                print(filename, " saved for later")
                # cv.imwrite('C:/Users/chomi/Desktop/later/' + filename, copy)
                flag = 0
            elif(key == ord('c')):
                flag = 2
            else:
                print("Invalid key press")
                flag = 1
    if(flag == 2):
        break
    
print("Finished.", end=(''))
if(flag == 2):
    print("..User interrupt")
cv.destroyAllWindows()

