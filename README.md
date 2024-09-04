# mlops_laptop_price_prediction

# Steps
#### 1. Create Git Repo & Clone it on local pc
#### 2. Create VENV, Activate
#### 3. Create requirements.txt & setup.py (to build application as package)
#### 4. Write setup.py code (meta data information about project)
#### 5. Create a folder src & __init__ file inside it to find this folder as package. All the project development will happen inside this folder.
#### 6. Add "-e ." in requirements.txt file to enable it to install setup.py also when requirements.txt executes
#### 7. Install requirements "pip install -r requirements.txt", It will also run setup.py & build package of ml project "laptop_price_prediction.egg-info"
#### 8. Git commit & push
#### 9. Folder structure can be created automatically using template.py or cookiecutter library
#### 10. src --> create a folder "components" & inside it create a __init__ file, folder contains all the modules like data_ingestion (reading data), data_transformation, model_trainer, model_pusher
#### 11. src --> create a folder "pipeline" & inside it create a __init__ file & train_pipeline & predict_pipeline
#### 12. Also create logger, exception & utils.py (to keep common functions) file inside src folder
#### 