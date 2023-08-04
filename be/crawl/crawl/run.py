import os
import subprocess
import requests
import config


log_file_path = config.PATH_FILE_CRAWL + 'dateInfo.txt'
proxy_url = f"http://{config.PROXY_USER}:{config.PROXY_PASS}@{config.PROXY_IP}:{config.PROXY_PORT}"
link_check = "https://www.google.com/"
with open(log_file_path, 'a') as log_file:
    crawl_dir = config.PATH_FILE_CRAWL
    os.chdir(crawl_dir)

    spiders = [
        "megasop.py"
    ]
    for spider in spiders:
        try:
            response = requests.get(link_check, proxies={"http": proxy_url, "https": proxy_url})
            if response.status_code == 200:
                subprocess.call(["scrapy", "runspider", spider])
                log_file.write(spider + ' -------> success\n')
            else:
                log_file.write(spider + ' -------> false \n')
        except requests.exceptions.RequestException as e:
            print(f"Error occurred while checking proxy {proxy_url} for {spider}: {str(e)}")

