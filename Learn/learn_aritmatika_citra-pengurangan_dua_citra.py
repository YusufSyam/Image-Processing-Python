import cv2 as cv

# Pengurangan citra
# Biasanya digunakan untuk mendeteksi kecacatan, atau perubahan pada sebuah citra

# Misal pada keadaan pertama kita punya citra seperti ini
img_first_state= cv.imread('..\\img\\taj.png')

# Lalu pada keadaan ke-dua terjadi sesuatu dan citra berubah
img_second_state= cv.imread('..\\img\\taj_tom.png')

cv.imshow('first state', img_first_state)
cv.imshow('second state', img_second_state)
cv.waitKey(0)

# Dan dengan mengurangi citra keadaan awal dan citra keadaan ke-dua
# Kita bisa mengetahui apa yang telah berubah pada citra awal

img_substraction= cv.subtract(img_first_state, img_second_state)
cv.imshow('substraction state', img_substraction)
cv.waitKey(0)
