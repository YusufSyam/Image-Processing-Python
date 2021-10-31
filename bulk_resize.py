import cv2 as cv
import glob

path= glob.glob('C:/Users/LENOVO/PycharmProjects/LearnOpenCV/img/twice/*.png')

for file in path:
    img= cv.imread(file)
    img = cv.resize(img, (820, 461))

    img_name = file.split('\\')[-1][0:-4]
    cv.imwrite(('output_img\\twice_data_mining\\' + img_name + '.png'), img)