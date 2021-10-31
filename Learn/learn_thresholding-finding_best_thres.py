import cv2 as cv
from matplotlib import pyplot as plt
from skimage.io import imread
from skimage.color import rgb2gray
import numpy as np

# img= imread('..\\img\\Lena512warna.bmp')
img= imread('..\\img\\tree.jpeg')

# https://datacarpentry.org/image-processing/
img= rgb2gray(img)

thres_list= np.linspace(0.1, 1, 10)
print(thres_list)

fig, ax= plt.subplots(nrows=2, ncols=5, figsize=(12,6))
nrows= fig.axes[0].get_subplotspec().get_topmost_subplotspec().get_gridspec().get_geometry()[1]

for i in range(len(thres_list)):
    temp_img= img < thres_list[i]

    row= int(np.floor(i/nrows))
    col= i%nrows

    ax[row][col].imshow(temp_img, cmap='gray')
    ax[row][col].set_title('{:.1f}'.format(thres_list[i]))

plt.tight_layout()
plt.show()
