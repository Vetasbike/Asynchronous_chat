#1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить
#   тип и содержание соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать
#   строковые представление в формат Unicode и также проверить тип и содержимое переменных.
word = ['разработка', 'сокет', 'декоратор']
for i in word:
    print(type(i),i)

word_unicode = [
    '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
    '\u0441\u043e\u043a\u0435\u0442',
    '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
    ]

for i in word_unicode:
    print(type(i), i)


#2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования
#   в последовательность кодов (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
import binascii

word_n = [b'class', b'function', b'method']

for i in word_n:
    print(type(i), binascii.hexlify(i), len(i))


#3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
var_list =['attribute', 'класс', 'функция', 'type']

for i in var_list:
    try:
        print(bytes(i, 'ascii'))
    except UnicodeEncodeError:
        print(f'"{i}" невозможно записать в байтовом типе.')

#4. Преобразовать слова «разработка», «администрирование», «protocol», «sntadard» из строкового представления
#   в байтовое и выполнить обратное преобразование (используя методы encode и decode).

strs = ['разработка', 'администрирование', 'protocol', 'sntadard']
strs_in_bytes = []

for i in strs:
    i = i.encode('utf-8')
    strs_in_bytes.append(i)
print(strs_in_bytes)

strs_in_str = []
for i in strs_in_bytes:
    i = i.decode('utf-8')
    strs_in_str.append(i)
print(strs_in_str)


#5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип на кириллице.
import subprocess, chardet

args = ['ping', 'yandex.ru']
subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in subproc_ping.stdout:
    ping_results = chardet.detect(line)
    print(ping_results)
    line = line.decode(ping_results['encoding']).encode('utf-8')
    print(line.decode('utf-8'))

args = ['ping', 'youtube.com']
subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in subproc_ping.stdout:
    ping_results = chardet.detect(line)
    print(ping_results)
    line = line.decode(ping_results['encoding']).encode('utf-8')
    print(line.decode('utf-8'))

#6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
#   Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.
import locale
import chardet

print(locale.getpreferredencoding())

# cp1251

with open('test_file.txt', 'rb') as fl:
    s = fl.read()
    print(s)
    print(chardet.detect(s))

# b'\xf1\xe5\xf2\xe5\xe2\xee\xe5 \xef\xf0\xee\xe3\xf0\xe0\xec\xec\xe8\xf0\xee\xe2\xe0\xed\xe8\xe5\r\n\xf1\xee\xea\xe5
# \xf2\r\n\xe4\xe5\xea\xee\xf0\xe0\xf2\xee\xf0'
# {'encoding': 'windows-1251', 'confidence': 0.9929305516756276, 'language': 'Russian'}

with open('test_file.txt', encoding='utf-8', errors='replace') as fl:
    print(fl.read())

# ������� ����������������
# �����
# ���������