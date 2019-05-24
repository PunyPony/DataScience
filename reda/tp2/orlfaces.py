import numpy as np
import PIL.Image as img
import matplotlib.pyplot as plt

import matplotlib
matplotlib.rcParams['figure.figsize'] = (17.0, 5.0)
matplotlib.rcParams['font.size'] = 15

def loadDataTrain(rep):
    trainimgs = np.empty([360, 112, 92], np.float32)
    trainlabels = np.empty(360, np.int32)
    
    for i in range(40):
        for j in range(9):
            trainimgs[i * 9 + j,] = img.open(rep + "/Train/s" + str(i + 1) + "/" + str(j+1) + ".pgm")
            
        trainlabels[i * 9 + j] = i

    return trainimgs.reshape((360, 112*92)).T, trainlabels

def loadDataTest(rep):
    testimgs = np.empty([40, 112, 92], np.float32)
    testlabels = np.empty(40, np.int32)
    
    for i in range(40):
        testimgs[i,] = img.open(rep + "Test/s" + str(i + 1) + "/s10.pgm")
        
    testlabels[i] = i

    return testimgs.reshape((40, 112 * 92)).T, testlabels

def showFaces(img):
    plt.imshow(img.reshape((112, 92)), cmap='Greys_r')
    plt.axis('off');

