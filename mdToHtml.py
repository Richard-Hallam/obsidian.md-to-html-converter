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
        result.append('\n')#separates lines later.
    print(result)
    return result        


#returns a 4 character long string
def return_string_segment_from_list(list_of_chars, count):
    return_string = list_of_chars[count] + list_of_chars[count1] + list_of_chars[count+2] + list_of_chars[count +3]


def convert_to_html(list_of_chars):
    count = 0
    while count < len(list_of_chars):
        pass
        
    
    
files_to_process = ['flexbox.md']
#print(insert_lines_into_list(files_to_process))
insert_characters_into_list(insert_lines_into_list(files_to_process))