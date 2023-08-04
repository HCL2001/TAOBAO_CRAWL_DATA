class ModelDAO:
    def __init__(self, brand_id, report_id, success, failure, total, start_crawl, end_crawl):
        self.brand_id = brand_id
        self.report_id = report_id
        self.success = success
        self.failure = failure
        self.total = total
        self.start_crawl = start_crawl
        self.end_crawl = end_crawl

    def set_brand_id(self, value):
        self.brand_id = value

    def set_report_id(self, value):
        self.report_id = value

    def set_success(self, value):
        self.success = value

    def set_fail(self, value):
        self.fail = value

    def set_total(self, value):
        self.total = value

    def set_start_crawl(self, value):
        self.start_crawl = value

    def set_end_crawl(self, value):
        self.end_crawl = value

