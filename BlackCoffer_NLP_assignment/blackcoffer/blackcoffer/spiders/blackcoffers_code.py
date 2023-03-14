import scrapy
import json

import pandas as pd
import numpy as np
from script_functions import *

path= "C:\\Users\\USER\\Downloads\\Input.xlsx"
url,url_id=create_url(path)

print(url)
print("*********************************")
print(url_id)
class scrap_data(scrapy.Spider):
    name="blackcoffer_scrap"
    start_urls=[]

    def parse(self,response):
        pass
        