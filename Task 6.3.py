file_list = ['1.txt', '2.txt', '3.txt']
row_count_list = []

for file in file_list:
    file_contents = open(file, encoding='utf-8')
    row_count = len(file_contents.readlines())
    row_count_list.append(row_count)

file_name_and_length = list(zip(row_count_list, file_list))
file_name_and_length.sort()

file_list_sort = map(lambda element: element[1], file_name_and_length)

for file in file_list_sort:
    print(file)
    file_contents = open(file, encoding='utf-8')
    row_count = len(file_contents.readlines())
    print(row_count)
    file_contents = open(file, encoding='utf-8')
    text_of_file = file_contents.read()
    print(text_of_file)
