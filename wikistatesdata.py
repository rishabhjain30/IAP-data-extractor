import requests
import bs4
import xlsxwriter
from itertools import izip
from time import sleep
import scrapy

class item(scrapy.Item):
  name=scrapy.field()
  address=scrapy.field()
  phone=scrapy.field()
  email=scrapy.field()

class Spider(scrapy.Spider):
  name="data for doctors"
  allowed_domains=['www.iapindia.org']
  start_urls=["http://www.iapindia.org/members.php"]

  def parse(self, response):
     filename = response.url.split("/")[-2]
     with open(filename, 'wb') as f:
        f.write(response.body)