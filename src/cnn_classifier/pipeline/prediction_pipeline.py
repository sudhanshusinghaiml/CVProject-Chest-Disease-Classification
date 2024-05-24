"""This module contains methods that are used for prediction pipeline"""

import numpy as np
import tensorflow as tf
from src.cnn_classifier.logger import logging
from src.cnn_classifier.config.configuration import ConfigurationManager


class PredictionPipeline:
    """This method encapsulates the method that is used for prediction"""

    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        """
        This is the main method which predicts the input image
        classification into Adenocarcinoma Cancer or Normal
        """

        config = ConfigurationManager()
        prediction_config = config.get_prediction_config()
        logging.info(
            "Completed execution get_model_training_config method of \
                src.cnn_classifier.config.configuration.ConfigurationManager"
        )

        model = tf.keras.models.load_model(prediction_config.model_path)
        logging.info("Loaded models from directory", model)

        loaded_image = tf.keras.preprocessing.image.load_img(
            self.filename,
            target_size=(
                prediction_config.params_image_size[0],
                prediction_config.params_image_size[1],
            ),
        )
        logging.info("Loaded image for prediction", loaded_image)

        loaded_image_array = tf.keras.preprocessing.image.img_to_array(loaded_image)
        logging.info("Loaded image array for prediction", loaded_image_array)

        image_array = np.expand_dims(loaded_image_array / 255, axis=0)
        logging.info("Expanded image array for prediction", image_array)

        predicted_output = model.predict(image_array)
        logging.info("Predicted Probabilities of Image are", predicted_output)

        result = np.argmax(predicted_output, axis=1)
        logging.info("Getting result[0] from model:", result[0])
        # logging.info("Getting result[1] from model:", result[1])

        if result[0] == 1:
            prediction = "Normal"
            return [{"image": prediction}]
        else:
            prediction = "Adenocarcinoma Cancer"
            return [{"image": prediction}]
