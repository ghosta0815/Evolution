from PyQt5 import uic
import os

if __name__ == '__main__':
    files_path = os.path.join(os.getcwd(),"View")
    file_list = os.listdir(files_path)

    for file in file_list:
        filename, file_extension = os.path.splitext(file)
        if file_extension == ".ui":
            full_path_ui = os.path.join(files_path, filename + ".ui")
            full_path_py = os.path.join(files_path, "Ui_" + filename + ".py")
            print("Converting: " + full_path_ui)
            with open(full_path_py, 'w') as output_file:
                uic.compileUi(full_path_ui, output_file)

           
                
            
