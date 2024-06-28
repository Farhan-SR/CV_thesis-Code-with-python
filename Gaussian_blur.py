from PIL import Image, ImageFilter
import os

def apply_gaussian_blur(image_path, output_path, radius):
    # Open an image file
    image = Image.open(image_path)

    # Apply Gaussian blur
    blurred_image = image.filter(ImageFilter.GaussianBlur(radius))

    # Save the blurred image
    blurred_image.save(output_path)

    print(f"Gaussian blur applied with radius {radius} and saved to {output_path}")

def process_multiple_images(input_dir, output_dir, radius):
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # List all files in the input directory
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')):
            input_image_path = os.path.join(input_dir, filename)
            output_image_path = os.path.join(output_dir, filename)
            apply_gaussian_blur(input_image_path, output_image_path, radius)

# Example usage
input_directory = 'C:/Users/alien/Desktop/img_aug/img_in'  # Directory containing input images
output_directory = 'C:/Users/alien/Desktop/img_aug/img_out'  # Directory to save blurred images
process_multiple_images(input_directory, output_directory, radius=2)
