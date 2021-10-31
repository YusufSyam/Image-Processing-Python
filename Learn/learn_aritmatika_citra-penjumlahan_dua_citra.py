import cv2 as cv

# Penjumlahan citra / penggabungan dua citra

# Perlu diingat kalau ingin menjumlahkan dua buah citra, shape / ukuran nya harus sama (panjang x lebar)
# Jika berbeda, gambar yg lebih besar harus dispesifikan pixel panjang dan lebar
# (yang shape sama dengan gambar kecil) Dari bagian gambar yang akan dijumlahkan

img_tom= cv.imread('..\\img\\taj_tom.png')
img_jerry= cv.imread('..\\img\\taj_jerry.png')

cv.imshow('tom', img_tom)
cv.imshow('jerry', img_jerry)
cv.waitKey(0)

# Penambahan citra

img_tom_and_jerry= img_tom + img_jerry
cv.imshow('tom and jerry', img_tom_and_jerry)
cv.waitKey(0)

# Cara di atas tidak dianjurkan karena tidak dilakukan clipping
# Cara yang direkomendasikan
img_tom_and_jerry2= cv.add(img_tom, img_jerry)
cv.imshow('tom and jerry 2', img_tom_and_jerry2)
cv.waitKey(0)