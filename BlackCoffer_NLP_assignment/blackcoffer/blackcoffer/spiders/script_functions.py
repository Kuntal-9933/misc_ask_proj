import pandas as pd
import numpy as np

def create_url(dataset_path):
    df=pd.read_excel(dataset_path)
    lst_url = df[['URL']].values
    lst_id = df[['URL_ID']].values
    return list(lst_url),list(lst_id)

def SaveData():
    pass
