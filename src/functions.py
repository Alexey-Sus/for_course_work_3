def define_new_vac_list(vac_list: list) -> list:
    """Ф-ия возвращает новый список вак-ий, каждая из кот. представлена
    только 5-ю параметрами: название, url, ЗП, треб-ия и обязанности. На вход
    подается спис. вак., полученных по API"""
    vac_new: dict = {}
    new_list: list = []

    if not vac_list:
        return []

    else:

        for vacancy in vac_list:
            vac_new["name"] = vacancy["name"]
            vac_new["url"] = vacancy["alternate_url"]

            if vacancy["salary"] is not None:
                if vacancy["salary"]["from"] is not None:

                    vac_new["salary_from"] = vacancy["salary"]["from"]
                else:
                    vac_new["salary_from"] = 0
            else:
                vac_new["salary_from"] = 0

            vac_new["reqr"] = vacancy.get("snippet", {}).get("requirement")
            vac_new["responsibility"] = (
                vacancy.get("snippet", {}).get("responsibility"))

            new_list.append(vac_new)
            vac_new = {}

        return new_list
