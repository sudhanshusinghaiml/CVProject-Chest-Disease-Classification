"""This module contains class and methods for model evaluation pipeline"""

from src.cnn_classifier.config.configuration import ConfigurationManager
from src.cnn_classifier.logger import logging
from src.cnn_classifier.components.model_evaluator import ModelEvaluation

STAGE_NAME = "Model Evaluation Pipeline"


class ModelEvaluationPipeline:
    """This class encapsulates the methods for model evaluation"""

    def __init__(self):
        pass

    def main(self):
        """This method performs Model Evaluation and saves score for auditing purpose"""
        logging.info(
            "Inside src.cnn_classifier.components.pipeline.ModelEvaluationPipeline"
        )
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()

        logging.info(
            "Completed execution of get_model_evaluation_config method of \
                src.cnn_classifier.config.configuration.ConfigurationManager"
        )

        model_evaluation = ModelEvaluation(model_evaluation_config)
        model_evaluation.evaluation()
        logging.info(
            "Completed execution of evaluation method of \
                src.cnn_classifier.components.model_evaluator.ModelEvaluation"
        )

        model_evaluation.save_score()
        logging.info(
            "Completed execution of save_score method of \
                src.cnn_classifier.components.model_evaluator.ModelEvaluation"
        )
        model_evaluation.log_into_mlflow()
        logging.info(
            "Completed execution of log_into_mlflow method of \
                src.cnn_classifier.components.model_evaluator.ModelEvaluation"
        )


if __name__ == "__main__":
    try:
        logging.info(">>>>>> Started %s <<<<<<", STAGE_NAME)
        obj = ModelEvaluationPipeline()
        obj.main()
        logging.info(">>>>>> stage %s completed <<<<<<\n\n", STAGE_NAME)
    except Exception as error:
        logging.exception(error)
        raise error
