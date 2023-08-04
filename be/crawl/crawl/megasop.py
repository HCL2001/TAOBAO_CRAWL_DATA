import uuid
import xml.etree.ElementTree as ET
from datetime import datetime

from scrapy import signals
from model import ModelDAO
import requests

import config
import scrapy
from bs4 import BeautifulSoup

from database import get_links_from_database, get_success_fail_product_list_from_database, save_objects_to_database,get_all_link_brand
from items import SaveToProductList


def generate_report_id():
    id_uuid = uuid.uuid4().hex
    create_id = id_uuid
    return create_id


report_id = generate_report_id()
start_crawl = datetime.now()


class LinkSpider(scrapy.Spider):
    name = 'link-spider'

    def start_requests(self):
        proxy_url = f"http://{config.PROXY_USER}:{config.PROXY_PASS}@{config.PROXY_IP}:{config.PROXY_PORT}"
        link_check = 'https://www.google.com.vn/'
        links = get_links_from_database()
        count = 0
        response = requests.get(link_check, proxies={"http": proxy_url, "https": proxy_url})
        print(response.status_code == 200)
        for link in links:
            count += 1
            if count == 500:
                response = requests.get(link_check, proxies={"http": proxy_url, "https": proxy_url})
                count = 0
            if response.status_code == 200:
                if link.brand_id == 1:
                    print("hasaki")
                    yield scrapy.Request(
                        url=link.name,
                        callback=self.hasaki,
                        errback=self.handle_error,
                        meta={'link': link, 'link_name': link.link, 'report_id': report_id, 'proxy': proxy_url})
                        # meta={'link': link, 'link_name': link.link, 'report_id': report_id})

                if link.brand_id == 2:
                    print("pharmacity")
                    url = f"https://api-gateway.pharmacity.vn/api/product?slug={link.name}"
                    yield scrapy.Request(
                        url,
                        callback=self.pharmacity,
                        errback=self.handle_error,
                        headers={'User-Agent': 'Mozilla/5.0'},
                        meta={'link': link, 'link_name': link.link, 'report_id': report_id, 'proxy': proxy_url})

                if link.brand_id == 3:
                    print("guardian")
                    yield scrapy.Request(
                        url=link.name,
                        callback=self.guardian,
                        errback=self.handle_error,
                        meta={'link': link, 'link_name': link.link, 'report_id': report_id, 'proxy': proxy_url})

                if link.brand_id == 4:
                    print("watson")
                    product_code = f"BP_{link.name}"
                    url = f"https://api.watsons.vn/api/v2/wtcvn/products/{product_code}"

                    yield scrapy.Request(
                        url=url,
                        callback=self.watson,
                        errback=self.handle_error,
                        meta={'link': link, 'link_name': link.link, 'report_id': report_id, 'proxy': proxy_url})
            else:
                return {
                    'status': 'failed',
                    'message': 'Proxy hết hạn'
                }

    # xử lí bất đồng bộ và đa luồng
    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(LinkSpider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider

    def spider_closed(self, spider):
        products = get_success_fail_product_list_from_database(report_id)
        hasaki_success = 0
        guardian_success = 0
        pharmacity_success = 0
        watson_success = 0
        hasaki_fail = 0
        guardian_fail = 0
        pharmacity_fail = 0
        watson_fail = 0
        objects = []
        end_time = datetime.now()
        for product in products:
            if product.status != 0:
                if product.brand_id == 1:
                    hasaki_success += 1
                elif product.brand_id == 2:
                    pharmacity_success += 1
                elif product.brand_id == 3:
                    guardian_success += 1
                else:
                    watson_success += 1
            else:
                if product.brand_id == 1:
                    hasaki_fail += 1
                elif product.brand_id == 2:
                    pharmacity_fail += 1
                elif product.brand_id == 3:
                    guardian_fail += 1
                else:
                    watson_fail += 1
        total_hasaki = get_all_link_brand(1)
        total_pharmacity = get_all_link_brand(2)
        total_guardian = get_all_link_brand(3)
        total_watson = get_all_link_brand(4)
        hasaki = ModelDAO(1, report_id, hasaki_success, hasaki_fail, total_hasaki, start_crawl, end_time)
        pharmacity = ModelDAO(2, report_id, pharmacity_success, pharmacity_fail, total_pharmacity, start_crawl, end_time)
        guardian = ModelDAO(3, report_id, guardian_success, guardian_fail, total_guardian, start_crawl, end_time)
        watson = ModelDAO(4, report_id, watson_success, watson_fail, total_watson, start_crawl, end_time)
        objects.append(hasaki)
        objects.append(pharmacity)
        objects.append(guardian)
        objects.append(watson)
        save_objects_to_database(objects)

    @staticmethod
    def create_item(link_id, brand_id, report_id, product_price, original_price, product_status, crawl_time, status,
                    product_name, link):
        item = SaveToProductList()
        item['link_id'] = link_id
        item['brand_id'] = brand_id
        item['report_id'] = report_id
        item['price'] = product_price
        item['original_price'] = original_price
        item['status'] = status
        item['crawl_time'] = crawl_time
        item['total'] = product_status
        item['name'] = product_name
        item['link'] = link
        item['table_name'] = 'product_list'
        return item

    @staticmethod
    def create_item_with_defaults(self, link_id, brand_id, report_id, crawl_time, link):
        print("loi nef")
        product_price = 0
        original_price = 0
        product_status = 0
        product_name = 0
        status = 0
        item = self.create_item(link_id, brand_id, report_id, product_price, original_price, product_status,
                                crawl_time, status, product_name, link)
        return item

    @staticmethod
    def check_null(condition):
        if condition:
            return condition
        return 0

    @staticmethod
    def get_status(status_code):
        if status_code == 200:
            return 1
        else:
            return 0

    # Handle 404
    def handle_error(self, failure):
        print("loi link ne")
        response = failure.value.response
        link = response.meta['link']
        link_name = response.meta['link_name']
        print(link_name)
        brand_id = link.brand_id
        crawl_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        item = self.create_item_with_defaults(self=self, link_id=link.id, brand_id=brand_id, report_id=report_id,
                                              crawl_time=crawl_time, link=link_name)
        yield item

    def hasaki(self, response):
        link = response.meta['link']
        status_code = response.status
        brand_id = link.brand_id
        crawl_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if status_code == 200:
            status = self.get_status(status_code)
            html_content = response.body
            soup = BeautifulSoup(html_content, "html.parser")
            span_element_name = soup.find('span', class_='product__title', itemprop="name")

            if span_element_name:
                product_name = span_element_name.text.strip()
            else:
                product_name = ""

            span_element_price = soup.find('input', id='product_final_price')
            if span_element_price:
                product_price = span_element_price['value']
            else:
                product_price = 0

            span_original_price = soup.find('span', id='market_price')
            if span_original_price and span_original_price.text[0] != '0':
                original_price = span_original_price.text.strip().replace("₫", "").replace(".", "")
            else:
                original_price = product_price

            div = soup.find('div', class_='button_check_stock_card')
            if div:
                b = div.find("b").text.strip()
                if b[0] != '0':
                    product_status = 'Còn hàng'
                else:
                    product_status = 'Hết hàng'
            else:
                product_status = None
        else:
            product_name = None

        print("hasaki go save")
        if product_name:
            item = self.create_item(link.id, brand_id, report_id, product_price, original_price, product_status,
                                    crawl_time, status, product_name, link.name)
        else:
            item = self.create_item_with_defaults(self=self, link_id=link.id, brand_id=brand_id, report_id=report_id,
                                                  crawl_time=crawl_time, link=link.link)
        yield item

    def watson(self, response):
        link = response.meta['link']
        xml_data = response.text
        root = ET.fromstring(xml_data)
        status_code = response.status
        status = self.get_status(status_code)
        try:
            product_name = self.check_null(f"{root.find('name').text}")
            product_price = self.check_null(f"{root.find('variantOptions/priceData/value').text}")
            total_quantity = self.check_null(f"{root.find('variantOptions/stock/stockLevel').text}")
            original_price = self.check_null(f"{root.find('elabPrice/value').text}")
            name_link = "https://www.watsons.vn/vi" + self.check_null(f"{root.find('variantOptions/url').text}")
        except AttributeError:
            product_price = None
            total_quantity = None
            original_price = None
            name_link = 'url not found'
        crawl_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        brand_id = link.brand_id

        print("watson go save" + link.name)
        if product_name and product_price and original_price:
            item = self.create_item(link.id, brand_id, report_id, product_price, original_price, total_quantity,
                                    crawl_time, status, product_name, name_link)
        else:
            item = self.create_item_with_defaults(self=self, link_id=link.id, brand_id=brand_id, report_id=report_id,
                                                  crawl_time=crawl_time, link=name_link)
        yield item

    def pharmacity(self, response):
        crawl_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        link = response.meta['link']
        data = response.json()
        products = data['data']['product']
        status_code = response.status
        status = self.get_status(status_code)
        name_link = "https://www.pharmacity.vn/" + link.name + ".html"

        product_name = None
        product_price = None
        total_quantity = None
        original_price = None
        product_status = None

        try:
            if products is not None:
                product_name = products['name']
                price = products['pricing']['priceRange']['start']['gross']['amount']
                total_quantity = products['variants'][0]['quantityAvailable']
                original_price = products['pricing']['priceRangeUndiscounted']['start']['gross']['amount']
                if price:
                    product_price = price
                else:
                    product_price = 0
                if total_quantity:
                    if total_quantity < 0:
                        product_status = 0
                    else:
                        product_status = total_quantity
        except KeyError:
            pass

        brand_id = link.brand_id
        print("pharma go save")
        if products:
            item = self.create_item(link.id, brand_id, report_id, product_price, original_price, product_status,
                                    crawl_time, status, product_name, name_link)
        else:
            item = self.create_item_with_defaults(self=self, link_id=link.id, brand_id=brand_id,
                                                  report_id=report_id, crawl_time=crawl_time, link=name_link)
        yield item

    def guardian(self, response):
        link = response.meta['link']
        status_code = response.status
        crawl_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if status_code == 200:
            status = self.get_status(status_code)
            html_content = response.body
            soup = BeautifulSoup(html_content, "html.parser")

            div_element_name = soup.find("div", class_="product-title")
            product_name = ''
            if div_element_name:
                product_name = div_element_name.find("h1").text.strip()

            span_element_price = soup.find("span", class_="pro-price")
            if span_element_price:
                product_price = span_element_price.text.strip().replace(",", "").replace("₫", "")
            else:
                product_price = 0
            div_original_price = soup.find("div", class_="product-price")
            original_price = 0

            if div_original_price:
                if div_original_price.find('del'):
                    get_price = div_original_price.find('del')
                    original_price = get_price.text.strip().replace(",", "").replace("₫", "")
                else:
                    original_price = product_price
            button_element = soup.find("button", class_="add-to-cartProduct")
            if button_element and button_element.has_attr("disabled"):
                product_status = "Hết hàng"
            else:
                product_status = "Còn hàng"
            brand_id = link.brand_id
            print("guardian go save")
        else:
            product_name = None
        print(original_price)
        if product_name:
            item = self.create_item(link.id, brand_id, report_id, product_price, original_price, product_status,
                                    crawl_time, status, product_name, link.name)
        else:
            print("flase")
            item = self.create_item_with_defaults(self=self, link_id=link.id, brand_id=brand_id, report_id=report_id,
                                                  crawl_time=crawl_time, link=link.link)
        yield item
