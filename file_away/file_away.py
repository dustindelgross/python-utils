import os
import sys
import shutil

def create_folder_with_files(files):
    if not files:
        print("No files provided.")
        return

    # Create a new folder
    folder_name = "New Folder"
    parent_dir = os.path.dirname(os.path.abspath(files[0]))
    print(f"Parent directory: {parent_dir}")
    new_folder_path = os.path.join(parent_dir, folder_name)
    os.makedirs(new_folder_path, exist_ok=True)


    # Move files to the new folder
    for file in files:
        shutil.move(file, new_folder_path)

    print(f"Folder created: {new_folder_path}")

if __name__ == "__main__":
    create_folder_with_files(sys.argv[1:])
