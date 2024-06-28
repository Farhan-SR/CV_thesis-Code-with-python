#!/usr/bin/env python
# coding: utf-8

# In[4]:


import os
from PIL import Image


def compress_images_in_folder(input_folder, output_folder, max_size=(1024, 1024), quality=95):
    """
    Compresses all images in the input folder and saves the compressed versions in the output folder.

    Args:
        input_folder (str): Path to the folder containing input images.
        output_folder (str): Path to save the compressed images.
        max_size (tuple): Maximum dimensions (width, height) of the compressed images.
        quality (int): The quality of the compressed images (0-100).
    """
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over all files in the input folder
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)

        # Check if the file is an image
        if os.path.isfile(input_path) and any(
                filename.endswith(extension) for extension in ['.jpg', '.jpeg', '.png', '.gif']):
            output_path = os.path.join(output_folder, filename)

            # Compress the image
            compress_image(input_path, output_path, max_size, quality)


def compress_image(input_path, output_path, max_size=(1024, 1024), quality=70):
    """
    Compresses the image located at input_path and saves the compressed version at output_path.

    Args:
        input_path (str): Path to the input image file.
        output_path (str): Path to save the compressed image.
        max_size (tuple): Maximum dimensions (width, height) of the compressed image.
        quality (int): The quality of the compressed image (0-100).
    """
    with Image.open(input_path) as img:
        img.thumbnail(max_size)
        img.save(output_path, optimize=True, quality=quality)


# Example usage:
input_folder = "C:/Users/alien/Desktop/img_aug/img_out/"
output_folder = "C:/Users/alien/Desktop/img_aug/out_compressed/"
compress_images_in_folder(input_folder, output_folder)

# In[ ]:




