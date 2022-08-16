from fileinput import filename
import cv2
from pathlib import Path
import os

file_name = "C:\\Users\\Franco Mezzarapa\\Downloads\\test\\new"

for myfile in os.listdir(file_name):
    
    
    # Read the image
    src = cv2.imread(file_name +"\\" + myfile, 1)
  
    # Convert image to image gray
    tmp = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
  
    # Applying thresholding technique
    _, alpha = cv2.threshold(tmp, 0, 255, cv2.THRESH_BINARY)
  
    # Using cv2.split() to split channels 
    # of coloured image
    b, g, r = cv2.split(src)
  
    # Making list of Red, Green, Blue
    # Channels and alpha
    rgba = [b, g, r, alpha]
  
    # Using cv2.merge() to merge rgba
    # into a coloured/multi-channeled image
    dst = cv2.merge(rgba, 4)
  
    # Writing and saving to a new image
    cv2.imwrite(file_name +"\\" + myfile, dst)
