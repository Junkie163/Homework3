import os
import glob


def get_file_paths():
    files_path = os.getcwd() + "/files/"
    file_paths = glob.glob(files_path + "*.txt")
    print(files_path)
    print(file_paths)
    return file_paths


print(get_file_paths())


def read_file_and_write_to_result():
    file_paths = get_file_paths()
    file_content_list = []
    for file in file_paths:
        file_name = file.split("/")[-1]
        with open(file, encoding="utf-8") as f:
            data = f.readlines()
            file_content_list.append([len(data), file_name, data])
    file_content_list.sort()
    with open("files/result.txt", "w", encoding="utf-8") as res_f:
        for item in file_content_list:
            res_f.write(f"{item[0]}\n{item[1]}\n{item[2]} \n")
    return file_content_list


print(read_file_and_write_to_result())
