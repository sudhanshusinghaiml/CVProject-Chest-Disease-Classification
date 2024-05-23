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
