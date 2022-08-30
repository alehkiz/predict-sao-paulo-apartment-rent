from joblib import dump, load
import pandas as pd
import numpy as np
from sklearn.preprocessing import OrdinalEncoder
from sklearn.metrics import mean_absolute_percentage_error as mape, mean_absolute_error as mae
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from app.config.config import BaseConfig as config





class Pipeline(object):
    data = []
    predict_value_orig = 0.0
    predict_value_real = 0.0
    
    
    def __init__(self) -> None:
        self.ordinal_encoder = load(config.ORDINAL_ENCODER)
        self.pipeline = load(config.PIPELINE)

    def load(self, bedrooms:int =0, toilets:int=0, suites:int=0, parking:int=0, area:int=0, furnished:bool=False, swimming_pool:bool=False, elevator:bool=False, neighborhood:str=''):
        """Insert in `self.data` values for sample inserted by user for prediction

        Args:
            bedrooms (int): Number of bedrooms
            bathrooms (int): Number of bathrooms
            parking (int): Number of parking lot
            area (int): Size area
            tenement (str): neighborhood in string
        """
        neighborhood = self.ordinal_encoder.transform([[neighborhood]]).flatten()[0]
        # print(f'Bairro: {tenement}:{bairro}')
        #Size 	Rooms 	Toilets 	Suites 	Parking 	Elevator 	Furnished 	Swimming Pool 	District
        self.data = [area, bedrooms, toilets, suites, parking, elevator, furnished, swimming_pool, neighborhood]
    def get_neighborhood_id(self, neighborhood:str) -> str:
        return int(self.ordinal_encoder.transform([[neighborhood]]).flatten()[0])
        
    def predict(self):
        """After load run predict to get value of price of rent of house.
        Return value in reais rounded
        """
        if not self.data:
            raise Exception('Primeiro rode load e informe os dados do aportamento')
        self.predict_value_orig = self.pipeline.predict(np.array(self.data).reshape(1,-1))
        self.predict_value_real = np.round(np.exp(self.predict_value_orig), decimals=2)[0]
        return {'original': self.predict_value_real,
                'monetary': config.locale.currency(self.predict_value_real)}
        
