import cv2 as cv
import numpy as np

def show(img, title='title'):
    cv.imshow(title, img)
    cv.waitKey(0)

# ----------------------- Masking --------------------------
# Masking adalah cara untuk hanya menampilkan bagian tertentu dari gambar
# Mask pada masking harus lah berupa citra biner

# Gambar yang ingin dimasking
img= cv.imread('..\\img\\twice\\twice (2).png')
show(img, 'jihyo')

# Membuat mask
mask= np.zeros(img.shape[:2], dtype='uint8') # Untuk masking, hanya length dan width yang perlu sama

# Membuat rectangle di dalam kanvas yang nantinya hanya bagian ini yang ditampilkan
kiri_atas_mask= ((img.shape[1]//2)-80, (img.shape[0]//4)-80)
kanan_bawah_mask= ((img.shape[1]//2)+150, (img.shape[0]//4)+150)
cv.rectangle(mask, kiri_atas_mask, kanan_bawah_mask, (255,255,255), -1)
show(mask, 'mask')

masked= cv.bitwise_and(img, img, mask=mask)
show(masked, 'masked implemented')

# ---------------------------------------------------
# Kita juga bisa melakukan 2 masking pada satu gambar
# Masking juga tidak harus berbentuk kotak

mina= cv.imread('..\\img\\mina.png')
show(mina, 'mina')

mask2= np.zeros(img.shape[:2], dtype='uint8')
# Menggambar lingkaran pada kanvas mask
cv.circle(mask2, (415, 210), 130, 255, -1) # Di sini saya mendapatkan centernya pake matplotlib pyplot
show(mask2, 'mask lingkaran')

# Menggambar lagi kotak pada kanvas mask
cv.rectangle(mask2, (472, 168), (mask2.shape[1], mask2.shape[0]), 255, -1)
show(mask2, 'mask lingkaran lalu kotak')

masked= cv.bitwise_and(mina, mina, mask= mask2)
show(masked, 'masked implemented (2)')

# Tes tes
# show(cv.bitwise_and(img, mina, mask=mask2))