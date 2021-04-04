import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import os,sys

try:
    os.mkdir('src')
except Exception as e:
    pass

video_dir = ""
template_dir = ""
video_out = "out"

#methods = ['cv.TM_CCOEFF']#, 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR','cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
methods = [cv.TM_SQDIFF_NORMED]

if len(sys.argv) >= 3:
    video_dir = sys.argv[1]
    template_dir = sys.argv[2]
    if len(sys.argv) >= 4:
        video_out= sys.argv[3]
        if len(sys.argv) >= 5:
            methods = [eval(sys.argv[4])]
else:
    raise Exception("Parametros insuficientes\nColocar <video_entrada> <template_entrada> <video_saida(opcional)> <metodo_processamento(opcional)>")

os.system('ffmpeg -i '+video_dir+' -vf fps=30 ./src/render%d.png')

#img_r = cv.imread('./img/img_all_characters.jpg',0)
drone_frames = []#cv.imread('')
template = cv.imread('./'+template_dir,0)
w, h = template.shape[::-1]

for i in range(len(os.listdir('./src/'))):
    img = cv.imread(os.path.join('./src/','render'+str(i+1)+'.png'),0)
    if img is not None:
        drone_frames.append(img)


ii=0

for method in methods:
    for frame in drone_frames:
        img = frame.copy()
        res = cv.matchTemplate(img,template,method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        
        if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
            
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv.rectangle(img,top_left, bottom_right, 255, 2)
        cv.imwrite(os.path.join('./src/render'+str(ii)+'.png'),img)
        ii+=1

os.system('ffmpeg -r 30 -i ./src/render%d.png -c:v libx264 -pix_fmt yuv420p '+video_out+'.mp4')
#os.remove('src')