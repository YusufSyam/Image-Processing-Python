import cv2 as cv

img= cv.imread('img\\jihyo.png')
print(img.shape[0:2])

img2= cv.imread('img\\chaeyoung.png')
img2= cv.resize(img2, (820,461))
cv.imshow('chae',img2)
cv.waitKey(0)