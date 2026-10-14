# Kindy-disease-Classification
This is a Deep learning project for kidney disease Classification.
# How to Run?

## Workflows

1. Update `config/config.yaml`
2. Update `secrets.yaml` [Optional]
3. Update `params.yaml`
4. Update the entity (`src/cnnClassifier/entity/config_entity.py`)
5. Update the configuration manager (`src/cnnClassifier/config/configuration.py`)
6. Update the components (`src/cnnClassifier/components/`)
7. Update the pipeline (`src/cnnClassifier/pipeline/`)
8. Update `main.py`
9. Update `dvc.yaml`
10. app.py

### STEPS:

Clone the repository

```bash
https://github.com/afnanm25/Kindy-disease-Classification
```
### step 01- create a conda environments after opening the repository

```bash
conda create -n environment_name python=3.8 -y 


conda activate environment_name 
```
### step 02- install the requirments
```bash
python -m pip install -r requirements.txt
```