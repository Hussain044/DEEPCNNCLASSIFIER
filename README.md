

## workflow

1. Update config.yaml
2. Update secrets.yaml [optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config.
6. Update the components
7. Update the pipeline
8. Test run pipeline stage
9. run tox for testing package
10. Update the dvc.yaml 
11. run "dvc repro" command for running all the stages in pipeline


MLFLOW_TRACKING_URI=https://dagshub.com/Hussain044/DEEPCNNCLASSIFIER.mlflow \
MLFLOW_TRACKING_USERNAME=Hussain044 \
MLFLOW_TRACKING_PASSWORD=<>\
python script.py