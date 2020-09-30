import cv2
from PIL import Image
import numpy as np

img = cv2.imread(r"C:\Users\sasi1\Desktop\ricardo.png")
img = np.array(img)
cv2.imshow("RICARDO",img)
cv2.waitKey()
cv2.destroyAllWindows()
