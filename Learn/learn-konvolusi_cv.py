import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img= cv.cvtColor(cv.imread('..\\img\\bush.jpg'), cv.COLOR_BGR2RGB)

# Sharpen
# kernel= np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])

# Outline
kernel= np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

# Blur
# kernel = np.array([[0.11111111111, 0.11111111111, 0.11111111111], [0.11111111111, 0.11111111111,0.11111111111], [0.11111111111,0.11111111111,0.11111111111]])

conv_result1= cv.filter2D(img, -1, kernel=kernel)
# for i in range(1):
#     conv_result1 = cv.filter2D(conv_result1, -1, kernel=kernel)

fig, ax= plt.subplots(ncols=2, figsize=(14,10))

ax[0].imshow(img)
ax[0].set_title('normal image')

ax[1].imshow(conv_result1)
ax[1].set_title('convolution image')

plt.show()

