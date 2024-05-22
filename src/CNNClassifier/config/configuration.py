"""
This is the configuration manager for all the stages of pipelines for this Projects.
It will have all the configuration methods encapsulated in a class
"""

from CNNClassifier.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from CNNClassifier.utils.common import read_yaml, create_directories
from CNNClassifier.entity.config_entity import DataIngestionConfig


class ConfigurationManager:
    """
    This is the configuration manager for all the stages of pipelines for this Projects
    """

    def __init__(self, config_path=CONFIG_FILE_PATH, params_path=PARAMS_FILE_PATH):
        self.config = read_yaml(config_path)
        self.params = read_yaml(params_path)
        create_directories(directory_list=[self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
        This is to assign the config values for data_ingestion pipeline
        """
        config = self.config.data_ingestion
        create_directories(directory_list=[config.root_directory])

        data_ingestion_config = DataIngestionConfig(
            root_directory=config.root_directory,
            source_url=config.source_url,
            downloaded_data_file=config.downloaded_data_file,
            unzip_directory=config.unzip_directory,
        )

        return data_ingestion_config
