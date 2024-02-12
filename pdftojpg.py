import cv2 as cv
import numpy as np
from pdf2image import convert_from_path
import PyPDF2
from PIL import Image
import re

file = open('C:\\Users\\Admin\\Major_project\\An Analysis of the Performance of Named Entity Recognition.pdf', 'rb')
readpdf = PyPDF2.PdfReader(file)
count = len(readpdf.pages)
print('Page Count ==>', count)

a = 0
open('C:\\Users\\Admin\\Major_project\\path.txt', 'w').close()
while a < count:
    file1 = open('C:\\Users\\Admin\\Major_project\\path.txt', 'a')
    file1.write("C:\\Users\\Admin\\Major_project\\images" + str(a) + ".jpg\n")
    a += 1

images = convert_from_path('C:\\Users\\Admin\\Major_project\\An Analysis of the Performance of Named Entity Recognition.pdf',poppler_path= r'C:\Users\Admin\Downloads\Release-23.11.0-0\poppler-23.11.0\Library\bin')

for i, image in enumerate(images):
    fname = "image" + str(i) + ".jpg"
    image.save(fname, 'JPEG')

img = np.array(Image.open('image0.jpg'))