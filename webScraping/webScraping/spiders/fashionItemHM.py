import scrapy
from webScraping.items import AdditionalData
from scrapy.http import Request

#to read from a csv file
import csv
import json


class FashionhmSpider(scrapy.Spider):
	name = 'fashionItemHM'
	allowed_domains = ['www2.hm.com']
	start_urls = ['http://www2.hm.com/']
	
	# This function helps us to scrape the whole content of the website 
	# by following the links in a csv file.
	def start_requests(self):

		# Read main category links from a csv file		
		with open("/home/janekkttme/Документы/FindIt/webScraping/data_HM.csv", "rU") as f:
			reader=csv.DictReader(f)
		
			for row in reader:

				url=row['productLink']
				# Change the offset value incrementally to navigate through the product list
				# You can play with the range value according to maximum product quantity
				link_urls = [url.format(i*100) for i in range(0,5)]

				
				for link_url in link_urls:

					#Pass the each link containing 100 products, to parse_product_pages function with the gender metadata
					request=Request(link_url, callback=self.parse_product_page)
		
					yield request

  
	# This function scrapes the page with the help of xpath provided
	def parse_product_page(self, response):

		item=AdditionalData()
		
		item['productLink'] = "https://www2.hm.com" + response.xpath('//li[@class="list-item"]/a[@class="filter-option miniature active"]/@href').extract_first()
		
		item['description'] = response.xpath('//p[@class="pdp-description-text"]/text()').extract_first()
		
		#item['color'] = response.xpath('//dd[@class="details-list-item"]/text()').get()
		
		yield item
	    
	    

	def parse(self, response):
		pass
