import time

start = time.time()

import argparse
import cv2
import os
import pickle
import sys

from operator import itemgetter

import numpy as np
np.set_printoptions(precision=2)
import pandas as pd

import openface

fileDir = os.path.dirname(os.path.realpath(__file__))
modelDir = os.path.join(fileDir, '..', 'models')
dlibModelDir = os.path.join(modelDir, 'dlib')
openfaceModelDir = os.path.join(modelDir, 'openface')

align = openface.AlignDlib(default=os.path.join(dlibModelDir, "shape_predictor_68_face_landmarks.dat"))

#im1: target face
#im2: actual face

def assess(imgPath1, imgPath2, imgdim):
    net = openface.TorchNeuralNet(os.path.join(openfaceModelDir, 'nn4.small2.v1.t7'), imgdim)

    im1 = cv2.imread(imgPath1)
    im2 = cv2.imread(imgPath2)
    if im1 is None and im2 is None:
        raise Exception("Unable to load images: {}, {}".format(imgPath1, imgPath2))
    if im1 is None:
        raise Exception("Unable to load image: {}".format(imgPath1))
    if im2 is None:
        raise Exception("Unable to load image: {}".format(imgPath2))

    rgbImg1 = cv2.cvtColor(im1, cv2.COLOR_BGR2RGB)
    rgbImg2 = cv2.cvtColor(im2, cv2.COLOR_BGR2RGB)

    bb1 = align.getLargestFaceBoundingBox(rgbImg1)
    bb2 = align.getLargestFaceBoundingBox(rgbImg2)

    if bb1 is None:
        raise Exception("Unable to find a face: {}".format(imgPath1))
    if bb2 is None:
        raise Exception("Unable to find a face: {}".format(imgPath2))

    alignedFace1 = align.align(imgdim, rgbImg1, bb1,
                              landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)
    alignedFace2 = align.align(imgdim, rgbImg2, bb2,
                              landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)

    if alignedFace1 is None:
        raise Exception("Unable to align image: {}".format(imgPath1))
    if alignedFace2 is None:
        raise Exception("Unable to align image: {}".format(imgPath2))

    rep1 = net.forward(alignedFace1)
    rep2 = net.forward(alignedFace2)

    d = rep1 - rep2
    return d
