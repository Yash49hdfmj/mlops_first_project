from src.datascienceproject import logger
# logger.info("welcome to custom logging datascience")
from src.datascienceproject.entity.config_entity import DataIngestconfig
from src.datascienceproject.pipeline.dataingestion_pipeline_01 import DataIngestionTrainingPipeline
from src.datascienceproject.pipeline.datavalidation_pipeline_01 import DataValidationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
        logger.info(f">>>> stage {STAGE_NAME} started <<<<")
        obj = DataIngestionTrainingPipeline()
        obj.initiate_data_ingestion()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<<")

except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = " data validation stage"
try:
        logger.info(f">>>> stage {STAGE_NAME} started <<<<")
        obj = DataValidationTrainingPipeline()
        obj.initiate_data_validation()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<<")

except Exception as e:
        logger.exception(e)
        raise e