def file_reading(filename):
    with open ('file.txt', 'r') as file:
        for line in file:
            yield line.strip()


file = file_reading('file.txt')
for line in file:
    print(line)
