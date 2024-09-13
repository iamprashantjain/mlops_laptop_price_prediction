import os
import sys

import pandas as pd
import numpy as np

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, load_object


class PredictPipeline:
    def __init__(self):
        pass
    
    
    def predict(self,features):
        try:
            model_path = 'artifacts\model.pkl'
            preprocessor_path = 'artifacts\preprocessor.pkl'
            
            model = load_object(file_path = model_path)
            preprocessor = load_object(file_path = preprocessor_path)
            
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
                      
            return preds
            
        except Exception as e:
            raise CustomException(e,sys)
        
    
class CustomData:
    def __init__(self,rating:float,specScore:int,brand:str,threads:int,screen_size:float,os:str,warranty:int,core_count:int,processor_brand:str,ram_capacity:int,ram_type:str,memory_capacity:int,memory_type:str,graphics_card_brand:str,PPI:float):
        self.rating = rating
        self.specScore = specScore
        self.brand = brand
        self.threads = threads
        self.screen_size = screen_size
        self.os = os
        self.warranty = warranty
        self.core_count = core_count
        self.processor_brand = processor_brand
        self.ram_capacity = ram_capacity
        self.ram_type = ram_type
        self.memory_capacity = memory_capacity
        self.memory_type = memory_type
        self.graphics_card_brand = graphics_card_brand
        self.PPI = PPI
        
    
    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'rating' : [self.rating],
                'specScore' : [self.specScore],
                'brand' : [self.brand],
                'threads' : [self.threads],
                'screen_size' : [self.screen_size],
                'os' : [self.os],
                'warranty' : [self.warranty],
                'core_count' : [self.core_count],
                'processor_brand' : [self.processor_brand],
                'ram_capacity' : [self.ram_capacity],
                'ram_type' : [self.ram_type],
                'memory_capacity' : [self.memory_capacity],
                'memory_type' : [self.memory_type],
                'graphics_card_brand' : [self.graphics_card_brand],
                'PPI' : [self.PPI]
                }
            
            return pd.DataFrame(custom_data_input_dict)

        
        except Exception as e:
            raise CustomException(e,sys)