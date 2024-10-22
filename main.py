from src.textsummarizer.logging import logger
from src.textsummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.textsummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.textsummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.textsummarizer.pipeline.stage_04_model_trainer import ModelTrainingPipeline
from src.textsummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline 


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

STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>>{STAGE_NAME} started<<<<<")
    data_transformation= DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>{STAGE_NAME} completed<<<<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model training Stage"
try:
    logger.info(f">>>>>{STAGE_NAME} started<<<<<")
    model_training = ModelTrainingPipeline()
    model_training.main()
    logger.info(f">>>>>{STAGE_NAME} completed<<<<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f">>>>>{STAGE_NAME} started<<<<<")
    model_evaluation = ModelEvaluationPipeline()
    model_evaluation.main()
    logger.info(f">>>>>{STAGE_NAME} completed<<<<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e