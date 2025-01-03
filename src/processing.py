def filter_by_state(word_list: list, state: str = "EXECUTED") -> list:
    """
    Функция возвращает новый список словарей, содержащий
    только те словари, у которых ключ state соответствует указанному значению.
    Получает: [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, ит.д.]
    Возвращает: список словарей где 'state' равен 'EXECUTED'
    """
    return [word_list[word] for word in range(len(word_list)) if state == word_list[word]["state"]]


def sort_by_date(word_list: list, sorting: bool = True) -> list:
    """
    Функция сортировки данных по дате
    Получает: [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, ит.д.]
    Возвращает: отсортированный по дате список словарей
    """
    data_sort = sorted([word_list[item]["date"] for item in range(len(word_list))], reverse=sorting)
    sort_list = []
    for data in data_sort:
        for entry in word_list:
            if data in entry["date"]:
                sort_list.append(entry)
    return sort_list
