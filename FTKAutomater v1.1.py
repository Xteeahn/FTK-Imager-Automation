
#©FTK Automater v1.1 - 2020 Xteeahn
from time import strftime
import datetime
from pywinauto.application import Application
from pywinauto import timings
import time
import pyautogui
import pyscreeze
import easygui
from argparse import ArgumentParser
import sys

#Ignore 64 bit warning
import warnings
warnings.simplefilter('ignore', category=UserWarning)

#Script arguments
parser = ArgumentParser()
parser.add_argument("-q", '--queue', metavar='', help= "The filepath of your text file that contains all Imaging Notes (text file must be in UTF-8 formatting)")
parser.add_argument("-p", '--filepath', metavar='', help= "The filepath of your text file that contains all sources for the targeted image (text file must be in UTF-8 formatting)")
parser.add_argument("-t", '--type', metavar='', help= "For targeted collection type \"targeted\", for physical collection type \"physical\" for logical collection type \"logical\"")
parser.add_argument("-c", '--casenumber', metavar='', help= "FTK: Case Number")
parser.add_argument("-ev", '--evidencenumber', metavar='', help= "FTK: Evidence Number")
parser.add_argument("-e", '--examiner', metavar='', help= "FTK: Examiner")
parser.add_argument("-n", '--notes', metavar='', help= "FTK: Notes")
parser.add_argument("-d", '--destinationfolder', metavar='', help= "FTK: Image Destination Folder")
parser.add_argument("-f", '--filename', metavar='', help= "FTK: Image Filename")
parser.add_argument("-s", '--segmentsize', metavar='', help= "FTK: Segment Size")
parser.add_argument("-co", '--compression', metavar='', help= "FTK: Compression (accepts values between 1-9)")
parser.add_argument("-ft", '--ftklocation', metavar='', help= "Optional: Full folder path to FTK Imager (e.g. \"C:\\Program Files\\AccessData\\FTK Imager\\FTK Imager.exe\"")
args = parser.parse_args()

def FTKAutomater():
    #Checking if required arguments are set
    if args.type is None:
        print("Argument -t \"type\" is not set")
        sys.exit()
    if args.casenumber is None:
        print("Argument -c \"casenumber\" is not set")
        sys.exit()
    if args.casenumber is None:
        print("Argument -ev \"evidencenumber\" is not set")
        sys.exit()
    if args.casenumber is None:
        print("Argument -e \"examiner\" is not set")
        sys.exit()
    if args.casenumber is None:
        print("Argument -n \"notes\" is not set")
        sys.exit()
    if args.destinationfolder is None:
        print("Argument -d \"destinationfolder\" is not set")
        sys.exit()
    if args.filename is None:
        print("Argument -f \"filename\" is not set")
        sys.exit()
    if args.segmentsize is None:
        print("Argument -s \"segmentsize\" is not set")
        sys.exit()
    if args.compression is None:
        print("Argument -co \"compression\" is not set")
        sys.exit()


    #Converting file path and type argument to all lower caps
    args.type = args.type.lower()

    #Removing the neccessary trailing space (from the imaging notes template) from the destinationfolder
    args.destinationfolder = args.destinationfolder.strip()

    #Appending a backslash if destination folder ends with a colon
    if args.destinationfolder.endswith(':'):
        args.destinationfolder += "\\"

    #Launching application
    if args.ftklocation is None:
        app = Application().start("C:\\Program Files\\AccessData\\FTK Imager\\FTK Imager.exe") #location of FTK
    else:
        app = Application().start(args.ftklocation)
    time.sleep(0.5) 

    #-----------------START TARGETED COLLECTIONS-----------------------
    if args.type == "targeted":
        print("Targeted imaging selected")
        #Importing full paths from txt file that need to be imaged
        ProjectFile = open(args.filepath, 'r') #Python default is UTF-8 for reading files
        lines = ProjectFile.readlines()  # return a list of lines in file
        
        #For each line in txt file add the source path, making sure the FTK window is active
        ftkOpen = app.window(title_re=".*AccessData*") 
        if ftkOpen.wait(wait_for = 'active', timeout=120, retry_interval = 3):
            for line in lines:                      
                pyautogui.hotkey('alt', 'f')
                time.sleep(0.5)
                pyautogui.keyDown('a')
                time.sleep(0.1)
                pyautogui.keyDown('down')
                pyautogui.keyDown('down')
                pyautogui.keyDown('down')
                time.sleep(0.1)
                pyautogui.keyDown('n')
                time.sleep(0.1) 
                pyautogui.typewrite(line)
                pyautogui.hotkey('alt', 'f')
        #Closing text file                   
        ProjectFile.close   
        
        #Navigating to Create Image, making sure the FTK window is active
        while ftkOpen.wait(wait_for = 'active', timeout=120, retry_interval = 2):
            pyautogui.hotkey('alt', 'v')
            pyautogui.keyDown('c')
            # print("Locating \"New\" button on screen")
            # pyautogui.click(pyautogui.locateCenterOnScreen('New.png')) #Click on the "new" button in FTK Imager
            pyautogui.keyDown('tab')
            pyautogui.keyDown('enter')
            time.sleep(0.1)
            pyautogui.hotkey('alt', 'f')
            time.sleep(0.2)
            pyautogui.keyDown('e')
            time.sleep(0.1)
            break
    #-----------------END TARGETED COLLECTIONS-----------------------

    #-----------------START PHYSICAL & LOGICAL COLLECTIONS-----------------------

    #For physical collections do the following
    if args.type == "physical" or args.type == "logical":
        if args.type == "physical":
            print("Physical imaging selected")
        if args.type == "logical":
            print("Logical imaging selected")
        #Making sure the FTK window is active
        ftkOpen = app.window(title_re=".*AccessData*") 
        if ftkOpen.wait(wait_for = 'active', timeout=120, retry_interval = 5):
            pyautogui.hotkey('alt', 'f')
            time.sleep(0.5)
            pyautogui.keyDown('c')
            time.sleep(0.1)
            if args.type == "logical":
                pyautogui.keyDown('down')
            pyautogui.keyDown('n')
            time.sleep(0.5)
            if args.type == "physical":
                easygui.msgbox("Please select the drive to be imaged \n The script will continue after you select \"Finish\"", title="Select Drive")
                print("Waiting for user to select drive")
            if args.type == "logical":
                easygui.msgbox("Please select the parition to be imaged \n The script will continue after you select \"Finish\"", title="Select Drive")
                print("Waiting for user to select partition")    


    #-----------------END PHYSICAL & LOGICAL COLLECTIONS-----------------------

    #Wait for create image window to continue
    createImage = app.window(title_re=".*Create*") 
    while createImage.wait(wait_for = 'exists', timeout=120, retry_interval = 3):
        
        #Printing messages for user
        if args.type == "physical":
            print("Drive selected")
        if args.type == "logical":
            print("Partition selected")

        pyautogui.hotkey('alt', 'a')
        if args.type == "physical" or args.type == "logical":
            pyautogui.hotkey('e')
            pyautogui.hotkey('enter')
        break

    #Auto fill in evidence item information, making sure that the window is active
    evidenceInformation = app.window(title_re=".*Evidence*") 
    while evidenceInformation.wait(wait_for = 'ready', timeout=120, retry_interval = 5):
        print("Adding evidence information")
        pyautogui.typewrite(args.casenumber)
        pyautogui.keyDown('tab')
        pyautogui.typewrite(args.evidencenumber)
        pyautogui.keyDown('tab')
        pyautogui.typewrite(args.evidencenumber)
        pyautogui.keyDown('tab')
        pyautogui.typewrite(args.examiner)
        pyautogui.keyDown('tab')
        pyautogui.typewrite(args.notes)
        pyautogui.keyDown('enter')
        break

    #Auto fill in select image destination, making sure that the window is active
    selectImage = app.window(title="Select Image Destination")
    while selectImage.wait(wait_for = 'ready', timeout=120, retry_interval = 2):
        print("Setting image destination details")
        pyautogui.typewrite(args.destinationfolder) 
        pyautogui.keyDown('tab')
        pyautogui.keyDown('tab')
        pyautogui.typewrite(args.filename)
        time.sleep(0.1)
        pyautogui.keyDown('tab')
        pyautogui.typewrite(args.segmentsize)
        pyautogui.keyDown('tab')
        pyautogui.typewrite(args.compression)
        pyautogui.keyDown('enter')
        time.sleep(0.1)
        pyautogui.keyDown('down')
        pyautogui.keyDown('enter')
        break

    #Checking for destination folder errors

    time.sleep(0.5)
    try:
        if selectImage.wait(wait_for = 'exists', timeout=1):
            print("It seems like something went wrong. Make sure to check if the destination folder exists and is empty")
            sys.exit()
    except timings.TimeoutError:
        print(datetime.datetime.now().strftime("Imaging started at: ""%Y-%m-%d %H:%M:%S"))
            
    #waiting for image completion and closing FTK
    imageComplete = app.window(title="Drive/Image Verify Results") 
    while imageComplete.wait(wait_for = 'active', timeout=999999, retry_interval = 5):
        pyautogui.keyDown('enter')
        break
    pyautogui.keyDown('enter')
    pyautogui.keyDown('enter')

    #Close application
    print(datetime.datetime.now().strftime("Imaging was completed at: ""%Y-%m-%d %H:%M:%S"))
    print("FTK is closing down")
    time.sleep(0.5)
    pyautogui.hotkey('alt', 'F4')

FTKAutomater() 