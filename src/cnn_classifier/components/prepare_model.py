"""
This Module covers the class and methods for preparing the model ARCHITECTURE
that will be used for classification
"""

from pathlib import Path
import tensorflow as tf
from src.cnn_classifier.entity.config_entity import PrepareModelArchitectureConfig


class PrepareModelArchitecture:
    """
    This Class encapsulates the methods for preparing the base models from VGG!6
    """

    def __init__(self, config: PrepareModelArchitectureConfig):
        self.config = config
        self.model: tf.keras.Model = None
        self.updated_model: tf.keras.Model = None

    def get_base_model(self):
        """
        This fetches the pre-trained model from Keras and saves it in our directory
        """
        self.model = tf.keras.applications.vgg16.VGG16(
            input_shape=self.config.params_image_size,
            weights=self.config.params_weights,
            include_top=self.config.params_include_top,
        )

        self.save_model(path=self.config.model_path, model=self.model)

    @staticmethod
    def _prepare_full_model(
        model: tf.keras.models,
        classes: int,
        freeze_all: bool,
        freeze_till: int,
        learning_rate: float,
    ) -> tf.keras.Model:
        """
        This is the private method that freezes the CNN layers and trains
        the top most layers of Pretrained models
        """
        if freeze_all:
            for layer in model.layers:
                layer.trainable = False
        elif (freeze_till is not None) and (freeze_till > 0):
            for layer in model.layers[:-freeze_till]:
                layer.trainable = False

        flatten_in = tf.keras.layers.Flatten()(model.output)
        prediction = tf.keras.layers.Dense(units=classes, activation="softmax")(
            flatten_in
        )

        full_model = tf.keras.models.Model(inputs=model.input, outputs=prediction)

        full_model.compile(
            optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=["accuracy"],
        )

        full_model.summary()
        return full_model

    def update_model(self):
        """
        This method calls the private method for preparing the updated model
        """
        self.updated_model = self._prepare_full_model(
            model=self.model,
            classes=self.config.params_classes,
            freeze_all=True,
            freeze_till=None,
            learning_rate=self.config.params_learning_rate,
        )

        self.save_model(path=self.config.updated_model_path, model=self.updated_model)

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        """This method is used to save the model - pre-trained model or finetuned model"""
        model.save(path)
