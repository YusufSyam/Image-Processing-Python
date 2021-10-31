from skimage import io
from matplotlib import pyplot as plt

img= io.imread('..\\img\\Lena512warna.bmp')

fig, (plot_img, plot_hist_img)= plt.subplots(ncols=2, figsize=(10,4))

# Memplot gambar
plot_img.imshow(img)

# Memplot histogram

hist_img= img.flatten()
# Flatten adalah fungsi untuk mengubah n dimensi array menjadi 1 dimensi, karena seperti yang kita tau
# Plot histogram membutuhkan 1d array. Kita tidak menggunakan ravel() karena ravel memengaruhi imagenya

# Bins adalah seberapa banyak bar
# Range adalah batas bawah dan atas dari bins
plot_hist_img.hist(hist_img, bins=256, range=[0,256])

plt.show()

# ------------------------ Dengan opencv -----------------------
# Menghitung histogram dengan built in fungsi opencv

import cv2 as cv

img2= cv.imread('..\\img\\Lena512warna.bmp')

histr= cv.calcHist(images=img2, channels=[0], mask=None, histSize=[256], ranges=[0,256])
plt.plot(histr)
plt.show()