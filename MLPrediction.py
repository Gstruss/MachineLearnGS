import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_log_error

from grafi_moshe import CapturaDatos
class PrepareData:
    def __init__(self):
        self.listReturned = CapturaDatos()
        self.listData = []

    def PrepareJson(self):
        self.listReturned.captura()
        self.listData = self.listReturned.limpieza()

    def pandasData(self):
        df = pd.DataFrame(self.listData,columns=['Year','Quarter','Provider','Income','amountSMS'])
        print(df)

prueba = PrepareData()
prueba.PrepareJson()
prueba.pandasData()
