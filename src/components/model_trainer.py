import os
import sys
from dataclasses import dataclass
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import KFold, cross_val_score
from sklearn.preprocessing import FunctionTransformer
from sklearn.linear_model import Ridge, Lasso, ElasticNet, HuberRegressor, TheilSenRegressor, QuantileRegressor
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression, SGDRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.isotonic import IsotonicRegression
from sklearn.neural_network import MLPRegressor
from xgboost import XGBRegressor
from src.logger import logging
from src.exception import CustomException
from src.utils import save_object

@dataclass
class ModelTrainerConfig:
    trained_model_path = os.path.join("artifacts", "model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
        
    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("Splitting train & test input data")
            X_train, X_test, y_train, y_test = (
                train_array[:, :-1],
                test_array[:, :-1],
                train_array[:, -1],
                test_array[:, -1]
            )
            
            # Define models
            models = {
                'LinearRegression': LinearRegression(),
                'SGDRegressor': SGDRegressor(),
                'KNeighborsRegressor': KNeighborsRegressor(),
                'GaussianProcessRegressor': GaussianProcessRegressor(),
                'DecisionTreeRegressor': DecisionTreeRegressor(),
                'GradientBoostingRegressor': GradientBoostingRegressor(),
                'RandomForestRegressor': RandomForestRegressor(),
                'MLPRegressor': MLPRegressor(),
                'XGBRegressor': XGBRegressor(),
                'Ridge': Ridge(),
                'Lasso': Lasso(),
                'ElasticNet': ElasticNet(),
                'HuberRegressor': HuberRegressor(),
                'TheilSenRegressor': TheilSenRegressor(),
                'QuantileRegressor': QuantileRegressor()
            }

            best_model_name = None
            best_model_score = -float('inf')  # Start with a very low score for maximization
            best_model = None

            for name, model in models.items():
                logging.info(f"Training model: {name}")
                model.fit(X_train, y_train)
                
                # Predict on test data
                y_pred = model.predict(X_test)
                
                # Calculate evaluation metrics
                mae = mean_absolute_error(y_test, y_pred)
                mse = mean_squared_error(y_test, y_pred)
                r2 = r2_score(y_test, y_pred)
                
                logging.info(f"{name} - MAE: {mae}, MSE: {mse}, R^2: {r2}")
                
                # Cross-validation score
                cv_score = cross_val_score(model, X_train, y_train, cv=5, scoring='r2').mean()
                logging.info(f"{name} - Cross-Validation R^2 Score: {cv_score}")

                # Compare and store the best model
                if r2 > best_model_score:
                    best_model_name = name
                    best_model_score = r2
                    best_model = model
            
            logging.info(f"Best Model: {best_model_name} with R^2 Score: {best_model_score}")
            
            save_object(
                file_path=self.model_trainer_config.trained_model_path,
                obj = best_model
            )
           
            return best_model_name, best_model_score
        
        except Exception as e:
            raise CustomException(e, sys)