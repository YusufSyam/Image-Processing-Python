import cv2 as cv
import numpy as np

from matplotlib import pyplot as plt

img= cv.cvtColor(cv.imread('..\\img\\Lena512warna.bmp'), cv.COLOR_BGR2GRAY)

# Mengubah citra sesuai dengan transformasi fourier diskrit
# Citra harus dikonversi ke float32 dulu
# Output dari dft ini adalah citra yang mempunyai 2 channel, 0 real dan 1 imajiner
dft= cv.dft(np.float32(img), flags=cv.DFT_COMPLEX_OUTPUT)

# Memindahkan Frekuensi 0 ke tengah citra / array
# Ini untuk memudahkan proses masking maupun visualisasi
dft_shift= np.fft.fftshift(dft)

# Magnitude Spectrum nya, yang nantinya di sinilah sebagian besar operasi terjadi
# Rumus= 20.log(abs(f)). Yang di-log adalah magnitudo dari channel real dan imajiner dari dft
# Pusat dari magnitude spectrum bersifat low frequency, sedangkan semakin jauh semakin bersifat high frequency
magnitude_spectrum= 20 * np.log(cv.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))

plt.subplot(121)
plt.imshow(img, cmap='gray')
plt.title('input image')

plt.subplot(122)
plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('magnitudo spectrum')

plt.show()

# ---------------------------- Low pass filter ---------------------------------
# Low pass filter atau hanya menyisakan frekuensi rendah dan memblok frekuensi tinggi (yang jauh dari pusat)
# Untuk memblok frekuensi tertentu bisa dengan melakukan masking
# Low pass filter akan menghasilkan gambar yang blur, dan biasanya digunakan untuk menghilangkan noise

# Transformasi fourier
img= cv.cvtColor(cv.imread('..\\img\\Lena_noisy.png'), cv.COLOR_BGR2GRAY)

dft= cv.dft(np.float32(img), flags=cv.DFT_COMPLEX_OUTPUT)
dft_shift= np.fft.fftshift(dft)
magnitude_spectrum= 20 * np.log(cv.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))

# Membuat mask
rows, cols= img.shape
center_rows, center_cols= rows//2, cols//2

# Membuat kanvas untuk masking
masking_area= np.zeros((rows, cols), np.uint8)

# Membuat area masking berupa lingkaran pada kanvas
rad= 80
cv.circle(masking_area, (center_rows, center_cols), rad, 1, -1)

# Melakukan operasi and antara magnitude spectrum dengan masking area
masking_channel= cv.bitwise_and(magnitude_spectrum, magnitude_spectrum, mask=masking_area)

# Lalu membuat mask, terdiri dari dua channel agar menyesuaikan channel real dan imajiner dari dft_shift
mask= np.zeros((rows, cols, 2))

# Menyimpan masking_channel tersebut ke dalam dua channel masking
mask[:, :, 0], mask[:, :, 1]= masking_channel, masking_channel

# Mengalikan mask dengan dft, agar frekuensi yang kita inginkan dikali 1 (tetap)
# Frekuensi yang kita ingin buang dikalikan dengan 0
fshift= dft_shift * mask

# Membuat magnitudo spectrum dari dft yang telah diubah
fshift_mag_spec= 20 * np.log(cv.magnitude(fshift[:, :, 0], fshift[:, :, 1]))

# Mengembalikan pusat ke atas kiri
f_ishift= np.fft.ifftshift(fshift)

# Menginverskan dft yang sudah ditransformasi
img_back= cv.idft(f_ishift)

# Mengekstrak magnitudo dari dft yg sudah diinvers, agar kembali menjadi gambar
img_back= cv.magnitude(img_back[:, :, 0], img_back[:, :, 1])

plt.subplot(221)
plt.imshow(img, cmap='gray')
plt.title('noisy image')

plt.subplot(222)
plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('mag spec of noisy image')

plt.subplot(223)
plt.imshow(img_back, cmap='gray')
plt.title('denoised image')

plt.subplot(224)
plt.imshow(fshift_mag_spec, cmap='gray')
plt.title('mag spec denoised image')

plt.tight_layout()
plt.show()

# ---------------------------- High pass filter ---------------------------------
# High pass filter atau hanya menyisakan frekuensi tinggi dan memblok frekuensi rendah
# High pass filter akan menghasilkan gambar dengan tepi yang jelas

# Transformasi fourier
img= cv.cvtColor(cv.imread('..\\img\\Lena512warna.bmp'), cv.COLOR_BGR2GRAY)

dft= cv.dft(np.float32(img), flags=cv.DFT_COMPLEX_OUTPUT)
dft_shift= np.fft.fftshift(dft)
magnitude_spectrum= 20 * np.log(cv.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))

# Membuat mask, tapi kali ini dengan cara berbeda
rows, cols= img.shape
center_rows, center_cols= rows//2, cols//2

mask= np.ones((rows, cols, 2), np.uint8)

center= [center_rows, center_cols]
x, y= np.ogrid[:rows, :cols]
mask_area= (x-center[0]) ** 2 + (y-center[1]) ** 2 <= rad*rad
mask[mask_area]= 0

#

fshift= dft_shift * mask
fshift_mag_spec= 20 * np.log(cv.magnitude(fshift[:, :, 0], fshift[:, :, 1]))

f_ishift= np.fft.ifftshift(fshift)
img_back= cv.idft(f_ishift)
img_back= cv.magnitude(img_back[:, :, 0], img_back[:, :, 1])

# Plot

plt.subplot(221)
plt.imshow(img, cmap='gray')
plt.title('normal image')

plt.subplot(222)
plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('mag spec of normal image')

plt.subplot(223)
plt.imshow(img_back, cmap='gray')
plt.title('edge image')

plt.subplot(224)
plt.imshow(fshift_mag_spec, cmap='gray')
plt.title('mag spec edge image')

plt.tight_layout()
plt.show()

# Terakhir, ada yang dinamakan band pass filter, yang pada dasarnya menggabungkan low pass dan high pass
# Filter, dan hanya menyisakan daerah antara kedua filter tersebut