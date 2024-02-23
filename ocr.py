import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
image_path = "C:\\Users\\Neha\\Documents\\Major_project\\black.jpg"
image = Image.open(image_path)
extracted_text = pytesseract.image_to_string(image)

print(extracted_text)
with open("C:\\Users\\Neha\\Documents\\Major_project\\output.txt", "w") as output_file:
    output_file.write(extracted_text)