from textsummarizer.pipeline.stage_01_data_ingention import DataIngestionTrainingPipeline
from textsummarizer.logging import logger

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    data_ingenstion = DataIngestionTrainingPipeline()
    data_ingenstion.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<< \n\nx ====================x")
except Exception as e:
    raise e