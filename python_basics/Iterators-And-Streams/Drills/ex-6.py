def count_words(line):
    return len(line.split())

def file_processing_pipeline(filename, keyword):
    lines = filtered_file_generator(filename, keyword)
    for line in lines:
        word_count = count_words(line)
        print(f"Line: {line} | Word Count: {word_count}")


file_processing_pipeline('sample.txt', 'Python')