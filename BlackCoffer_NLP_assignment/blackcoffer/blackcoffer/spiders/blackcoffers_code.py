import scrapy
import json

import pandas as pd
import numpy as np


path="C:\\Users\\KUNTAL MUKHERJEE\\Downloads\\Input.xlsx"
import pandas as pd
import numpy as np

def create_url(dataset_path):
    df=pd.read_excel(dataset_path)
    lst_url = df['URL'].values
    lst_id = df['URL_ID'].values
    return lst_url,lst_id

url,url_id=create_url(path)

print(url)

class scrap_data(scrapy.Spider):
    name="blackcoffer_scrap"
    def start_requests(self):
        for i in url:
            yield scrapy.Request(i)

    def parse(self,response):
        title=response.xpath("//title/text()").getall()
        print(title)
        
        