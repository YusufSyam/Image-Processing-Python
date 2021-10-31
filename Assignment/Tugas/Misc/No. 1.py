import numpy as np
import matplotlib.pyplot as plt
import imageio
import colorsys

# Membuat fungsi-fungsi yang akan digunakan nanti
rgb_hsv = np.vectorize(colorsys.rgb_to_hsv)
hsv_rgb = np.vectorize(colorsys.hsv_to_rgb)
rgb_yiq = np.vectorize(colorsys.rgb_to_yiq)
yiq_rgb = np.vectorize(colorsys.yiq_to_rgb)

# No. 1
img1 = imageio.imread('bird.jpeg')

# Variabel r, g, b secara berurutan merupakan citra grayscale red, green dan blue
r = img1[:, :, 0]
g = img1[:, :, 1]
b = img1[:, :, 2]

# Fungsi subplots untuk menampilkan gambar dalam dimensi 1 baris 3 kolom
fig1, img1_rgb = plt.subplots(1,3,figsize=(15,15))

img1_rgb[0].imshow(r, cmap='gray')
img1_rgb[0].set_title('Red')

img1_rgb[1].imshow(g, cmap='gray')
img1_rgb[1].set_title('Green')

img1_rgb[2].imshow(b, cmap='gray')
img1_rgb[2].set_title('Blue')

# Menampilkan citra grayscale r, g dan b
plt.show()

# No. 2
img2 = imageio.imread('bird.jpeg')

# Menukar channel rgb sesuai soal
img2_new = np.dstack((img2[:, :, 1], img2[:, :, 2], img2[:, :, 0]))

plt.imshow(img2_new)

# No. 3
img3 = imageio.imread('bird.jpeg')/255

# Variabel h, s, v secara berurutan merupakan variabel untuk grayscale hue, saturation dan value
# Yang diubah dari rgb ke hsv dengan fungsi rgb_hsv
h, s, v= rgb_hsv(img3[...,0], img3[...,1], img3[...,2])

fig3, img3_hsv = plt.subplots(1,3, figsize=(15,15))

img3_hsv[0].imshow(h, cmap='gray')
img3_hsv[0].set_title('Hue')

img3_hsv[1].imshow(s, cmap='gray')
img3_hsv[1].set_title('Saturation')

img3_hsv[2].imshow(v, cmap='gray')
img3_hsv[2].set_title('Value')

# Menampilkan citra grayscale berdasarkan hsv
plt.show()

# No. 4
img4= imageio.imread('bird.jpeg')

# Variabel y, i, q secara berurutan merupakan citra grayscale untuk Iuma (y), In-phase dan Quadrature
# Diubah dari rgb ke yiq dengan fungsi rgb_yiq
y, i, q= rgb_yiq(img4[...,0], img4[...,1], img4[...,2])

fig4, img4_yiq = plt.subplots(1,3, figsize=(15,15))

img4_yiq[0].imshow(y, cmap="gray")
img4_yiq[0].set_title("Iuma")

img4_yiq[1].imshow(i, cmap="gray")
img4_yiq[1].set_title("In-Phase")

img4_yiq[2].imshow(q, cmap="gray")
img4_yiq[2].set_title("Quadrature")

# Menampilkan semua gambar grayscale berdasarkan yiq
plt.show()

# No. 5
# Kali ini skala gambar diubah menjadi skala 0-1
# Agar memudahkan operasi-operasi yang akan dilakukan
img5 = imageio.imread('bird.jpeg')/255

# Mengubah citra dari rgb ke hsv dengan fungsi rgb_hsv
img5_h, img5_s, img5_v, = rgb_hsv(img5[...,0], img5[...,1], img5[...,2])

# Membuat citra rgb baru dari hsv, dengan hsv yang nilai hue (h) nya telah dikali 2/3
img5_r, img5_g, img5_b = hsv_rgb((img5_h)*2/3, img5_s, img5_v)
img5_new = np.dstack((img5_r, img5_g, img5_b))

# Menampilkan hasil operasi
plt.imshow(img5_new)

# No. 6
img6 = imageio.imread('bird.jpeg')/255

# Konversi ke yiq
img6_y, img6_i, img6_q = rgb_yiq(img6[...,0], img6[...,1], img6[...,2])

# Konversi warna dari yiq di atas kembali ke rgb
img6_r, img6_g, img6_b = yiq_rgb(img6_y, img6_i, img6_q)

# Membuat citra rgb
img6_rgb = np.dstack((img6_r, img6_g, img6_b))

# Mengecek kehilangan informasi
img6_new = np.abs(img6_rgb - img6)

# Menampilkan gambar hasil operasi
plt.imshow(img6_new)

# Mengecek kehilangan informasi
img6_new.max()

# No. 7
img7 = imageio.imread("bird.jpeg")/255

# Konversi gambar ke hsv
img7_h, img7_s, img7_v = rgb_hsv(img7[...,0], img7[...,1], img7[...,2])

# Konversi kembali ke rgb dan gunakan channel h yang dipangkatduakan
img7_r, img7_g, img7_b = hsv_rgb((img7_h**(1/2)), img7_s, img7_v)

# Membuat citra rb
img7_new = np.dstack((img7_r, img7_g, img7_b))

# Menampilkan hasil operasi
plt.imshow(img7_new)

# No. 8
img8 = imageio.imread("a_child_beside_the_van.jpeg")

# Buat model hsv
img8_h, img8_s, img8_v = rgb_hsv(img8[...,0], img8[...,1], img8[...,2])

# Buat model yiq
img8_y, img8_i, img8_q = rgb_yiq(img8[...,0], img8[...,1], img8[...,2])

# Menggunakan fungsi subplots untuk menampilkan gambar 3 baris 3 kolom
fig8, img8_new = plt.subplots(nrows=3,ncols=3, figsize=(15,15))

img8_new[0][0].imshow(img8[...,0],cmap="gray")
img8_new[0][0].set_title("RGB - R")
img8_new[0][1].imshow(img8[...,1],cmap="gray")
img8_new[0][1].set_title("RGB - G")
img8_new[0][2].imshow(img8[...,2],cmap="gray")
img8_new[0][2].set_title("RGB - B")

img8_new[1][0].imshow(img8_h,cmap="gray")
img8_new[1][0].set_title("HSV - H")
img8_new[1][1].imshow(img8_s,cmap="gray")
img8_new[1][1].set_title("HSV - S")
img8_new[1][2].imshow(img8_v,cmap="gray")
img8_new[1][2].set_title("HSV - V")

img8_new[2][0].imshow(img8_y,cmap="gray")
img8_new[2][0].set_title("YIQ - Y")
img8_new[2][1].imshow(img8_i,cmap="gray")
img8_new[2][1].set_title("YIQ - I")
img8_new[2][2].imshow(img8_q,cmap="gray")
img8_new[2][2].set_title("YIQ - Q")

# Menampilkan gambar, secara berurutan: rgb, hsv, yiq
plt.show()
