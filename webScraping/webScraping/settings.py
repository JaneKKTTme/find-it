BOT_NAME = 'webScraping'
SPIDER_MODULES = ['webScraping.spiders']
NEWSPIDER_MODULE = 'webScraping.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'janekkttme'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

DOWNLOAD_DELAY = 1

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = { 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Language': 'ru',}

# Configure item pipelines
ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1}

IMAGES_STORE = '/home/janekkttme/Документы/FindIt/webScraping/images_scraped'
