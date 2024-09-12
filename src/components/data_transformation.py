import os
import sys
from dataclasses import dataclass

import pandas as pd
import numpy as np

# Imported preprocessing classes from sklearn
from sklearn.preprocessing import OneHotEncoder, StandardScaler, OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object


@dataclass
class DataTransformationConfig:
    # Path where the preprocessor object will be saved
    preprocessor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        """
        Initializes the DataTransformation class with the configuration settings
        for data transformation.
        """
        self.data_transformation_config = DataTransformationConfig()
        
    def get_data_transformer_object(self):
        """
        Creates and returns a data transformation pipeline.
        
        This function defines and sets up a preprocessing pipeline for both
        numerical and categorical features. The preprocessing steps include:
        
        - **Numerical Features Transformation:** 
          - StandardScaler is used to standardize numerical features by removing 
            the mean and scaling to unit variance.
          
        - **Categorical Features Transformation:** 
          - OneHotEncoder is used to perform one-hot encoding on categorical features 
            while dropping the first category to avoid multicollinearity.
          - OrdinalEncoder is used to encode 'memory_type' feature based on predefined 
            categories where 'SSD' is considered higher than 'Hard'.
        
        The preprocessor is created using the `ColumnTransformer` class, which allows 
        different preprocessing pipelines to be applied to different columns.
        
        Returns:
            ColumnTransformer: A scikit-learn ColumnTransformer object that contains
            separate pipelines for categorical and numerical feature transformation.
            
        Raises:
            CustomException: If there is any issue during the creation of the
            data transformation pipelines.
        """
        try:
            # Lists of feature names for numerical and categorical features
            num_features = ['rating', 'specScore', 'threads', 'screen_size', 'warranty',
                            'core_count', 'ram_capacity', 'memory_capacity', 'PPI']
            cat_features = ['brand', 'os', 'processor_brand', 'ram_type', 'memory_type',
                            'graphics_card_brand']
            
            # Define transformers for different feature types
            numeric_transformer = StandardScaler()
            oh_transformer = OneHotEncoder(sparse_output=False, drop='first')
            ordinal_transformer = OrdinalEncoder(categories=[['Hard', 'SSD']])
            
            # Create the ColumnTransformer to apply different transformers to specified columns
            preprocessor = ColumnTransformer(
                transformers=[
                    ('cat', Pipeline(steps=[
                        ('onehot', oh_transformer)
                    ]), cat_features),
                    ('mem', Pipeline(steps=[
                        ('ordinal', ordinal_transformer)
                    ]), ['memory_type']),
                    ('num', Pipeline(steps=[
                        ('scaler', numeric_transformer)
                    ]), num_features)
                ]
            )
            
            logging.info("Encoding & scaling completed on both numerical & categorical columns in their respective pipelines in a transformer.")
            
            return preprocessor
            
        except Exception as e:
            raise CustomException(e, sys)
        
        
    
    def initiate_data_transformation(self, train_path, test_path):
        try:
            logging.info("read train & test data under transformation module")
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
                        
            
            logging.info("obtaining pre processor object")
            preprocessing_obj = self.get_data_transformer_object()            
            
            
            logging.info("setting input & target columns for train & test data to apply transformations")
            target_column_name = "price"
            input_feature_train_df = train_df.drop(columns=[target_column_name], axis=1)
            target_feature_train_df = train_df[target_column_name]
            
            input_feature_test_df = test_df.drop(columns=[target_column_name], axis=1)
            target_feature_test_df = test_df[target_column_name]
            
            
            logging.info("applying pre processing object on train & test df")
            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)
            
            
            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            
            
            test_arr = np.c_[
                input_feature_test_arr, np.array(target_feature_test_df)
            ]
            
            
            logging.info("saved preprocessing object")
            
            save_object(
                file_path = self.data_transformation_config.preprocessor_obj_file_path, 
                obj = preprocessing_obj
            )
            
            
            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path, 
            )
            
                    
        except Exception as e:
            raise CustomException(e,sys)