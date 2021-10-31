from skimage import data
from matplotlib import pyplot as plt

print(data.__all__)

plt.imshow(data.camera(), cmap='gray')
plt.show()

plt.imshow(data.stereo_motorcycle()[1])
plt.show()