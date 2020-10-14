from PIL import Image
import os
import xlwt
from xlwt import Workbook

path = './Originals/' # Contains the red/green images
workbook = Workbook() # Excel workbook to contain the results
sheet = workbook.add_sheet("Results")

def process_img(image, row_num):
    print(image)
    img = Image.open(os.path.join(path, image))
    width, height = img.size
    red = 0
    green = 0

    # Iterate through each pixel. 
    # If pixel is red, increment the red count.
    # If pixel is green, increment the green count.
    for x in range(1, width):
        for y in range(1, height):
            r, g, b = img.getpixel( (x, y) )
            if (r > 180 and g < 30 and b < 30):
                red += 1
            elif (r < 30 and g > 180 and b < 30):
                green += 1

    # Write results to Excel
    sheet.write(row_num, 0, image)
    sheet.write(row_num, 1, red)
    sheet.write(row_num, 2, green)
    sheet.write(row_num, 3, red/(red+green)*100)
    sheet.write(row_num, 4, green/(red+green)*100)

if __name__ == '__main__':
    # Write headers for results file
    style = xlwt.easyxf('font: bold 1') 
    sheet.write(0, 0, 'Image name', style)
    sheet.write(0, 1, 'Red pixels', style)
    sheet.write(0, 2, 'Green pixels', style)
    sheet.write(0, 3, 'Percentage red', style)
    sheet.write(0, 4, 'Percentage green', style)

    # Process each file and write results to Excel
    print('Processing images... (please be patient)')
    row_num = 1
    for filename in os.listdir(path):
        process_img(filename, row_num)
        row_num += 1
    print('Processing complete!')

    # Write results to Excel
    print('Writing results...')
    workbook.save("Results.xls")
    print('Results written successfully!')
