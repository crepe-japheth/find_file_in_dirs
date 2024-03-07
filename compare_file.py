import os
import filecmp

class CompareFiles(object):

    def __init__(self, all_files) -> None:
        self.all_files = all_files
        self.equal_files = []

    def compare_files(self):
        files = self.get_all_file_path()
        for i in range(len(files)):
            for j in range(i+1,len(files)):
                file1 = files[i]
                file2 = files[j]
                if filecmp.cmp(file1, file2, shallow=True):
                    self.equal_files.append((file1, file2))
        return self.equal_files
            

    def get_all_file_path(self) -> list:
        files = []
        for path, filename, ext in zip( self.all_files['file_path'], self.all_files['file_name'], self.all_files['extension']):
            full_path = os.path.join(path,filename + ext)
            files.append(full_path)
        return files