import os
from pathlib import Path

project_directory = 'CNNClassifier'

list_of_files = [
    f'src/{project_directory}/__init__.py',
    f'src/{project_directory}/components/__init__.py',
    f'src/{project_directory}/components/data_ingestion.py',
    f'src/{project_directory}/components/model_trainer.py',
    f'src/{project_directory}/components/model_evaluator.py',
    f'src/{project_directory}/components/prepare_base_model.py',
    f'src/{project_directory}/config/__init__.py',
    f'src/{project_directory}/config/configuration.py',
    f'src/{project_directory}/constants/__init__.py',
    f'src/{project_directory}/entity/__init__.py',
    f'src/{project_directory}/entity/config_entity.py',
    f'src/{project_directory}/pipeline/__init__.py',
    f'src/{project_directory}/pipeline/first_stage_data_ingestion.py',
    f'src/{project_directory}/pipeline/second_stage_prepare_base_model.py',
    f'src/{project_directory}/pipeline/third_stage_model_training.py',
    f'src/{project_directory}/pipeline/fourth_stage_model_evaluation.py',
    f'src/{project_directory}/pipeline/prediction.py',
    f'src/{project_directory}/utils/__init__.py',
    f'src/{project_directory}/utils/common_utils.py',
    'app.py',
    'requirements.txt',
    'Dockerfile',
    'setup.py',
    'config/config.yaml',
    'templates/index.html'
]

for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path)

    if file_dir !='':
        os.makedirs(file_dir, exist_ok=True)

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)!=0):
        with open(file_path, 'w') as f:
            pass
    else:
        print(f"File or directory is already exists at: {file_path}")