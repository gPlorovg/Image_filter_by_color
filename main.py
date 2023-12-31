import os
from os import listdir
import cv2
import numpy as np
#new
import shutil

print("Input example image name:")
example_name = input()


dom_colors = dict()

for name in listdir("data"):
    # read img
    img = cv2.imread("data/" + name)
    # resize img
    img = cv2.resize(img, (128, 128), interpolation=cv2.INTER_AREA)
    # change color model to HSL
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
    # get list of pixels each contains three value [H, S, L]
    pixels = img.reshape(-1, 3)
    # get only Hues
    hues = pixels[:, 0]
    # remove white colors
    hues = hues[hues != 0]
    # count each hue repetition in image
    counts = np.bincount(hues)
    # get most frequently hue
    dom_colors[name] = np.argmax(counts)
# newstart
if os.path.isdir("result"):
    for i in os.listdir("result"):
        os.remove("result/" + i)
else:
    os.mkdir("result")
# newend
for name in dom_colors:
    # find images with dominant color close to example image dominant color on value 18 (value find in many tests)
    if name != example_name and abs(dom_colors[example_name] - dom_colors[name]) < 18:
        print(name)
        # new
        shutil.copy("data/" + name, "result/" + name)
