import os

from seeds.schema.result import SeedsResult


def save_seeds_result(result: SeedsResult, scenario: str):
    """
    Сохраняет результат сидинга в json файл

    :param result: Результат сидинга созданный билдером
    :param scenario: Название сценария нагрузки, для которого создаются данные.
                    Используется для генерации имени файла
    """
    if not os.path.exists("dumps"):
        os.mkdir("dumps")

    with open(f"./dumps/{scenario}_seeds.json", "w+", encoding="utf-8") as file:
        file.write(result.model_dump_json())


def load_seeds_result(scenario: str) -> SeedsResult:
    """
    Загружает результат сидинга из json файла

    :param scenario: Название сценария нагрузки
    :return: Объект SeedsResult восстановленный из json файла
    """
    with open(f"./dumps/{scenario}_seeds.json", "r", encoding="utf-8") as file:
        return SeedsResult.model_validate_json(file.read())
