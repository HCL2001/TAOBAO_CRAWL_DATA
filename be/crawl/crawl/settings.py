from . import config
BOT_NAME = "crawl"

SPIDER_MODULES = ["crawl.spiders"]
NEWSPIDER_MODULE = "crawl.spiders"
ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'crawl.pipelines.MySQLPipeline': 300,
}

MYSQL_HOST = config.HOST
MYSQL_PORT = config.PORT
MYSQL_DATABASE = config.DB_NAME
MYSQL_USER = config.USER_NAME
MYSQL_PASSWORD = config.PASSWORD

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"


LOG_ENABLED = True
LOG_LEVEL = 'DEBUG'
LOG_FILE = 'spider.log'