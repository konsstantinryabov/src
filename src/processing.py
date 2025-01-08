def filter_by_state(word_list: list, state: str = "EXECUTED") -> list | str:
    """
    Функция возвращает новый список словарей, содержащий
    только те словари, у которых ключ state соответствует указанному значению.
    Получает: [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, ит.д.]
    Возвращает: список словарей где 'state' равен 'EXECUTED'
    """

    if word_list is None or not word_list:
        return "Словарь с данными отсутствует"

    else:
        filtered_word_list = []
        if not state or state is None:
            state = "EXECUTED"
            for dict_key in word_list:
                if dict_key["state"] == state:
                    filtered_word_list.append(dict_key)
        else:
            for dict_key in word_list:
                if dict_key["state"] == state:
                    filtered_word_list.append(dict_key)

    return filtered_word_list


def sort_by_date(word_list: list, sorting: bool = True) -> str | list:
    """
    Функция сортировки данных по дате
    Получает: [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, ит.д.]
    Возвращает: отсортированный по дате список словарей
    """

    if not word_list or word_list is None:
        return "Словарь с данными отсутствует"

    else:
        if not sorting:
            var_reverse_date = sorting is True
            sorted_data = sorted(
                word_list, key=lambda dictionary_key: dictionary_key["date"], reverse=var_reverse_date
            )

        else:
            sorted_data = sorted(word_list, key=lambda dictionary_key: dictionary_key["date"], reverse=sorting)

        return sorted_data
