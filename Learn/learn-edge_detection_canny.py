import cv2 as cv
from matplotlib import pyplot as plt

img= cv.cvtColor(cv.imread('..\\img\\shape.jpg'), cv.COLOR_BGR2GRAY)

# Algoritma canny pada dasarnya adalah melakukan threshold setelah melakukan
# Edge detection entah dengan sobel maupun laplace

# Untuk memaksimalkan hasil deteksi tepi, disarankan melakukan pelembutan citra
# Menggunakan gaussian blur
img_blur= cv.GaussianBlur(img, (3,3), 0)

# threshold1= threshold ke bawah, threshold2= threshold ke atas
# apertureSize= besar kernel
img_canny = cv.Canny(img_blur, threshold1=100, threshold2=200, apertureSize=3)

plt.figure(figsize=(10,4))
plt.subplot(131)
plt.imshow(img, cmap='gray')
plt.title('original image')

plt.subplot(132)
plt.imshow(img_blur, cmap='gray')
plt.title('blurred image')

plt.subplot(133)
plt.imshow(img_canny, cmap='gray')
plt.title('laplace edge image')

plt.tight_layout()
plt.show()