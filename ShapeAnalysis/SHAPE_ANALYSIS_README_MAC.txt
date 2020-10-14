Otolith Shape Analyzer

This program uses the ShapeR package (detailed at https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0121102#sec004) to calculate otolith area, length, perimeter and width.

Overview:
* The folder 'Originals' contains .jpg files of the otoliths, separated into area folders each with two-letter names of the sampling unit, eg. 'GS' (as specified in the ShapeR documentation)
* The folder 'Fixed' must be an exact copy of the Originals folder
* The file shape_analysis.py is the Python script to analyze the otoliths
* Getting accurate measurements of the otoliths requires a calibration value equal to the number of pixels representing 1mm in the images
* CAUTION - running the script will overwrite the files 'original_files.csv' and 'OUTPUT.csv'

For the first time running the code on your computer, please read the documentation in OtolithScripts/README_MAC.txt to ensure you have the correct programs installed.

To run this program:
1. Open 'shape_analysis.py' in a text editor to change the calibration value (called 'CAL') if necessary
2. In Finder, navigate to the folder 'OtolithScripts'
3. Right-click on the 'ShapeAnalysis' folder and click on 'New Terminal at Folder'
4. Enter the following command: python3 shape_analysis.py
5. The script creates a file called 'original_files.csv' listing all of the files in the 'Originals' folder
6. Once the script has finished running, the file 'Results.csv' will contain the otolith measurements