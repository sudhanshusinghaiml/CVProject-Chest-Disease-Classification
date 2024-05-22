"""This module primarly covers the class and methods that will be used for data ingestion"""

import os
import zipfile
import gdown
from CNNClassifier import logger
from CNNClassifier.entity.config_entity import DataIngestionConfig


class DataIngestion:
    """
    This class encapsulates download data and extract_zip_file function for Data Ingestion Pipeline
    """

    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self):
        """
        Code feteches the data and downloads from google drive
        """
        try:
            dataset_url = self.config.source_url
            zipped_file = self.config.downloaded_data_file
            os.makedirs(self.config.root_directory, exist_ok=True)
            file_id = dataset_url.split("/")[-2]
            logger.info(
                "Started Downloading data from %s into %s", dataset_url, zipped_file
            )
            url = f"https://drive.google.com/uc?id={file_id}"
            gdown.download(url, zipped_file)
            logger.info(
                "Successfully downloaded data from %s into file %s",
                dataset_url,
                zipped_file,
            )
        except Exception as error:
            raise error

    def extract_zip_file(self):
        """
        Extracts the zip file into the data directory and returns None
        """
        try:
            unzip_file_path = self.config.unzip_directory
            os.makedirs(unzip_file_path, exist_ok=True)
            with zipfile.ZipFile(self.config.downloaded_data_file, "r") as zip_file:
                zip_file.extractall(unzip_file_path)
            logger.info(
                "Unzipped file from %s to file %s",
                self.config.downloaded_data_file,
                unzip_file_path,
            )
        except Exception as error:
            raise error
