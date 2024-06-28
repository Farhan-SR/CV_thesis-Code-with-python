import os
import sys
import random
import cv2
import numpy as np
import tkinter as tk
from glob import glob
from tkinter import filedialog


def rotate_image(image, angle):
    center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(center, angle, 1.0)
    result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT,
                            borderValue=(255, 255, 255))
    return result


def adjust_brightness_contrast(image, brightness=0, contrast=0):
    return cv2.addWeighted(image, 1 + float(contrast) / 100.0, image, 0, float(brightness))


# Hide the main tkinter window
root = tk.Tk()
root.withdraw()

# Ask user to select input directory
print("Please select the input directory...")
input_dir = filedialog.askdirectory(title="Select input directory")

# Ask user to select output directory
print("Please select the output directory...")
output_dir = filedialog.askdirectory(title="Select output directory")

# If output directory does not exist, create it
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Process images in input directory
image_formats = ('*.jpg', '*.jpeg', '*.png', '*.bmp', '*.gif', '*.tiff', '*.heic', '*.heif')
image_paths = []
for format in image_formats:
    image_paths.extend(glob(os.path.join(input_dir, format)))

# Get user input for data augmentation parameters
num_rotations = int(input("Enter the number of rotations for each image: "))
# num_crops = int(input("Enter the number of random crops for each image: "))
num_contrasts = int(input("Enter the number of contrast adjustments for each image: "))
num_brightnesses = int(input("Enter the number of brightness adjustments for each image: "))

print("Processing images...")

try:
    # Loop through all image files in the input directory
    for image_path in image_paths:
        # print(f"Processing image: {image_path}")

        # Read the image
        image = cv2.imread(image_path)

        # Save a copy of the original image
        original_image_path = os.path.join(output_dir, f"orig_{os.path.splitext(os.path.basename(image_path))[0]}.jpg")
        # cv2.imwrite(original_image_path, image)

        # Perform specified number of rotations and save copies
        for j in range(num_rotations):
            angle = random.uniform(-10, 10)
            rotated_image = rotate_image(image, angle)
            rotated_image_path = os.path.join(output_dir,
                                              f"rot{j + 1}_{os.path.splitext(os.path.basename(image_path))[0]}.jpg")
            cv2.imwrite(rotated_image_path, rotated_image)
            print(f"Saved rotated image: {rotated_image_path}")

        # Perform specified number of brightness adjustments and save copies
        for j in range(num_brightnesses):
            brightness = random.uniform(-0.5, 60)
            brightened_image = adjust_brightness_contrast(image, brightness=brightness)
            brightened_image_path = os.path.join(output_dir,
                                                 f"brightness_{j + 1}_{os.path.splitext(os.path.basename(image_path))[0]}.jpg")
            cv2.imwrite(brightened_image_path, brightened_image)
            print(f"Saved brightness-adjusted image: {brightened_image_path}")

        print("Data augmentation completed.")

except KeyboardInterrupt:
    print("Data augmentation interrupted by the user.")
    sys.exit(0)