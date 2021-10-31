from skimage import img_as_ubyte
from skimage.io import imread, imshow, show
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# -------------------------- skimage to cv ---------------------------------

skimage_img= imread('img\\Lena512warna.bmp')
# imshow(skimage_img)
# show()

cv_img = img_as_ubyte(skimage_img)

# Karena skimage rgb dan cv gbr, maka perlu dikonversi dulu
cv_img= cv.cvtColor(cv_img, cv.COLOR_RGB2BGR)

cv.imshow('skimage to cv', cv_img[:, :, 0])
cv.waitKey(0)

# -------------------------- cv to skimage ---------------------------------

cv_img2= cv.imread('img\\Lena512warna.bmp')
cv_img2= cv.cvtColor(cv_img2, cv.COLOR_BGR2RGB)

skimage_img2= cv_img2.astype(np.uint64)

print(skimage_img)
print('------------')
# print(skimage_img2[..., 0]==skimage_img2[:, 0])

# imshow(skimage_img2, vmin=0, vmax= 255)
# show()

# Plot pada matpolotlib

plt.imshow(skimage_img2[..., 0])
plt.show()