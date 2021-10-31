import numpy as np
import colorsys

import matplotlib.pyplot as plt
import cv2 as cv

img1= cv.imread('img\\peppers512warna.bmp')
img1= cv.cvtColor(img1, cv.COLOR_BGR2RGB)
img2= cv.cvtColor(img1, cv.COLOR_RGB2HSV)

h, s, v= cv.split(img2)

r= img1[..., 0]
g= img1[..., 1]
b= img1[..., 2]


img1_hsv= np.dstack((r, g, b))

# x= cv.merge([h[0-360], s[0-1.], v[0-1.]])
plt.imshow(img2)
plt.show()