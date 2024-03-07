import os

class SearchInFile(object):

    def __init__(self, all_files, extension, search_content) -> None:
        
        self.all_files = all_files
        self.extension = extension
        self.search_content = search_content
        self.contain_content = []


    def get_file_full_path(self) -> list:
        directories = []
        for path, filename, ext in zip( self.all_files[0]['file_path'], self.all_files[0]['file_name'], self.all_files[0]['extension']):
            full_path = os.path.join(path,filename + ext)
            directories.append(full_path)
        return directories
    

    

class SearchContentInFile(SearchInFile):        

    def search_file_content(self):
        for directory in self.get_file_full_path():
            if directory.endswith(f'.{self.extension}'):
                try:
                    with open(directory, 'r') as file:
                        for i, line in enumerate(file):
                            if self.search_content in line:
                                self.contain_content.append((directory, i))
                except:
                    print("somethin wrong")  
        return self.contain_content
    

class SearchInPDF(SearchInFile):

    pass


class SearchInExcel(SearchInFile):
    pass
    