import os
import shutil



def copy_files(source_dir, destination_dir):
    # Ensure the destination directory exists
    os.makedirs(destination_dir, exist_ok=True)

    # Loop through all files in the source directory
    for file_name in os.listdir(source_dir):
        # Create full file paths
        source_file = os.path.join(source_dir, file_name)
        destination_file = os.path.join(destination_dir, file_name)

        # Check if it's a file and copy it
        if os.path.isfile(source_file):
            shutil.copy(source_file, destination_file)





source = r"C:\Users\MekaMallikharjunaRed\Downloads"
destination = r"C:\Users\MekaMallikharjunaRed\Desktop\vscode\bargage"


copy_files(source, destination)



def copy_files_sub_dirs(source_dir, destination_dir):
    # Copy the entire directory
    shutil.copytree(source_dir, destination_dir)
    print(f"All files and subdirectories copied from {source_dir} to {destination_dir}")



def skip_onerwrite_existing_files(source_dir, destination_dir):
    os.makedirs(destination_dir, exist_ok=True)

    for file_name in os.listdir(source_dir):
        source_file = os.path.join(source_dir, file_name)
        destination_file = os.path.join(destination_dir, file_name)

        # Copy only if the file does not exist at the destination
        # os.path.isfile(), os.path.isdir()
        if os.path.isfile(source_file) and not os.path.exists(destination_file):
            shutil.copy(source_file, destination_file)

    print(f"Files copied from {source_dir} to {destination_dir}")
