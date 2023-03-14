import pandas as pd
import numpy as np

def create_url(dataset_path):
    df=pd.read_xlsx(dataset_path)
    lst_url = df[['URL']]
    lst_id = df[['URL_ID']]
    return lst_url,lst_id

def SaveData():
    pass

def XYZ():
    pass