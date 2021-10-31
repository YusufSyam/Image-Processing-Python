import numpy as np
import cv2 as cv

def show(img, title='title'):
    cv.imshow(title, img)
    cv.waitKey(0)

persegi= np.zeros((300,300), dtype='uint8') # uint8 artinya integer dari 0-255
cv.rectangle(persegi, (50,50), (250,250), (255,255,255), -1)
show(persegi, 'persegi')

lingkaran= np.zeros((300,300), dtype='uint8')
cv.circle(lingkaran, ((lingkaran.shape[1]//2),(lingkaran.shape[0]//2)), 120, (275, 255,255), -1)
show(lingkaran, 'lingkaran')

# Operasi AND / dan (biasanya dipakai untuk masking)
operasi_dan= cv.bitwise_and(persegi, lingkaran)
show(operasi_dan, 'and')

# Operasi OR / atau
operasi_atau= cv.bitwise_or(persegi, lingkaran)
show(operasi_atau, 'or')

# Operasi NOT / negasi
operasi_not= cv.bitwise_not(persegi)
show(operasi_not, 'not persegi')

# Operasi XOR / tidak mengambil irisan (kebalikan dari AND)
operasi_xor= cv.bitwise_xor(persegi, lingkaran)
show(operasi_xor, 'xor')

# Note: Untuk operasi and , kita bisa saja melakukan persegi & lingkaran
# Namun itu hanya berlaku untuk gambar biner, dan untuk melakukan itu pada gambar gray/warna
# Tetap bisa, tapi akan melakukan proses yang ribet