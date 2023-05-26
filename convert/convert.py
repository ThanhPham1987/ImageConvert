from colorama import Fore, init
import os
from PIL import Image

def convert_images_to_png(input_folder, output_folder, supported_extensions):
    init()  # Initialize colorama

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all files in the input folder
    files = os.listdir(input_folder)

    # Process each file in the input folder
    for file in files:
        filename, extension = os.path.splitext(file)
        if extension.lower() in supported_extensions:
            # Construct the input and output file paths
            input_path = os.path.join(input_folder, file)
            output_path = os.path.join(output_folder, f"{filename}.png")

            # Open the image file and convert it to PNG
            image = Image.open(input_path)
            image.save(output_path, 'PNG')

            print(Fore.RED + f"Converted {file} to {os.path.basename(output_path)}")
    
    print(Fore.GREEN + f"Conversion completed!")  # Reset color after printing

# Specify the input and output folders
input_folder = 'C:\\Users\\Szymon\\Desktop\\convert\\toconvert'
output_folder = 'C:\\Users\\Szymon\\Desktop\\convert\\converted'

# Specify the supported image file extensions
supported_extensions = ['.jfif', '.webp', '.jpg', '.jpeg', '.png']

# Call the conversion function
convert_images_to_png(input_folder, output_folder, supported_extensions)
