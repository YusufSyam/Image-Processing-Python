import cv2
import numpy as np
import matplotlib.pyplot as plt

img = np.zeros((100,256),dtype=np.uint8)
for i in range(img.shape[1]):
    for j in range(img.shape[0]):
        img[j,i]=i

cv2.imshow('a',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#--------- using Matplotlib ------------
##plt.imshow(img, cmap = 'gray')
##plt.tick_params(axis='y',left = False,labelleft = False)
##plt.xticks([0,50,100,150,200,255])
##plt.show()