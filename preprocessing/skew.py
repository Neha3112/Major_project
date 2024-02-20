import cv2
import os
import numpy as np
from scipy.ndimage import interpolation as inter

def correct_skew(image, delta=1, limit=5):
    def determine_score(arr, angle):
        data = inter.rotate(arr, angle, reshape=False, order=0)
        histogram = np.sum(data, axis=1, dtype=float)
        score = np.sum((histogram[1:] - histogram[:-1]) ** 2, dtype=float)
        return histogram, score

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    scores = []
    angles = np.arange(-limit, limit + delta, delta)
    for angle in angles:
        histogram, score = determine_score(thresh, angle)
        scores.append(score)

    best_angle = angles[scores.index(max(scores))]

    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, best_angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, \
          borderMode=cv2.BORDER_REPLICATE)

    return best_angle, rotated

# Specify the input folder and output folder
input_folder_path = 'C:\\Users\\Admin\\Major_project\\preprocessing\\gray scale'
output_folder_path = 'C:\\Users\\Admin\\Major_project\\preprocessing\\skew image'


# Create the output folder if it doesn't exist
os.makedirs(output_folder_path, exist_ok=True)

# List all files in the input folder
image_files = [f for f in os.listdir(input_folder_path) if os.path.isfile(os.path.join(input_folder_path, f))]

# Process and save images
for image_file in image_files:
    input_path = os.path.join(input_folder_path, image_file)

    # Load the image
    image = cv2.imread(input_path)

    # Correct skew
    angle, rotated = correct_skew(image)

    # Save the rotated image to the output folder
    output_path = os.path.join(output_folder_path, f"rotated_{os.path.basename(input_path)}")
    cv2.imwrite(output_path, rotated)

    print(f"Rotated image saved: {output_path}")