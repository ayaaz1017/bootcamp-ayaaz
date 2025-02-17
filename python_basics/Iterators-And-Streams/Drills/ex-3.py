def file_line_generator(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()

for line in file_line_generator('sample.txt'):
    print(line)
    
    
