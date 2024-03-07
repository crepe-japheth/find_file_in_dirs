from utils import UserInput, ConvertToCSV
from file_explorer import FileExplorer
from file_search import SearchContentInFile
from compare_file import CompareFiles

def main():
    user_path = UserInput()
    file_explorer = FileExplorer()
    file_explorer_data = file_explorer.get_path_content(user_path.path)
    converted_to_csv = ConvertToCSV(file_explorer_data[0])
    converted_to_csv.turn_to_csv()

    run = True
    while run:
        user_next_step = user_path.next_step()
        print(user_next_step)
        if user_next_step == 1:
            ext, content = user_path.get_ext_content(file_explorer_data[0]["extension"])
            search_content_obj = SearchContentInFile(file_explorer_data, ext, content)
            print(search_content_obj.search_file_content())
        elif user_next_step == 2:
            cmp_obj = CompareFiles(file_explorer_data[0])
            equal_files = cmp_obj.compare_files()
            print(equal_files)
        else:
            run = False



if __name__=="__main__":
    main()