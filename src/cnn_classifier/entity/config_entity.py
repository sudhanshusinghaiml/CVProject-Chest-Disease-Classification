"""Module provides configurations for all the different stages of Project Lifecycle."""

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    """
    This class encapsulates the variables configurations for DataIngestion
    pipelines that will be used further
    """

    root_directory: Path
    source_url: str
    downloaded_data_file: Path
    unzip_directory: Path


@dataclass(frozen=True)
class PrepareModelArchitectureConfig:
    """
    This class encapsulates the variables configuration for Model Architecture
    """

    root_directory: Path
    model_path: Path
    updated_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int


@dataclass(frozen=True)
class ModelTrainingConfig:
    """
    This class encapsulates the variables associated with Model Training
    """

    root_directory: Path
    trained_model_path: Path
    updated_model_path: Path
    training_data: Path
    params_epochs: int
    params_batch_size: int
    params_augmentation_required: bool
    params_image_size: list
    params_validation_split: float
    params_interpolation: str
    params_rotation_range: int
    params_horizontal_flip: bool
    params_width_shift_range: float
    params_height_shift_range: float
    params_shear_range: float
    params_zoom_range: float
    params_shuffle: bool
    params_validation_subset: str
    params_training_subset: str


@dataclass(frozen=True)
class ModelEvaluationConfig:
    """
    This class encapsulates the variables associated with Model Evaluation
    """

    path_of_model: Path
    training_data: Path
    all_params: dict
    mlflow_uri: str
    params_image_size: list
    params_batch_size: int
    params_validation_split: float
    params_shuffle: bool
    params_validation_subset: str
    params_interpolation: str


@dataclass(frozen=True)
class PredictionPipelineConfig:
    """
    This class encapsulates the variables associated with Prediction Pipeline
    """

    model_path: Path
    params_image_size: list
