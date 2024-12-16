from typing import Union
def filter_by_state(word_list: Union[list], state='EXECUTED') -> Union[list]:
    """
    Функция
    """
    return [word_list[word] for word in range(len(word_list)) if state == word_list[word]["state"]]

