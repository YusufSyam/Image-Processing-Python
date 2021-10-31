import numpy as np
import cv2 as cv

def show(img, title='title'):
    cv.imshow(title, img)
    cv.waitKey(0)

img= cv.imread('..\\img\\twice\\twice (2).png')
show(img)

# Membuat matriks bernilai satu berbentuk (panjang x lebar x channel) seperti img, lalu nilainya dikali 100 menhasilkan citra abu2
x= np.ones(img.shape, dtype='uint8') * 100
show(x)

# Penambahan / add
penambahan_citra= cv.add(img, x)
show(penambahan_citra)

# Penambahan dengan weight
penambahan_citra_weight= cv.addWeighted(img, 0.8, x, 0.5, 0) # 0.8 adalah weigth img, 0.5 weight x, yang terakhir itu gamma
show(penambahan_citra_weight)

# Pengurangan / substract
substrak_citra= cv.subtract(img, x)
show(substrak_citra)