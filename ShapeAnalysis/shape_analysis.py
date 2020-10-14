# Source for navigating the R embedding in Python: https://towardsdatascience.com/an-introduction-to-working-with-r-and-python-1c51fac0b16f 

# Import packages
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri
from rpy2.robjects.conversion import localconverter
import os
import pandas as pd
import csv
shapeR_pkg = importr('shapeR')

# Import Functions
shapeR = shapeR_pkg.shapeR
detect_outline = shapeR_pkg.detect_outline
smoothout = shapeR_pkg.smoothout
generate_shape_coefficients = shapeR_pkg.generateShapeCoefficients
enrich_master_list = shapeR_pkg.enrich_master_list
get_measurements = shapeR_pkg.getMeasurements

path = './Originals'

# INSERT CALIBRATION VALUE HERE
# Calibration should equal the number of pixels representing 1mm
CAL = 203

# Write a .csv file containing the image name, folder name, and calibration value of every .jpg file in the Originals folder
# This .csv file tells the ShapeR package which images to process
with open('./original_files.csv', 'w+', newline='') as csvfile:
    fieldnames = ['folder', 'picname', 'cal']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    picnames_list = []
    folders_list = []
    cals_list = []
    for root, dirs, files in os.walk(path):
        folder = root.split('/')[-1]
        for filename in files:
            if filename.split('.')[-1] == "jpg":
                picnames_list.append(filename)
                folders_list.append(folder)
                cals_list.append(CAL)
                name = filename.split('.')[0]
                writer.writerow({'folder': folder, 'picname': name, 'cal': CAL})

filedata = {'folder': folders_list, 'picname': picnames_list, 'cal': cals_list}
file_dataframe = pd.DataFrame(data=filedata)

# Generate shape file
anchovyshape = shapeR("./", "original_files.csv")

# Create outlines
anchovyshape = detect_outline(anchovyshape, 0.2, False) 

# Smooth shape
anchovyshape = smoothout(anchovyshape, 100) 

# Get measurement coefficients
anchovyshape = generate_shape_coefficients(anchovyshape) 

# Add measurements to shape file
anchovyshape = enrich_master_list(anchovyshape) 

# Get otolith measurements and put them in an R data frame
anchovymeasures = get_measurements(anchovyshape) 

# Convert R data frame to a python data structure
with localconverter(robjects.default_converter + pandas2ri.converter):
    measurements = robjects.conversion.rpy2py(anchovymeasures)

# Write results to OUTPUT.csv
measurements['picname'] = picnames_list
measurements.to_csv("./Results.csv")