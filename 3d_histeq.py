from matplotlib import pyplot as plt
import cv2 as cv

img= cv.cvtColor(cv.imread('img\\dahyun_low_contrast.png'), cv.COLOR_BGR2RGB)

plt.style.use('seaborn-pastel')
fig, (img_plot, hist_plot)= plt.subplots(ncols= 2)

img_plot.imshow(img, cmap='gray')
hist_plot.hist(img.flatten(), bins=256, range=[0,256])

plt.tight_layout()
plt.show()

# Histogram equalization for 3 channel

[r_histeq, g_histeq, b_histeq]= [cv.equalizeHist(i) for i in cv.split(img)]

img_new= cv.merge([r_histeq, g_histeq, b_histeq])

fig, (img_new_plot, hist_plot)= plt.subplots(ncols= 2)

img_new_plot.imshow(img_new, cmap='gray')
img_new_plot.set_title('Histogram equalized image')

hist_plot.hist(img_new.flatten(), bins=256, range=[0,256])

plt.tight_layout()
plt.show()
