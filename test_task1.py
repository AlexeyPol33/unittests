import unittest
from task1 import geo_filter, _stats, maximum_volume, converter

class TestTaskOne (unittest.TestCase):

    def test_stats (self):
        queries_one = [
        'запрос из четырех слов',
        'запрос',
        'слово',
        'смотреть сериалы онлайн',
        'новости спорта',
        'афиша кино',
        'курс доллара',
        'сериалы этим летом',
        'курс по питону',
        'сериалы про спорт']
        queries_two = ['один']
        result_one = {4:1,1:2,3:4,2:3}
        result_two = {1:1}
        self.assertEqual(_stats(queries_one),result_one)
        self.assertEqual(_stats(queries_two),result_two)


    def test_maximum_volume (self):
        stats_one = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
        stats_two = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 999, 'email': 42, 'ok': 98}
        stats_three = {'ok': 98}
        self.assertEqual(maximum_volume(stats_one), 'yandex')
        self.assertEqual(maximum_volume(stats_two), 'google')
        self.assertEqual(maximum_volume(stats_three), 'ok')


    def test_converter (self):
        date_one = ['2018-01-01', 'yandex', 'cpc', 100]
        result_one = {'2018-01-01': {'yandex': {'cpc': 100}}}
        data_two = ['2018-01-01', 'yandex', 'cpc', 100,True, False, (19,99), 'test']
        result_two = {'2018-01-01': {'yandex': {'cpc': {100: {True: {False: {(19, 99): 'test'}}}}}}}
        self.assertEqual(converter(date_one),result_one)
        self.assertEqual(converter(data_two),result_two)

if __name__ == '__main__':
    unittest.main()