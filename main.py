import logging
import os
from src.swapi_data_manager import SWAPIDataManager
from src.swapi_client import SWAPIClient

if __name__ == "__main__":  # Виправлено на '__name__' і '__main__'
    logging.basicConfig(level=logging.INFO)

    client = SWAPIClient()
    manager = SWAPIDataManager(client)

    endpoints = ['people', 'planets', 'films']  # Вкажіть ендпоінти, які хочете завантажити

    for endpoint in endpoints:
        manager.fetch_entity(endpoint)

    # Приклад фільтрації колонок
    manager.apply_filter('people', ['height', 'mass'])

    # Перевірка наявності директорії перед збереженням
    directory = 'data'
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Збереження в Excel
    manager.save_to_excel('data/swapi_data.xlsx')
