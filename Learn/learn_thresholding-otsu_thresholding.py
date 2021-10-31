import imageio
import numpy as np
from matplotlib import pyplot as plt
from skimage.filters import threshold_otsu

img8= imageio.imread('..\\img\\bubble.tif')

thresh= threshold_otsu(img8)
binary= img8 > thresh

fig, axes= plt.subplots(ncols=2, figsize=(10, 10))

ax= axes.ravel()
ax[0], ax[1]= plt.subplot(1, 3, 1), plt.subplot(1, 3, 2)

ax[0].imshow(img8, cmap=plt.cm.gray)
ax[0].set_title('Original Image')
ax[0].axis('off')

ax[1].imshow(binary, cmap=plt.cm.gray)
ax[1].set_title('Thressholded Image')
ax[1].axis('off')

plt.tight_layout()
plt.show()