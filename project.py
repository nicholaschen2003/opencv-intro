import numpy as np
import argparse
import cv2

#chapter 3: loading and displaying images
#type 'py project.py --image ericMuah.png'
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

width = image.shape[1]
height = image.shape[0]
channels = image.shape[2]

print("width: {} pixels".format(width))
print("height: {} pixels".format(height))
print("channels: {}".format(channels))

cv2.imshow("Original", image)
cv2.waitKey(0)

#chapter 4: getting and editing pixels, and chapter 5: using opencv methods to edit pic
smileyFace = image.copy()
#eyes
smileyFace[int(height/10):int(height/10+10), int(3*width/4):int(3*width/4+10)] = (255, 0, 0)
smileyFace[int(height/10):int(height/10+10), int(3*width/4+30):int(3*width/4+40)] = (255, 0, 0)

#mouth
smileyFace[int(height/10+20):int(height/10+30), int(3*width/4):int(3*width/4+10)] = (255, 0, 0)
smileyFace[int(height/10+20):int(height/10+30), int(3*width/4+30):int(3*width/4+40)] = (255, 0, 0)
smileyFace[int(height/10+30):int(height/10+40), int(3*width/4+10):int(3*width/4+30)] = (255, 0, 0)

#face outline
center = (int((3*width/4+3*width/4+40)/2), int((height/10+height/10+40)/2))
r = 40
cv2.circle(smileyFace, (center[0], center[1]), r, (255, 0, 0), 10)

cv2.imshow(":)", smileyFace)
cv2.waitKey(0)
