import imageio
import numpy as np
from matplotlib import pyplot as plt

img1 = imageio.imread('..\\img\\Lena_dark.tif')
hist, bins = np.histogram(img1.flatten(), 256, [0, 256])

img1_r = img1[..., 0]
img1_g = img1[..., 1]
img1_b = img1[..., 2]

img1_r_cdf = hist.cumsum()
img1_g_cdf = hist.cumsum()
img1_b_cdf = hist.cumsum()

img1_r_cdf2 = np.ma.masked_equal(img1_r_cdf, 0)
img1_r_cdf2 = (img1_r_cdf2 - img1_r_cdf2.min()) * 255 / (img1_r_cdf2.max() - img1_r_cdf2.min())
img1_r_cdf_result = np.ma.filled(img1_r_cdf2, 0).astype('uint8')

img1_g_cdf2 = np.ma.masked_equal(img1_g_cdf, 0)
img1_g_cdf2 = (img1_g_cdf2 - img1_g_cdf2.min()) * 255 / (img1_g_cdf2.max() - img1_g_cdf2.min())
img1_g_cdf_result = np.ma.filled(img1_g_cdf2, 0).astype('uint8')

img1_b_cdf2 = np.ma.masked_equal(img1_b_cdf, 0)
img1_b_cdf2 = (img1_b_cdf2 - img1_b_cdf2.min()) * 255 / (img1_b_cdf2.max() - img1_b_cdf2.min())
img1_b_cdf_result = np.ma.filled(img1_b_cdf2, 0).astype('uint8')

img1_r_new = img1_b_cdf_result[img1_r]
img1_g_new = img1_g_cdf_result[img1_g]
img1_b_new = img1_r_cdf_result[img1_b]

img1_result = np.dstack((img1_r_new, img1_g_new, img1_b_new))

fig, ax = plt.subplots(1, 2, figsize=(10, 10))
ax[0].imshow(img1)
ax[0].set_title('Original Image')

ax[1].imshow(img1_result)
ax[1].set_title('Result Image')

plt.show()