import cv2 as cv
from matplotlib import pyplot as plt

img= cv.cvtColor(cv.imread('img\\mina.png'), cv.COLOR_BGR2RGB)

plt.imshow(img)
plt.show()