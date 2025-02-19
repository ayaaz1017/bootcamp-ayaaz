def filtered_file_generator(filename, keyword):
    for line in file_line_generator(filename):
        if keyword in line:
            yield line


for line in filtered_file_generator('sample.txt', 'Python'):
    print(line)