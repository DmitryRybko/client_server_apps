import csv
import codecs
import re


def get_data(data_files):

    headers = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_list = []

    for file in data_files:
        with codecs.open(file, encoding='cp1251') as text_file:
            text_file_lines = text_file.read()
            text_os_prod = re.search(rf"{headers[0]}:(.*?)\r\n", text_file_lines)
            text_os_name = re.search(rf"{headers[1]}:(.*?)\r\n", text_file_lines)
            text_os_code = re.search(rf"{headers[2]}:(.*?)\r\n", text_file_lines)
            text_os_type = re.search(rf"{headers[3]}:(.*?)\r\n", text_file_lines)

        os_prod_list.append(text_os_prod.group(1).lstrip())
        os_name_list.append(text_os_name.group(1).lstrip())
        os_code_list.append(text_os_code.group(1).lstrip())
        os_type_list.append(text_os_type.group(1).lstrip())

    main_list.append(headers)
    main_list.append(os_prod_list)
    main_list.append(os_name_list)
    main_list.append(os_code_list)
    main_list.append(os_type_list)

    return main_list


def write_to_csv(summary_file):

    data = get_data(datafiles)

    with codecs.open(summary_file, 'w', encoding='utf-8') as output_file:
        output_file_writer = csv.writer(output_file, quoting=csv.QUOTE_NONNUMERIC)
        output_file_writer.writerows(data)


datafiles = ["info_1.txt", "info_2.txt", "info_3.txt"]
write_to_csv('extracted_data.csv')
