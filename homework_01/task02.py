"""2. Каждое из слов «class», «function», «method»
записать в байтовом типе без преобразования в последовательность кодов (не используя методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных."""

# class
word01_bytes = b'\u0063\u006c\u0061\u0073\u0073'
print(word01_bytes)
print(type(word01_bytes))
print(len(word01_bytes))

'''
b'\\u0063\\u006c\\u0061\\u0073\\u0073'
<class 'bytes'>
30
'''

# function

word02_bytes = b'\u0066\u0075\u006e\u0063\u0074\u0069\u006f\u006e'
print(word02_bytes)
print(type(word02_bytes))
print(len(word02_bytes))

'''
b'\\u0066\\u0075\\u006e\\u0063\\u0074\\u0069\\u006f\\u006e'
<class 'bytes'>
48
'''

# method

word03_bytes = b'\u006d\u0065\u0074\u0068\u006f\u0064'
print(word03_bytes)
print(type(word03_bytes))
print(len(word03_bytes))

'''
b'\\u006d\\u0065\\u0074\\u0068\\u006f\\u0064'
<class 'bytes'>
36
'''