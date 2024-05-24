"""This module includes class and methods that executed the Model Training Pipeline"""

from src.cnn_classifier.components.model_trainer import ModelTraining
from src.cnn_classifier.config.configuration import ConfigurationManager
from src.cnn_classifier.logger import logging

STAGE_NAME = "Model Training Pipeline"


class ModelTrainingPipeline:
    """This class enapsulates the methods to trigger the Model Training Pipeline"""

    def __init__(self):
        pass

    def main(self):
        """Main method to call methods for model training"""
        logging.info(
            "Inside src.cnn_classifier.components.pipeline.ModelTrainingPipeline"
        )
        config = ConfigurationManager()
        model_training_config = config.get_model_training_config()
        logging.info(
            "Completed execution get_model_training_config method of \
                src.cnn_classifier.config.configuration.ConfigurationManager"
        )
        model_training = ModelTraining(config=model_training_config)

        model_training.get_pretrained_model()
        logging.info(
            "Completed execution get_pretrained_model method of \
                src.cnn_classifier.components.model_trainer.ModelTraining"
        )
        model_training.image_preprocessing()
        logging.info(
            "Completed execution image_preprocessing method of \
                src.cnn_classifier.components.model_trainer.ModelTraining"
        )
        model_training.train()
        logging.info(
            "Completed Model Training using train method of \
                src.cnn_classifier.components.model_trainer.ModelTraining"
        )
        logging.info(
            "Completed execution of \
                src.cnn_classifier.components.model_trainer.ModelTraining"
        )


if __name__ == "__main__":
    try:
        logging.info(">>>>>> Started %s <<<<<<", STAGE_NAME)
        obj = ModelTrainingPipeline()
        obj.main()
        logging.info(">>>>>> %s completed <<<<<<\n\n", STAGE_NAME)
    except Exception as error:
        logging.exception(error)
        raise error
