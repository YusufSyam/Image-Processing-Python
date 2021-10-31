# Niblack dan sauvola threshold merupakan jenis threshold yang cocok digunakan pada gambar berisi teks

from matplotlib import pyplot as plt

# Mengimport image berisi teks yang disediakan scikit image
from skimage.data import page

# Mengimport niblack dan sauvola threshold, otsu threshold untuk threshold global (hanya untuk dibandingkan)
from skimage.filters import threshold_otsu, threshold_niblack, threshold_sauvola

image= page()

global_threshold= image > threshold_otsu(image)

window_size= 25

thresh_niblack = threshold_niblack(image, window_size=window_size, k=0.8)
thresh_sauvola = threshold_sauvola(image, window_size=window_size)

binary_niblack = image > thresh_niblack
binary_sauvola = image > thresh_sauvola

plt.figure(figsize=(8, 7))
plt.subplot(2, 2, 1)
plt.imshow(image, cmap=plt.cm.gray)
plt.title('Original')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.title('Global Threshold')
plt.imshow(global_threshold, cmap=plt.cm.gray)
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(binary_niblack, cmap=plt.cm.gray)
plt.title('Niblack Threshold')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(binary_sauvola, cmap=plt.cm.gray)
plt.title('Sauvola Threshold')
plt.axis('off')

plt.show()