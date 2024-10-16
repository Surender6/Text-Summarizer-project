from src.textsummarizer.logging import logger
from src.textsummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.textsummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>{STAGE_NAME} started<<<<<")
    data_ingestion= DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>{STAGE_NAME} completed<<<<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data validation Stage"
try:
    logger.info(f">>>>>{STAGE_NAME} started<<<<<")
    data_validation= DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>{STAGE_NAME} completed<<<<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e