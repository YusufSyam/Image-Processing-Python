import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


img6 = cv.imread('..\\img\\shape2.tif')
gray = cv.cvtColor(img6,cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray,150,580,apertureSize = 3)

lines = cv.HoughLines(edges,1,np.pi/180,110)

for line in lines:
    for rho, theta in line:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv.line(img6, (x1, y1), (x2, y2), (0, 0, 255), 2)

fig, ax = plt.subplots(1,2, figsize=(10,10))
ax[0].imshow(edges, cmap='gray')
ax[0].set_title('Edges')

ax[1].imshow(img6, cmap='gray')
ax[1].set_title('Drawed Lines')

plt.show()