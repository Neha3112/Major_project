import numpy as np
from PIL import Image
import os

folder_path = 'C:\\Users\\Neha\\Documents\\Major_project\\images'  # Replace this with the path to your folder
output_folder = 'C:\\Users\\Neha\\Documents\\Major_project\\preprocessing\\grayimage'

# List all files in the folder
image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

for image_file in image_files:
    image_path = os.path.join(folder_path, image_file)

    # Process each image
    im_gray = np.array(Image.open(image_path).convert('L'))
    print(f"Processed image: {image_path}")
    # Add your processing logic here
    thresh = 128

    im_bool = im_gray > thresh
    print(im_bool)
    # [[ True  True  True ...  True  True False]
    #  [ True  True  True ...  True  True False]
    #  [ True  True  True ...  True False False]
    #  ...
    #  [False False False ... False False False]
    #  [False False False ... False False False]
    #  [False False False ... False False False]]
    
   # Assuming you have defined im_gray and thresh earlier in your code
   

    # Binarization
    im_bin_keep = (im_gray > thresh) * im_gray
    
    # Save the binarized image to the output folder
    os.makedirs(output_folder, exist_ok=True)  # Ensure the folder exist
    output_path = os.path.join(output_folder, f"binarized_{image_file}")
    Image.fromarray(np.uint8(im_bin_keep)).save(output_path)

    print(f"Binarized image saved: {output_path}")

