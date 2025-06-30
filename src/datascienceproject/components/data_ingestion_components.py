import os
import urllib.request as request
from src.datascienceproject import logger
import zipfile

from src.datascienceproject.entity.config_entity import (DataIngestconfig)
class DataIngestion:
    def __init__(self, config:DataIngestconfig):
        self.config = config

    def download_file(self):
        url = str(self.config.source_URL).replace("\\", "/").replace("https:/", "https://")
        local_file = str(self.config.local_data_file).replace("\\", "/")

        logger.info(f"About to download from URL: '{url}'")
        print("URL before download:", url)
        print("Local file path:", local_file)

        if not os.path.exists(local_file):
            filename, headers = request.urlretrieve(
                url=url,
                filename=local_file
            )
            logger.info(f"{filename} downloaded with info: \n{headers}")
        else:
            logger.info(f"File already exists: {local_file}")



    def extract_zip(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)

