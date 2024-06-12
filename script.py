import argparse
import os
import shutil

def main():
    parser = argparse.ArgumentParser(description='Automate a batch-creation of working directories')
    parser.add_argument('input_file', type=argparse.FileType('r'), help='Input 1.txt with directory names, one per line')
    parser.add_argument('input_files', nargs='+', type=argparse.FileType('r'), help='Input 2.txt, 3.txt, ... with file names, one per line')
    args = parser.parse_args()

    dir_names = [line.strip() for line in args.input_file.readlines()]
    file_names_list = [file.readlines() for file in args.input_files]

    for i, dir_name in enumerate(dir_names):
        dir_path = os.path.join('./', dir_name)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
            print(f"Directory {dir_name} created!")
        else:
            print(f"Directory {dir_name} already exists")

        for j, file_names in enumerate(file_names_list):
            subdirname, _ = os.path.splitext(args.input_files[j].name)
            sub_dir_path = os.path.join(dir_path, subdirname)
            if not os.path.exists(sub_dir_path):
                os.mkdir(sub_dir_path)
                print(f"  Subdirectory {subdirname} created in {dir_name}!")

            for k, file_name in enumerate(file_names):
                file_name = file_name.strip()
                file_path = os.path.join('./', file_name)
                if k < len(dir_names) and dir_names[k] == dir_name:
                    if os.path.exists(file_path):
                        shutil.move(file_path, sub_dir_path)
                        print(f"  File {file_name} moved to {dir_name}/{subdirname}!")
                    else:
                        print(f"  File {file_name} not found!")

if __name__ == "__main__":
    main()