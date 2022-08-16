from typing import Type
import cv2
from PIL import Image
import glob
import os
from pathlib import Path


def SetFilePath():
######################################
#   Set File Paths for program       #
######################################
    
    menuOption = 0
    Input_Path = "null"
    Output_Path = "null"
    Alpha_Path = "null"

    while(menuOption != "5"):
       menuOption = input("1) Set Input Path:\n" + "2) Set Output Path\n" + "3) Set Alpha Path\n" + "4) Show Current Paths\n" + "5) Exit\n")
      
       if (menuOption == "1"):
            Input_Path = input("Input Path:")

       elif (menuOption == "2"):
            Output_Path = input("Output Path:")
            #Set Output

       elif (menuOption == "3"):
            #Set Alpha
            Alpha_Path = input("Alpha Path:")
       elif (menuOption == "4"):
            print("Input Path:" +Input_Path + "\n")
            print("Output Path:" + Output_Path + "\n")
            print("Alpha Path:" + Alpha_Path + "\n")

       elif (menuOption != "5"):
            #Check for Input
            print("Please Select Valid Input\n")

    return(Input_Path, Output_Path, Alpha_Path)

            
def SaveAsPNG(Input_Path, Output_Path):
######################################
#   Save as PNG                      #
######################################

    for img in glob.glob(str(Input_Path + "/*.bmp")):
        filename = Path(img).stem
        Image.open(img).save(str(Output_Path + f'/{filename}.png'))
        
    print("Done!")

def AddAlpha(Output_Path, Alpha_Path):
###########################################
# Remove Background from Images add Alpha #
###########################################

    for myfile in os.listdir(Output_Path):
      
        # Read the image
        src = cv2.imread(Output_Path +"\\" + myfile, 1)
  
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
        cv2.imwrite(Alpha_Path +"\\" + myfile, dst)
    print("Done!")

menuOption = 0
Input_Path = "null"
Output_Path = "null"
Alpha_Path = "null"

while menuOption != "4":
    menuOption = input("What would you Like to do:\n" + "1) Set File Paths\n" + "2) Convert Bitmap to PNG\n" + "3) Remove Background add Alpha\n" + "4) Exit\n")
    
    if menuOption == "1":
        #Call File PATH function
      Input_Path, Output_Path, Alpha_Path = SetFilePath()

    elif menuOption == "2":
        #Convert Bitmap to PNG
        SaveAsPNG(Input_Path, Output_Path)

    elif menuOption == "3":
        #Add Alpha
        AddAlpha(Output_Path, Alpha_Path)

    elif (menuOption != "4"):
        #Check for Input
        print("Please Select Valid Input\n")
 

