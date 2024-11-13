import json
from abc import ABC, abstractmethod

from src.class_api import HHVacancyAPI

# Определить абстрактный класс, кот. обяз. реализовать методы для 1 - доб.
# вакансий в файл, 2 - получ. данных из ф-ла по указ. критериям и 3 - удаления
# информации о вакансиях. Создать класс для сохр. инф-ии о вак. в JSON-файл.


class AbstractJobManager(ABC):
    """Абстр. класс для шаблонизации методов и наследования их друг. кл."""

    @abstractmethod
    def add_job(self, job_details, file_name):
        pass

    @abstractmethod
    def get_jobs(self):
        pass

    @abstractmethod
    def remove_jobs(self):
        pass


class JobManager(AbstractJobManager):
    """Наследуем этот класс от абстрактного класса выше"""

    def add_job(self, vac_list, file_name):
        """Метод для добавления вакансий в файл в виде JSON-строки"""
        try:
            with open(file_name, "w", encoding="utf-32") as file:
                json.dump(vac_list, file, ensure_ascii=False, indent=4)
            print(f"Список вакансий добавлен в файл {file_name}")

        except Exception as e:
            print("Вакансии в файл не добавлены. Произошла ошибка", e)

    def get_jobs(self, file_name):
        """Метод для чтения данных по вакансиям из файла"""
        try:
            keyword = input("Введите ключевое слово для поиска вакансий: ")

            with open(file_name, "r", encoding="utf-32") as file:

                job_list = json.load(file)
                filtered_jobs = [
                    j for j in job_list if keyword.lower() in j["name"].lower()
                ]

                if filtered_jobs:
                    print(f"Найдено вакансий: {len(filtered_jobs)}")

                    for job in filtered_jobs:
                        print(job["name"])
                else:
                    print("Вакансии с введенным ключевым словом не найдены.")

        except Exception as e:
            print("Ошибка при получении вакансий из файла:", e)

    def remove_jobs(self, file_name):
        """Метод для удаления вакансий из файла. Просто очищает весь файл."""
        decs: str = input(
            'Удалить файл с вакансиями? ("Да" - введите yes,\n'
            '"Нет" - любой символ или Enter): '
        ).lower()

        if decs == "yes":
            with open(file_name, "w", encoding="utf-32") as file:
                try:
                    file.truncate(0)
                    print("Вакансии из файла удалены.")

                except Exception as e:
                    print(f"Не удалось удалить содержимое файла: ошибка {e}")
        else:
            print("Вакансии из файла не удалены.")
            pass


job_list: list = HHVacancyAPI.get_vacancies(self="")

file_name = "../data/my_json.json"
job_manager = JobManager()

job_manager.add_job(job_list, file_name)
print()

job_manager.get_jobs(file_name)
print()

job_manager.remove_jobs(file_name)
