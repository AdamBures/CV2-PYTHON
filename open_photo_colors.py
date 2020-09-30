import cv2
from PIL import Image
import numpy as np

img = cv2.imread(r"C:\Users\sasi1\Desktop\ricardo.png")
img = np.array(img)
img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
cv2.imshow("RICARDO ON DRUGS",img)
cv2.waitKey()
cv2.destroyAllWindows()
