"""
This module contains class and methods that are
responsible for data preprocessing and model training
"""

from pathlib import Path
import tensorflow as tf
from src.cnn_classifier.entity.config_entity import ModelTrainingConfig


class ModelTraining:
    """
    This class encapsulates methods that are used for
    data preprocessing, train test split and model training
    """

    def __init__(self, config: ModelTrainingConfig):
        self.config = config
        self.model: tf.keras.models = None
        self.validation_data_generator: tf.data.Dataset = None
        self.training_data_generator: tf.data.Dataset = None
        self.steps_per_epoch: int = 0
        self.validation_steps: int = 0

    def get_pretrained_model(self):
        """
        Loads pretrained model from artifacts
        """
        self.model = tf.keras.models.load_model(self.config.updated_model_path)

    def image_preprocessing(self):
        """
        Performs Data Augmentation and Preprocess the image data using ImageDataGenerator
        """
        data_generator_kwargs = dict(
            rescale=1.0 / 255, validation_split=self.config.params_validation_split
        )

        data_flow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation=self.config.params_interpolation,
        )

        validation_image_datagenerator = (
            tf.keras.preprocessing.image.ImageDataGenerator(**data_generator_kwargs)
        )

        self.validation_data_generator = (
            validation_image_datagenerator.flow_from_directory(
                directory=self.config.training_data,
                subset=self.config.params_validation_subset,
                shuffle=self.config.params_shuffle,
                **data_flow_kwargs,
            )
        )

        if self.config.params_augmentation_required:
            training_image_datagenerator = (
                tf.keras.preprocessing.image.ImageDataGenerator(
                    rotation_range=self.config.params_rotation_range,
                    horizontal_flip=self.config.params_horizontal_flip,
                    width_shift_range=self.config.params_width_shift_range,
                    height_shift_range=self.config.params_height_shift_range,
                    shear_range=self.config.params_shear_range,
                    zoom_range=self.config.params_zoom_range,
                    **data_generator_kwargs,
                )
            )
        else:
            training_image_datagenerator = validation_image_datagenerator

        self.training_data_generator = training_image_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset=self.config.params_training_subset,
            shuffle=self.config.params_shuffle,
            **data_flow_kwargs,
        )

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        """Method to save the model definition"""
        model.save(path)

    def train(self):
        """Training the prepared model"""
        self.steps_per_epoch = (
            self.training_data_generator.samples
            // self.training_data_generator.batch_size
        )
        self.validation_steps = (
            self.validation_data_generator.samples
            // self.validation_data_generator.batch_size
        )

        self.model.fit(
            self.training_data_generator,
            epochs=self.config.params_epochs,
            steps_per_epoch=self.steps_per_epoch,
            validation_steps=self.validation_steps,
            validation_data=self.validation_data_generator,
        )

        self.save_model(path=self.config.trained_model_path, model=self.model)
