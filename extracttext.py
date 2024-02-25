import cv2
import numpy as np

# Function to draw bounding box on image
def draw_bbox(image, bbox):
    x, y, w, h = bbox
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Function to annotate images with bounding boxes
def annotate_images(images, annotations):
    for image_path, bbox_list in zip(images, annotations):
        image = cv2.imread(image_path)
        for bbox in bbox_list:
            draw_bbox(image, bbox)
        cv2.imshow('Annotated Image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# Example usage
if __name__ == '__main__':
    # List of image paths
    images = ['C:\\Users\\Admin\\Major_project\\images\\image0.jpg', 'C:\\Users\\Admin\\Major_project\\images\\image1.jpg', 'C:\\Users\\Admin\\Major_project\\images\\image2.jpg']
    
    # List of bounding box annotations for each image
    annotations = [
        [(100, 100, 200, 150), (300, 200, 150, 100)],  # Bounding boxes for image1
        [(50, 50, 300, 200)],                            # Bounding boxes for image2
        [(200, 150, 250, 200)]                           # Bounding boxes for image3
    ]
    
    # Annotate images with bounding boxes
    annotate_images(images, annotations)