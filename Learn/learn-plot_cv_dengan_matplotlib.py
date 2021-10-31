import cv2 as cv
import matplotlib.pyplot as plt

img= cv.imread('..\\img\\twice\\twice (1).png')

plt.imshow(img)
# Seperti yang bisa kita lihat, gambarnya tidak sama dengan gambar yang sebenarnya
# Itu karena opencv membaca gambar secara gbr sementara matplotlib memplot gambar secara rgb

# Maka kita perlu menukar tempat r dengan b pada img
# Cara 1
img_fixed1= cv.imread('..\\img\\twice\\twice (1).png')
img_fixed1= cv.cvtColor(img_fixed1, cv.COLOR_BGR2RGB)

# Cara2 (lebih cepat)
# img_fixed2= cv.imread('..\\img\\twice\\twice (1).png')[...,::-1]

plt.imshow(img_fixed1)
plt.show()