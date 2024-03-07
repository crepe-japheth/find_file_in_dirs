import os, time


class FileExplorer(object):

    def __init__(self) -> None:

        # self.path = path
        self.folder_with_files = {
            "extension":[], 
            "file_name":[],
            "file_created":[],
            "file_modified":[],
            "file_accessed":[], 
            "file_path":[],
            "file_size (in KB)":[]
        }
        self.numb_of_file_in_folder = {}
    

    def get_path_content(self, path):
        
        folder_files = os.listdir(path)

        for file in folder_files:
            if os.path.isdir(os.path.join(path, file)):
                new_path = os.path.join(path, file)
                self.get_path_content(new_path)
            else:
                number_of_file = len(list(os.walk(path))[0][-1])
                self.numb_of_file_in_folder[path] = number_of_file
                full_path = os.path.join(path, file)
                self.folder_with_files["file_path"].append(path)
                file_name, ext = os.path.splitext(file)
                self.folder_with_files["file_name"].append(file_name)
                self.folder_with_files["extension"].append(ext)
                self.folder_with_files["file_created"].append(time.ctime(os.path.getctime(rf'{full_path}')))
                self.folder_with_files["file_modified"].append(time.ctime(os.path.getmtime(full_path)))
                self.folder_with_files["file_accessed"].append(time.ctime(os.path.getatime(full_path)))
                self.folder_with_files["file_size (in KB)"].append(os.path.getsize(full_path))

        return self.folder_with_files, self.numb_of_file_in_folder