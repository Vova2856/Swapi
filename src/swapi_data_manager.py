import pandas as pd
import logging

logger = logging.getLogger(__name__)

class SWAPIDataManager:
    def __init__(self, client):
        self.client = client
        self.df_list = {}

    def fetch_entity(self, endpoint: str):
        try:
            raw_data = self.client.fetch_json(endpoint)
            self.df_list[endpoint] = pd.DataFrame(raw_data)
            logger.info(f"Отримано {len(raw_data)} записів для {endpoint}. Колонки: {self.df_list[endpoint].columns.tolist()}")
        except Exception as e:
            logger.error(f"Не вдалося отримати дані для {endpoint}: {e}")

    def apply_filter(self, endpoint: str, columns_to_remove: list):
        if endpoint in self.df_list:
            self.df_list[endpoint].drop(columns=columns_to_remove, inplace=True, errors='ignore')
            logger.info(f"Видалено колонки {columns_to_remove} з {endpoint}.")
        else:
            logger.warning(f"Дані для {endpoint} не завантажені.")

    def save_to_excel(self, file_name: str):
        with pd.ExcelWriter(file_name) as writer:
            for endpoint, df in self.df_list.items():
                df.to_excel(writer, sheet_name=endpoint, index=False)
                logger.info(f"Дані з {endpoint} збережено в Excel.")

2