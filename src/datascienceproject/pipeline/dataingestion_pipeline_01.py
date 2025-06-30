from src.datascienceproject.config.configuration import ConfigurationManager
from src.datascienceproject.components.data_ingestion_components import DataIngestion
from src.datascienceproject import logger

STAGE_NAME = " data ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    def initiate_data_ingestion(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config = data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip()

if __name__ == 'main':
    try:
        logger.info(f">>>> stage {STAGE_NAME} started <<<<")
        obj = DataIngestionTrainingPipeline()
        obj.initiate_data_ingestion()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<<")

    except Exception as e:
        logger.exception(e)
        raise e