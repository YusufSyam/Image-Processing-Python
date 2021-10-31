# Mengimport imageio, matplotlib dan numpy lalu mengaliaskan dengan plt dan np
import imageio
import matplotlib .pyplot as plt
import numpy as np

# Memanggil magic function untuk memudahkan pengerjaan pada jupyter
# %matplotlib inline

# Membaca gambar, lalu menyimpannya dalam variabel img
img = imageio.imread("bird.jpeg")

# Mengubah format gambar dari 8-bit / 255 menjadi skala 0-1 per warna
img= img.astype(np.float64)/255

# Mengekstrak hanya warna merah pada img, parameter yang lain dibiarkan
red= img[:,:,0]

# Mengekstrak hanya warna hijau, lalu menambahkan nilai sebanyak 0.1
green= img[:,:,1] + 0.1

# Membagi nilai pixel red dan green lalu menyimpannya ke variabel divider
divider= red/green

# Operasi Threshold, jika nilai pixel lebih besar dari 1 menjadi true, kalau tidak diubah menjadi 0
r= (divider>1)*divider
red= r/r.max()

# Mengkonversi citra menjadi gambar gray scale dengan operasi perkalian array numpy
gray= np.dot(img[:,:,:],[0.2989, 0.5870, 0.1140])

# Mengubah unsur ke dalam format integer 8 bit
b= (gray*255.0).astype(np.uint8) & 0xc0
b= b.astype(np.float64)/255

# Menyimpan semua pixel yang bernilai 0
m= (b==0)

# Mengubah unsur b dengan mengalikannya dengan invers, disimpan ke bg
bg= (1-m)*b

# Unsur Merah diganti dengan hasil kali dari variabel m dan r sebelumnya, kemudian hasil operasi disimpan dalam bentuk array
c= np.dstack((m*red+bg, bg, bg))

# Menunjukkan gambar hasil
plt.imshow(c)