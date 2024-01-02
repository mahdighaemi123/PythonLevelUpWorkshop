# solution 1
import cv2

# install cv2: pip install opencv-python

def resize_image(image_path, new_width, new_height):
    image = cv2.imread(image_path)
    resized_image = cv2.resize(image, (new_width, new_height))
    return resized_image


resize_image("image.png", 1024, 1024)