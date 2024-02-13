
import numpy as np
from pdf2image import convert_from_path
import PyPDF2
from PIL import Image
import re
import os

pdf_path = 'C:\\Users\\Admin\\Major_project\\images\\6th Semester Provisional Result Sheet.pdf'
output_folder = 'C:\\Users\\Admin\\Major_project\\images'

file = open(pdf_path, 'rb')
readpdf = PyPDF2.PdfReader(file)
count = len(readpdf.pages)
print('Page Count ==>', count)

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

with open('C:\\Users\\Admin\\Major_project\\path.txt', 'w') as file1:
    file1.write("\n")  # Add a newline for separation if needed
    a = 0
    while a < count:
        file1.write(output_folder + "\\image" + str(a) + ".jpg\n")
        a += 1

images = convert_from_path(pdf_path, poppler_path=r'C:\Users\Admin\Downloads\Release-23.11.0-0\poppler-23.11.0\Library\bin')

for i, image in enumerate(images):
    fname = f"{output_folder}\\image{i}.jpg"
    image.save(fname, 'JPEG')

img = np.array(Image.open(f"{output_folder}\\image0.jpg"))

