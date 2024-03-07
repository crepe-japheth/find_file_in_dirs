import pandas as pd
from datetime import datetime

class ConvertToCSV(object):

    def __init__(self, data) -> None:
        self.data = data

    def turn_to_csv(self):
        df1 = pd.DataFrame(self.data)
        df1.to_csv(f"path_with_files_and_extensions_{str(datetime.today()).split()[0]}.csv")


class UserInput(object):

    def __init__(self) -> None:
        self.path = input("Please Enter Path You want to explore: ")

    
    def next_step(self):
        print("What would you like to do next : \n")
        print("Type (1) to Search content in file \n")
        print("Type (2) to compare the files \n")
        print("Type (0) to to exit. \n")
        user_input = input("Type your number here: ")
        if not user_input.isnumeric():
            print("Please Enter a valid number...")
            # user_input = input("Type your number here: ")
            self.next_step()
        elif int(user_input) > 3 or int(user_input) < 0:
            print("Value must not greater 3 and must not less that 0")
            self.next_step()
        else:
            user_input = int(user_input)
        return user_input
        

    def get_ext_content(self, all_files_list):
        print("Please Enter Extension of your file name example(xlxs, ppt, py, java...) \n")
        extension = input("Extension here: ")
        print(all_files_list)
        if self.validate_extension(f'.{extension}', all_files_list):
            print("Please Enter content you would like to search for, in the file\n")
            content = input("Enter content here: ")
            return extension, content
        else:
            self.get_ext_content(all_files_list)
    

    def validate_extension(self, extension, all_files_list):
        if extension not in all_files_list:
            return False
        return True


        