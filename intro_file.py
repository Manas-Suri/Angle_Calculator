import cv2
import OutputLogic
#import scratch_11
webcam = False
path = r'SampleImage.jpg'
#this file is included as an image file
path = cv2.imread(path)
img = cv2.resize(path,(600,600))
output = OutputLogic.getContours(img)
cv2.imshow('Normal',img)
cv2.waitKey()
