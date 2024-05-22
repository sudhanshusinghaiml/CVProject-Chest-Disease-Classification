"""
This module contains the code for executing all the pipelines for the project
"""

from CNNClassifier import logger
from CNNClassifier.pipeline.data_ingestion_pipeline import DataIngestionPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(">>>>>> %s started <<<<<<", STAGE_NAME)
    data_ingestion_object = DataIngestionPipeline()
    data_ingestion_object.main()
    logger.info(">>>>>> %s completed <<<<<<\n\nx==========x", STAGE_NAME)
except Exception as e:
    logger.exception(e)
    raise e
