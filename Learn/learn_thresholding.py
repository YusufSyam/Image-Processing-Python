import cv2 as cv
from matplotlib import pyplot as plt
from skimage.io import imread
from skimage.color import rgb2gray

# img= imread('..\\img\\Lena512warna.bmp')
img= imread('..\\img\\tree.jpeg')

# https://datacarpentry.org/image-processing/
img= rgb2gray(img)

img2= img < 0.5

plt.imshow(img2, cmap='gray')
plt.show()