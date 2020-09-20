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

#chapter 10: edge dectection, chapter 6: converting colorspaces, chapter 8: blurring
edges = image.copy()
edges = cv2.cvtColor(edges, cv2.COLOR_BGR2GRAY)
edges = cv2.GaussianBlur(edges, (9, 9), 0) #kernel size chosen to blur as much as possible without losing nose

cv2.imshow("Blurred grayscale image", edges)
cv2.waitKey(0)

edges = cv2.Canny(edges, 30, 150)

cv2.imshow("Edges", edges)
cv2.waitKey(0)

#chapter 11: contours (builds on previous code)
(contours, _) = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

contour = image.copy()
#used to display each individual contour and find heart
# for cntr in contours:
#     cv2.drawContours(contour, cntr, -1, (255, 255, 255), 2)
#     cv2.imshow("Contour", contour)
#     cv2.waitKey(0)

#heart outline
cv2.drawContours(contour, contours[15], -1, (255, 255, 0), 7)
cv2.imshow("Contour", contour)
cv2.waitKey(0)
