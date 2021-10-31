import cv2 as cv
from matplotlib import pyplot as plt

img= cv.cvtColor(cv.imread('..\\img\\Lena.bmp'), cv.COLOR_BGR2GRAY)

# Untuk memaksimalkan hasil deteksi tepi, disarankan melakukan pelembutan citra
# Menggunakan gaussian blur
img_blur= cv.GaussianBlur(img, (3,3), 0)

img_laplacian = cv.Laplacian(img_blur,cv.CV_64F)

plt.figure(figsize=(10,4))
plt.subplot(131)
plt.imshow(img, cmap='gray')
plt.title('original image')

plt.subplot(132)
plt.imshow(img_blur, cmap='gray')
plt.title('blurred image')

plt.subplot(133)
plt.imshow(img_laplacian, cmap='gray')
plt.title('laplace edge image')

plt.tight_layout()
plt.show()