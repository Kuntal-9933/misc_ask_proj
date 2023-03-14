import pandas as pd
import numpy as np

def create_url(dataset_path):
    df=pd.read_xlsx(dataset_path)
    lst_url = df[['URL']].values
    lst_id = df[['URL_ID']].values
    return lst_url,lst_id

def SaveData():
    pass
