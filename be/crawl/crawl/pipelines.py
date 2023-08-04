import mysql.connector


class MySQLPipeline:
    def __init__(self, mysql_host, mysql_port, mysql_user, mysql_password, mysql_database):
        self.connection = None
        self.mysql_host = mysql_host
        self.mysql_port = mysql_port
        self.mysql_user = mysql_user
        self.mysql_password = mysql_password
        self.mysql_database = mysql_database

    @classmethod
    def from_crawler(cls, crawler):
        mysql_host = crawler.settings.get('MYSQL_HOST')
        mysql_port = crawler.settings.get('MYSQL_PORT')
        mysql_user = crawler.settings.get('MYSQL_USER')
        mysql_password = crawler.settings.get('MYSQL_PASSWORD')
        mysql_database = crawler.settings.get('MYSQL_DATABASE')

        return cls(mysql_host, mysql_port, mysql_user, mysql_password, mysql_database)

    def open_spider(self, spider):
        self.connection = mysql.connector.connect(
            host=self.mysql_host,
            port=self.mysql_port,
            user=self.mysql_user,
            password=self.mysql_password,
            database=self.mysql_database
        )

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        try:
            print("success go db")
            cursor = self.connection.cursor()
            if item['table_name'] == 'product_list':
                query = f"INSERT INTO {item['table_name']} (" \
                        f"link_id, brand_id, report_id, price, " \
                        f"original_price, crawl_time, status, total, name, link) " \
                        f"VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                values = (item['link_id'], item['brand_id'], item['report_id'],
                          item['price'], item['original_price'], item['crawl_time'], item['status'], item['total'], item['name'], item['link'])
            if item['table_name'] == 'report':
                print("pass DB")
                query = f"INSERT INTO {item['table_name']} (" \
                        f"brand_id, report_id, success," \
                        f" failure, start_crawl, end_crawl) " \
                        f"VALUES (%s, %s, %s, %s, %s, %s)"
                values = (item['brand_id'], item['report_id'], item['success'], item['failure'], item['start_crawl'], item['end_crawl'])

            cursor.execute(query, values)
            self.connection.commit()
            print("save pass to database")
            return item
        except mysql.connector.Error as error:
            print("Lỗi kết nối cơ sở dữ liệu: {}".format(error))

