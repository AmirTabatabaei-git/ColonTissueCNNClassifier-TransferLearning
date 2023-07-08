import os
import cv2
import imutils


directoryClassOneTrain = 'train/class 1'
directoryClassTwoTrain = 'train/class 2'
directoryClassThreeTrain = 'train/class 3'
directoryClassOneValid = 'valid/class 1'
directoryClassTwoValid = 'valid/class 2'
directoryClassThreeValid = 'valid/class 3'


def rotate90(directory, count):
    i = 0
    for filename in os.listdir(directory):
        imagePath = os.path.join(directory,filename)
        image = cv2.imread(imagePath)
        rotated = imutils.rotate(image, 90)
        newPath = imagePath[:-4]+'-rotate90'+'.jpg'
        cv2.imwrite("{}".format(newPath), rotated)
        # cv2.imshow("{}".format(newPath), rotated)
        # cv2.waitKey(0)
        i+=1
        if i == count:
            break

def rotate180(directory, count):
    i = 0
    for filename in os.listdir(directory):
        imagePath = os.path.join(directory,filename)
        image = cv2.imread(imagePath)
        rotated = imutils.rotate(image, 90)
        newPath = imagePath[:-4]+'-rotate180'+'.jpg'
        # cv2.imshow("{}".format(newPath), rotated)
        cv2.imwrite("{}".format(newPath), rotated)
        # cv2.waitKey(0)
        i+=1
        if i == count:
            break

rotate90(directoryClassOneTrain, 21)
rotate90(directoryClassThreeTrain, 27)
rotate90(directoryClassOneValid, 7)
rotate90(directoryClassThreeValid, 11)
rotate180(directoryClassThreeTrain, 8)
rotate180(directoryClassThreeValid, 4)



