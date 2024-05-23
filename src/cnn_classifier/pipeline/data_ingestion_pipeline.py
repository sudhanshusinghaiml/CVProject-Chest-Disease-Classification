"""
This module contains classes and methods that starts the data ingestion pipeline
"""

from src.cnn_classifier.config.configuration import ConfigurationManager
from src.cnn_classifier.components.data_ingestion import DataIngestion
from src.cnn_classifier.logger import logging

STAGE_NAME = "Data Ingestion stage"


class DataIngestionPipeline:
    """
    This class encapsulates all the methods that is needed to trigger data ingestion pipeline
    """

    def __init__(self):
        pass

    def main(self):
        """
        This method calles the methods to donload and extract all the files
        in the Data Ingestion Pipeline
        """
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_data()
        data_ingestion.extract_zip_file()


if __name__ == "__main__":
    try:
        logging.info(">>>>>> %s started <<<<<<", STAGE_NAME)
        obj = DataIngestionPipeline()
        obj.main()
        logging.info(">>>>>> %s completed <<<<<<\n\nx==========x", STAGE_NAME)
    except Exception as e:
        logging.exception(e)
        raise e
