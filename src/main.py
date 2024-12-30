import cv2
import output_logic

webcam = False

#  File name and file format to be provided in the sample_input folder
image_location = "sample_image"
file_format = "jpg"


image_address = '../sample_input/'+ image_location + "."+ file_format 
path = image_address
path = cv2.imread(path)
img = cv2.resize(path,(600,600))
output = output_logic.getContours(img)

# Displaying the image to be taken
cv2.imshow(image_location,img)
cv2.waitKey()
