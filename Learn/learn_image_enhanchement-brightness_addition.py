# Untuk menambah keterangan bisa dengan operasi + atau x
# Untuk mengurangi, - atau :

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img= cv.imread('..\\img\\camera.bmp').astype(np.uint8)

# ------------------------ Menambah brightness dengan penambahan ------------------------------

# >>>>>>>>>> Cara 1, Penambahan deengan skalar
# Jika kita langsung tambah seperti ini, pixel yang melewati 255 akan dimodulo
# Jadi gambar tidak akan tampak seperti yang diinginkan
img_bplus1= img + 100

cv.imshow('Adding brightness 1.1', img_bplus1)
cv.waitKey(0)

# Maka kita harus melakukan clipping

# Pertama-tama kita harus mengubah tipe data dari img_bplus menjadi int (agar tidak dimodulo)
img_bplus1_correct= img.astype('int')

# Lalu kita tambah dengan skalar (penambahan brightness)
img_bplus1_correct+= 100

# Lalu kita lakukan clipping
img_bplus1_correct= np.clip(img_bplus1_correct, a_min=0, a_max=255)

# Konversi kembali ke uint8
img_bplus1_correct= img_bplus1_correct.astype(np.uint8)

cv.imshow('Adding brightness 1.2', img_bplus1_correct)
cv.waitKey(0)

# # >>>>>>>>>> Cara 2, cv.add() , secara otomatis melakukan clipping

def make_grey_color(addition=50):
    temp= img.copy()
    temp.fill(addition)
    return temp

# Penambahan dengan sesama array
img_bplus2= cv.add(img, make_grey_color(100))

# Penambahan dengan skalar
img_bplus2_2= cv.add(img, (100,100,100,100))

cv.imshow('Adding brightness 2', img_bplus2)
cv.imshow('Adding brightness 2', img_bplus2_2)
cv.waitKey(0)

# ------------------------ Menambah brightness dengan perkalian ------------------------------

# >>>>>>>>>> Cara 1, Perkalian dengan skalar
# Menambah kecerahan dengan perkalian secara tidak langsung memperkontras gambar
img_bplus3= np.clip((img.astype('int') * 1.5), 0, 255).astype(np.uint8)

cv.imshow('Adding brightness 3', img_bplus3)
cv.waitKey(0)

# >>>>>>>>>> Cara 2, Perkalian dengan cv
# Menambah kecerahan dengan perkalian secara tidak langsung memperkontras gambar
# img_bplus4=
img_bplus4= cv.multiply(img, (1.5, 1.5, 1.5, 1.5), scale=0.5)

cv.imshow('Adding brightness 4', img_bplus3)
cv.waitKey(0)

# Operasi2 opencv untuk mengurangi kecerahan: cv.divide, cv.substract