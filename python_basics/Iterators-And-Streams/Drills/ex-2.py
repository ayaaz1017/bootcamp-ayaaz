class FileLineIterator:
    def __init__(self, filename):
        self.file = open(filename, 'r')

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline()
        if line:
            return line.strip()  
        else:
            self.file.close()
            raise StopIteration


file_iterator = FileLineIterator('sample.txt')
for line in file_iterator:
    print(line)