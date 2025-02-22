"""
This module contains the code for executing all the pipelines for the project
"""

from src.cnn_classifier.logger import logging
from src.cnn_classifier.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.cnn_classifier.pipeline.prepare_model_pipeline import (
    PrepareModelArchitecturePipeline,
)
from src.cnn_classifier.pipeline.model_training_pipeline import ModelTrainingPipeline

from src.cnn_classifier.pipeline.model_evaluation_pipeline import (
    ModelEvaluationPipeline,
)


STAGE_NAME = "Data Ingestion Pipeline"

try:
    logging.info(">>>>>> %s started <<<<<<", STAGE_NAME)
    data_ingestion_object = DataIngestionPipeline()
    data_ingestion_object.main()
    logging.info(">>>>>> %s completed <<<<<<\n\nx==========x", STAGE_NAME)
except Exception as error:
    logging.exception(error)
    raise error


STAGE_NAME = "Prepare model architecture"

try:
    logging.info(">>>>>> Started %s <<<<<<", STAGE_NAME)
    model_architecture_obj = PrepareModelArchitecturePipeline()
    model_architecture_obj.main()
    logging.info(">>>>>> %s completed <<<<<<\n\nx==========x", STAGE_NAME)
except Exception as error:
    logging.exception(error)
    raise error


STAGE_NAME = "Model Training Pipeline"

try:
    logging.info(">>>>>> Started %s <<<<<<", STAGE_NAME)
    model_trainer_object = ModelTrainingPipeline()
    model_trainer_object.main()
    logging.info(">>>>>> stage %s completed <<<<<<\n\n", STAGE_NAME)
except Exception as error:
    logging.exception(error)
    raise error


STAGE_NAME = "Model Evaluation Pipeline"

try:
    logging.info(">>>>>> Started %s <<<<<<", STAGE_NAME)
    model_evaluation_object = ModelEvaluationPipeline()
    model_evaluation_object.main()
    logging.info(">>>>>> stage %s completed <<<<<<\n\n", STAGE_NAME)
except Exception as error:
    logging.exception(error)
    raise error
