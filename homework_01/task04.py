"""
4. Преобразовать слова «разработка», «администрирование», «protocol», «standard»
из строкового представления в байтовое и выполнить обратное преобразование 
(используя методы encode и decode).
"""

word01 = "разработка"
word02 = "администрирование"
word03 = "protocol"
word04 = "standard"

words = [word01, word02, word03, word04]
words_bytes = []
words_str = []

for word in words:
    words_bytes.append(word.encode('utf-8'))

for word in words_bytes:
    words_str.append(word.decode('utf-8'))

print("входящие слова:")
print(*words, sep="\n")
print()
print("слова преобразованы в байтовое представление:")
print(*words_bytes, sep="\n")
print()
print("слова преобразованы обратно в строковое представление:")
print(*words_str, sep="\n")
