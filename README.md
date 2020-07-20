# FTK-Imager-Automation  
A python script for automating the FTK Imager GUI.  

The script's main function is to add source paths to the FTK Imager GUI which it reads from a text file. Once the source paths are added to the GUI automatic image creation can take place.
So basically this script works great if you have many batches of directories that you would like to image. All source paths can be imaged into one image or have imaged seperately.  

I've added in a "Image Notes Template" that can simplify the process and makes sure you are filling in all the required fields. The template is also great to log essential information  
about the evidence that you are collecting.  
```sh
It is possible to create imaging queues by creating a simple batch file, for example the following content will create two images with different content:  
"D:\FTKAutomater.exe"  -p "D:\SourcePaths1.txt" -t "targeted" -c "Project test" -ev "DFT-0001" -e "Fred" -n "Project Name: Project test; " -d "D:\ " -f "3" -s "1024" -co "0"  
"D:\FTKAutomater.exe"  -p "D:\SourcePaths2.txt" -t "targeted" -c "Project test" -ev "DFT-0001" -e "Fred" -n "Project Name: Project test; " -d "D:\ " -f "2" -s "1024" -co "0"  
```
```
usage: FTKAutomater.exe [-h] [-q] [-p] [-t] [-c] [-ev] [-e] [-n] [-d] [-f]  
                                             [-s] [-co] [-ft]  

optional arguments:  
  -h, --help            show this help message and exit  
  -q , --queue          The filepath of your text file that contains all  
                        Imaging Notes (text file must be in UTF-8 formatting)  
  -p , --filepath       The filepath of your text file that contains all  
                        sources for the targeted image (text file must be in  
                        UTF-8 formatting)  
  -t , --type           For targeted collection type "targeted", for physical  
                        collection type "physical" for logical collection type  
                        "logical"  
  -c , --casenumber     FTK: Case Number  
  -ev , --evidencenumber  
                        FTK: Evidence Number  
  -e , --examiner       FTK: Examiner  
  -n , --notes          FTK: Notes  
  -d , --destinationfolder  
                        FTK: Image Destination Folder  
  -f , --filename       FTK: Image Filename  
  -s , --segmentsize    FTK: Segment Size  
  -co , --compression   FTK: Compression (accepts values between 1-9)  
  -ft , --ftklocation   Optional: Full folder path to FTK Imager (e.g.  
                        "C:\Program Files\AccessData\FTK Imager\FTK Imager.exe"  
```                        
Tested with FTK Imager 4.2.0.13  
The script might require some debugging to make it work with the latests version of FTK Imager.  
