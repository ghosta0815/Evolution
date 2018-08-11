"""Script to convert all Python UI files in the View folder to .py files"""
import os
from PyQt5 import uic


if __name__ == '__main__':
    FILES_PATH = os.path.join(os.getcwd(), "Evolution\\View")
    FILE_LIST = os.listdir(FILES_PATH)

    for file in FILE_LIST:
        filename, file_extension = os.path.splitext(file)
        if file_extension == ".ui":
            full_path_ui = os.path.join(FILES_PATH, filename + ".ui")
            full_path_py = os.path.join(FILES_PATH, "Ui_" + filename + ".py")
            print("Converting: " + full_path_ui)
            with open(full_path_py, 'w') as output_file:
                uic.compileUi(full_path_ui, output_file)
                