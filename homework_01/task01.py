"""1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате
и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode
и также проверить тип и содержимое переменных."""


word01 = "разработка"
word02 = "сокет"
word03 = "декоратор"

word01_enc = "\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430"  # разработка

print(word01)
print(type(word01))
print(word01_enc)
print(type(word01_enc))
print(word01.encode('utf-8'))

"""
разработка
<class 'str'>
разработка
<class 'str'>
b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0'
"""

word02_enc = "\u0441\u043e\u043a\u0435\u0442"  # сокет

print(word02)
print(type(word02))
print(word02_enc)
print(type(word02_enc))
print(word02.encode('utf-8'))

"""
сокет
<class 'str'>
сокет
<class 'str'>
b'\xd1\x81\xd0\xbe\xd0\xba\xd0\xb5\xd1\x82'
"""

word03_enc = "\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440"  # декоратор

print(word03)
print(type(word03))
print(word03_enc)
print(type(word03_enc))
print(word03.encode())

"""
декоратор
<class 'str'>
декоратор
<class 'str'>
b'\xd0\xb4\xd0\xb5\xd0\xba\xd0\xbe\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80'
"""