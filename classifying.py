# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 15:42:38 2021

@author: chomi
"""

import cv2 as cv
import os

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

path = 'Samples/images/'

print("NOTE: the window with the sample image must be in focus for this program to work.")
print("i.e: click on the image before starting")
print("")
print("press '0',  '1',  '2',  '3', or '4' to classify sample.")
print("press 'J' to come back to current sample at the end.")
print("press 'K' check how many images are left.")
print("press 'L' to save and quit.")

cond = False
while (len(os.listdir(path)) > 6 ):
    imList = os.listdir(path)
    for filename in imList:
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
                    cv.imwrite('Samples/images/0/' + filename, copy)
                    cv.imwrite('Samples/images/sorted/' + filename, img)
                    os.remove(path + filename)
                    flag = 0
                elif(key == ord('1')):
                    print(filename, " Saved as:  1")
                    cv.imwrite('Samples/images/1/' + filename, copy)
                    cv.imwrite('Samples/images/sorted/' + filename, img)
                    os.remove(path + filename)
                    flag = 0
                elif(key == ord('2')):
                    print(filename, " Saved as:  2")
                    cv.imwrite('Samples/images/2/' + filename, copy)
                    cv.imwrite('Samples/images/sorted/' + filename, img)
                    os.remove(path + filename)
                    flag = 0
                elif(key == ord('3')):
                    print(filename, " Saved as:  3")
                    cv.imwrite('Samples/images/3/' + filename, copy)
                    cv.imwrite('Samples/images/sorted/' + filename, img)
                    os.remove(path + filename)
                    flag = 0
                elif(key == ord('4')):
                    print(filename, " Saved as:  4")
                    cv.imwrite('Samples/images/4/' + filename, copy)
                    cv.imwrite('Samples/images/sorted/' + filename, img)
                    os.remove(path + filename)
                    flag = 0
                elif(key == ord('j')):
                    print(filename, " saved for later")
                    flag = 0
                elif(key == ord('l')):
                    print("Saving and quitting...")
                    flag = 2
                    cond = True
                elif(key == ord('k')):
                    tempList = os.listdir(path)
                    size = len(tempList) - 6
                    print(size, 'images left.')
                    flag = 1
                else:
                    print("Invalid key press")
                    flag = 1
        if(flag == 2):
            break
    if(cond):
        print("Saved with", len(os.listdir(path)) - 6, "images left.")
        break
if(len(os.listdir(path)) < 7):
    print("Finished judging all samples.")
print("closing...")
cv.destroyAllWindows()

