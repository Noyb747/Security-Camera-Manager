import numpy as np, pygame, cv2, datetime, sys, psutil

pygame.init()

def getn(x):
    if x == 1:
        return 1
    if x <= 4:
        return 2
    if x <= 9:
        return 3
    if x <= 16:
        return 4
    if x <= 25:
        return 5
    if x <= 36:
        return 6
    if x <= 49:
        return 7
    if x <= 64:
        return 8

CAMS = [] #[0, 1]
command = ",".join(sys.argv[1:])
for obj in command.split(","):
    if "-" in obj:
        CAMS += [i for i in range(eval(obj.split("-")[0]), eval(obj.split("-")[1]) + 1)]
    else:
        CAMS.append(eval(obj))

n = getn(len(CAMS))
caps = {}
for cam in CAMS:
    caps[cam] = cv2.VideoCapture(cam)

import pygame.font, pygame.image
from pygame.locals import *

fontbold = pygame.font.SysFont("Courier New", round(50 / n), True)

displayinfo = pygame.display.Info()
display = pygame.display.set_mode([displayinfo.current_w, displayinfo.current_h])

displaystate = True
while displaystate:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            displaystate = False
    
    display.fill([0, 0, 0])

    x = 0
    y = 0
    for cap in caps:
        ret, frame = caps[cap].read()
        if not ret:
            continue
        size = [round(displayinfo.current_w / n), round(displayinfo.current_h / n)]
        frame = pygame.surfarray.make_surface(
            np.rot90(
                cv2.cvtColor(
                    cv2.resize(
                        frame, [size[0], size[1]]
                    ), cv2.COLOR_BGR2RGB
                )
            )
        )
        display.blit(frame, [x, y])
        ts = fontbold.render(str(datetime.datetime.now()).split(".")[0].replace("-", "/"), True, [0, 0, 0])
        display.blit(ts, [x + round(17.5 / n), y])
        display.blit(fontbold.render(f"CAM {cap}", True, [0, 0, 0]), [x + round(17.5 / n), y + ts.get_height() - (10 / n)])

        x += displayinfo.current_w / n
        if x == displayinfo.current_w:
            x = 0
            y += displayinfo.current_h / n

    pygame.display.flip()

for cap in caps:
    caps[cap].release()
cv2.destroyAllWindows()
