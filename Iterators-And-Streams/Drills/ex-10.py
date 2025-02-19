def advanced_pipeline(file_list, keyword, output_file):
    try:
        with open(output_file, 'w') as outfile:
            for filename in file_list:
                for line in filtered_file_generator(filename, keyword):
                    word_count = count_words(line)
                    outfile.write(f"Line: {line} | Word Count: {word_count}\n")
    except Exception as e:
        print(f"An error occurred: {e}")


file_list = ['file1.txt', 'file2.txt']
advanced_pipeline(file_list, 'Python', 'output.txt')