import argparse
import os
import shutil

def main():
    parser = argparse.ArgumentParser(description='Automate a batch-creation of working directories')
    parser.add_argument('input_file', type=argparse.FileType('r'), help='Input 1.txt with directory names, one per line')
    parser.add_argument('input_file1', type=argparse.FileType('r'), help='Input 2.txt with file names, one per line')
    args = parser.parse_args()

    dir_names = [line.strip() for line in args.input_file.readlines()]
    file_names = [line.strip() for line in args.input_file1.readlines()]
    subdirs = ['workspace', 'models', 'textures']  # Define subdirectory names

    for i, dir_name in enumerate(dir_names):
        dir_path = os.path.join('./', dir_name)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
            print(f"Directory {dir_name} created!")
        else:
            print(f"Directory {dir_name} already exists")

        if i < len(file_names) and file_names[i]:  # Check if file name is not empty
            file_name = file_names[i]
            file_path = os.path.join('./', file_name)

            if os.path.exists(file_path):
                shutil.move(file_path, dir_path)
                print(f"  File {file_name} moved to {dir_name}!")
            else:
                print(f"  File {file_name} not found!")
        else:
            print(f"  No file to move to {dir_name}!")

        workspace_path = os.path.join(dir_path, 'workspace')
        if not os.path.exists(workspace_path):
            os.mkdir(workspace_path)
            print(f"  Subdirectory workspace created in {dir_name}!")
        else:
            print(f"  Subdirectory workspace already exists in {dir_name}!")

        models_path = os.path.join(workspace_path, 'models')
        if not os.path.exists(models_path):
            os.mkdir(models_path)
            print(f"  Subdirectory models created in {dir_name}/workspace!")
        else:
            print(f"  Subdirectory models already exists in {dir_name}/workspace!")

        textures_path = os.path.join(workspace_path, 'textures')
        if not os.path.exists(textures_path):
            os.mkdir(textures_path)
            print(f"  Subdirectory textures created in {dir_name}/workspace!")
        else:
            print(f"  Subdirectory textures already exists in {dir_name}/workspace!")

if __name__ == "__main__":
    main()