def safe_file_processing_pipeline(filename, keyword):
    try:
        for line in filtered_file_generator(filename, keyword):
            word_count = count_words(line)
            print(f"Line: {line} | Word Count: {word_count}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

safe_file_processing_pipeline('sample.txt', 'Python')