import cv2 as cv
import numpy as np

# Membuat canvas untuk menggambar line atau shape, bisa juga menggambar di foto btw
# Canvas dibuat menggunakan numpy.zeros yang membuat matriks bernilai 0 dgn shape yg diinginkan, arg pertama shape
canvas= np.zeros((400,700,3),dtype='uint8')

cv.imshow('Canvas',canvas)
cv.waitKey(0)

# -------------------------------- bangun 2d ------------------------------
# Menggambar line/garis pada canvas, argument kedua adalah posisi awal garis, argument ketiga posisi akhir
warna_garis= (74,133,235) # Btw ini format gbr
cv.line(canvas, (0,0), tuple(reversed(canvas.shape[0:2])), warna_garis)
cv.imshow('Canvas', canvas)
cv.waitKey()

# Membuat fungsi supaya nda capek
def imshow(c):
    cv.imshow('Canvas', c)
    cv.waitKey(0)

# Menggambar kotak, menambahkan 1 argument ketebalan
cv.rectangle(canvas, (10,10), tuple(reversed(np.array(canvas.shape[0:2])-10)), (255,255,255), 3)
imshow(canvas)

# print(tuple(reversed(np.array(canvas.shape[0:2])-10)))

# Membuat canvas baru warna putih, tidak bisa cara di bawah
# canvas2= np.full((400,700,3), 255)
canvas2= canvas
canvas2.fill(255)
imshow(canvas2)

# Lingkaran
cx_canvas2, cy_canvas2= canvas2.shape[1]//2, canvas2.shape[0]//2 # Pertama menentukan center x,y
cv.circle(canvas2, (cx_canvas2,cy_canvas2), 50, (warna_garis), -1) # 50 adalah radius, set ketebalan menjadi -1 agar warna menjadi fill
imshow(canvas2)

# Shape lain: ellipse, polygon

# ----------------------------------- teks ke gambar -----------------------------------
font= cv.FONT_HERSHEY_SIMPLEX # Font
cv.putText(canvas2, text='Once a once always be a once', org=(0,cy_canvas2), fontFace=font, fontScale=1, color=(0,0,0), thickness=2)
imshow(canvas2)

# Membuat text di tengah
text= 'Once a once always be a once'
textsize = cv.getTextSize(text, font, 1, 2)[0]

cx_text= (canvas2.shape[1]-textsize[0])//2
cy_text= (canvas2.shape[0]-textsize[1])//2

# Membersihkan canvas
canvas2.fill(255)

cv.putText(canvas2, text, (cx_text,cy_text), font, 1, (216, 176, 255), 3)
imshow(canvas2)

# --------------------------------- Menggabungkan gambar ------------------------------
img_chaeyoung= cv.imread('..\\img\\chaeyoung_big.png')

# Untuk menggabungkan 2 gambar, kedua gambar tersebut harus mempunyai size x dan y yang sama
img_chaeyoung= cv.resize(img_chaeyoung, tuple(reversed(canvas2.shape[0:2])))
imshow(img_chaeyoung)

# # Menggabungkan gambar tanpa weight
# combined_img= cv.add(canvas2, img_chaeyoung)
# imshow(combined_img)

# Menggabungkan gambar dengan weight
combined_img= cv.addWeighted(canvas2, 0.6, img_chaeyoung, 0.4, 0)
imshow(combined_img)