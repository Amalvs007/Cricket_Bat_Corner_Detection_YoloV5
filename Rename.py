import os
import shutil

# Input and output folders
input_folder = r"F:\AI\Object_Detection_Data\Bat"
output_folder = r"F:\AI\Object_Detection_Data\Renamed"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# List all files in the input folder
image_files = [f for f in os.listdir(input_folder) if f.lower().endswith((".jpg", ".jpeg", ".png", ".gif"))]

# Initialize a counter for renaming
counter = 0

# Loop through the image files and rename them sequentially
for image_file in image_files:
    # Generate the new filename with leading zeros
    new_filename = f"{counter:04d}.jpg"
    
    # Construct the full path to the input and output files
    old_path = os.path.join(input_folder, image_file)
    new_path = os.path.join(output_folder, new_filename)
    
    # Rename and move the file
    shutil.copy(old_path, new_path)
    
    # Increment the counter for the next file
    counter += 1

print(f"Renamed {counter} image files.")
