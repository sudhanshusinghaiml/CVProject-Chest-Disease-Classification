"""
This module is typically used for creating project template
"""

import os
from pathlib import Path

PROJECT_DIRECTORY = "cnn_classifier"

list_of_files = [
    f"src/{PROJECT_DIRECTORY}/__init__.py",
    f"src/{PROJECT_DIRECTORY}/components/__init__.py",
    f"src/{PROJECT_DIRECTORY}/components/data_ingestion.py",
    f"src/{PROJECT_DIRECTORY}/components/model_trainer.py",
    f"src/{PROJECT_DIRECTORY}/components/model_evaluator.py",
    f"src/{PROJECT_DIRECTORY}/components/prepare_base_model.py",
    f"src/{PROJECT_DIRECTORY}/config/__init__.py",
    f"src/{PROJECT_DIRECTORY}/config/configuration.py",
    f"src/{PROJECT_DIRECTORY}/constants/__init__.py",
    f"src/{PROJECT_DIRECTORY}/entity/__init__.py",
    f"src/{PROJECT_DIRECTORY}/entity/config_entity.py",
    f"src/{PROJECT_DIRECTORY}/pipeline/__init__.py",
    f"src/{PROJECT_DIRECTORY}/pipeline/first_stage_data_ingestion.py",
    f"src/{PROJECT_DIRECTORY}/pipeline/second_stage_prepare_base_model.py",
    f"src/{PROJECT_DIRECTORY}/pipeline/third_stage_model_training.py",
    f"src/{PROJECT_DIRECTORY}/pipeline/fourth_stage_model_evaluation.py",
    f"src/{PROJECT_DIRECTORY}/pipeline/prediction.py",
    f"src/{PROJECT_DIRECTORY}/utils/__init__.py",
    f"src/{PROJECT_DIRECTORY}/utils/common_utils.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    "setup.py",
    "config/config.yaml",
    "templates/index.html",
]

for file_path in list_of_files:
    # file_path = Path(file_path)
    file_dir, file_name = os.path.split(Path(file_path))

    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) != 0):
        with open(file_path, "w", encoding="utf-8") as f:
            pass
    else:
        print("File or directory is already exists at: ", file_path)
