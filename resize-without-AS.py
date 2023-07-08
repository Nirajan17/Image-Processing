from PIL import Image
import os
import shutil

# Set the target size for the resized images
target_size = (300, 300)  # Adjust as per your requirement

# Define the path to the directory containing your images
image_dir = "/Users/nirajanpaudel17/Documents/Python/Major-Project/Web-Scrapping/images/"

# Define the path to the directory where resized images will be saved
output_dir = "/Users/nirajanpaudel17/Documents/Python/Major-Project/Temple-Classification/Dataset"  # Adjust as per your requirement

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Iterate over all the files and subdirectories in the image directory
for root, dirs, files in os.walk(image_dir):
    # Get the corresponding subdirectory in the output directory
    relative_dir = os.path.relpath(root, image_dir)
    output_subdir = os.path.join(output_dir, relative_dir)

    # Create the corresponding subdirectory in the output directory if it doesn't exist
    os.makedirs(output_subdir, exist_ok=True)

    for file in files:
        # Check if the file is an image file
        if file.endswith(('.jpg', '.jpeg', '.png')):
            # Get the full path of the image file
            image_path = os.path.join(root, file)

            # Open the image file
            image = Image.open(image_path)

            # Resize the image to the target size
            resized_image = image.resize(target_size)

            # Construct the output path to save the resized image
            output_path = os.path.join(output_subdir, file)

            # Save the resized image to the output path, overwriting if necessary
            resized_image.save(output_path)

            # Print the original and resized dimensions for reference
            print(f"Resized {file}: Original Size: {image.size}, Resized Size: {target_size}")
