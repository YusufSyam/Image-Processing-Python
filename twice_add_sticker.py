import cv2 as cv
import glob

path= glob.glob('path-to-img-dir/*.png')

sticker= cv.imread('img\\twice_logo3_resized.png', -1)

input_x_position= int(input("Masukkan posisi horizontal sticker:\n1. Kiri\n2. Kanan\n3. Tengah\n>> "))
input_y_position= int(input("Masukkan posisi vertikal sticker:\n1. Atas\n2. Bawah\n3. Tengah\n>> "))

input_grid_x= int(input("Masukkan grid horizontal: "))
input_grid_y= int(input("Masukkan grid vertikal: "))

def sticker_placement(img_x, img_y, sticker_x, sticker_y, x, y, grid_x=0, grid_y=0):
    if (grid_y+y+sticker_y > img_y): grid_y*= (-1)
    if (grid_x+x+sticker_x > img_x): grid_x*= (-1)

    x1, x2= x+grid_x, x+sticker_x+grid_x
    y1, y2= y+grid_y, y+sticker_y+grid_y

    return x1, x2, y1, y2

for file in path:
    img= cv.imread(file)

    # Resize
    img= cv.resize(img, (820, 461))

    x_location_left= 0
    x_location_right=  (img.shape[1] - sticker.shape[1])
    x_location_center= (img.shape[1] - sticker.shape[1]) // 2

    y_location_top= 0
    y_location_bottom= (img.shape[0] - sticker.shape[0])
    y_location_center= (img.shape[0] - sticker.shape[0]) // 2

    x_location= 0
    y_location= 0

    if(input_x_position==1): x_location= x_location_left
    elif(input_x_position==2): x_location= x_location_right
    elif(input_x_position==3): x_location= x_location_center

    if(input_y_position==1): y_location= y_location_top
    elif(input_y_position==2): y_location= y_location_bottom
    elif(input_y_position==3): y_location= y_location_center

    x1, x2, y1, y2 = sticker_placement(img.shape[1], img.shape[0], sticker.shape[1], sticker.shape[0], x_location, y_location, input_grid_x, input_grid_y)

    alpha_s= sticker[:, :, 3]/255.0
    alpha_l= 1.0-alpha_s

    for c in range(0, 3):
        img[y1:y2, x1:x2, c]= (alpha_s*sticker[:, :, c]+alpha_l*img[y1:y2, x1:x2, c])

    img_name= file.split('\\')[-1][0:-4]
    cv.imwrite(('output_img\\img_p1\\'+img_name+'_added_sticker.png'), img)
    # cv.imshow(img_name, img)
    # cv.waitKey(0)