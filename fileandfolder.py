import os
import shutil

# Create a new file
with open('example.txt', 'w') as file:
    file.write('Hello, world!')
print('File created: example.txt')

# Create a new directory
os.makedirs('example_folder', exist_ok=True)
print('Folder created: example_folder')

# Move the file into the directory
shutil.move('example.txt', 'example_folder/example.txt')
print('File moved to: example_folder/example.txt')

# Create a destination folder
os.makedirs('new_location', exist_ok=True)

# Move the directory
shutil.move('example_folder', 'new_location/example_folder')
print('Folder moved to: new_location/example_folder')

# Rename the file
os.rename('new_location/example_folder/example.txt', 'new_location/example_folder/new_example.txt')
print('File renamed to: new_example.txt')

# Rename the directory
os.rename('new_location/example_folder', 'new_location/new_example_folder')
print('Folder renamed to: new_example_folder')

# Delete the file
os.remove('new_location/new_example_folder/new_example.txt')
print('File deleted: new_example.txt')

# Delete the directory
shutil.rmtree('new_location/new_example_folder')
print('Folder deleted: new_example_folder')