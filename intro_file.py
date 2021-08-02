import cv2
import scratch_10
#import scratch_11
webcam = False
path = r'C:\Users\Manas\Downloads\B9ECED6F.ASUSPCAssistant_qmba6cd70vzyy!App\Link_to_MyASUS\img1.jpg'
path = cv2.imread(path)
img = cv2.resize(path,(600,600))
img = scratch_10.getContours(img)
cv2.imshow('Normal',img)
cv2.waitKey()