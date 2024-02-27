import os, time
from datetime import datetime
import pandas as pd
import logging


folder_with_files = {
    "extension":[], "file_name":[],"file_created":[],"file_modified":[],"file_accessed":[], "file_path":[]
    }

numb_of_file_in_folder = {}

contain_content = []


def get_path():
    path = input('Please enter your full Path: ')
    return path



def get_path_content(path):

    folder_files = os.listdir(rf'{path}')

    for file in folder_files:
        if os.path.isdir(os.path.join(path, file)):
            new_path = os.path.join(path, file)
            get_path_content(new_path)
        else:
            number_of_file = len(list(os.walk(path))[0][-1])
            numb_of_file_in_folder[path] = number_of_file
            full_path = os.path.join(path, file)
            folder_with_files["file_path"].append(path)
            file_name, ext = os.path.splitext(file)
            folder_with_files["file_name"].append(file_name)
            folder_with_files["extension"].append(ext)
            folder_with_files["file_created"].append(time.ctime(os.path.getctime(full_path)))
            folder_with_files["file_modified"].append(time.ctime(os.path.getmtime(full_path)))
            folder_with_files["file_accessed"].append(time.ctime(os.path.getatime(full_path)))

    return folder_with_files, numb_of_file_in_folder


def search_content(result, extension, content):
    directories = []
    for path, filename, ext in zip( result[0]['file_path'], result[0]['file_name'], result[0]['extension']):
        full_path = os.path.join(path,filename + ext)
        directories.append(full_path)

    for directory in directories:
        if directory.endswith(f'.{extension}'):
            try:
                with open(directory, 'r') as file:
                    if content in file.read():
                        contain_content.append(directory)
            except:
                print("somethin wrong")  
    return contain_content


def turn_to_csv(dict_data):
    df1 = pd.DataFrame(dict_data[0])
    # df2 = pd.DataFrame(dict_data[1])
    df1.to_csv(f"path_with_files_and_extensions_{str(datetime.today()).split()[0]}.csv")
    # df2.to_csv(f"path_with_number_of_files_{str(datetime.today()).split()[0]}.csv")


if __name__=="__main__":
    my_path = get_path()
    result = get_path_content(my_path)
    turn_to_csv(result)
    content = search_content(result,"txt", "Hello this file")
    print(f' the file that contain is : {content}')



# my_path = 'C:\Users\PC\Desktop\projects\scrap_data'