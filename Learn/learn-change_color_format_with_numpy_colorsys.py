import imageio

import numpy as np
import colorsys

import matplotlib.pyplot as plt

rgb_hsv = np.vectorize(colorsys.rgb_to_hsv)
hsv_rgb = np.vectorize(colorsys.hsv_to_rgb)
rgb_yiq = np.vectorize(colorsys.rgb_to_yiq)
yiq_rgb = np.vectorize(colorsys.yiq_to_rgb)

img1= imageio.imread('img\\peppers512warna.bmp')

r= img1[..., 0]
g= img1[..., 1]
b= img1[..., 2]


img1_hsv= np.dstack((rgb_hsv(r, g, b)))

plt.imshow(img1_hsv)
plt.show()