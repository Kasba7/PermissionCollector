import os
import subprocess

def take_ownership(folder_path, owner_name):
    # List all files and directories in the given folder
    for root, dirs, files in os.walk(folder_path):
        # Take ownership of files in the current directory
        for file_name in files:
            file_path = os.path.join(root, file_name)
            print(f"Taking ownership of file: {file_path}")

            # Execute takeown command to take ownership of the file
            try:
                subprocess.run(['takeown', '/F', file_path], check=True, capture_output=True)
            except subprocess.CalledProcessError as e:
                print(f"Error taking ownership of {file_path}: {e.stderr.decode('utf-8')}")

            # Optional: Grant full control permissions to the specified owner
            try:
                subprocess.run(['icacls', file_path, '/grant', f"{owner_name}:(F)"], check=True, capture_output=True)
            except subprocess.CalledProcessError as e:
                print(f"Error granting permissions for {owner_name} on {file_path}: {e.stderr.decode('utf-8')}")

        # Recursively take ownership of files in subdirectories
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            print(f"Taking ownership of folder: {dir_path}")

            # Execute takeown command to take ownership of the directory
            try:
                subprocess.run(['takeown', '/F', dir_path], check=True, capture_output=True)
            except subprocess.CalledProcessError as e:
                print(f"Error taking ownership of {dir_path}: {e.stderr.decode('utf-8')}")

            # Optional: Grant full control permissions to the specified owner
            try:
                subprocess.run(['icacls', dir_path, '/grant', f"{owner_name}:(F)"], check=True, capture_output=True)
            except subprocess.CalledProcessError as e:
                print(f"Error granting permissions for {owner_name} on {dir_path}: {e.stderr.decode('utf-8')}")

if __name__ == "__main__":
    folder_path = r"Replace with the path to your folder"  # path of your folder
    owner_name = "Replace with the desired owner name(User)"  # Owner name

    take_ownership(folder_path, owner_name)