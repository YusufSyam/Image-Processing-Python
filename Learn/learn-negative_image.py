import cv2 as cv

img= cv.imread('..\\img\\peppers512warna.bmp')
img= 255-img

cv.imshow('lena', img)
cv.waitKey(0)