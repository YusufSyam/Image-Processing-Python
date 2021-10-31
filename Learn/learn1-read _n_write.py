# Memang namana cv2
import cv2

# Read file png, directory img/dahyun.png
path= '..\\img\\jihyo.png'
img1= cv2.imread(path)

# Menampilkan gambar, parameter pertama judul pada dialog box, kedua image
cv2.imshow('Pacarku', img1)
# Wait key
cv2.waitKey(0)

# Write gambar, btw path sekalianmi sama judul file baru
output_path= 'img\\jihyo_my_girlfriend.png'
cv2.imwrite(output_path, img1)
print('Image has been displayed and then saved')