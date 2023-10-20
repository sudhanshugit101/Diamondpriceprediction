import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PredictionPipeline:
    def __init__(self):
        pass

    def predict(self, data: pd.DataFrame):
        

class CustomData:
    def __init__(self, carat: float, cut: str, color: str, clarity: str, 
                 depth: float, table: float, x: float, y: float, z: float):
        self.carat = carat
        self.cut = cut
        self.color = color
        self.clarity = clarity
        self.depth = depth
        self.table = table
        self.x = x
        self.y = y
        self.z = z
    def get_data(self):
        return pd.DataFrame({'carat': [self.carat],
                             'cut': [self.cut],
                             'color': [self.color],
                             'clarity': [self.clarity],
                             'depth': [self.depth],
                             'table': [self.table],
                             'x': [self.x],
                             'y': [self.y],
                             'z': [self.z]})
    