import cv2
import numpy as np

s_img = cv2.imread("img\\twice_logo3_resized.png", -1)
# s_img = cv2.imread("img\\twice_logo3.png")

# s_img= cv2.resize(s_img, (int(s_img.shape[0]*0.9),int(s_img.shape[1]*0.9)))
# s_img= cv2.resize(s_img, tuple(reversed(np.array(s_img.shape[0:2])*0.9)))

l_img = cv2.imread("img\\chaeyoung.png")
# x_offset=y_offset=50
# l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img

x_location_center= (l_img.shape[1]-s_img.shape[1])//2

y1, y2 = s_img.shape[0]+160, s_img.shape[0]+(s_img.shape[0]+160)
# x1, x2 = 0,s_img.shape[1]
x1, x2 = x_location_center, x_location_center+s_img.shape[1]

# alpha_s = s_img[:, :, 3] / 255.0
# alpha_l = 1.0 - alpha_s
#
# for c in range(0, 3):
#     l_img[y1:y2, x1:x2, c] = (alpha_s * s_img[:, :, c] + alpha_l * l_img[y1:y2, x1:x2, c])
#
# cv2.imshow('Twice', l_img)
# cv2.waitKey(0)
#
# print(s_img.shape[0:2])

print(y1, y2)
print(x1, x2)

