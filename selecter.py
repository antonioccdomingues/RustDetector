import cv2 
import numpy as np
import sys

ref_point = []
cropping = False

def shape_selection(event, x, y, flags, param):
  # grab references to the global variables
  global ref_point, cropping

  # if the left mouse button was clicked, record the starting
  # (x, y) coordinates and indicate that cropping is being performed
  if event == cv2.EVENT_LBUTTONDOWN:
    ref_point = [(x, y)]
    cropping = True

  
  elif event == cv2.EVENT_LBUTTONUP:    # check to see if the left mouse button was released
                                        # record the ending (x, y) coordinates and indicate that the cropping operation is finished
    ref_point.append((x, y))
    cropping = False

    # draw a rectangle around the region of interest
    cv2.rectangle(image, ref_point[0], ref_point[1], (0, 255, 0), 2)
    cv2.imshow("image", image)

# load the image, copy it, and setup the mouse callback function
img = sys.argv[1]
image = cv2.imread(img)
clone = image.copy()
cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.setMouseCallback("image", shape_selection)

print("---Select a part of an image to detect rust---\n")
print("*Press r key to reset the selection\n*Press c to cut de selected area\n*Press q to quit")
print("\nIf several areas selected, only the last one will be chosen ")

# keep looping until the 'q'|'c' key is pressed
while True:
  # display the image and wait for a keypress
  cv2.imshow("image", image)
  key = cv2.waitKey(1) & 0xFF

  # if the 'r' key is pressed, reset the cropping region
  if key == ord("r"):
    image = clone.copy()

  # if the 'c' key is pressed, break from the loop
  elif key == ord("c"):
    break
  
  # if the 'q' key is pressed, exit
  elif key == ord("q"):
    sys.exit("Exiting...")

# if there are two reference points, then crop the region of interest
if len(ref_point) == 2:
  crop_img = clone[ref_point[0][1]:ref_point[1][1], ref_point[0][0]:ref_point[1][0]]
else:
  crop_img = clone

