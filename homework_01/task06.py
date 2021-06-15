"""
6. Создать текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор».
Проверить кодировку файла по умолчанию.
Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""

test_file = open("test_file.txt", "w", encoding="utf-8")  # без параметра encoding (по умолчанию) в файл не пишет
test_file.write("сетевое программирование\n")
test_file.write("сокет\n")
test_file.write("декоратор")
test_file.close()

with open("test_file.txt", encoding='utf=8') as test_file:
    for el_str in test_file:
        print(el_str)
