import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img= np.ones((500, 500, 3), dtype= np.uint8) * (255, 0, 0)

img[0:20, 0:20]= np.zeros((20, 20, 3), dtype=np.uint8)
img = cv.convertScaleAbs(img) # Atau  img= np.uint8(img)
cv.imshow('b', img)
cv.waitKey(0)

#--------- using Matplotlib ------------
##plt.imshow(img, cmap = 'gray')
##plt.tick_params(axis='y',left = False,labelleft = False)
##plt.xticks([0,50,100,150,200,255])
##plt.show()