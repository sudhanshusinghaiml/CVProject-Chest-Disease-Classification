"""
This module contains class and methods for model evaluation
these methods are triggerd in model evaluation pipeline
"""

from urllib.parse import urlparse
from pathlib import Path
import mlflow
import mlflow.keras
import tensorflow as tf
from src.cnn_classifier.entity.config_entity import ModelEvaluationConfig
from src.cnn_classifier.utils.common import save_json


class ModelEvaluation:
    """This class encapsulates all the methods for model evaluation"""

    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
        self.validation_data_generator = None
        self.score = None
        self.model = None

    def _valid_generator(self):
        """This method is to process images before model evaluation"""

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

    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        """Loading the saved model from directory"""
        return tf.keras.models.load_model(path)

    def evaluation(self):
        """Loads model and generates loss and accuracy score"""
        self.model = self.load_model(self.config.path_of_model)
        self._valid_generator()
        self.score = self.model.evaluate(self.validation_data_generator)
        self.save_score()

    def save_score(self):
        """Saves the score in json format"""
        scores = {"loss": self.score[0], "accuracy": self.score[1]}
        save_json(json_file_path=Path("scores.json"), data=scores)

    def log_into_mlflow(self):
        """This method registers the model scores and parametes into ML Flow"""
        mlflow.set_registry_uri(self.config.model_training.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics({"loss": self.score[0], "accuracy": self.score[1]})
            # Model registry does not work with file store
            if tracking_url_type_store != "file":
                # Register the model
                # There are other ways to use the Model Registry, which depends on the use case,
                # please refer to the doc for more information:
                # https://mlflow.org/docs/latest/model-registry.html#api-workflow
                mlflow.keras.log_model(
                    self.model, "model", registered_model_name="VGG16Model"
                )
            else:
                mlflow.keras.log_model(self.model, "model")
