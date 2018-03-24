import os
import sys


def find_file(file_to_search, path):
    result = []
    if file_to_search.startswith("*"):
        pattern = file_to_search[1:]
        for dirpath, _, file_names_list in os.walk(os.path.join(path,"")):
            for filename in file_names_list:
                if filename.endswith(pattern):
                    result.append(os.path.join(dirpath, filename))
    elif file_to_search.endswith("*"):
        pattern = file_to_search[:-1]
        for dirpath, _, file_names_list in os.walk(os.path.join(path,"")):
            for filename in file_names_list:
                if filename.startswith(pattern):
                    result.append(os.path.join(dirpath, filename))
    else:
        for dirpath, _, file_names_list in os.walk(os.path.join(path, "")):
            if file_to_search in file_names_list:
                result.append(os.path.join(dirpath, file_to_search))
    return result


if len(sys.argv) >= 2:
    filename_to_search = sys.argv[1]
    found_filename = find_file(filename_to_search, sys.argv[2])
    if found_filename:
        print("Files found:")
        for fn in found_filename:
            print(fn)
    else:
        print("File not found")
else:
    print("Please provide a filename as a first parameter and path as second")