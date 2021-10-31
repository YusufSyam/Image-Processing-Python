import imageio
import numpy as np
from matplotlib import pyplot as plt
import cv2

img8= imageio.imread('..\\img\\keyboard.tif')

pixel_vals= img8.reshape((-1,3))
pixel_vals= np.float32(pixel_vals)

criteria= (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 1)

k= 3
_, labels, (centers)= cv2.kmeans(pixel_vals, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

centers= np.uint8(centers)

img_8_data= centers[labels.flatten()]
img_8_result= img_8_data.reshape((img8.shape))

fig, ax= plt.subplots(1,2, figsize=(10,10))
ax[0].imshow(img8, cmap='gray')
ax[0].set_title('Original Image')
ax[1].imshow(img_8_result, cmap='gray')
ax[1].set_title('Result Image')

plt.show()