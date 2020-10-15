Otolith Composition Analyzer

Overview:
* The file composition_analysis.py is the Python code to get the percentages of red or green pixels in an otolith image
* The folder Originals is where the red/ green images are to be stored
* After running the script, the results will be in a file called Results.xls in this folder
* CAUTION - running the script will overwrite the file 'original_files.csv' and 'OUTPUT.csv'

For the first time running the code on your computer, please read the documentation in OtolithScripts/README.txt to ensure you have the correct programs installed.

To run this program:
1. In Finder (File Explorer for Windows), navigate into the folder 'OtolithScripts'
2. For Mac users:
    a. Right-click on the 'CompositionAnalysis' folder and click on 'New Terminal at Folder'
    b. Enter the following command: python3 composition_analysis.py
3. For Windows users:
    a. Shift-right-click on the 'CompositionAnalysis' folder and select 'Open command window here'
    b. Enter the following command: python3 composition_analysis.py
4. The script may take a few minutes to run, depending on the number of images (typically ~3 seconds per photo)
5. Once the script is finished, the results will appear in the file 'OtolithScripts/Results.xls'