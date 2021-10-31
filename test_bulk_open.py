import cv2 as cv
import glob

# Cara 1
path= glob.glob('C:/Users/LENOVO/PycharmProjects/LearnOpenCV/img/img_p1/*.png')

for file in path:
    img= cv.imread(file)
    cv.imshow('Twice', img)
    cv.waitKey(0)