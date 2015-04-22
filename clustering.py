import cv2

import numpy as np

f = open('digits.raw', 'r')

images = []

for line in f:
	tokens = line.split(',')

	row = []
	img_data = []

	for x in tokens:
	    if int(x) == 16:
	        row.append(255)
	    else:
	        row.append(int(x) * 16)
	    if len(line) == 8:
	        img_data.append(row)
	        row = []

	images.append(img_data)

