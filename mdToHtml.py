def file_import(file):
    with open(file, 'r') as f:
        return [line.strip() for line in f]


def insert_lines_into_list(files):
    result = []
    for file in files:
        result.extend(file_import(file))
    return result


# #separates all characters into one list
# def insert_characters_into_list(list):
#     result = []
#     for i in list:
#         for char in i:
#             result.append(char)
#         result.append('\n')#separates lines later.
#     print(result)
#     return result        


#returns a 4 character long string
def return_string_segment_from_list(list_of_chars, count, length):
    return_string = ''
    for i in range(count, (count+length), 1):
        try:
            return_string = return_string + list_of_chars[i]
        except IndexError:
            return_string = return_string + ''


    return return_string


def convert_to_html(list_of_chars):
    count = 0
    line_to_return = ''
    open_code_tag = False
    open_bold_and_em_tag= False
    open_h6_tag = False
    open_h5_tag = False
    open_h4_tag = False
    open_h3_tag = False
    open_h2_tag = False
    open_h1_tag = False
    open_h_tag = False      
    while count < len(list_of_chars):
        if return_string_segment_from_list(list_of_chars, count, 1) == '`' and open_code_tag == False:
            open_code_tag = True
            line_to_return = line_to_return +'<code>'
            count += 1
        elif return_string_segment_from_list(list_of_chars, count, 1) == '`' and open_code_tag == True:
            open_code_tag = False
            line_to_return = line_to_return + '</code>'
            count += 1
        elif return_string_segment_from_list(list_of_chars, count, 3) == ('***' or '___') and open_bold_and_em_tag == False:
            open_bold_and_em_tag = True
            line_to_return = line_to_return +'<b><em>'
            count += 1
        elif return_string_segment_from_list(list_of_chars, count, 3) == ('***' or '___') and open_bold_and_em_tag == False:
            open_bold_and_em_tag = True
            line_to_return= line_to_return +'</b></em>'
            count += 1
        elif return_string_segment_from_list(list_of_chars, count, 6 ) == ('######') and open_h6_tag == False and open_h_tag == False:
            open_h6_tag = True
            open_h_tag = True
            line_to_return = line_to_return + '<h6>'
            count += 1
        elif return_string_segment_from_list(list_of_chars, count, 5) == ('#####') and open_h5_tag == False and open_h_tag == False:
            open_h5_tag = True
            open_h_tag = True
            line_to_return =line_to_return + '<h5>'
            count += 1
        elif return_string_segment_from_list(list_of_chars, count, 4) == ('####') and open_h4_tag == False and open_h_tag == False:
            open_h4_tag = True
            open_h_tag = True
            line_to_return = line_to_return+  '<h4>'
            count += 1
        elif return_string_segment_from_list(list_of_chars, count, 3) == ('###') and open_h3_tag == False and open_h_tag == False:
            open_h3_tag = True
            open_h_tag = True
            line_to_return = line_to_return +'<h3>'
            count += 1
        elif return_string_segment_from_list(list_of_chars, count, 2) == ('##') and open_h2_tag == False and open_h_tag == False:
            open_h2_tag = True
            open_h_tag = True
            line_to_return =line_to_return +'<h2>'
            count += 1
        elif return_string_segment_from_list(list_of_chars, count, 1) == ('#') and open_h1_tag == False and open_h_tag == False:
            open_h1_tag = True
            open_h_tag = True
            line_to_return =line_to_return +'<h1>'
            count += 1
        else:
            count+=1
            line_to_return = line_to_return + return_string_segment_from_list(list_of_chars, count, 1)
    return line_to_return
    
    
files_to_process = ['flexbox.md']
#print(insert_lines_into_list(files_to_process))
# insert_characters_into_list(insert_lines_into_list(files_to_process))
list_of_lines = insert_lines_into_list(files_to_process)
for lines in list_of_lines:
    print(convert_to_html(lines))