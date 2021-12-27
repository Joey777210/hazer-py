import os.path

import hazer
import cv2
import glob

basePath = "./Pics/"

def getHazeFactorExample():
    paths = glob.glob(os.path.join(basePath, '*.png'))
    paths.sort()
    for path in paths :
        img = cv2.imread(path)
        img_norm = cv2.normalize(img.astype('float'), None, 0.0, 1.0,
                                 cv2.NORM_MINMAX)  # Convert to normalized floating point

        hazeFactor = hazer.getHazeFactor(img_norm)
        print("{}\t{}".format(path[len(basePath):], hazeFactor))


if __name__ == '__main__':
    getHazeFactorExample()
