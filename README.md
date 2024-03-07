# File Explorer

Welcome to File Explorer! This is a simple command-line tool designed to help you explore files within a specified directory path. It provides details like file extension, modification time, access time, and creation time for each file found in the given directory. not only file explorer but you can also see the file that are the same in that directory and search a specific text, words or paragraph in all that return file in directory with specific extensions

## How to Use

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/crepe-japheth/find_file_in_dirs.git
    ```

2. **Navigate to the Project Directory:**

    ```bash
    cd find_file_in_dirs
    ```
2. **create virtual environments (optional):**

    ```bash
    python -m venv env
    ```

3. **Install Dependencies (if any):**

    If there are any dependencies required, please install them using:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Application:**

    ```bash
    python main.py
    ```

5. **Enter the Path:**

    Once the application prompts you to enter a path, provide the directory path you want to explore.

6. **Review Results:**

    After entering the path, the application will generate a CSV file containing information about all the files in the specified directory. This includes details such as file extension, modification time, access time, and creation time.
   
7. **The application will continue to ask you more further action like search, compare files etc:**

    after getting your csv file, keep explorer more action or quit the application if you want


8. **Explore Further:**

    Feel free to modify the code according to your requirements or contribute to the project by opening a pull request.

## Example

Here's an example of how the output CSV file might look:

```csv
File Path,Extension,Modified Time,Accessed Time,Created Time
/path/to/file1.txt,txt,2024-02-27 10:15:32,2024-02-27 10:15:32,2024-02-25 14:20:10
/path/to/file2.csv,csv,2024-02-26 15:45:21,2024-02-26 15:45:21,2024-02-25 14:20:10
...
