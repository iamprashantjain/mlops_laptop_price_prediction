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


#### 13. Until now we have created a structure of a ml project which will remain common for all ML Projects, From now on we will try to convert our ml project jupyter code into modular coding
#### 14. Add a new folder "notebook" to keep the data file & jupyter file of ml project where we perform EDA, Feature Engineering, Model Building etc
#### 15. We are assuming that the dataset we have is cleaned by the data scraping team like feature engineering, missing value imputation, duplicates etc so whatever techniques we will use in data transformation & Model building, We will convert those into modular coding except EDA. EDA we are using to understand the techniques to use to pre-process the data
#### 16. Prepare X, y variables and perform Scaling like standardization or normalization & encoding like OHE or label in a pipeline
#### 17. All the helper functions which i've used, we will keep those in utils
#### 18. Perform model training in jupyter to understand all the steps & best methods which we can use in modular coding
#### 19. When we work in a team, we will have different teams working on webscraping data or preparing/collecting data and saving them into databases or locally or on cloud, Our job as a data scientist is to fetch data from that source & perform cleaning, eda, feature engineering, preprocessing, building models & deploy that on production
#### 20. In src > components > data_ingestion.py : we will write code to read data fom data source which can be either a database or api. for now, we will use the data file saved locally & split into train & test
#### 21. We will be reading already cleaned data, we only have to perform encoding & scaling.
#### 22. Also we need to update gitignore to not read artifacts folder