import os
import shutil

def copy_files(source_folder, destination_folder):
    if not os.path.exists(source_folder):
        print(f"The soruce folder {source_folder} does not exist.")
        return
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)

        try:
            if os.path.isfile(source_path):
                shutil.copy2(source_path, destination_path)
            elif os.path.isdir(source_path):
                if not os.path.exists(destination_path):
                    os.makedirs(destination_path)
                copy_files(source_path, destination_path)
        except Exception as e:
            print(f"Error copying {source_path} to {destination_path}")

def delete_files(folder_path):
    if os.path.exists(folder_path):
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Error removing {file_path}: {e}")
    else:
        print(f"The folder {folder_path} does not exist.")


option = int(input('Do you want clear(1) or copy(2) or clear and copy donwloads(3): '))
if option == 1:
    folder = input('Send me a path: ')
    delete_files(folder)
elif option == 2:
    folder_copy = input('Send me a path to copy: ')
    folder_past = input('Send me a path to past: ')
    copy_files(folder_copy, folder_past)
else:
    delete_files("C:\\Users\\Franww\\Documents\\last_downloads")
    copy_files("C:\\Users\\Franww\\Downloads", "C:\\Users\\Franww\\Documents\\last_downloads")
    delete_files("C:\\Users\\Franww\\Downloads")
print('Finished!!! Enjoy!!!')
