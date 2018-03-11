import chardet
import json
from pprint import pprint

# Чтение json файлов
# Выделение текстовой части файла
# Преобразование выделенной части текста в список
# Далее по аналогии с заданием 2.2

# with open('./Jsonfiles/newscy.json', 'rb') as f:
#     data = f.read()
#     result = chardet.detect(data)
#     l = json.loads(data.decode(result['encoding']))
#     # print(l)
#     u = l['rss']['channel']['items']
#     temp = ''
#     for i in range(len(u)):
#         temp += u[i]['description']
#
#
#     print(temp.split())
# Функция file_decode получая на входе закодированный json, на выходе выдает объект - словарь

def file_decode(file_name):
    with open('./Jsonfiles/' + file_name, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        decode_json_data = json.loads(data.decode(result['encoding']))

    return decode_json_data
# Функция  get_items на входе получает объект словарь, на выходе получаем данные из 'items'

def get_items(decoded_file):
    get_items_text = decoded_file['rss']['channel']['items']
    return get_items_text

# На вход получает словарь, из него на выходе получаем строку содержащую в колонке description
def get_description(dict_file):
    temp_text = ''
    for i in range(len(dict_file)):
        temp_text += dict_file[i]['description']
    return temp_text.lower()

#  Создание списка из компонентов текста
def get_split_text(text):
    splitted_text = text.split()
    return splitted_text

# Создание словаря из 10 элементов (самых
# часто встречающихся слов) структурой слово - количество слов (длина слова свыше  6 символов)
def word_dictinary(splitted_text_list):
    word_dict = {}
    for word in splitted_text_list:
        if word in word_dict and len(word) > 6:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    sorted_dict = [(k, word_dict[k]) for k in sorted(word_dict, key=word_dict.get, reverse=True)[:10]]
    return dict(sorted_dict)

def print_result(sorted_word_dict):
    for key, value in sorted_word_dict.items():
        print(f"Слово '{key}' встречается {value} раз")

def core():
    file_name_list = ['newsafr.json', 'newscy.json', 'newsfr.json', 'newsit.json']
    for file_name in file_name_list:

        print(f"В файле {file_name}")
        a = file_decode(file_name)
        b = get_items(a)
        c = get_description(b)
        d = get_split_text(c)
        e = word_dictinary(d)
        print_result(e)
        print("="*70)

core()