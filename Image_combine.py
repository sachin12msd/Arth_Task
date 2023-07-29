import cv2

img1 = cv2.imread("image1.jpg")
img2 = cv2.imread("image2.jpg")

cv2.imshow('Image 1', img1)
cv2.imshow('Image 2', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()


import cv2
import numpy as np

def combine_images(image1, image2):
    # Resize both images to have the same smaller dimensions
    target_width = 400  # Set your desired width here
    target_height = int(image1.shape[0] * target_width / image1.shape[1])
    
    image1 = cv2.resize(image1, (target_width, target_height))
    image2 = cv2.resize(image2, (target_width, target_height))
    
    # Combine the images horizontally
    combined_image = np.hstack((image1, image2))
    
    return combined_image

if __name__ == "__main__":
    # Load the two input images
    image1 = cv2.imread("image1.jpg")
    image2 = cv2.imread("image2.jpg")

    # Combine the images horizontally
    combined_image = combine_images(image1, image2)

    # Show the combined image
    cv2.imshow("Combined Image", combined_image)
    cv2.waitKey(0) #0 to exit
    cv2.destroyAllWindows()
