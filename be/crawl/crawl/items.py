import scrapy


class SaveToProductList(scrapy.Item):
    link_id = scrapy.Field()
    brand_id = scrapy.Field()
    report_id = scrapy.Field()
    original_price = scrapy.Field()
    price = scrapy.Field()
    status = scrapy.Field()
    crawl_time = scrapy.Field()
    total = scrapy.Field()
    name = scrapy.Field()
    link = scrapy.Field()
    table_name = scrapy.Field()


class SaveToReportList(scrapy.Item):
    brand_id = scrapy.Field()
    report_id = scrapy.Field()
    success = scrapy.Field()
    failure = scrapy.Field()
    start_crawl = scrapy.Field()
    end_crawl = scrapy.Field()
    table_name = scrapy.Field()
