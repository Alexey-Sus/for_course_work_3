from unittest.mock import patch
from src.class_api import VacancyProcess, HHVacancyAPI
import pytest

@pytest.fixture()
def vacancy_test():
    return VacancyProcess('Тестировщик', 'https://hh.ru/tester', 50000,
                          'Быть хорошим человеком', 'Работать хорошо')

def test_init(vacancy_test):
    assert vacancy_test.vac_name == 'Тестировщик'
    assert vacancy_test.vac_url == 'https://hh.ru/tester'
    assert vacancy_test.vac_salary == 50000
    assert vacancy_test.vac_reqr == 'Быть хорошим человеком'
    assert vacancy_test.vac_respons == 'Работать хорошо'

def test_str(vacancy_test):
    assert str(vacancy_test) == ('VacancyProcess: Тестировщик, https://hh.ru/tester, 50000, Быть хорошим человеком, '
                            'Работать хорошо')

def test_get_vacancies():
    with patch('src.class_api.requests.get') as mock_get:
        #прописываем мок ответа
        mock_response = {'items': [{'id': '1', 'name': 'Вакансия 1'},
                {'id': '2', 'name': 'Вакансия 2'}]}

        #устанавливаем статус-код и JSON-ответ для мока
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        #создаем экземпляр класса HHVacancyAPI
        api_test = HHVacancyAPI()

        assert api_test.get_vacancies() == mock_response['items']









