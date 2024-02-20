import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

def image_denoising(image):
    image = np.float32(image)
    denoised_image = cv2.bilateralFilter(image, -1, 25, 25)
    denoised_image = np.uint8(denoised_image)
    return denoised_image

def process_images(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    image_files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]

    for image_file in image_files:
        input_path = os.path.join(input_folder, image_file)
        image = cv2.imread(input_path, 0)

        # Perform image denoising
        denoised_image = image_denoising(image)

        

        # Save denoised image
        output_path = os.path.join(output_folder, f"denoised_{image_file}")
        cv2.imwrite(output_path, denoised_image)

        print(f"Denoised image saved: {output_path}")

# Specify the input and output folders
input_folder_path = 'C:\\Users\\Admin\\Major_project\\preprocessing\\skew image'
output_folder_path = 'C:\\Users\\Admin\\Major_project\\preprocessing\\bilateralimage'

# Process images and save denoised images
process_images(input_folder_path, output_folder_path)