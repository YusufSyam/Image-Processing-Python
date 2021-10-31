import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img= np.ones((500, 1000, 3), dtype= np.uint8) * 255

# Kita akan mengiterasi setiap 25 (jadi setiap 25 pixel akan berbeda warna)

iterator= 25
for i in range(0, img.shape[1], iterator):
    for j in range(0, img.shape[0], iterator):
        img[j:j+iterator, i:i+iterator]= (np.random.randint((255, 255, 255)))

# rand= (np.random.randint((255, 255, 255)))
# img[50:200, 0:10]=  rand
#
# print(rand)
# print(rand + 100)
# print(rand + 100)

# img = cv.convertScaleAbs(img)
cv.imshow('b', img)
cv.waitKey(0)

#--------- using Matplotlib ------------
##plt.imshow(img, cmap = 'gray')
##plt.tick_params(axis='y',left = False,labelleft = False)
##plt.xticks([0,50,100,150,200,255])
##plt.show()