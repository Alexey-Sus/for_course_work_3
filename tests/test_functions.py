from src.functions import define_new_vac_list

def test_define_new_vac_list():
    ''' Тестируем функцию преобразования списка вакансий, полученного от класса Vacancy, в удобный и короткий список.
        Эта исходная функция выдает список из коротеньких словарей, состоящих из 4 пар "ключ-значение" '''

    test_list_0: list = [{'name': 'Говновоз', 'alternate_url': 'https://kremlin.ru', 'salary': {'from': 900000000},
                        'snippet': {'requirement': 'Уметь жить в ... и радоваться',
                                    'responsibility': 'Возить ... с улыбкой. Давать мороженку постоянным клиентам.'}}]

    test_list_1: list = [{'name': 'Говновоз', 'alternate_url': 'https://kremlin.ru', 'salary': None,
                        'snippet': {'requirement': 'Уметь жить в ... и радоваться',
                                    'responsibility': 'Возить ... с улыбкой. Давать мороженку постоянным клиентам.'}}]

    test_list_2: list = [{'name': 'Говновоз', 'alternate_url': 'https://kremlin.ru', 'salary': {'from': None},
                        'snippet': {'requirement': 'Уметь жить в ... и радоваться',
                                    'responsibility': 'Возить ... с улыбкой. Давать мороженку постоянным клиентам.'}}]

    assert define_new_vac_list(test_list_0) == [{'name': 'Говновоз', 'url': 'https://kremlin.ru',
                                               'salary_from': 900000000, 'reqr': 'Уметь жить в ... и радоваться',
                                                'responsibility': 'Возить ... с улыбкой. Давать мороженку постоянным клиентам.'}]

    assert define_new_vac_list(test_list_1) == [{'name': 'Говновоз', 'url': 'https://kremlin.ru',
                                               'salary_from': 0, 'reqr': 'Уметь жить в ... и радоваться',
                                                'responsibility': 'Возить ... с улыбкой. Давать мороженку постоянным клиентам.'}]

    assert define_new_vac_list(test_list_2) == [{'name': 'Говновоз', 'url': 'https://kremlin.ru',
                                               'salary_from': 0, 'reqr': 'Уметь жить в ... и радоваться',
                                                'responsibility': 'Возить ... с улыбкой. Давать мороженку постоянным клиентам.'}]

    assert define_new_vac_list([]) == []

