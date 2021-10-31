from matplotlib import pyplot as plt
import cv2 as cv

# Histogram equalization adalah teknik pemrosesan citra yang menyesuaikan kontras global suatu gambar
# dengan memperbarui distribusi intensitas piksel histogram gambar, dengan ini
# area dengan kontras rendah akan menjadi lebih tinggi pada gambar keluaran.

img= cv.cvtColor(cv.imread('..\\img\\dahyun_low_contrast.png'), cv.COLOR_BGR2GRAY)

plt.style.use('seaborn-pastel')
fig, (img_plot, hist_plot)= plt.subplots(ncols= 2)

img_plot.imshow(img, cmap='gray')
hist_plot.hist(img.flatten(), bins=256, range=[0,256])

plt.tight_layout()
plt.show()

# -------------- Meregangkan kontras --------------------

img_new= cv.equalizeHist(img)

fig, (img_new_plot, hist_plot)= plt.subplots(ncols= 2)

img_new_plot.imshow(img_new, cmap='gray')
hist_plot.hist(img_new.flatten(), bins=256, range=[0,256])

plt.tight_layout()
plt.show()

# Pada kasus tertentu, meregangkan kontras juga akan memunculkan noise
# Untuk mengatasinya kita bisa menggunakan adaptive histogram equalization

clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
# Parameter clipLimit: pembatasan kontras, semakin besar semakin regang kontrasnya
# tileGridSize: Membagi gambar input menjadi array M x N
# kemudian menerapkan pemerataan histogram ke setiap aras lokal (menggeser pixel per pixel)

# Setelah membuat clahe nya baru kita mengapplynya ke gambar dan menyimpannya ke variabel baru
img_new_adaptive = clahe.apply(img)

fig, (img_new_adaptive_plot, hist_plot)= plt.subplots(ncols= 2)

img_new_adaptive_plot.imshow(img_new_adaptive, cmap='gray')
img_new_adaptive_plot.set_title('adaptive histogram equalization')

hist_plot.hist(img_new_adaptive.flatten(), bins=256, range=[0,256])

plt.tight_layout()
plt.show()