import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

gray_image = cv.imread('..\\img\\shape.jpg', 0)

# Thresholding
thresh = 220
ret, thresh_binary = cv.threshold(gray_image, thresh, 255, cv.THRESH_BINARY)
ret, thresh_binary_inv = cv.threshold(gray_image, thresh, 255, cv.THRESH_BINARY_INV)
ret, thresh_trunc = cv.threshold(gray_image, thresh, 255, cv.THRESH_TRUNC)
ret, thresh_tozero = cv.threshold(gray_image, thresh, 255, cv.THRESH_TOZERO)
ret, thresh_tozero_inv = cv.threshold(gray_image, thresh, 255, cv.THRESH_TOZERO_INV)

names = ['Original Image', 'BINARY', 'THRESH_BINARY_INV', 'THRESH_TRUNC', 'THRESH_TOZERO', 'THRESH_TOZERO_INV']
images = gray_image, thresh_binary, thresh_binary_inv, thresh_trunc, thresh_tozero, thresh_tozero_inv

cols = 3
rows = 2
img_index = 0

fig, ax = plt.subplots(nrows=rows, ncols=cols, figsize=(14, 6))
for i in range(rows):
    for j in range(cols):
        ax[i][j].imshow(images[img_index], 'gray')
        ax[i][j].set_title(names[img_index])
        ax[i][j].set_xticks([]), ax[i][j].set_yticks([])

        img_index += 1

plt.show()

# Adaptive thresholding
ret, thresh_global = cv.threshold(gray_image, thresh, 255, cv.THRESH_BINARY)
thresh_mean = cv.adaptiveThreshold(gray_image, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
thresh_gaussian = cv.adaptiveThreshold(gray_image, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

names = ['Original Image', 'Global Thresholding', 'Adaptive Mean Threshold', 'Adaptive Gaussian Thresholding']
images = [gray_image, thresh_global, thresh_mean, thresh_gaussian]

cols = 2
rows = 2
img_index = 0

fig, ax = plt.subplots(nrows=rows, ncols=cols, figsize=(9, 6))
for i in range(rows):
    for j in range(cols):
        ax[i][j].imshow(images[img_index], 'gray')
        ax[i][j].set_title(names[img_index])
        ax[i][j].set_xticks([]), ax[i][j].set_yticks([])

        img_index += 1

plt.show()

