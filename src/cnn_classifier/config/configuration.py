"""
This is the configuration manager for all the stages of pipelines for this Projects.
It will have all the configuration methods encapsulated in a class
"""

import os
from pathlib import Path
from src.cnn_classifier.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from src.cnn_classifier.utils.common import read_yaml, create_directories
from src.cnn_classifier.entity.config_entity import (
    DataIngestionConfig,
    PrepareModelArchitectureConfig,
    ModelTrainingConfig,
    ModelEvaluationConfig,
)


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

    def get_model_config(self) -> PrepareModelArchitectureConfig:
        """
        This method is to fetch the config details for Pretrained Models
        """
        config = self.config.prepare_model
        create_directories([config.root_directory])

        prepare_model_config = PrepareModelArchitectureConfig(
            root_directory=Path(config.root_directory),
            model_path=Path(config.model_path),
            updated_model_path=Path(config.updated_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES,
        )

        return prepare_model_config

    def get_model_training_config(self) -> ModelTrainingConfig:
        """
        This method is to fetch the config details for Model Training
        """
        config = self.config.model_training
        prepare_model_config = self.config.prepare_model
        training_data = os.path.join(
            self.config.data_ingestion.unzip_dir, "training_data"
        )

        create_directories([Path(config.root_directory)])

        model_training_config = ModelTrainingConfig(
            root_directory=Path(config.root_directory),
            trained_model_path=Path(config.trained_model_path),
            updated_model_path=Path(prepare_model_config.updated_model_path),
            training_data=Path(training_data),
            params_epochs=self.params.EPOCHS,
            params_batch_size=self.params.BATCH_SIZE,
            params_augmentation_required=self.params.AUGMENTATION,
            params_image_size=self.params.IMAGE_SIZE,
            params_validation_split=self.params.VALIDATION_SPLIT,
            params_interpolation=self.params.INTERPOLATION,
            params_rotation_range=self.params.ROTATION_RANGE,
            params_horizontal_flip=self.params.HORIZONTAL_FLIP,
            params_width_shift_range=self.params.WIDTH_SHIFT_RANGE,
            params_height_shift_range=self.params.HEIGHT_SHIFT_RANGE,
            params_shear_range=self.params.SHEAR_RANGE,
            params_zoom_range=self.params.ZOOM_RANGE,
            params_shuffle=self.params.SHUFFLE,
            params_validation_subset=self.params.VALIDATION_SUBSET,
            params_training_subset=self.params.TRAINING_SUBSET,
        )

        return model_training_config

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        """This method is to fetch the config details for Model Evaluation"""

        model_evaluation_config = ModelEvaluationConfig(
            path_of_model=self.config.model_training.trained_model_path,
            training_data=self.config.data_ingestion.downloaded_data_file,
            all_params=self.params,
            mlflow_uri=self.config.model_training.mlflow_uri,
            params_image_size=self.params.IMAGE_SIZE,
            params_batch_size=self.params.BATCH_SIZE,
        )

        return model_evaluation_config
