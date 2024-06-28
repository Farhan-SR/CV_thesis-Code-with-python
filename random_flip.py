from PIL import Image
import random
import os

def randomly_flip_image(image_path, output_path):
    # Open an image file
    image = Image.open(image_path)

    # Randomly choose the flip direction
    flip_direction = random.choice(['horizontal'])

    # Perform the flip operation
    if flip_direction == 'horizontal':
        flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)
    else:  # flip_direction == 'vertical'
        flipped_image = image.transpose(Image.FLIP_TOP_BOTTOM)

    # Save the flipped image
    flipped_image.save(output_path)

    print(f"Image flipped {flip_direction} and saved to {output_path}")

def process_multiple_images(input_dir, output_dir):
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # List all files in the input directory
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')):
            input_image_path = os.path.join(input_dir, filename)
            output_image_path = os.path.join(output_dir, filename)
            randomly_flip_image(input_image_path, output_image_path)

# Example usage
input_directory = 'C:/Users/alien/Desktop/img_aug/img_in'  # Directory containing input images
output_directory = 'C:/Users/alien/Desktop/img_aug/img_out'  # Directory to save flipped images
process_multiple_images(input_directory, output_directory)
