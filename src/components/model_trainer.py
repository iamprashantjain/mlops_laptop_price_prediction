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
from src.utils import save_object, evaluate_models

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

            # Evaluate models using the utility function
            best_model_name, best_model, best_model_score = evaluate_models(X_train, X_test, y_train, y_test, models)
            
            logging.info(f"Best Model: {best_model_name} with Adjusted R^2 Score: {best_model_score}")

            save_object(
                file_path=self.model_trainer_config.trained_model_path,
                obj=best_model
            )

            return best_model_name, best_model_score

        except Exception as e:
            raise CustomException(e, sys)