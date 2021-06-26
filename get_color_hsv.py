import cv2
import os
from PIL import ImageGrab

ImageGrab.grab().save('IMG/screenshot.bmp')
img = cv2.imread('IMG/screenshot.bmp', cv2.IMREAD_COLOR)
window_name = 'img'
imgBoxHsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

def onMouse(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        crop_img = imgBoxHsv[[y], [x]]
        H_val = crop_img.T[0].flatten().mean()
        S_val = crop_img.T[1].flatten().mean()
        V_val = crop_img.T[2].flatten().mean()
        print("H: {}, S: {}, V: {}".format(H_val, S_val, V_val))

def my_makedirs(path):
    if not os.path.isdir(path):
        os.makedirs(path)

dirpath= "./IMG"
my_makedirs(dirpath)


cv2.imshow(window_name, img)
cv2.setMouseCallback(window_name, onMouse)
cv2.waitKey(0)