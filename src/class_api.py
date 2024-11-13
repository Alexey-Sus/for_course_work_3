import re
from abc import ABC, abstractmethod
import requests

from src.functions import define_new_vac_list


class AbstractVacancyAPI(ABC):
    """Абстрактный класс для наследования другими классами"""

    @abstractmethod
    def get_vacancies(self, keyword):
        """Шаблон для метода получения вакансий - исп-ся в дочернем классе"""
        pass


class HHVacancyAPI(AbstractVacancyAPI):
    """Класс для получ. вак. по API hh.ru. Наслед. от AbstractVacancyAPI"""

    def get_vacancies(self) -> list:
        """Метод для получения raw-списка вакансий от hh.ru"""

        url = "https://api.hh.ru/vacancies?per_page=10"
        response = requests.get(url)
        if response.status_code == 200:
            vacancies = response.json()
            return vacancies.get("items", [])
        return []


# cоздаем экземпляр класса HHVacancyAPI
hh_api = HHVacancyAPI()

# Получаем список вакансий с помощью метода get_vacancies у экземпляра класса
vacancies = hh_api.get_vacancies()

test_vac_0 = define_new_vac_list(vacancies)[0]
test_vac_1 = define_new_vac_list(vacancies)[1]


class VacancyProcess:
    """Класс для вакансий. Маг. методы, а также методы сравнения вакансий,
    сортировки списка вакансий и вывода вакансий по ключевому слову"""

    def __init__(
        self,
        vac_name: str,
        vac_url: str,
        vac_salary: int | str,
        vac_reqr: str,
        vac_respons: str,
    ):

        if vac_salary:
            self.vac_salary = vac_salary
        else:
            self.vac_salary = "Зарплата не указана"

        self.vac_name = vac_name
        self.vac_url = vac_url
        self.vac_reqr = vac_reqr
        self.vac_respons = vac_respons

    def __str__(self):
        """Маг. метод str для представления экз-ов класса в соотв. виде"""
        return (
            f"{self.__class__.__name__}: {self.vac_name},"
            f"{self.vac_url}, {self.vac_salary}, {self.vac_reqr}, "
            f"{self.vac_respons}"
        )

    def sort_by_salary(self) -> list:
        """Этот метод выводит отсортированный по зарплате список вакансий"""

        sorted_list = sorted(
            define_new_vac_list(vacancies),
            key=lambda x: x["salary_from"], reverse=True)

        return sorted_list

    def vacancies_keyword(self) -> str:
        """Метод запрашивает у польз. keyword и выводит
        все вакансии с kw в назв-ии"""

        keyword = str(
            input("Введите ключевое слово для поиска в названиях вакансий: ")
        ).lower()
        new_list = []

        for elem in define_new_vac_list(vacancies):
            if re.search(keyword, elem["name"].lower()):
                new_list.append(elem)

        return (
            f"Вакансия, в назв. кот. есть слово" f'"{keyword}":\n{new_list}'
        )

    def compare_vac_by_salary(self, other):
        """Метод для сравнения двух вакансий"""

        if not isinstance(self.vac_salary, int) or not isinstance(
            other.vac_salary, int
        ):

            print(
                f"Сравнение вакансий по зарплате:\n"
                f"Невозможно сравнить вакансии {self.vac_name} и"
                f"{other.vac_name}, поскольку как минимум"
                f"у одной из них ЗП не указана."
            )

        else:

            if self.vac_salary > other.vac_salary:
                print(f"Вакансия с макс. ЗП из двух - это {self.vac_name}")

            elif self.vac_salary < other.vac_salary:
                print(f"Вакансия с макс. ЗП из двух - это {other.vac_name}")

            else:
                print("Эти вакансии по зарплате равны")

    def find_max_salary(self) -> str:
        """Метод  для поиска вакансии с макс. зарплатой"""

        max_salary_job: dict = max(
            define_new_vac_list(vacancies), key=lambda x: x["salary_from"]
        )["name"]

        return (
            f'Вакансия с макс. ЗП - это "{max_salary_job}", зарплата равна '
            f"{max(define_new_vac_list(vacancies),
                   key=lambda x: x['salary_from'])['salary_from']} руб."
        )


if __name__ == "__main__":

    print(f"Просто первая вакансия из списка после функции: {test_vac_0}")

    vac_test = VacancyProcess(
        test_vac_0["name"],
        test_vac_0["url"],
        test_vac_0["salary_from"],
        test_vac_0["reqr"],
        test_vac_0["responsibility"],
    )

    vac_test_1 = VacancyProcess(
        test_vac_1["name"],
        test_vac_1["url"],
        test_vac_1["salary_from"],
        test_vac_1["reqr"],
        test_vac_1["responsibility"],
    )

    # выводится на печать список вакансий, отсортированный по ЗП.
    # Выводится список в одну строчку

    print(VacancyProcess.sort_by_salary(self=""))
    print(vac_test.sort_by_salary())
    print()

    # тут выводятся на печать вакансии, полученные в ф-ии define_new_vac_list,
    # каждая - на своей (новой) строчке
    for i in define_new_vac_list(vacancies):
        print(i)
    print()

    # тут выводится, на печать выводится список вакансий, в которых
    # есть в названии ключевое слово, которое введет пользователь
    print(vac_test.vacancies_keyword())
    print()

    # здесь вызывается метод compare_vac_by_salary. В нем уже есть print,
    # так что он тут принтует вакансию с максимальной ЗП из данных
    # двух, которые поданы ему (этому методу) на вход
    VacancyProcess.compare_vac_by_salary(vac_test, vac_test_1)
    print()

    # а здесь выводится на печать вакансия с макс. ЗП из всего списка
    print(vac_test.find_max_salary())
