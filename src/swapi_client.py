import requests
import logging

logger = logging.getLogger(__name__)


class SWAPIClient:
    BASE_URL = "https://swapi.dev/api/"

    def __init__(self, base_url: str = BASE_URL):
        self.base_url = base_url

    def fetch_json(self, endpoint: str) -> list:
        results = []
        url = f"{self.base_url}{endpoint}/"

        while url:
            logger.info(f"Запит до: {url}")
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            results.extend(data['results'])
            url = data.get('next')  # Оновлюємо URL для наступної сторінки

        return results

2