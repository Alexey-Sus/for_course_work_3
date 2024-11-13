import re

from src.class_api import HHVacancyAPI
from src.functions import define_new_vac_list

vac_global: list = define_new_vac_list(HHVacancyAPI.get_vacancies(self=""))


def func_for_vac(vacancies: list, vac_n: int, kw: str) -> tuple:
    """Ф-ия принимает на вход от пользователя keyword для его поиска в названии
    вакансий, принимает N, выводит топ-N вакансий по зарплате и список вак-ий,
    содержащих в названии keyword"""

    if not vacancies:
        return "Отсутствуют", "исходные данные."

    else:
        vac_list: list = []

        # проверяем, подали ли на вход keyword. Если нет, выводим весь спс. вак.
        if kw:

            for i in vacancies:
                if re.search(kw, i["name"].lower()):
                    vac_list.append(i["name"])
        else:
            vac_list = vacancies

        if vac_n:
            sorted_vac: list = sorted(
                vacancies, key=lambda x: x["salary_from"], reverse=True
            )[0:vac_n]
        else:
            sorted_vac = []

        return vac_list, sorted_vac, vac_n


if __name__ == "__main__":

    for vac in vac_global:
        print(vac)
    print()

    try:
        number_vac = int(
            input(
                f"Введите кол-во вак-ий N для вывода топ-N вак-ий по ЗП.\n"
                f"N должно быть не более {len(vac_global)}: "
            )
        )

        while number_vac > len(vac_global):
            try:
                number_vac = int(
                    input(
                        f"Снова введите N для вывода топ-N вак-ий. N д.б. не больше "
                        f"{len(vac_global)}: "
                    )
                )
            except ValueError:
                number_vac = 0
                print(
                    "Вы ввели нечисловое значение. Список топ-N вакансий составлен не будет."
                )

    except ValueError:
        number_vac = 0
        print("Вы ввели нечисловое значение. Список топ-N вакансий составлен не будет.")

    keyword: str = input(
        "Введите ключевое слово для поиска в названии вакансии: "
    ).lower()

    print()
    list_kw, vac_sorted, _ = func_for_vac(vac_global, number_vac, keyword)

    print(
        f"Список топ-{func_for_vac(vac_global, number_vac, keyword)[2]} вакансий по зарплате:"
    )
    print(func_for_vac(vac_global, number_vac, keyword)[1])

    print()
    for vac in vac_sorted:
        print(f"{vac['name']}, зарплата {vac['salary_from']} руб.")
    print()

    print("Вакансии с ключевым словом в названии:")
    for vac in list_kw:
        print(vac)
