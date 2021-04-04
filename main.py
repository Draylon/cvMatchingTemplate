import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import os

#img_r = cv.imread('./img/img_all_characters.jpg',0)
drone_frames = []#cv.imread('')
template = cv.imread('./img/drone_template.png',0)
w, h = template.shape[::-1]

for i in range(len(os.listdir('./img/drone_png/'))+1):
    img = cv.imread(os.path.join('./img/drone_png/','drone_render'+str(i)+'.png'),0)
    if img is not None:
        drone_frames.append(img)

# All the 6 methods for comparison in a list
#methods = ['cv.TM_CCOEFF']#, 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR','cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
methods = [cv.TM_CCOEFF]

ii=0

for method in methods:
    for frame in drone_frames:
        img = frame.copy()
        res = cv.matchTemplate(img,template,method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv.rectangle(img,top_left, bottom_right, 255, 2)
        cv.imwrite(os.path.join('./img/drone_rendered/drone_rendered_'+str(ii)+'.png'),img)
        ii+=1


