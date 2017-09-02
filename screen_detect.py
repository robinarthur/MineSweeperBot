from mss.windows import MSS
from PIL import Image
import cv2
import numpy as np

mon = {'top': 160, 'left': 160, 'width': 200, 'height': 200}

sct = MSS()

while 1:
    sct.get_pixels(mon)
    img = Image.frombytes('RGB', (sct.width, sct.height), sct.image)
    cv2.imshow('test', np.array(img))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
