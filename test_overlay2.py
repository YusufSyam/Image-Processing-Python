import cv2
import numpy as np

s_img = cv2.imread("img\\twice_logo.png", -1)
# s_img = cv2.imread("img\\twice_logo3.png")

# s_img= cv2.resize(s_img, (int(s_img.shape[0]*0.9),int(s_img.shape[1]*0.9)))
# s_img= cv2.resize(s_img, tuple(reversed(np.array(s_img.shape[0:2])*0.9)))

l_img = cv2.imread("img\\dahyun_big.png")
# x_offset=y_offset=50
# l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img

# x_location_center= (l_img.shape[1]-s_img.shape[1])//2
# y_location= (l_img.shape[0]-s_img.shape[0])
# y_location_center= (l_img.shape[0]-s_img.shape[0])//2

def sticker_placement(img_x, img_y, sticker_x, sticker_y, x, y, grid_x=0, grid_y=0):
    if (grid_y+y+sticker_y > img_y): grid_y*= (-1)
    if (grid_x+x+sticker_x > img_x): grid_x*= (-1)

    x1, x2= x+grid_x, x+sticker_x+grid_x
    y1, y2= y+grid_y, y+sticker_y+grid_y

    return x1, x2, y1, y2

x_location_left= 0
x_location_right=  (l_img.shape[1] - s_img.shape[1])
x_location_center= (l_img.shape[1] - s_img.shape[1]) // 2

y_location_top= 0
y_location_bottom= (l_img.shape[0] - s_img.shape[0])
y_location_center= (l_img.shape[0] - s_img.shape[0]) // 2

x1, x2, y1, y2 = sticker_placement(l_img.shape[1], l_img.shape[0], s_img.shape[1], s_img.shape[0], x_location_center, y_location_bottom, grid_y=75)

alpha_s = s_img[:, :, 3] / 255.0
alpha_l = 1.0 - alpha_s

for c in range(0, 3):
    l_img[y1:y2, x1:x2, c] = (alpha_s * s_img[:, :, c] + alpha_l * l_img[y1:y2, x1:x2, c])

cv2.imshow('Twice', l_img)
cv2.waitKey(0)

cv2.imwrite('WallpDahyun.png', l_img)
# print(s_img.shape[0:2])

# print((s_img.shape[0]+(l_img.shape[0]-50))-(l_img.shape[0]-50))
# print(l_img.shape[0]-50)
# print(s_img.shape[0])
# print((s_img.shape[0]+(s_img.shape[0]+160))-(s_img.shape[0]+160))