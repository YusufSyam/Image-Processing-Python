import imageio
import numpy as np
from matplotlib import pyplot as plt

img2 = imageio.imread('..\\img\\bit_plane.tif')

lst = []
for i in range(img2.shape[0]):
    for j in range(img2.shape[1]):
        lst.append(np.binary_repr(img2[i][j], width=8))

img2_one_bit = (np.array([int(i[7]) for i in lst], dtype=np.uint8) * 1).reshape(img2.shape[0], img2.shape[1])
img2_two_bit = (np.array([int(i[6]) for i in lst], dtype=np.uint8) * 2).reshape(img2.shape[0], img2.shape[1])
img2_three_bit = (np.array([int(i[5]) for i in lst], dtype=np.uint8) * 4).reshape(img2.shape[0], img2.shape[1])
img2_four_bit = (np.array([int(i[4]) for i in lst], dtype=np.uint8) * 8).reshape(img2.shape[0], img2.shape[1])
img2_five_bit = (np.array([int(i[3]) for i in lst], dtype=np.uint8) * 16).reshape(img2.shape[0], img2.shape[1])
img2_six_bit = (np.array([int(i[2]) for i in lst], dtype=np.uint8) * 32).reshape(img2.shape[0], img2.shape[1])
img2_seven_bit = (np.array([int(i[1]) for i in lst], dtype=np.uint8) * 64).reshape(img2.shape[0], img2.shape[1])
img2_eight_bit = (np.array([int(i[0]) for i in lst], dtype=np.uint8) * 128).reshape(img2.shape[0], img2.shape[1])

fig, ax = plt.subplots(3, 3, figsize=(8, 8))
ax[0][0].imshow(img2, cmap='gray')
ax[0][0].set_title('Original Image')

ax[0][1].imshow(img2_one_bit, cmap='gray')
ax[0][1].set_title('One Bit Plane')

ax[0][2].imshow(img2_two_bit, cmap='gray')
ax[0][2].set_title('Two Bit Plane')

ax[1][0].imshow(img2_three_bit, cmap='gray')
ax[1][0].set_title('Three Bit Plane')

ax[1][1].imshow(img2_four_bit, cmap='gray')
ax[1][1].set_title('Four Bit Plane')

ax[1][2].imshow(img2_five_bit, cmap='gray')
ax[1][2].set_title('Five Bit Plane')

ax[2][0].imshow(img2_six_bit, cmap='gray')
ax[2][0].set_title('Six Bit Plane')

ax[2][1].imshow(img2_seven_bit, cmap='gray')
ax[2][1].set_title('Seven Bit Plane')

ax[2][2].imshow(img2_eight_bit, cmap='gray')
ax[2][2].set_title('Eight Bit Plane')

plt.tight_layout()
plt.show()
