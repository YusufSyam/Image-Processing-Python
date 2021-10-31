import cv2 as cv
import imutils

def showim(img, title='pictures', multiple=False):
    cv.imshow(title,img)
    if(not multiple): cv.waitKey(0)

img= cv.imread('img\\dahyun_added_sticker.png')
showim(img)

# Translation
X= 90 # X positif berarti ke kanan
Y= -40 # Y negatif berarti ke atas
translated_img= imutils.translate(img, X, Y)
# showim(translated_img)

# Rotation
angle= 170 # Angle juga bisa minus
rotated_img= imutils.rotate(img, angle)
# showim(rotated_img)

# Resize
height= 520
width= 520
resized_cv= cv.resize(img, (height,width)) # CV menyetel width dan height tanpa memedulikan aspect ratio
resized_im= imutils.resize(img, width=width) # imutils memedulikan aspect ratio, hanya memasukkan width akan secara otomatis menyesuaikan heigth
# showim(resized_cv)
# showim(resized_im)

# Flip
flip_horizontal= cv.flip(img, flipCode=1) # Parameter flipcode: 1=horizontal, 0 vertikal, -1 horizontal+vertikal
showim(flip_horizontal)

# Cropping
# Bisa dengan simpel seperti indexing matriks
cropped= img[0:(img.shape[1]//2), (img.shape[0]//2):img.shape[0]]
showim(cropped)