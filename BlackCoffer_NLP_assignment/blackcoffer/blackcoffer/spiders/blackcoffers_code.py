import scrapy
import json

class scrap_data(scrapy.Spider):
    name="blackcoffer_scrap"
    start_urls=[]

    def parse(self,response):
        pass