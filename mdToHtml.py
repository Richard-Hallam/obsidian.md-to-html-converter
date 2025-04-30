import os

def file_import(file):
    try:
        with open(file, 'r') as f:
            return [line.strip() for line in f]
    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")
        return []


def file_output(content, filename):
    with open(filename, 'w') as f:
        f.write(content)
    print(f'file converted and saved as {filename}')


def convert_filename(filename):#to do handle being passed a list
    print(filename)
    filename = filename.replace('.md', '.html')
    print(filename)
    return(filename)

# def insert_lines_into_list(files):
#     result = []
#     for file in files:
#         if os.path.isfile(file) and file.endswith('.md'):
#             try:
#                 result.extend(file_import(file))
#             except Exception as e:
#                 print(f"Error processing file '{file}': {e}")
#         else:
#             print(f"Skipping non-Markdown file: '{file}'")
#     return result




def convert_table(lines):
    table_lines = []
    for line in lines:
        if line.startswith('|'):
            line = line.replace('|', '<td>').replace('\n', '</td>\n')
            line = line.replace('<td>', '<tr><td>').replace('</td>', '</td></tr>')
        table_lines.append(line)
    return table_lines




def convert_headers(lines):
    header_map = {
        '######': '<h6>',
        '#####': '<h5>',
        '####': '<h4>',
        '###': '<h3>',
        '##': '<h2>',
        '#': '<h1>'
    }

    html_lines = []
    for line in lines:
        for header, tag in header_map.items():
            if line.startswith(header):
                # Add opening and closing tags
                line = line.replace(header, f"{tag}{line[len(header):]}</{tag[1:]}")
                break
        html_lines.append(line)
    return html_lines


def convert_to_html(lines):
    lines = convert_headers(lines)
    lines = convert_table(lines)
    return '\n'.join(lines)+ '\n'

file_to_process = 'Flexbox.md'
#file_to_process = 'Python.md'
#lines_to_print = insert_lines_into_list(files_to_process)
conversion_file_content = file_import(file_to_process)

file_output(convert_to_html(conversion_file_content), convert_filename(file_to_process))


