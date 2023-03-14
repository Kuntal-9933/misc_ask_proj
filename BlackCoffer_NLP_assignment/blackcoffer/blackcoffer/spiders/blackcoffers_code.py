import scrapy
import json
import shutil
import pandas as pd
import numpy as np


path="C:\\Users\\KUNTAL MUKHERJEE\\Downloads\\Input.xlsx"
import pandas as pd
import numpy as np
current_loc="F:\MISC_Projects_ASK\BlackCoffer_NLP_assignment\blackcoffer"
destination_loc="F:\MISC_Projects_ASK\BlackCoffer_NLP_assignment\blackcoffer\data_folder"

def create_url(dataset_path):
    df=pd.read_excel(dataset_path)
    lst_url = df['URL'].values
    lst_id = df['URL_ID'].values
    return lst_url,lst_id

url,url_id=create_url(path)

class scrap_data(scrapy.Spider):
    name="blackcoffer_scrap"
    def start_requests(self):
        for i in range(len(url)-2,len(url)):
            file_name=url_id[i]
            yield scrapy.Request(url[i],callback=self.parse,cb_kwargs={'file_name':file_name})

    def parse(self,response,file_name):
        title=response.xpath("//title/text()").get()
        web_text=response.xpath("//div[@class='td-container']//text()").getall()
        web_text=web_text.insert(0,title)
        print(title)
        # text=" ".join(web_text)
        # main_string=(title+" "+text)
        # file=f"{file_name}.txt"
        # np.savetxt(file,web_text,delimiter=' ')
        # shutil.move(src=(current_loc+"\\"+file),dst=(destination_loc+"\\"+file))
        
        