"""Module provides configurations for all the different stages of Project Lifecycle."""

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    """
    This class encapsulates the variables configurations that will be used further in pipelines
    """

    root_directory: Path
    source_url: str
    downloaded_data_file: Path
    unzip_directory: Path
