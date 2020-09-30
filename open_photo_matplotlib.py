import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img = cv2.imread(r"C:\Users\sasi1\Desktop\ricardo.png")
plt.imshow(img,cmap="gray")
plt.plot([800,400],[400,200],"red",linewidth=12)
plt.show()