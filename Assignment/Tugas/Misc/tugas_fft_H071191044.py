# Nama: Muh. Yusuf Syam
# NIM: H071191044

import imageio
import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack
from matplotlib.colors import LogNorm
%matplotlib inline

# Citra asli
img = imageio.imread('period_input.jpeg', as_gray=True).astype('float64')/255

# Frekuensi spektrum gambar noisy period_input.jpeg
im_fft = fftpack.fft2(img)

# Mendefinisikan koefisien pecahan dari setiap direksi
keep_fraction = 0.1
im_fft2 = im_fft.copy()

# Atur r dan c ke dalam jumlah baris dan kolom pada array. 
r, c = im_fft2.shape

# Filter spektrum
# Setel semua baris menjadi nol dengan indeks antara r * keep_fraction dan r * (1-keep_fraction) 
im_fft2[int(r*keep_fraction):int(r*(1-keep_fraction))] = 0
im_fft2[:, int(c*keep_fraction):int(c*(1-keep_fraction))] = 0

# Merekonstruksi citra yang telah di-denoised dari spektrum yang difilter
im_new = fftpack.ifft2(im_fft2).real

# Menampilkan perbandingan citra asli dan citra yang telah direkonstruksi
fig, ax = plt.subplots(1,2, figsize=(10,10))
ax[0].set_title('Original Image')
ax[0].imshow(im, cmap='gray')
ax[1].set_title('Reconstructed Image')
ax[1].imshow(im_new, cmap='gray')