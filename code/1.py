import numpy as np
import cv2
from matplotlib import pyplot as plt
#plt.axvspan(ขอบเขตซ้าย, ขอบเขตขวา, ขอบเขตล่าง, ขอบเขตบน)
img = cv2.imread('frame0.JPG') # 0 คือ ค่าสีโทนเทา (grayscale)
plt.axvspan(458,518,707,899,alpha=0.2,lw=7,fc='r')
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')

plt.plot()
plt.show()
