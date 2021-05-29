import scrapy
from webScraping.items import WebScrapingItem
from webScraping.items import ImgData
from scrapy.http import Request

#to read from a csv file
import csv


class FashionhmSpider(scrapy.Spider):
	name = 'fashionHM'
	allowed_domains = ['www2.hm.com']
	start_urls = ['http://www2.hm.com/']
	
	# This function helps us to scrape the whole content of the website 
	# by following the links in a csv file.
	def start_requests(self):

		# Read main category links from a csv file		
		with open("/home/janekkttme/Документы/FindIt/webScraping/csvFiles/HM.csv", "rU") as f:
			reader=csv.DictReader(f)
		
			for row in reader:

				url=row['url']
				# Change the offset value incrementally to navigate through the product list
				# You can play with the range value according to maximum product quantity
				link_urls = [url.format(i*100) for i in range(0,5)]

				
				for link_url in link_urls:

					#Pass the each link containing 100 products, to parse_product_pages function with the gender metadata
					request=Request(link_url, callback=self.parse_product_pages, meta={'gender': row['gender']})
		
					yield request

  
	# This function scrapes the page with the help of xpath provided
	def parse_product_pages(self,response):

		item=WebScrapingItem()

		# Get the HTML block where all the products are listed
		# <ul> HTML element with the "products-listing small" class name
		content=response.xpath('//ul[@class="products-listing large"]')
		
		# loop through the <li> elements with the "product-item" class name in the content
		for product_content in content.xpath('//li[@class="product-item"]'):

			# get the product details and populate the items
			item['productId']=product_content.xpath('.//article[@class="hm-product-item"]/@data-articlecode').extract_first()
			item['productName']=product_content.xpath('.//a[@class="link"]/text()').extract_first()

			item['priceOriginal']=product_content.xpath('.//span[@class="price regular"]/text()').extract_first()
			item['priceSale']=product_content.xpath('.//span[@class="price sale"]/text()').extract_first()

			if item['priceSale']==None:
				item['priceSale']=item['priceOriginal']

			item['productLink']="https://www2.hm.com"+product_content.xpath('.//a[@class="link"]/@href').extract_first()
			
			#yield Request(item['productLink'], self.parse_product_page, cb_kwargs=dict(item=item))
						
			item['imageLink']="https:"+product_content.xpath('.//img/@data-src').extract_first()


			item['company']="HM"

			item['gender']=response.meta['gender']

			
			if item['productId']==None:
				break

			print(item['productLink'])

			
			yield (item)

	def parse_product_page(self, response, item):
	    item['description'] = response.xpath('//p[@class="pdp-description-text"]/text()').extract_first()
	    #item['color'] = response.xpath('//dd[@class="details-list-item"]/text()').get()
	    yield item
	    

	def parse(self, response):
		pass
