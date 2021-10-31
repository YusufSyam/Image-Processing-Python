import cv2 as cv
import numpy as np

def show(img, title='title'):
    cv.imshow(title, img)
    cv.waitKey(0)

img= cv.imread('..\\img\\twice\\twice (1).png')
show(img)

# Seperti yang kita tau, urutan channel rgb di cv2 adalah gbr
(b, g, r)= cv.split(img)

cv.imshow('R', r)
cv.imshow('G', g)
cv.imshow('B', b)
cv.waitKey(0)

# Menggabung kembali
merged= cv.merge([b,g,r])

# Karena gambarnya memang hanya satu channel, maka dia berupa grayscale
# Maka dari itu kita harus membuat citra 3 channel dan mengisi channel, misal untuk R, kita isi slot R, lalu slot G dan B kita isi dengan 0

# Kita membuat variabel matriks 0 dulu
zeros= np.zeros(img.shape[:2], dtype='uint8')

hanya_merah= cv.merge([zeros, zeros, r])
hanya_hijau= cv.merge([zeros, g, zeros])
hanya_biru= cv.merge([b, zeros, zeros])

cv.imshow('R', hanya_merah)
cv.imshow('G', hanya_hijau)
cv.imshow('B', hanya_biru)
cv.waitKey(0)

# tes menggabungkan salah
show(cv.merge([g, b, r]), 'tes')
