from text_summariser.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from text_summariser.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from text_summariser.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from text_summariser.logging import logger


STAGE_NAME = "STAGE 01: DATA INGESTION"
try:
    logger.info(f"{STAGE_NAME} started")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"{STAGE_NAME} completed")

except Exception as e:
    logger.error(f"{STAGE_NAME} failed with error: {str(e)}")
    raise e



STAGE_NAME = "STAGE 02: DATA VALIDATION"
try:
    logger.info(f"{STAGE_NAME} started")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f"{STAGE_NAME} completed")
except Exception as e:
    raise e


STAGE_NAME = "STAGE 03: DATA TRANSFORMATION"
try:
    logger.info(f"{STAGE_NAME} started")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f"{STAGE_NAME} completed")
except Exception as e:
    raise e