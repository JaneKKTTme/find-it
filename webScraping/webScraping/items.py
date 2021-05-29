#items.py
import scrapy
from scrapy.item import Item, Field

class WebScrapingItem(Item):
    #product related items, such as id,name,price
    gender = Field()
    productId = Field()
    productName = Field()
    priceOriginal = Field()
    priceSale = Field()
    
 
    #items to store links
    imageLink = Field()
    productLink = Field()#item for company name
    company = Field()
    

pass

class ImgData(Item):
#image pipline items to download product images
    image_urls = scrapy.Field()
    images=scrapy.Field()
    
class AdditionalData(Item):
    #color = Field()
    productLink = Field()
    description = Field()
