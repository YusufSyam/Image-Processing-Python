import cv2 as cv
from matplotlib import pyplot as plt

img= cv.cvtColor(cv.imread('..\\img\\Lena.bmp'), cv.COLOR_BGR2GRAY)

# Untuk memaksimalkan hasil deteksi tepi, disarankan melakukan pelembutan citra
# Menggunakan gaussian blur
img_blur= cv.GaussianBlur(img, (3,3), 0)

# Kita akan melakukan deteksi tepi pada x, y, dan xy

# Deteksi tepi x
# Parameter dx=1 , dx= 0 artinya akan melakukan operasi sobel x, ksize adalah kernel size
img_sobelx= cv.Sobel(src=img_blur, ddepth=cv.CV_64F, dx=1, dy=0, ksize=5)

# Deteksi tepi y, dx=0 dy=1
img_sobely= cv.Sobel(img_blur, cv.CV_64F, dx=0, dy=1, ksize=5)

# Deteksi tepi xy (direkomendasikan), dx=1 dy=1
img_sobelxy= cv.Sobel(img_blur, cv.CV_64F, dx=1, dy=1, ksize=5)

plt.figure(figsize=(10,6))

plt.subplot(231)
plt.imshow(img, cmap='gray')
plt.title('original image')

plt.subplot(233)
plt.imshow(img_blur, cmap='gray')
plt.title('blurred image')

plt.subplot(234)
plt.imshow(img_sobelx, cmap='gray')
plt.title('sobelx image')

plt.subplot(235)
plt.imshow(img_sobely, cmap='gray')
plt.title('sobely image')

plt.subplot(236)
plt.imshow(img_sobelxy, cmap='gray')
plt.title('sobelxy image')

plt.tight_layout()
plt.show()