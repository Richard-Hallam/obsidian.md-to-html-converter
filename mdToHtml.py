def file_import(file):
    with open(file, 'r') as f:
        return [line.strip() for line in f]


def insert_lines_into_list(files):
    result = []
    for file in files:
        result.extend(file_import(file))
    return result


#separates all characters into one list
def insert_characters_into_list(list):
    result = []
    for i in list:
        for char in i:
            result.append(char)
    print(result)
    return result        
    

files_to_process = ['flexbox.md']
#print(insert_lines_into_list(files_to_process))
insert_characters_into_list(insert_lines_into_list(files_to_process))