"""
This module contains class and methods that triggers the PrepareModel pipeline
and sets up the model architecture using pre-trained models
"""

from src.cnn_classifier.config.configuration import ConfigurationManager
from src.cnn_classifier.components.prepare_model import PrepareModelArchitecture
from src.cnn_classifier.logger import logging


STAGE_NAME = "Prepare model architecture"


class PrepareModelArchitecturePipeline:
    """This class and its methods triggers the PrepareModel pipeline to setup model"""

    def __init__(self):
        pass

    def main(self):
        """
        This method triggers all the functions from PrepareModel class
        """
        logging.info(
            "Inside src.cnn_classifier.components.pipeline.PrepareModelArchitecturePipeline"
        )
        config = ConfigurationManager()
        prepare_model_config = config.get_model_config()
        logging.info(
            "Completed execution get_model_config method of \
                src.cnn_classifier.config.configuration.ConfigurationManager "
        )
        logging.info(
            "Started execution of \
            src.cnn_classifier.components.prepare_model.PrepareModelArchitecture "
        )
        prepare_model = PrepareModelArchitecture(config=prepare_model_config)
        prepare_model.get_base_model()
        logging.info(
            "Completed execution get_base_model method of \
                src.cnn_classifier.components.prepare_model.PrepareModelArchitecture"
        )
        prepare_model.update_model()
        logging.info(
            "Saving the model - completed execution update_model method of \
                src.cnn_classifier.components.prepare_model.PrepareModelArchitecture"
        )
        logging.info(
            "Completed execution of \
                src.cnn_classifier.components.prepare_model.PrepareModelArchitecture"
        )


if __name__ == "__main__":
    try:
        logging.info("*******************")
        logging.info(">>>>>> Started %s <<<<<<", STAGE_NAME)
        obj = PrepareModelArchitecturePipeline()
        obj.main()
        logging.info(">>>>>> %s completed <<<<<<\n\n", STAGE_NAME)
    except Exception as error:
        logging.exception(error)
        raise error
