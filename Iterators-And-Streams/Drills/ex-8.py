def count_words(line):
    return len(line.split())

def filtered_file_generator(filename, keyword):
    """Generator that yields lines from the file containing the specified keyword."""
    with open(filename, 'r') as file:
        for line in file:
            if keyword in line:
                yield line.strip()  

def file_processing_pipeline(filename, keyword):
    lines = filtered_file_generator(filename, keyword)
    for line in lines:
        word_count = count_words(line)
        print(f"Line: {line} | Word Count: {word_count}")


file_processing_pipeline('sample.txt', 'Python')