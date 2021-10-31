import cv2

img1= cv2.imread('..\\img\\jihyo.png')

# Mendapatkan (tinggi,lebar) / (y/x) dari gambar
(height, width)= img1.shape[0:2]
print(height), print(width)
# Kita mendapat dimensi gambar adalah 820x461, index ketiga dari shape adalah rgb

# Mendapatkan informasi gbr pixel tertentu, misal pixel pada 0,0
(g, b, r)= img1[0,0]
print('R={}, G={}, B={}'.format(r,g,b))

# Mengganti nilai gbr pixel top kiri dan bot bawah dengan warna lain
# Pertama mendapatkan nilai center yg dicast ke int
centerX= width//2
centerY= height//2
altered_image= img1

# Mengganti nilai di sini, top kiri
altered_image[0:centerY, 0:centerX]= (0,0,255)

# Mengganti nilai bot bawah
altered_image[centerY:height, centerX:width]= (240,240,240)

cv2.imshow('God jihyo',altered_image)
cv2.waitKey(0)