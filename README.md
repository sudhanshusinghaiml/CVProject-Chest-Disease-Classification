# CVProject-Chest-Disease-Classification
Computer Vision - Chest Disease Classification from CT Scan Images

## Workflows

1. Update config/config.yaml
2. Update params.yaml
3. Update the entity - config_entity.py
4. Update the configuration manager in src config - configuration.py
5. Update the components
6. Update the pipeline
7. Update the main.py/app.py
8. Update the dvc.yaml


## Git commands

```bash
git add .

git commit -m "Updated"

git push origin main
```

## How to run?

```bash
conda create -n chest python=3.8 -y
```

```bash
conda activate chest
```

```bash
pip install -r requirements.txt
```

```bash
python app.py
```


### MLFlow Dagshub Connection URI

``` bash
MLFLOW_TRACKING_URI=https://dagshub.com/sudhanshusinghaiml/MLFlow-with-Dagshub-Experiment.mlflow \
MLFLOW_TRACKING_USERNAME=sudhanshusinghaiml \
MLFLOW_TRACKING_PASSWORD=<password> \
python script.py
```


### Run from bash terminal
``` bash
export MLFLOW_TRACKING_URI=https://dagshub.com/sudhanshusinghaiml/MLFlow-with-Dagshub-Experiment.mlflow

export MLFLOW_TRACKING_USERNAME=sudhanshusinghaiml

export MLFLOW_TRACKING_PASSWORD=<password>

python script.py
```


## DVC commands

```bash
dvc init
```

```bash
dvc repro
```

```bash
dvc dag
```

To track the changes with git, run:
```bash
git add dvc.lock
```

To enable auto staging, run:
```bash
dvc config core.autostage true
```

Use `dvc push` to send your updates to remote storage.
