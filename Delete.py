import os
import shutil

def delete_files_with_name(directory, file_name):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == file_name:
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"Deleted file: {file_path}")

if __name__ == "__main__":
    folder_A = "/home/starfish/Dataset/BankAccountTP-1BUG"  # 替换为文件夹A的实际路径
    file_name_to_delete = "spc_10.log"      # 替换为要删除的文件名(B文件)
    file_name_to_delete_2 = "slicing_10.log"

    if not os.path.exists(folder_A):
        print(f"Folder {folder_A} not found.")
    else:
        delete_files_with_name(folder_A, file_name_to_delete)
        delete_files_with_name(folder_A, file_name_to_delete_2)
