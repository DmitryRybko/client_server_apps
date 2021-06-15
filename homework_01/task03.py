"""3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе."""

# можно записать в байтовом типе:

word_01 = 'attribute'
word_02 = 'type'

# нельзя записать в байтовом типе:

word_03 = 'класс'
word_04 = 'функция'


def ascii_string(*args):
    """функция для проверки, что строку можно записать в байтовом типе"""
    for item in args:
        check_byte_type_possibility = item.isascii()
        if check_byte_type_possibility:
            conclusion = "можно"
        else:
            conclusion = "нельзя"
        print(f'слово "{item}" {conclusion} записать в байтовом типе')
    return None


ascii_string(word_01, word_02, word_03, word_04)
