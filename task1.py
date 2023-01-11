#  Домашнее задание к лекции 4.Коллекции данных.Словари.Множества»

#                             Задание 1
# Дан список с визитами по городам и странам. Напишите код, который возвращает отфильтрованный список geo_logs, содержащий только визиты из России."

geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

def geo_filter(geo_logs):
    country = 'Россия'
    filtered_list = []
    for log in geo_logs:
        if country in str(log):
            filtered_list.append(log)
    return filtered_list

print(geo_filter(geo_logs))
print('\n' + '*' * 50 + '\n')
#                                Задание 2
# Выведите на экран все уникальные гео-ID из значений словаря ids.
# Т.е. список вида [213, 15, 54, 119, 98, 35]

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

def get_unique (ids):
    list_ids = []
    for key in ids:
        list_ids.extend(ids[key])
    return list(set(list_ids))

print(get_unique (ids))

print('\n' + '*' * 50 + '\n')
#                                Задание 3
#Дан список поисковых запросов. Получить распределение количества слов в них. Т.е. поисковых запросов из одного - слова 5%, из двух - 7%, из трех - 3% и т.д.

queries = [
    'запрос из четырех слов',
    'запрос',
    'слово',
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]


def _stats(queries):
    counts_counts_words = dict()
    for querie in queries:
        key = len(querie.split())
        if key in counts_counts_words.keys():
            counts_counts_words[key] += 1
        else:
            counts_counts_words[key] = 1
    return counts_counts_words

for key, value in _stats(queries).items():
  procent = round((value / len(queries)) * 100)
  print(f'поисковых запросов из {key} слов(а): {procent}%')

print('\n' + '*' * 50 + '\n')

#                                   Задание 4
# Дана статистика рекламных каналов по объемам продаж.Напишите скрипт, который возвращает название канала с максимальным объемом. Т.е. в данном примере скрипт должен возвращать 'yandex'.
stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

def maximum_volume(stats):
    max_volume = stats.popitem()
    while len(stats) > 0:
        item = stats.popitem()
        if item[1] > max_volume[1]:
            max_volume = item
    return max_volume[0]

print (maximum_volume(stats))

print('\n' + '*' * 50 + '\n')
#                                    Задание 5
#Напишите код для преобразования произвольного списка вида ['2018-01-01', 'yandex', 'cpc', 100] (он может быть любой длины) в словарь {'2018-01-01': {'yandex': {'cpc': 100}}}

some_list = ['2018-01-01', 'yandex', 'cpc', 100,True, False, (19,99), 'test']
def converter(some_list):
    value = some_list.pop()
    while len(some_list) > 0:
        some_dict = dict()
        key = some_list.pop()
        some_dict[key] = value
        value = some_dict
    return some_dict

print (converter(some_list))