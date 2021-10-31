from matplotlib import pyplot as plt
import cv2 as cv

img= cv.cvtColor(cv.imread('..\\img\\dahyun_low_contrast.png'), cv.COLOR_BGR2GRAY)

plt.style.use('seaborn-pastel')
fig, (img_plot, hist_plot)= plt.subplots(ncols= 2)

img_plot.imshow(img, cmap='gray')
hist_plot.hist(img.flatten(), bins=256, range=[0,256])

plt.tight_layout()
plt.show()

# Kita meregangkan kontras agar citra menjadi lebih jelas (dalam beberapa kasus)
# Bukti suatu citra tidak mempunyai kontras yang regang bisa dilihat dari histogramnya yang sempit

# -------------- Meregangkan kontras --------------------

img_min= min(img.flatten())
img_max= max(img.flatten())

# Dan berikut fungi peregangan kontrasnya
img_new= (img - img_min) * (255/(img_max - img_min))

plt.style.use('seaborn-pastel')
fig, (img_new_plot, hist_plot)= plt.subplots(ncols= 2)

img_new_plot.imshow(img_new, cmap='gray')
hist_plot.hist(img_new.flatten(), bins=256, range=[0,256])

plt.tight_layout()
plt.show()

# # Peregangan kontras yang lebih 'terang'
# m= 255/(img_max-img_min)
# c= 255 -(m*img_max)
# img_new= (m*img) + c