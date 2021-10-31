import cv2 as cv
import numpy as np

img= cv.imread('img\\Lena512warna.bmp')

cv.imshow('Lena berwarna', img)
cv.waitKey(0)

# Rumus grayscale => G= 0.2989 R + 0.5870 G + 0.1140 B
[b, g, r]= [ img[:,:,i] for i in range(img.shape[2])]
cv.imshow('Lena grayscale tapi salah', g)
cv.waitKey(0)
# print(b==img[:, :, 0])

correct_grayscale= np.uint8(0.2989*r + 0.5870*g + 0.1140*b) # One line code: correct_grayscale= np.dot(img[:,:,:],[0.5870, 0.1140, 0.2989])
# print(correct_grayscale)
cv.imshow('Lena grayscale yang benar', correct_grayscale)
cv.waitKey(0)