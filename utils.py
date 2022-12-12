import json


def load_candidates():
    """
    Загружает данные из файла
    :return: данные
    """
    with open("candidates.json", encoding="utf-8") as file:
        data = json.load(file)
    return data


def get_all():
    """

    :return: Всех кандидатов
    """
    return load_candidates()


def get_by_pk(pk):
    """
    Проверяет кандидата по "pk"
    :param pk: int
    :return: Кандидата по его "pk"
    """
    for candidate in get_all():
        if candidate['pk'] == pk:
            return candidate
    return "Такого кандидата нет"


def get_by_skill(skill_name):
    """
    Проверяет кандидата по его навыкам
    :param skill_name: Название навыка
    :return: Кандидата по его навыкам
    """
    candidates = []
    for candidate in get_all():
        if skill_name.lower() in candidate['skills'].lower().split(', '):
            candidates.append(candidate)
    return candidates



