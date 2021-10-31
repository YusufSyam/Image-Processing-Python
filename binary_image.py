import cv2 as cv
import numpy as np

# Jika ingin menghasilkan gambar hitam putih, gambar sebaiknya bersifat grayscale terlebih dahulu
grayscale_img= cv.imread('img\\Lena.bmp')

cv.imshow('Lena Grayscale', grayscale_img)
cv.waitKey(0)

one_dim_grayscale_img= grayscale_img[:, :, 0]

# Membuat threshold
threshold= 128

# Membuat fungsi threshold
def bin(img, threshold=128):
    bin_img= np.zeros((img.shape[1], img.shape[0]), dtype=np.uint8)

    for i in range(img.shape[1]):
        for j in range(img.shape[0]):
            bin_img[j, i]= 0 if(img[j, i]<threshold) else 255

    return np.uint8(bin_img)

binary_img= bin(one_dim_grayscale_img, threshold)

cv.imshow('Lena Binary', binary_img)
cv.waitKey(0)