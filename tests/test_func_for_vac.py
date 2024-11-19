from src.func_for_vac import func_for_vac

def test_func_for_vac():
    test_list_0: list = [{'name': 'Оператор call-центра', 'url': 'some_url_0.ru', 'salary_from': 105000,
                        'reqr': 'Знание русского языка и компьютера. Умение общаться с людьми.',
                        'responsibility': 'Отвечать на входящие звонки от клиентов.'},

                       {'name': 'Оператор call-центра', 'url': 'some_url_1.ru', 'salary_from': 95000,
                        'reqr': 'Знание Узбекского и Русского языков',
                        'responsibility': 'Консультирование клиентов.'},

                       {'name': 'Менеджер', 'url': 'some_url_2.ru', 'salary_from': 80000,
                        'reqr': 'Опыт работы менеджером по продажам. ',
                        'responsibility': 'Ведение действующей клиентской базы.'}]

    # список из названий вакасий (первый список в кортеже результатов функции):
    test_list_1: list = ['Оператор call-центра', 'Оператор call-центра']

    # отсортированный по зарплате список для N=2:

    test_list_2: list = [{'name': 'Оператор call-центра', 'url': 'some_url_0.ru', 'salary_from': 105000,
                        'reqr': 'Знание русского языка и компьютера. Умение общаться с людьми.',
                        'responsibility': 'Отвечать на входящие звонки от клиентов.'},

                       {'name': 'Оператор call-центра', 'url': 'some_url_1.ru', 'salary_from': 95000,
                        'reqr': 'Знание Узбекского и Русского языков',
                        'responsibility': 'Консультирование клиентов.'}]

    n: int = 2
    kw: str = 'оператор'

    assert func_for_vac(test_list_0, n, kw) == (test_list_1, test_list_2, n)
    assert func_for_vac(test_list_0, None, kw) == (test_list_1, [], None)
    assert func_for_vac(test_list_0, n, None) == (test_list_0, test_list_2, n)
    assert func_for_vac(test_list_0, None, None) == (test_list_0, [], None)
    assert func_for_vac(None, n, kw) == ('Отсутствуют исходные данные.')
    assert func_for_vac(None, None, kw) == ('Отсутствуют исходные данные.')
    assert func_for_vac(None, 2, None) == ('Отсутствуют исходные данные.')
    assert func_for_vac(None, None, None) == ('Отсутствуют исходные данные.')
