import numpy as np
import cv2 as cv

x, y= 500, 500

arr= np.zeros((x, y), dtype=np.uint8)

for i in range(arr.shape[1]):
    for j in range(arr.shape[0]):
        arr[j, i]= np.random.randint(255)

cv.imshow('a', arr)
cv.waitKey(0)

f = open("tes_raw_format.RAW", "w")

f.write(f'{x} {y}')
for i in range(arr.shape[1]):
    f.write('\n')
    for j in range(arr.shape[0]):
        f.write(str(arr[j, i])+' ')

f.close()