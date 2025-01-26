import logging
import os
from src.swapi_data_manager import SWAPIDataManager
from src.swapi_client import SWAPIClient

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    client = SWAPIClient()
    manager = SWAPIDataManager(client)

    endpoints = ['people', 'planets', 'films']

    for endpoint in endpoints:
        manager.fetch_entity(endpoint)


    manager.apply_filter('people', ['height', 'mass'])


    directory = 'data'
    if not os.path.exists(directory):
        os.makedirs(directory)


    manager.save_to_excel('data/swapi_data.xlsx')
1