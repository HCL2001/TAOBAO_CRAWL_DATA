import asyncio
import time
import urllib.parse
import json
import aiohttp
from googletrans import Translator
import urllib.parse
from datetime import datetime
import models
import sys
import requests
import aiohttp
from bs4 import BeautifulSoup
from sqlalchemy.orm import Session
import database
import models
import constants

import requests
import ProductDetailDto


async def register():
    product_list = []
    headers = {
        'Cookie': 't=ec0d5bd680cef4c43c9f71708db31058; cna=BRxOHd8VWAICAXGhLjZWD5TR; xlly_s=1; sgcookie=E100H0swvfyYsdVvyTSCrnObIsrV9Aq5T474B8w3cwP5nWHOe6gtbUcYZOtKadjZUZn5FaAW%2BQ1uJQLhLtsuUfTrufcHNomxvIPXmNQua6gPTPE%3D; uc3=vt3=F8dCsGCl3JWCOZIAnLM%3D&id2=UUpgQEvyiTEr4C708g%3D%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D&nk2=F5RDLjqWCLCCNe6Q0ac%3D; lgc=tb627551502528; uc4=id4=0%40U2gqz6QY%2B2LU45CVgCnTHhyjjD3pXce2&nk4=0%40FY4I7WSY2SzxeSCD9wJSplBYHJHaEX%2BF0g%3D%3D; tracknick=tb627551502528; _cc_=WqG3DMC9EA%3D%3D; thw=xx; mt=ci=0_1; _uetsid=2e532be02f4f11ee80918f9d985d2979; _uetvid=dc870040ea5911ed8305a55f0f12c1b7; _m_h5_tk=bffc85d673ab2f3d0eebe9f130993d22_1690891184157; _m_h5_tk_enc=10d0b322cedd523f3f588213614f9e04; hng=VN%7Czh-CN%7CVNM%7C704; _gid=GA1.2.1343417350.1690881464; _ga=GA1.1.658097477.1690881463; _ga_YFVFB9JLVB=GS1.1.1690881463.1.0.1690881469.0.0.0; _ga_JBTWV3NHSY=GS1.1.1690881463.1.0.1690881469.54.0.0; cookie2=1c358ce26fd4234017e383ab667ef88d; _tb_token_=f60ee6eeeb3fe; tfstk=dEwBfWDMPeYQ2aHskBsa1qKLCcD7Oy6VF3i8mupe2vHdF0U45bpPtvlSFP3aL2rEpTi8uPG8z4rex544DpyFtYJSKYDRuZWV3MqnEYBC-c7VkXYd0C-O3tr3xHod0lBVrtfd4GGRnpx5Pl76Bd9ACFkQHiQ5PRiOxqEBJpobBDGikkeBnO5v3qs8BQtsiLisuGs6ZQfuLqHO.; l=fBIQOzNINiq0KRtBBO5Churza77O2COb8sPzaNbMiIEGa6Th1elM8NC61q3pRdtjQT5Y1etyzs0aOdhw5Ja38xOe7pP-OC0eQKp28eM3N7AN.; isg=BGhow2fRmMKnVLTcoTZoExvVOVZ6kcybJYC5NSKc4OPWfQnnyqPpKsX_dQ2NzYRz; x5sec=7b22617365727665723b32223a226137316262343934343964303833653439366131306266303238643831333839434b667a703659474550666873386175362b3461476738794d6a45324d6a41354d544d314d7a67774f7a4969436d4e6863484e736157526c646a49776b4b48466e76762f2f2f2f2f41554144227d',
        'Referer': 'https://item.taobao.com/item.htm?id=716819466729&ns=1&abbucket=12#detail',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Sec-Ch-Ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    }
    url = "https://item.taobao.com/item.htm?id=716819466729&ns=1&abbucket=12#detail"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        content = response.text
        soup = BeautifulSoup(content, "html.parser")
        li_elements_with_data_value = soup.find_all("li", attrs={"data-value": True})
        print(soup)
        listName = {}
        for li in li_elements_with_data_value:
            data_value = li["data-value"]
            value = li.span.text.strip()
            listName[data_value] = value
        script_tags = soup.find_all("script")
        for script_tag in script_tags:
            script_content = script_tag.string
            if script_content and "Hub.config.set" in script_content:
                start_index = script_content.find("wholeSibUrl      : '")
                end_index = script_content.find("tradeContract',")
                json_content = script_content[start_index + 20: end_index]
                detailLinkValue = "https:" + json_content
                print(detailLinkValue)
    # detailLink(url, detailLinkValue, listName)
    return product_list


#
def detailLink(link: str, linkDetail: str, list: list):
    product_list = []
    headers = {
        'Cookie': 't=ec0d5bd680cef4c43c9f71708db31058; cna=BRxOHd8VWAICAXGhLjZWD5TR; xlly_s=1; sgcookie=E100H0swvfyYsdVvyTSCrnObIsrV9Aq5T474B8w3cwP5nWHOe6gtbUcYZOtKadjZUZn5FaAW%2BQ1uJQLhLtsuUfTrufcHNomxvIPXmNQua6gPTPE%3D; uc3=vt3=F8dCsGCl3JWCOZIAnLM%3D&id2=UUpgQEvyiTEr4C708g%3D%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D&nk2=F5RDLjqWCLCCNe6Q0ac%3D; lgc=tb627551502528; uc4=id4=0%40U2gqz6QY%2B2LU45CVgCnTHhyjjD3pXce2&nk4=0%40FY4I7WSY2SzxeSCD9wJSplBYHJHaEX%2BF0g%3D%3D; tracknick=tb627551502528; _cc_=WqG3DMC9EA%3D%3D; ucn=center; thw=xx; mt=ci=0_1; _uetsid=2e532be02f4f11ee80918f9d985d2979; _uetvid=dc870040ea5911ed8305a55f0f12c1b7; _m_h5_tk=bffc85d673ab2f3d0eebe9f130993d22_1690891184157; _m_h5_tk_enc=10d0b322cedd523f3f588213614f9e04; hng=VN%7Czh-CN%7CVNM%7C704; _gid=GA1.2.1343417350.1690881464; _ga=GA1.1.658097477.1690881463; _ga_YFVFB9JLVB=GS1.1.1690881463.1.0.1690881469.0.0.0; _ga_JBTWV3NHSY=GS1.1.1690881463.1.0.1690881469.54.0.0; cookie2=1c358ce26fd4234017e383ab667ef88d; _tb_token_=f60ee6eeeb3fe; isg=BHx8j5M1NMarvgCAdVI0l2epTRoudSCfKWwtSVb672dKIR2rfoeFLsnQAVFZaVj3; l=fBIQOzNINiq0Kv4YBO5Churza77t5BOb8sPzaNbMiIEGa6Th1elM8NC61q3wRdtjQT5Ydetyzs0aOdhw5Ja38AkDBeYIOC0eQCvp-eM3N7AN.; tfstk=dbYJfsv4JxDkLhjpR_nm81N1H2GmiUdyMLR_-9XuAKpvECtlqB6hJppppTjIUaYpHLA6qgAB-6TdzExu-TDPJB9GJADiSVAyaZ7IIA2-zu1rNwb0fsqXaQ7FRS2IjnOP9zV8hGj8YlmIFPYMJ_iIAq7QGsqANgB6MqzQJYfaIOdSuPa6knIcQX8MW-q4IOC3VjhYYkS5gfxECqf..',
        'Referer': link,
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Sec-Ch-Ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'script',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }
    url = linkDetail
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        listPriceData = data['data']['originalPrice']
        listPrice = {}
        for key, value in listPriceData.items():
            listPrice[key.strip(';')] = value['price']
        del listPrice['def']
        listPromotionData = data['data']['promotion']['promoData']
        listPromotion = {}
        for key, value in listPromotionData.items():
            listPromotion[key.strip(';')] = value[0]['price']
        del listPromotion['def']
        count = 0;
        for key, value in list.items():
            objectProduct = {
                'id': count,
                'price': listPrice[key],
                'promotion': listPromotion[key],
                'name': value
            }
            product_list.append(objectProduct)
            count += 1;
        print(product_list)


async def crawl_taobao(keyWord: str):
    translator = Translator()
    product_list = []

    chinese_keyword = translator.translate(keyWord, src=constants.VIETNAMESE, dest=constants.CHINESE).text

    cookie_parameters = {
        'JSESSIONID': 'A5EA6A1FC6ED9491E8BFE168344D9E7C',
        '_cc_': 'VFC%2FuZ9ajQ%3D%3D',
        '_nk_': 'tb627551502528',
        '_samesite_flag_': 'true',
        '_tb_token_': 'ee73d9beb6709',
        'atpsida': 'c1ba942fb3fe1cbf03e466a6_1690536928_9',
        'aui': '2216209135380',
        '_tb_token_': '3e3868656177',
        'cancelledSubSites': 'empty',
        'cna': 'NVhKHQx8pxABASABDuD094HA',
        'cna': 'NVhKHQx8pxABASABDuD094HA',
        'cnaui': '2216209135380',
        'cookie1': 'AimSwy6Hu0cjkXBiNAEvUR5yUCjEb50QirZe9OQR8JM%3D',
        'cookie17': 'UUpgQEvyiTEr4C708g%3D%3D',
        'cookie2': '17baa001cddd95eeac0d14215754e2ba',
        'csg': 'c5ccb5b5',
        'dnk': 'tb627551502528',
        'existShop': 'MTY5MDUzNTUyMQ%3D%3D',
        'isg': 'BC4udLbkxtq_uDKu-9jGYYETf4TwL_Ipj4a_J1j3mTHsO86VwL6yOUI587_X4-pB',
        'l': 'fBIQOzNINiq0KI6SBOfZFurza779IIRAguPzaNbMi9fP911p5XodW1O06889CnMNFssBR38PiVPBBeYBqIv4n5U62j-la_HmnmOk-Wf..',
        'lgc': 'tb627551502528',
        'sca': '2ce1ff46',
        'sg': '807',
        'sgcookie': 'E1004mNHjdedFCalsA3%2BDwxBbDVzpPHNcfgCxQwpMn8WChT8qXmCxiXv2GtRWHqACR5GrqBtYgklE3nsJQ6iHc00COBH86rxO%2FnNB1FZN0UAlGA%3D',
        'skt': '5f59a84349d9041e',
        't': '6b6122a7cb9e97ce82d19b64b5cfa46b',
        'tbsa': '106e86f4144675054773332d_1690536928_9',
        'tfstk': 'd-N9HuZeMMjGzUMYGVBhgivTTP_hK5UNjlzWimmMhkELlDAc7fXqMonL0cDi1cAxMrE4moUV7qibcon0I9fu7PlqGgcAZ_4aQqlfq1ChKNaZgjsk-I6lwPrygXCFUn1fYdpww7Fx5t_FmoxTl5gtBmpivIdfoVHtVPidVg6a47VJxp-o2qv1Jwp23AgFr-S5t',
        'tracknick': 'tb627551502528',
        'uc1': 'cookie21=Vq8l%2BKCLiYYu&cookie14=Uoe9bfibByxgsA%3D%3D&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&existShop=false&pas=0&cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D',
        'uc3': 'nk2=F5RDLjqWCLCCNe6Q0ac%3D&vt3=F8dCsGCg2j4K6APJSMg%3D&lg2=UIHiLt3xD8xYTw%3D%3D&id2=UUpgQEvyiTEr4C708g%3D%3D',
        'uc4': 'id4=0%40U2gqz6QY%2B2LU45CVgCnTHhyjgZBJlJ9d&nk4=0%40FY4I7WSY2SzxeSCD9wJSplBYHJwWmW5zVQ%3D%3D',
        'x5sec': '7b22617365727665723b32223a226539313338386538643739643266303964613031653838663861323366623766434f4b4d6a71594745506e57343658446c59476b65786f504d6a49784e6a49774f54457a4e544d344d4473324d4f79586a4e4d4451414d3d227d',
        'xlly_s': '1',
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    encoded_keyWord = urllib.parse.quote(chinese_keyword, safe='')
    print(encoded_keyWord)
    url = f"https://s.taobao.com/search?q={encoded_keyWord}&type=p&tmhkh5=&from=sea_1_searchbutton&catId=100&spm=a2141.241046-vn.searchbar.d_2_searchbox"
    counter = 1
    # saveSearch = []
    # links = db.query(models.SearchProduct).all()
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, cookies=cookie_parameters) as resp:
            content = await resp.text()
            soup = BeautifulSoup(content, "html.parser")
            script_tags = soup.find_all("script")
        for script_tag in script_tags:
            script_content = script_tag.string
            if script_content and "g_page_config" in script_content:
                start_index = script_content.find("g_page_config =")
                end_index = script_content.find("}};")
                json_content = script_content[start_index + 15: end_index + 2]
                try:
                    g_page_config_json = json.loads(json_content)
                    data = g_page_config_json['mods']['itemlist']['data']['auctions']
                    for item in data:
                        # print(item)
                        sys.stdout.flush()

                        name = translator.translate(item['raw_title'], src=constants.CHINESE, dest=constants.VIETNAMESE)
                        shopName = translator.translate(item['shopName'], src=constants.CHINESE, dest=constants.VIETNAMESE).text
                        link = 'https:' + item['detail_url']
                        if 'click.simba.taobao' in link:
                            print(f"Ignoring item '{name}' as it contains 'click.taobao' link.")
                            continue

                        objectDto = {
                            'id': counter,
                            'productId': item['nid'],
                            'name': name.text,
                            'link': link,
                            'price': item['view_price'],
                            'image': 'https:' + item['pic_url'],
                            'shopName': shopName,
                        }
                        counter += 1
                        product_list.append(objectDto)
                        if counter == 6:  # Số sản phẩm cần search -1
                            break
                    save_list_data_to_db(product_list)
                except json.JSONDecodeError as e:
                    print(e)
    return product_list


def get_token(db: Session, token: str):
    try:
        result = db.query(models.Account).filter(models.Account.token == token)
        return result
    except Exception as e:
        return {
            'status': 'failed',
            'message': str(e)
        }
    finally:
        db.close()


def check_if_record_exists(session, name):
    return session.query(models.SearchProduct).filter_by(name=name).first() is not None


def error_handler(error):
    print(f"An error occurred: {error}")


def save_list_data_to_db(list_data, error_callback=None):
    session = database.SessionLocal()

    if session == "" or session == None:
        return "Session is null"

    try:
        for item in list_data:
            name = item['name']
            link = item['link']
            if "click.taobao" in link:
                print(f"Ignoring item '{name}' as it contains 'click.taobao' link.")
                continue

            if not check_if_record_exists(session, name):
                product = models.SearchProduct(product_id=item['productId'],
                                               name=name,
                                               price=item['price'],
                                               link=link,
                                               image=item['image'],
                                               shop_name=item['shopName'])
                session.add(product)
        session.commit()
        print("Data saved successfully.")
    except Exception as e:
        session.rollback()
        if error_callback is not None and callable(error_callback):
            error_callback(e)
        else:
            print(f"An error occurred: {e}")
    finally:
        session.close()


def get_data_from_db(page_number=1, items_per_page=10):
    session = database.SessionLocal()

    if session == None or session == "":
        return "Session is null"

    try:
        # Calculate the offset based on the page number and items per page
        offset = (page_number - 1) * items_per_page

        # Query the database to get a specific page of data
        data = session.query(models.SearchProduct).limit(items_per_page).offset(offset).all()

        return data
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Having error when getting data"
    finally:
        session.close()

def check_username_exists(db: Session, username: str) -> bool:
    return db.query(models.Account).filter(models.Account.username == username).first() is not None

def get_account_by_username(db: Session, username: str):
    try:
        account = db.query(models.Account).filter(models.Account.username == username).first()
        return account
    except Exception as e:
        return None
    finally:
        db.close()


def detail():
    product_list = []
    cookie_parameters = {
        'JSESSIONID': 'A5EA6A1FC6ED9491E8BFE168344D9E7C',
        '_cc_': 'VFC%2FuZ9ajQ%3D%3D',
        '_nk_': 'tb627551502528',
        '_samesite_flag_': 'true',
        '_tb_token_': 'ee73d9beb6709',
        'atpsida': 'c1ba942fb3fe1cbf03e466a6_1690536928_9',
        'aui': '2216209135380',
        '_tb_token_': '3e3868656177',
        'cancelledSubSites': 'empty',
        'cna': 'NVhKHQx8pxABASABDuD094HA',
        'cna': 'NVhKHQx8pxABASABDuD094HA',
        'cnaui': '2216209135380',
        'cookie1': 'AimSwy6Hu0cjkXBiNAEvUR5yUCjEb50QirZe9OQR8JM%3D',
        'cookie17': 'UUpgQEvyiTEr4C708g%3D%3D',
        'cookie2': '17baa001cddd95eeac0d14215754e2ba',
        'csg': 'c5ccb5b5',
        'dnk': 'tb627551502528',
        'existShop': 'MTY5MDUzNTUyMQ%3D%3D',
        'isg': 'BC4udLbkxtq_uDKu-9jGYYETf4TwL_Ipj4a_J1j3mTHsO86VwL6yOUI587_X4-pB',
        'l': 'fBIQOzNINiq0KI6SBOfZFurza779IIRAguPzaNbMi9fP911p5XodW1O06889CnMNFssBR38PiVPBBeYBqIv4n5U62j-la_HmnmOk-Wf..',
        'lgc': 'tb627551502528',
        'sca': '2ce1ff46',
        'sg': '807',
        'sgcookie': 'E1004mNHjdedFCalsA3%2BDwxBbDVzpPHNcfgCxQwpMn8WChT8qXmCxiXv2GtRWHqACR5GrqBtYgklE3nsJQ6iHc00COBH86rxO%2FnNB1FZN0UAlGA%3D',
        'skt': '5f59a84349d9041e',
        't': '6b6122a7cb9e97ce82d19b64b5cfa46b',
        'tbsa': '106e86f4144675054773332d_1690536928_9',
        'tfstk': 'd-N9HuZeMMjGzUMYGVBhgivTTP_hK5UNjlzWimmMhkELlDAc7fXqMonL0cDi1cAxMrE4moUV7qibcon0I9fu7PlqGgcAZ_4aQqlfq1ChKNaZgjsk-I6lwPrygXCFUn1fYdpww7Fx5t_FmoxTl5gtBmpivIdfoVHtVPidVg6a47VJxp-o2qv1Jwp23AgFr-S5t',
        'tracknick': 'tb627551502528',
        'uc1': 'cookie21=Vq8l%2BKCLiYYu&cookie14=Uoe9bfibByxgsA%3D%3D&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&existShop=false&pas=0&cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D',
        'uc3': 'nk2=F5RDLjqWCLCCNe6Q0ac%3D&vt3=F8dCsGCg2j4K6APJSMg%3D&lg2=UIHiLt3xD8xYTw%3D%3D&id2=UUpgQEvyiTEr4C708g%3D%3D',
        'uc4': 'id4=0%40U2gqz6QY%2B2LU45CVgCnTHhyjgZBJlJ9d&nk4=0%40FY4I7WSY2SzxeSCD9wJSplBYHJwWmW5zVQ%3D%3D',
        'x5sec': '7b22617365727665723b32223a226539313338386538643739643266303964613031653838663861323366623766434f4b4d6a71594745506e57343658446c59476b65786f504d6a49784e6a49774f54457a4e544d344d4473324d4f79586a4e4d4451414d3d227d',
        'xlly_s': '1',
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; Trident/7.0; AS; rv:11.0) like Gecko'
    }
    url = "https://item.taobao.com/item.htm?id=690907579222&ns=1&abbucket=12#detail"

    response = requests.get(url, headers=headers, cookies=cookie_parameters)
    if response.status_code != 200:
        return "Fail when getting value"
    content = response.text
    soup = BeautifulSoup(content, "html.parser")
    li_elements_with_data_value = soup.find_all("li", attrs={"data-value": True})
    print(soup)
    listName = {}
    for li in li_elements_with_data_value:
        data_value = li["data-value"]
        value = li.span.text.strip()
        listName[data_value] = value
    script_tags = soup.find_all("script")
    for script_tag in script_tags:
        script_content = script_tag.string
        if script_content and "Hub.config.set" in script_content:
            start_index = script_content.find("wholeSibUrl      : '")
            end_index = script_content.find("tradeContract',")
            json_content = script_content[start_index + 20: end_index]
            detailLinkValue = "https:" + json_content
            print(detailLinkValue)
    # detailLink(url, detailLinkValue, listName)
    return product_list


def detailValue(link: str, linkDetail: str, list: list):
    product_list = []
    headers = {
        'Cookie': 't=ec0d5bd680cef4c43c9f71708db31058; cna=BRxOHd8VWAICAXGhLjZWD5TR; xlly_s=1; sgcookie=E100H0swvfyYsdVvyTSCrnObIsrV9Aq5T474B8w3cwP5nWHOe6gtbUcYZOtKadjZUZn5FaAW%2BQ1uJQLhLtsuUfTrufcHNomxvIPXmNQua6gPTPE%3D; uc3=vt3=F8dCsGCl3JWCOZIAnLM%3D&id2=UUpgQEvyiTEr4C708g%3D%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D&nk2=F5RDLjqWCLCCNe6Q0ac%3D; lgc=tb627551502528; uc4=id4=0%40U2gqz6QY%2B2LU45CVgCnTHhyjjD3pXce2&nk4=0%40FY4I7WSY2SzxeSCD9wJSplBYHJHaEX%2BF0g%3D%3D; tracknick=tb627551502528; _cc_=WqG3DMC9EA%3D%3D; ucn=center; thw=xx; mt=ci=0_1; _uetsid=2e532be02f4f11ee80918f9d985d2979; _uetvid=dc870040ea5911ed8305a55f0f12c1b7; _m_h5_tk=bffc85d673ab2f3d0eebe9f130993d22_1690891184157; _m_h5_tk_enc=10d0b322cedd523f3f588213614f9e04; hng=VN%7Czh-CN%7CVNM%7C704; _gid=GA1.2.1343417350.1690881464; _ga=GA1.1.658097477.1690881463; _ga_YFVFB9JLVB=GS1.1.1690881463.1.0.1690881469.0.0.0; _ga_JBTWV3NHSY=GS1.1.1690881463.1.0.1690881469.54.0.0; cookie2=1c358ce26fd4234017e383ab667ef88d; _tb_token_=f60ee6eeeb3fe; isg=BHx8j5M1NMarvgCAdVI0l2epTRoudSCfKWwtSVb672dKIR2rfoeFLsnQAVFZaVj3; l=fBIQOzNINiq0Kv4YBO5Churza77t5BOb8sPzaNbMiIEGa6Th1elM8NC61q3wRdtjQT5Ydetyzs0aOdhw5Ja38AkDBeYIOC0eQCvp-eM3N7AN.; tfstk=dbYJfsv4JxDkLhjpR_nm81N1H2GmiUdyMLR_-9XuAKpvECtlqB6hJppppTjIUaYpHLA6qgAB-6TdzExu-TDPJB9GJADiSVAyaZ7IIA2-zu1rNwb0fsqXaQ7FRS2IjnOP9zV8hGj8YlmIFPYMJ_iIAq7QGsqANgB6MqzQJYfaIOdSuPa6knIcQX8MW-q4IOC3VjhYYkS5gfxECqf..',
        'Referer': link,
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Sec-Ch-Ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'script',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }
    url = linkDetail
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        listPriceData = data['data']['originalPrice']
        listPrice = {}
        for key, value in listPriceData.items():
            listPrice[key.strip(';')] = value['price']
        del listPrice['def']
        listPromotionData = data['data']['promotion']['promoData']
        listPromotion = {}
        for key, value in listPromotionData.items():
            listPromotion[key.strip(';')] = value[0]['price']
        del listPromotion['def']
        count = 0
        for key, value in list.items():
            objectProduct = {
                'id': count,
                'price': listPrice[key],
                'promotion': listPromotion[key],
                'name': value
            }
            product_list.append(objectProduct)
            count += 1;
        print(product_list)


def demo_function():
    translator = Translator()
    product_data = {
        "code": 200,
        "msg": "success",
        "data": {
            "item_id": 690907579222,
            "product_url": "https://item.taobao.com/item.htm?id=690907579222",
            "title": "纯种英短蓝猫活体蓝白猫幼崽矮脚猫小猫咪活物宠物猫咪英国短毛猫",
            "main_imgs": [
                "https://gd1.alicdn.com/imgextra/i4/2206570330851/O1CN01RnAEkF1I9nqGOJS1K_!!2206570330851.jpg",
                "https://gd1.alicdn.com/imgextra/i1/2206570330851/O1CN011siQez1I9nqEBQys1_!!2206570330851.jpg",
                "https://gd4.alicdn.com/imgextra/i4/2206570330851/O1CN01iyzWFb1I9nqL8mOaO_!!2206570330851.jpg",
                "https://gd3.alicdn.com/imgextra/i3/2206570330851/O1CN01ftjgnv1I9nqJH5DTQ_!!2206570330851.png",
                "https://gd3.alicdn.com/imgextra/i3/2206570330851/O1CN01PiJNO51I9nq9ownmv_!!2206570330851.jpg"
            ],
            "video_url": "http://cloud.video.taobao.com/play/u/p/1/e/6/t/1/383191028173.mp4",
            "currency": "CNY",
            "price_info": {
                "price": "800.0",
                "origin_price": "800.0"
            },
            "comment_count": "null",
            "category_id": 50016383,
            "root_category_id": "null",
            "product_props": [
                {
                    "品牌": "宝贝它"
                },
                {
                    "动物性别": "公 母"
                },
                {
                    "宠物毛长": "短毛"
                },
                {
                    "颜色分类": "蓝色"
                },
                {
                    "猫咪品种": "俄罗斯蓝猫"
                },
                {
                    "血统信息": "有血统证书"
                },
                {
                    "免疫驱虫": "已做完"
                },
                {
                    "宠物年龄": "幼年猫(12月以下)"
                },
                {
                    "卖家资质分类": "猫舍"
                }
            ],
            "delivery_info": {
                "area_from": [
                    "广东省",
                    "深圳市"
                ],
                "area_id": "",
                "postage": "0"
            },
            "shop_info": {
                "shop_id": 260638490,
                "seller_id": 2206570330851,
                "shop_name": "喵爪爪萌宠生活馆",
                "shop_url": "https://shop260638490.taobao.com",
                "shop_logo": "",
                "shop_rate": [
                    {
                        "title": "宝贝描述",
                        "type": "desc",
                        "score": 4.53036
                    },
                    {
                        "title": "卖家服务",
                        "type": "serv",
                        "score": 4.54464
                    },
                    {
                        "title": "物流服务",
                        "type": "post",
                        "score": 4.54643
                    }
                ],
                "shop_start_time": "null",
                "good_rate_percentage": "null",
                "followers": "null",
                "is_tmall": "false",
                "wangwang": "https://amos.alicdn.com/getcid.aw?groupid=0&s=1&Co1NDI&charset=utf-8&uid=tb469223107&site=cntaobao&Qxv3ba"
            },
            "sku_props": [
                {
                    "pid": "21241",
                    "prop_name": "动物性别",
                    "values": [
                        {
                            "vid": "3873886",
                            "name": "公",
                            "imageUrl": "null"
                        },
                        {
                            "vid": "9999473",
                            "name": "母",
                            "imageUrl": "null"
                        }
                    ]
                },
                {
                    "pid": "1627207",
                    "prop_name": "颜色分类",
                    "values": [
                        {
                            "vid": "28338",
                            "name": "蓝色",
                            "imageUrl": "null"
                        }
                    ]
                },
                {
                    "pid": "122276097",
                    "prop_name": "宠物年龄",
                    "values": [
                        {
                            "vid": "493262420",
                            "name": "幼年猫(12月以下)",
                            "imageUrl": "null"
                        }
                    ]
                }
            ],
            "skus": [
                {
                    "skuid": "4908202864795",
                    "sale_price": "800.0",
                    "origin_price": "1500.0",
                    "stock": 200,
                    "props_ids": "21241:3873886;1627207:28338;122276097:493262420",
                    "props_names": "动物性别:公;颜色分类:蓝色;宠物年龄:幼年猫(12月以下)",
                    "sub_price": "null",
                    "sub_price_type": "discounted price"
                },
                {
                    "skuid": "4908202864796",
                    "sale_price": "800.0",
                    "origin_price": "1500.0",
                    "stock": 200,
                    "props_ids": "21241:9999473;1627207:28338;122276097:493262420",
                    "props_names": "动物性别:母;颜色分类:蓝色;宠物年龄:幼年猫(12月以下)",
                    "sub_price": "null",
                    "sub_price_type": "discounted price"
                }
            ],
            "extra": "False"
        }
    }

    url = "http://api.tmapi.top/taobao/item_detail"

    querystring = {"apiToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VybmFtZSI6Imxvbmdob2FuZzA5MTFWTiIsIkNvbWlkIjpudWxsLCJSb2xlaWQiOm51bGwsImlzcyI6InRtYXBpIiwic3ViIjoibG9uZ2hvYW5nMDkxMVZOIiwiYXVkIjpbIiJdfQ.Nh5V5JaZlWP7lbGv_vNbANGRY1GUERGOWq0vE6lSTV8", "item_id": 714246212072}

    response = requests.get(url, params=querystring)

    if response.status_code != 200:
        print(response.status_code)
        return "Out of session"

    data = response.json()

    # Extract relevant data from the JSON response
    title = translator.translate(data["data"]["title"], src=constants.CHINESE, dest=constants.VIETNAMESE).text
    product_url = data["data"]["product_url"]
    main_imgs = data["data"]["main_imgs"]
    product_props = data["data"].get("product_props", [])
    sku_props = data["data"].get("sku_props", [])
    skus = data["data"].get("skus", [])

    # Translate the elements in product_props list
    translated_product_props = [translate_text(prop, constants.VIETNAMESE) for prop in product_props]

    # Translate the elements in sku_props list
    translated_sku_props = [translate_text(prop, constants.VIETNAMESE) for prop in sku_props]

    translated_skus = []

    for sku in skus:
        translated_sku = sku.copy()  # Create a copy of the original sku
        if "props_names" in sku:
            props_names = sku["props_names"]
            translated_props = []
            props_list = props_names.split(';')
            for prop in props_list:
                translated_prop = translate_text(prop, constants.VIETNAMESE)
                translated_props.append(translated_prop)
            translated_sku["props_names"] = ';'.join(translated_props)
        translated_skus.append(translated_sku)


    # Create the ProductDto object
    product_dto = ProductDetailDto.ProductDto(title, product_url, main_imgs, translated_product_props, translated_sku_props, translated_skus)



    # Access the data
    # print(product_dto.get_title())
    # print(product_dto.get_main_imgs())
    # print(product_dto.get_product_props())
    # print(product_dto.get_sku_props())
    # print(product_dto.get_skus())

    return product_dto


def translate_text(text, target_language):
    translator = Translator()
    # Replace this with your actual translation API call
    # This function should return the translated text
    translated_text = translator.translate(str(text), src=constants.CHINESE, dest=target_language).text
    return translated_text

def patternForDetail():

    global detail_link_value
    html = '''<!DOCTYPE html>

<html><!-- cph -->
<head>
<meta content="IE=edge" http-equiv="X-UA-Compatible"/>
<meta charset="utf-8"/>
<meta content="telephone=no, address=no" name="format-detection"/>
<link href="//g.alicdn.com" rel="dns-prefetch"/>
<link href="//gtms01.alicdn.com" rel="dns-prefetch"/>
<link href="//gtms02.alicdn.com" rel="dns-prefetch"/>
<link href="//gtms03.alicdn.com" rel="dns-prefetch"/>
<link href="//gtms04.alicdn.com" rel="dns-prefetch"/>
<link href="//gd1.alicdn.com" rel="dns-prefetch"/>
<link href="//gd2.alicdn.com" rel="dns-prefetch"/>
<link href="//gd3.alicdn.com" rel="dns-prefetch"/>
<link href="//gd4.alicdn.com" rel="dns-prefetch"/>
<link href="https://item.taobao.com/item.htm?id=690907579222" rel="canonical">
<link href="https://www.taobao.com/list/item-amp/690907579222.htm" hreflang="zh-Hans" rel="amphtml">
<link href="https://world.taobao.com/item/690907579222.htm" hreflang="zh-Hant" rel="alternate">
<meta content="webkit" name="renderer">
<meta content="always" name="referrer"/>
<meta content="欢迎前来淘宝网实力旺铺，选购纯种英短蓝猫活体蓝白猫幼崽矮脚猫小猫咪活物宠物猫咪英国短毛猫,想了解更多纯种英短蓝猫活体蓝白猫幼崽矮脚猫小猫咪活物宠物猫咪英国短毛，请进入实力旺铺，更多商品任你选购" name="description">
<meta content="淘宝,掏宝,网上购物,店铺, 纯种英短蓝猫活体蓝白猫幼崽矮脚猫小猫咪活物宠物猫咪英国短毛猫." name="keywords"/>
<meta content="2013" name="data-spm"/>
<meta content="pageId=1842749132;prototypeId=2;siteId=4;shopId=260638490;userid=2206570330851;" name="microscope-data"/>
<title>纯种英短蓝猫活体蓝白猫幼崽矮脚猫小猫咪活物宠物猫咪英国短毛猫-淘宝网</title>
<link href="//img.alicdn.com/favicon.ico" rel="shortcut icon" type="image/x-icon"><link href="//g.alicdn.com/??kg/global-util/1.0.5/index-min.css,kg/tb-gnav/1.0.5/index-min.css" rel="stylesheet"/>
<link href="//g.alicdn.com/tb/??item-detail/8.0.39/index-min.css" rel="stylesheet">
<script>
    var g_config = {
        startTime        : +new Date,
        ver              : '8.0.39',
        st               : '',
        online           : true,
        shopVer          : 2,
        appId            : 1 ,
        itemId           : '690907579222',

        shopId           : '260638490',
        shopName         : '\u55B5\u722A\u722A\u840C\u5BA0\u751F\u6D3B\u9986',
        sellerId         : '2206570330851',
        sellerNick       : 'tb469223107',
        sibUrl           : '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=690907579222&sellerId=2206570330851&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,activity,fqg,zjys,couponActivity,soldQuantity,page,originalPrice,tradeContract',
        descUrl          : location.protocol==='http:' ? '//itemcdn.tmall.com/desc/icoss!0690907579222!12316997544?var=desc' : '//itemcdn.tmall.com/desc/icoss!0690907579222!12316997544?var=desc',
        counterApi       : '//count.taobao.com/counter3?inc=ICVT_7_690907579222&sign=8906182cddc85f3b1df4c7f6ee2d67d80c4d9&keys=DFX_200_1_690907579222,ICVT_7_690907579222,ICCP_1_690907579222,SCCP_2_260638490',
        rateCounterApi   : '//rate.taobao.com/detailCount.do?itemId=690907579222',
        areaPrice        : false,

        lazyload         : '#J_DivItemDesc',

        tadComponetCdn   : true,
        delayInsurance   : false,
        fuwubao          : false,

        cdn              : true,
        sibFirst         : true,

        webp             : true,
        descWebP         : false,

        newDomain        : true,
        asyncStock       : true,
        enable           : true,

        m_ratio          : 20,

        beacon           : {},
        DyBase           : {
            iurl : '//item.taobao.com',
            purl : '//paimai.taobao.com',
            durl : '//siteadmin.taobao.com',
            lgurl: 'https://login.taobao.com/member/login.jhtml',
            surl : '//upload.taobao.com',
            suitUrl: '//jubao.taobao.com/index.htm?&spm=a1z6q.7847058&itemId='
        },
        idata            : {
            item: {
                id               : '690907579222',
                title            : '\u7EAF\u79CD\u82F1\u77ED\u84DD\u732B\u6D3B\u4F53\u84DD\u767D\u732B\u5E7C\u5D3D\u77EE\u811A\u732B\u5C0F\u732B\u54AA\u6D3B\u7269\u5BA0\u7269\u732B\u54AA\u82F1\u56FD\u77ED\u6BDB\u732B',
                pic              : '//gd4.alicdn.com/imgextra/i4/2206570330851/O1CN01RnAEkF1I9nqGOJS1K_!!2206570330851.jpg',
                price            : '',
                status           : 0,
                descVersion      : '',
                sellerNick       : 'tb469223107',
                sellerNickGBK    : 'tb469223107',
                skuComponentFirst: 'true',

                rcid             : '29',
                cid              : '50016383',
                virtQuantity     : '',
                holdQuantity     : '',

                quickAdd         : 1,

                edit             : true,

                initSizeJs:false,
                auto: '',

                bnow             : true,
                chong: false,

                dbst             : 1667055353000,
                stepdata         : {

                },
                xjcc: false,

                type             : '',
                customHeader     : false,

                disableAddToCart  : !true,

                auctionImages    : ["//gd3.alicdn.com/imgextra/i4/2206570330851/O1CN01RnAEkF1I9nqGOJS1K_!!2206570330851.jpg","//gd1.alicdn.com/imgextra/i1/2206570330851/O1C
N011siQez1I9nqEBQys1_!!2206570330851.jpg","//gd4.alicdn.com/imgextra/i4/2206570330851/O1CN01iyzWFb1I9nqL8mOaO_!!2206570330851.jpg","//gd3.alicdn.com/imgextra/i3/2206570330851/O1CN01ftjgnv1I9nqJH5DTQ_!!2206570330851.png","//gd3.alicdn.com/imgextra/i3/2206570330851/O1CN01PiJNO51I9nq9ownmv_!!2206570330851.jpg"]

            },
            seller: {
                id          : '2206570330851',
                mode        : 0,
                shopAge     : '-1'
                ,status      : 0
            },
            shop  : {

                id  : '260638490',
                url : '//shop260638490.taobao.com/'

                ,pid: 1842749132

                ,sid: 4

                ,xshop: true

                ,instId: 588278817


            }
        },
        vdata :{
        }

    };


    g_config.tadInfo = {};

    g_config.favoriteVersion = "1.1.1";


    g_config.hasContract = true;


    g_config.showBuyerDetail = true;


</script>
<script>
    function onSibRequestSuccess(res){g_config.sibRequest = {success: true, data: res&&res.data}}
        (function() {
            var getScript = function(f,c){var e=document,d=e.createElement("script");d.src=f;if(c){for(var b in c){d[b]=c[b];}};e.getElementsByTagName("head")[0].appendChild(d)};
            var sibUrl= g_config.sibUrl;sibUrl+="&callback=onSibRequestSuccess";
            var key=(function(){var params=location.search.substr(1).split("&");for(var i=0;i<params.length;i++){if(params[i].indexOf("key=")===0){return params[i]}}})();key&&(sibUrl+=("&"+key));
            if(!g_config.sibRequest){getScript(sibUrl,{onerror:function(){g_config.sibRequest={success: false}}})};
            getScript(g_config.descUrl);
        })();
</script>
</link></link></meta></meta></link></link></link></head>
<body class="tab-active-index-0 tb-detail" data-spm="1"><script>
with(document)with(body)with(insertBefore(createElement("script"),firstChild))setAttribute("exparams","category=item%5f50016383&userid=&at_isb=0&at_autype=5%5f260638490&apl
us&udpid=UUpgQEvyiTEr4C708g%253D%253D&at_alis=1%5f2206570330851&&yunid=&3e3868656177&trid=3dae2b2916915495213792429e&asid=AQAAAABU/9Jkk9VcKAAAAAAo7OK5aONCpQ==&sidx=CoDSe+R+
PrMPgwbrCAU1cAjowVeInU+Cop67IfXUpj80B4lre+9RZZZx5/U3EQGTnknIQ3UhVfLRTaODuFCMZA6KR/JcxomOeFJMWwHs9pkerVC8xa0UkIrpynGm7Fme9TYuJSmsx2B3z54WDS9+5JSNnvTbzJsr4kW71WxmPek=",id="tb-beacon-aplus",src=(location>"https"?"//g":"//g")+".alicdn.com/alilog/mlog/aplus_v2.js")
</script><script>
if(!g_config.vdata){g_config.vdata={};}
g_config.vdata.viewer={"id":"", "ct":"6b6122a7cb9e97ce82d19b64b5cfa46b", "tnik":unescape(unescape("tb627551502528"))};
g_config.vdata.sys={"now":1691549524000};
</script>
<script>if(g_config.vdata && g_config.vdata.sys){g_config.vdata.sys.toggle={"p":1.0,"globalHeadUpdate":true,"dcP":"true","favoriteVersion":"1.1.1","thumb":false,"descWebP":false,"seoDetail":true,"webp":true,"m_ratio":20,"asyncStock":true};}</script>
<div class="site-nav" data-component-config='{ "cart": "0.0.6","message": "3.4.6","umpp": "1.5.4","mini-login": "6.3.8","tb-ie-updater": "0.0.4","tbar": "2.1.0","tb-footer": "1.1.8","sidebar": "1.0.10" }' id="J_SiteNav">
<div class="site-nav-bd" id="J_SiteNavBd"></div>
</div>
<!--[if lt IE 8]>
<style>html{overflow-y:hidden}</style>
<div class="tb-ie-updater-layer" id="J_IEUpdaterLayer"></div>
<div class="tb-ie-updater-box" data-spm="20161112" id="J_IEUpdaterBox">
  <a href="https://www.google.cn/intl/zh-CN/chrome/browser/desktop/" class="tb-ie-updater-google" target="_blank" data-spm-click="gostr=/tbieupdate;locaid=d1;name=google"> 璋锋瓕 Chrome</a>
  <a href="http://www.uc.cn/ucbrowser/download/" class="tb-ie-updater-uc" target="_blank" data-spm-click="gostr=/tbieupdate20161112;locaid=d2;name=uc">UC 娴忚鍣 /a>"      
  <a class="tb-ie-updater-close" href="#" onclick="document.getElementById('J_IEUpdaterLayer').style.display='none';document.getElementById('J_IEUpdaterBox').style.display='none';document.documentElement.style.overflow='auto';return false">x</a>
</div>
<![endif]-->
<div id="J_Header"></div>
<form action="//buy.taobao.com/auction/buy_now.jhtml" id="J_FrmBid" method="post" name="bidForm">
<input name="onekey" type="hidden" value=""/>
<input name="gmtCreate" type="hidden" value=""/>
<input name="checkCodeIds" type="hidden" value=""/>
<input name="secStrNoCCode" type="hidden" value=""/>
<input id="J_frmTokenField" name="tb_token" type="hidden" value=""/>
<input id="J_ireferer" name="item_url_refer" type="hidden" value=""/>
<input name="item_id" type="hidden" value="690907579222"/>
<input name="item_id_num" type="hidden" value="690907579222"/>
<input name="auction_type" type="hidden" value="b"/>
<input name="from" type="hidden" value="item_detail"/>
<input id="J_From" name="frm" type="hidden" value=""/>
<input name="current_price" type="hidden" value="1500.00"/>
<input name="auto_post1" type="hidden" value=""/>
<input id="quantity" name="quantity" type="hidden" value="1"/>
<input id="skuId" name="skuId" type="hidden" value=""/>
<input id="skuInfo" name="skuInfo" type="hidden" value=""/>
<input id="J_TBuyerFrom" name="buyer_from" type="hidden" value=""/>
<input id="J_ChargeTypeId" name="chargeTypeId" type="hidden" value=""/>
<!-- FIXME 外店已经不支持

            -->
</form>
<input id="J_TokenField" name="tb_token" type="hidden" value=""/>
<div id="page">
<div id="content">
<p class="design-page" id="J_dcpg" style="display:none;"></p>
<div class="J_AsyncDC" data-type="css"></div><div class="J_AsyncDC tb-async-head tb-shop" data-type="head" id="J_DcHead"></div>
<div id="bd">
<div id="detail">
<div class="tb-detail-bd tb-clear">
<div class="tb-summary tb-clear">
<div class="tb-item-info tb-clear">
<div class="tb-item-info-l">
<div class="tb-gallery">
<div class="tb-booth tb-pic tb-main-pic">
<a href="//www.taobao.com/view_image.php?pic=HEYVDl9CEghRV1dcWwocCUQFGxVdQUZBVRdaXV1YWVxFUQ8EAAFFUUZVRCNHMXYJA2FaeXYCNFsiVR0Vf3t5YUQiLEVKXkRCDgwFAwcLA1FHW0UGAwM=&amp;title=
tL%2FW1tOitszAtsOou%2B7M5cC2sNfDqNPX4cywq73Fw6jQocOo3%2BS77s7vs%2BjO78Oo3%2BTTorn6tszDq8Oo&amp;version=2&amp;c=MjIwNjU3MDMzMDg1MQ%3D%3D&amp;sellerRate=10149&amp;itemId=690907579222&amp;fv=9&amp;shopId=260638490" rel="nofollow" target="_blank">
<img data-haszoom="700" data-size="400x400" id="J_ImgBooth" src="//gd4.alicdn.com/imgextra/i4/2206570330851/O1CN01RnAEkF1I9nqGOJS1K_!!2206570330851.jpg_400x400.jpg"/>      
</a>
<div class="zoom-icon hidden tb-iconfont" id="J_ZoomIcon">ő</div>
</div>
<ul class="tb-thumb tb-clearfix" id="J_UlThumb">
<li class="tb-selected">
<div class="tb-pic tb-s50">
<a href="#"><img data-src="//gd3.alicdn.com/imgextra/i4/2206570330851/O1CN01RnAEkF1I9nqGOJS1K_!!2206570330851.jpg_50x50.jpg"/></a>
</div>
</li>
<li>
<div class="tb-pic tb-s50">
<a href="#"><img data-src="//gd1.alicdn.com/imgextra/i1/2206570330851/O1CN011siQez1I9nqEBQys1_!!2206570330851.jpg_50x50.jpg"/></a>
</div>
</li>
<li>
<div class="tb-pic tb-s50">
<a href="#"><img data-src="//gd4.alicdn.com/imgextra/i4/2206570330851/O1CN01iyzWFb1I9nqL8mOaO_!!2206570330851.jpg_50x50.jpg"/></a>
</div>
</li>
<li>
<div class="tb-pic tb-s50">
<a href="#"><img data-src="//gd3.alicdn.com/imgextra/i3/2206570330851/O1CN01ftjgnv1I9nqJH5DTQ_!!2206570330851.png_50x50.jpg"/></a>
</div>
</li>
<li>
<div class="tb-pic tb-s50">
<a href="#"><img data-src="//gd3.alicdn.com/imgextra/i3/2206570330851/O1CN01PiJNO51I9nq9ownmv_!!2206570330851.jpg_50x50.jpg"/></a>
</div>
</li>
</ul>
<script>
    (function () {
        if (this.WebP)return;
        this.WebP = {}, WebP._cb = function (e, t) {
            this.isSupport = function (t) {
                t(e)
            }, t(e), (window.chrome || window.opera && window.localStorage) && window.localStorage.setItem("webpsupport", e)
        }, WebP.isSupport = function (e) {
            if (!e)return;
            if (!window.chrome && !window.opera)return WebP._cb(!1, e);
            if (window.localStorage && window.localStorage.getItem("webpsupport") !== null) {
                var t = window.localStorage.getItem("webpsupport");
                WebP._cb(t === "true", e);
                return
            }
            var n = new Image;
            n.src = "data:image/webp;base64,UklGRjoAAABXRUJQVlA4IC4AAACyAgCdASoCAAIALmk0mk0iIiIiIgBoSygABc6WWgAA/veff/0PP8bA//LwYAAA", n.onload = n.onerror = function () { 
                WebP._cb(n.width === 2 && n.height === 2, e)
            }
        }, WebP.run = function (e) {
            this.isSupport(function (t) {
                t && e()
            })
        }
    })();
    (function (e, f) {
        var d, c = function (g) {
            return document.getElementById(g)
        }, a = function (g) {
            var h = g.getAttribute("data-src");
            if (!h) {
                return
            }
            if (d && e) {
                h += "_.webp";
                f = true
            }
            g.src = f ? h.replace(/img0(\d)\.taobaocdn\.com/, "gd$1.alicdn.com") : h
        }, b = function (h) {
            if (h) {
                for (var g = 0; g < h.length; g++) {
                    a(h[g])
                }
            }
        };
        WebP.isSupport(function (g) {
            d = g;
            a(c("J_ImgBooth"));
            b(c("J_UlThumb").getElementsByTagName("img"));
            if (d) {
                g_config.beacon.webp = 1
            }
        })
    })(true, true);

</script>
</div>
<div class="tb-social tb-clearfix" data-spm="20140010" id="J_Social">
<ul>
<li class="tb-social-fav">
<a class="J_TDialogTrigger" data-closebtn="true" data-height="260" data-spm-click="gostr=/tbdetail;locaid=d1" data-spm-protocol="" data-width="440" href="//favorite.taobao.com/popup/add_collection.htm?itemtype=1&amp;scjjc=1&amp;id=690907579222" shortcut-effect="click" shortcut-key="c" shortcut-label="收藏宝贝">
<i class="tb-icon"></i> 收藏宝贝<em class="J_FavCount"></em>
</a>
</li>
<!--
            <li class="tb-social-split"></li>
            -->
<!--TODO:
            <li class="tb-social-like">
                <a data-spm-click="gostr=/tbdetail;locaid=d1"
                   href="javascript:;"
                   shortcut-key="x"
                   shortcut-label="喜欢宝贝"
                   shortcut-effect="click">
                    <i class="tb-icon"></i> 喜欢宝贝
                </a>
            </li>
            -->
<!--
            <li class="tb-social-share">
                <a data-spm-click="gostr=/tbdetail;locaid=d2"
                   class="J_Share"
                   href="javascript:;"
                   data-init="false"
                   shortcut-key="f"
                   shortcut-label="分享宝贝"
                   shortcut-effect="click">
                    <i class="tb-icon"></i> 分享
                </a>
            </li>
            -->
</ul>
</div>
</div>
<div class="tb-item-info-r" data-spm="iteminfo"> <div class="tb-property tb-property-x">
<div class="tb-wrap tb-wrap-newshop">
<div class="tb-title" id="J_Title" shortcut-effect="focus" shortcut-key="t" shortcut-label="查看宝贝标题">
<h3 class="tb-main-title" data-title="纯种英短蓝猫活体蓝白猫幼崽矮脚猫小猫咪活物宠物猫咪英国短毛猫">
            纯种英短蓝猫活体蓝白猫幼崽矮脚猫小猫咪活物宠物猫咪英国短毛猫
        </h3>
<p class="tb-subtitle"></p>
<div class="tb-editor-menu" id="J_TEditItem"></div>
</div>
<div class="tb-banner" id="J_Banner"></div>
<ul class="tb-meta">
<li class="tb-detail-price tb-clear" id="J_StrPriceModBox" shortcut-effect="focus" shortcut-key="p" shortcut-label="查看价格">
<span class="tb-property-type">价格</span>
<div class="tb-property-cont">
<strong id="J_StrPrice"><em class="tb-rmb">¥</em><em class="tb-rmb-num">1500.00</em></strong>
</div>
</li><li class="tb-detail-price tb-promo-price tb-clear tb-hidden" id="J_PromoPrice">
<span class="tb-property-type">淘宝价</span>
<div class="tb-property-cont">
<div class="tb-promo-mod" id="J_Promo">
<div class="tb-promo-hd tb-promo-item" id="J_PromoHd"></div>
<div class="tb-promo-bd" id="J_PromoBd"></div>
</div>
</div>
</li>
<li id="J_Duty"></li>
<li id="J_ActivityPrice"></li>
<li class="tb-clear tb-hidden" id="J_OtherDiscount">
<span class="tb-property-type">优惠</span>
<div class="tb-other-discount">
</div>
</li>
<li class="tb-counter" id="J_Counter">
<span class="tb-property-type">销量</span>
<div class="tb-counter-bd">
<div class="tb-rate-counter">
<a href="javascript:;" id="J_ReviewTabTrigger">
<strong id="J_RateCounter">-</strong>
<span>累计评论</span>
</a>
</div>
<div class="tb-sell-counter">
<a href="javascript:;">
<strong id="J_SellCounter">-</strong>
<span>月销量</span>
</a>
</div>
</div>
</li>
<li class="tb-more-promo-slider tb-clearfix" id="J_MorePromoSlider" style="display: none">
<ul id="J_MorePromoList"></ul>
<div class="post-script">以上价格可在付款时选择享用</div>
</li>
</ul>
<div id="J_StepPrice"></div>
<div id="J_logistic"></div>
<div class="sep-line" id="J_SepLine"></div>
<div class="tb-key tb-key-sku" id="J_isku" shortcut-effect="focus" shortcut-key="i" shortcut-label="挑选宝贝">
<div class="tb-skin">
<dl class="J_Prop tb-prop tb-clear">
<dt class="tb-property-type">动物性别</dt>
<dd>
<ul class="J_TSaleProp tb-clearfix" data-property="动物性别">
<li data-value="21241:3873886">
<a href="javascript:void(0);">
<span>公</span>
</a>
<i>已选中</i>
</li>
<li data-value="21241:9999473">
<a href="javascript:void(0);">
<span>母</span>
</a>
<i>已选中</i>
</li>
</ul>
</dd>
</dl>
<dl class="J_Prop tb-prop tb-clear J_Prop_Color">
<dt class="tb-property-type">颜色分类</dt>
<dd>
<ul class="J_TSaleProp tb-img tb-clearfix" data-property="颜色分类">
<li class="tb-txt" data-value="1627207:28338">
<a href="javascript:void(0);">
<span>蓝色</span>
</a>
<i>已选中</i>
</li>
</ul>
</dd>
</dl>
<dl class="J_Prop tb-prop tb-clear">
<dt class="tb-property-type">宠物年龄</dt>
<dd>
<ul class="J_TSaleProp tb-clearfix" data-property="宠物年龄">
<li data-value="122276097:493262420">
<a href="javascript:void(0);">
<span>幼年猫(12月以下)</span>
</a>
<i>已选中</i>
</li>
</ul>
</dd>
</dl>
<dl class="tb-amount tb-clear">
<dt class="tb-property-type">数量</dt>
<dd>
<span class="tb-stock" id="J_Stock">
<a class="tb-reduce J_Reduce tb-iconfont" hidefocus="" href="javascript:void(0);" title="减1">ƛ</a>
<input class="tb-text" id="J_IptAmount" maxlength="8" title="请输入购买量" type="text" value="1">
<a class="tb-increase J_Increase tb-iconfont" hidefocus="" href="javascript:void(0);" title="加1">ƚ</a>件
        </input></span>
<em>(库存<span class="tb-count" id="J_SpanStock">2</span>件)</em>
</dd>
</dl>
<dl class="tb-choice tb-clear" id="J_DlChoice">
<dt>请选择：</dt>
<dd>
<em>动物性别</em>
<em>颜色分类</em>
<em>宠物年龄</em>
</dd>
</dl>
<div class="tb-sure" id="J_SureSKU">
<p class="tb-choice">请勾选您要的商品信息</p>
<p class="tb-sure-continue">
<a href="javascript:;" id="J_SureContinue">确定</a>
</p>
<span class="close J_Close tb-iconfont">ß</span>
</div>
<div class="tb-action tb-clearfix" id="J_juValid">
<div class="tb-btn-buy">
<a class="J_LinkBuy" data-addfastbuy="true" data-spm-click="gostr=/tbdetail;locaid=d1" href="javascript:;" shortcut-effect="click" shortcut-key="b" shortcut-label="立即购买 title="点击此按钮，到下一步确认购买信息">
                立即购买
            </a>
</div>
<div class="tb-btn-add">
<a class="J_LinkAdd" data-spm-click="gostr=/tbdetail;locaid=d2" href="javascript:;" shortcut-effect="click" shortcut-key="a" shortcut-label="加入购物车" title="加入购物车">
<i class="tb-iconfont">ŭ</i>加入购物车
            </a>
</div>
</div>
</div>
</div>
<div class="tb-extra" id="J_tbExtra">
</div>
</div>
</div>
</div>
</div>
</div>
<div class="tb-sidebar tb-clear"> <div class="tb-shop-info" data-creditflag="cap" data-creditscore="10149" data-rateurl="//rate.taobao.com/user-rate-740c352df8e0390893debc5f064c239c.htm" data-spm="1000126" id="J_ShopInfo">
<a class="J_ShopInfoHeader tb-shop-info-bg" href="javascript:;" target="_blank"></a>
<div class="tb-shop-info-wrap">
<div class="tb-shop-info-hd">
<div class="tb-shop-name">
<dl>
<dd>
<strong>
<a href="//shop260638490.taobao.com" target="_blank" title="喵爪爪萌宠生活馆">
                          喵爪爪萌宠生活馆
                      </a>
</strong>
</dd>
</dl>
</div>
<div class="tb-shop-rank tb-rank-cap">
<dl>
<dt>信誉：</dt>
<dd>
<a href="//rate.taobao.com/user-rate-740c352df8e0390893debc5f064c239c.htm" target="_blank">
<i></i>
</a>
</dd>
</dl>
</div>
<div class="tb-shop-ww">
<dl>
<dt>联系：</dt>
<dd>
<span class="J_WangWang" data-encode="true" data-nick="tb469223107" data-tnick="tb469223107"></span>
</dd>
</dl>
</div>
<div class="tb-shop-icon">
<dl>
<dt>资质：</dt>
<dd>
<a class="tb-icon tb-icon-alipay-persion-auth" data-spm="d12" href="//help.alipay.com/lab/210120-210321/0-210321.htm" target="_blank" title="支付宝个人认证2022-07-30"></a> 
<a class="tb-icon tb-icon-qualification" data-spm="" href="https://scportal.taobao.com/quali_show.htm?uid=2206570330851&amp;qualitype=all" target="_blank" title="经营许可证></a>
</dd>
</dl>
</div>
</div>
<div class="tb-shop-info-bd">
<div class="tb-shop-rate">
<dl>
<dt>描述</dt>
<dd class="tb-rate-lower">
<a href="//rate.taobao.com/user-rate-740c352df8e0390893debc5f064c239c.htm" target="_blank" title="计算规则:(同行业平均分-店铺得分)/(同行业平均分-同行业店铺最低得分)">      
                              4.5
                          </a>
</dd>
</dl>
<dl>
<dt>服务</dt>
<dd class="tb-rate-lower">
<a href="//rate.taobao.com/user-rate-740c352df8e0390893debc5f064c239c.htm" target="_blank" title="计算规则:(同行业平均分-店铺得分)/(同行业平均分-同行业店铺最低得分)">      
                              4.5
                          </a>
</dd>
</dl>
<dl>
<dt>物流</dt>
<dd class="tb-rate-lower">
<a href="//rate.taobao.com/user-rate-740c352df8e0390893debc5f064c239c.htm" target="_blank" title="计算规则:(同行业平均分-店铺得分)/(同行业平均分-同行业店铺最低得分)">      
                              4.5
                          </a>
</dd>
</dl>
</div>
</div>
<div class="tb-shop-info-ft">
<a data-spm="d21" href="//shop260638490.taobao.com" target="_blank">进入店铺</a>
<a class="J_TDialogTrigger J_TokenSign" data-closebtn="true" data-height="260" data-info="param=SCCP_2_260638490&amp;countUrl=%2F%2Fcount.taobao.comcounter3&amp;mecuryUrl=%
2F%2Ffavorite.taobao.comcollect_item_relation---260638490-0-.htm" data-spm="d22" data-width="440" href="//favorite.taobao.com/popup/add_collection.htm?id=260638490&amp;item
id=260638490&amp;itemtype=0&amp;ownerid=740c352df8e0390893debc5f064c239c&amp;scjjc=2" mercury:params="id=260638490&amp;itemid=260638490&amp;itemtype=0&amp;scjjc=5&amp;ownerid=740c352df8e0390893debc5f064c239c">收藏店铺</a>
</div>
</div>
</div>
<div class="tb-pine" data-catid="50016383" data-itemid="690907579222" data-rootid="29" data-sellerid="2206570330851" data-shopid="260638490" data-spm="20141001" id="J_Pine"></div>
</div>
</div>
<div id="J_PPayGuide"></div><div data-spm="3" id="tad_first_area"></div>
</div>
<div class="tb-tabbar-wrap tb-clear" data-spm="20140004" id="J_TabBarWrap">
<div class="tb-tabbar-mid-wrap tb-clear">
<div class="tb-shop-search">
<div class="search-panel">
<form action="//shop260638490.taobao.com/search.htm" class="search-panel-focused" id="J_TShopSearchForm" name="search //shop260638490.taobao.com" target="_top">
<div class="search-button">
<button class="tb-iconfont" id="J_ShopSearchIcon" type="submit">ő</button>
</div>
<div class="search-panel-fields">
<input accesskey="s" aria-label="输本店" autocomplete="off" data-spm-click="gostr=/tbdetail;locaid=d6" id="q" name="q" placeholder="搜本店"/>
</div>
<input name="searcy_type" type="hidden" value="item"/>
<input name="s_from" type="hidden" value="newHeader"/>
<input name="source" type="hidden"/>
<input name="ssid" type="hidden" value="s5-e"/>
<input name="search" type="hidden" value="y"/>
<input id="J_TSearchSPM" name="spm" type="hidden" value="a1z10.1.1996643285.d4916901"/>
<input name="initiative_id" type="hidden" value=""/>
<input name="encoding" type="hidden" value="utf8"/>
</form>
</div>
</div>
<div class="tb-tabbar-inner-wrap">
<ul class="tb-tabbar tb-clear" id="J_TabBar"> <li class="tb-first selected">
<a class="tb-tab-anchor" data-index="0" data-spm-click="gostr=/tbdetail;locaid=d1" hidefocus="true" href="javascript:void(0);" shortcut-effect="click" shortcut-key="g d" shortcut-label="查看宝贝详情">宝贝详情</a>
<div class="tb-selected-indicator"></div>
</li>
<li>
<a class="tb-tab-anchor" data-index="1" data-spm-click="gostr=/tbdetail;locaid=d2" hidefocus="true" href="javascript:void(0);" shortcut-effect="click" shortcut-key="g c" shortcut-label="查看累计评论">
        累计评论

        <em class="J_ReviewsCount">0</em>
</a>
<div class="tb-selected-indicator"></div>
</li>
<li id="J_ServiceTab">
<a class="tb-tab-anchor" data-index="4" data-spm-click="gostr=/tbdetail;locaid=d4" hidefocus="true" href="javascript:void(0);" shortcut-effect="click" shortcut-key="g z" shortcut-label="查看专享服务">
        专享服务</a>
<div class="tb-selected-indicator"></div>
</li>
<li class="tb-shop-cart">
<a class="tb-tab-anchor" data-index="3" data-spm-click="gostr=/tbdetail;locaid=d5" href="javascript:void(0);" id="J_TabShopCart"><i class="tb-iconfont">Ů</i> 加入购物车</a>
</li><li class="tb-ids-mod">
<a class="tb-tab-anchor" href="javascript:void(0);" style="cursor: default;">快速直达</a>
</li>
</ul>
</div>
</div>
</div>
<div class="layout grid-s5m0 tb-main-layout">
<div class="col-main clearfix">
<div class="main-wrap J_TRegion" id="J_MainWrap">
<div class="sub-wrap" id="J_SubWrap">
<div class="attributes" id="attributes">
<!-- attributes div start -->
<ul class="attributes-list">
<li title="宝贝它">品牌: 宝贝它</li>
<li title="公 母">动物性别: 公 母</li>
<li title="短毛">宠物毛长: 短毛</li>
<li title="蓝色">颜色分类: 蓝色</li>
<li title="俄罗斯蓝猫">猫咪品种: 俄罗斯蓝猫</li>
<li title="有血统证书">血统信息: 有血统证书</li>
<li title="已做完">免疫驱虫: 已做完</li>
<li title="幼年猫(12月以下)">宠物年龄: 幼年猫(12月以下)</li>
<li title="猫舍">卖家资质分类: 猫舍</li>
</ul>
</div>
<div class="tb-attention-msg cat-warning tb-clearfix" data-spm="1000374" id="pet-purchase">
<p><strong>宠物活体交易提醒：</strong>支付宝直接转账、扫码付款，或者当面付款等交易形式脱离了淘宝购物流程，均不在淘宝规则保障范围内，可能存在交易欺诈风险。同时，网站只视阿里旺聊天记录为有效凭证，请不要使用阿里旺旺以外的聊天工具，谨防被骗。<a href="//bangpai.taobao.com/group/thread/1245496-252683255.htm" target="_blank">详情</a></p>
</div>
<div class="tb-attention-msg cat-warning">
<p><strong>消费提醒：</strong>受品相等因素影响，犬猫宠物个体价格差异较大，建议与商家充分沟通后下单购买，切勿线下转账，避免产生交易纠纷。</p>
</div>
<div data-item-id="690907579222" id="service"></div><div class="tad-stage" data-spm="4" id="tad_second_area"></div><div class="J_DetailSection tshop-psm ke-post" id="description">
<div class="content" id="J_DivItemDesc">

    描述加载中

    </div>
</div><div data-commonapi="//rate.taobao.com/detailCommon.htm?userNumId=2206570330851&amp;auctionNumId=690907579222&amp;siteID=4&amp;spuId=0" data-listapi="//rate.taobao.co
m/feedRateList.htm?userNumId=2206570330851&amp;auctionNumId=690907579222&amp;siteId=4&amp;spuId=0" data-reviewapi="//rate.taobao.com/detail_rate.htm?userNumId=2206570330851
&amp;auctionNumId=690907579222&amp;showContent=1&amp;currentPage=1&amp;ismore=0&amp;siteID=4" data-reviewcountapi="" data-usefulapi="//rate.taobao.com/vote_useful.htm?userNumId=2206570330851&amp;auctionNumId=690907579222" id="reviews">
</div>
<div id="deal-record">
<div class="tb-public-panel">
<div id="J_showBuyerList">
</div>
</div>
</div>
</div>
<div class="J_AsyncDC tb-custom-area tb-shop" data-type="main" id="J_AsyncDCMain"></div>
</div>
<div class="tb-price-spec">
<h3 class="spec-title">价格说明</h3>
<p class="title">划线价格</p>
<p class="info">指商品的专柜价、吊牌价、正品零售价、厂商指导价或该商品的曾经展示过的销售价等，<strong>并非原价</strong>，仅供参考。</p>
<p class="title">未划线价格</p>
<p class="info">指商品的<strong>实时标价</strong>，不因表述的差异改变性质。具体成交价格根据商品参加活动，或会员使用优惠券、积分等发生变化，最终以订单结算页价格为准。</p>   
<p class="info">商家详情页（含主图）以图片或文字形式标注的一口价、促销价、优惠价等价格可能是在使用优惠券、满减或特定优惠活动和时段等情形下的价格，具体请以结算页面的标价、优条件或活动规则为准。</p>
<p class="info">此说明仅当出现价格比较时有效，具体请参见《淘宝价格发布规范》。若商家单独对划线价格进行说明的，以商家的表述为准。</p>
</div>
<div class="correlative-items J_TAjaxContainer" data-catid="50016383" data-itemid="690907579222" data-rootid="29" data-sellerid="2206570330851" data-spm="20141002" id="detail-recommend-viewed"></div>
<div class="correlative-items J_TAjaxContainer" data-catid="50016383" data-itemid="690907579222" data-rootid="29" data-sellerid="2206570330851" data-spm="20141003" id="detail-recommend-bought"></div>
<div class="correlative-items" data-spm="20160405" id="detail-recommend-linjiahaohuo"></div>
<div class="J_AsyncDC" data-type="dr">
<div id="official-remind">
<dl class="tb-security">
<dt>安全提示：</dt>
<dd>
<p>交易中请勿使用<em class="tb-h">阿里旺旺</em>以外的聊天工具沟通，不要接收<em class="tb-h">可疑文件</em>和不要点击<em class="tb-h">不明来源</em>的链接，支付前核实好域名和 支付详情。
                    淘宝不会以订单有问题，让您提供任何<em class="tb-h">银行卡</em>、<em class="tb-h">密码</em>、<em class="tb-h">手机验证码</em>！遇到可疑情况可在安全中心中行举报。</p>
<p>推荐安全软件：
                        <span><img alt="UC浏览器" src="//img.alicdn.com/tps/i1/TB1XL5ZGFXXXXbDXFXXAz6UFXXX-16-16.png"/><a href="https://www.uc.cn/" target="_top">UC浏览器</a> </span>
</p>
</dd>
</dl>
<dl class="tb-exemption">
<dt>内容申明：</dt>
<dd>淘宝为第三方交易平台及互联网信息服务提供者，淘宝（含网站、客户端等）所展示的商品/服务的标题、价格、详情等信息内容系由店铺经营者发布，其真实性、准确性和合法性均由店铺经 
营者负责。淘宝提醒用户购买商品/服务前注意谨慎核实。如用户对商品/服务的标题、价格、详情等任何信息有任何疑问的，请在购买前通过阿里旺旺与店铺经营者沟通确认；淘宝存在海量店铺，用户发现店铺内有任何违法/侵权信息，请立即向淘宝举报并提供有效线索。</dd>
</dl>
</div>
</div>
</div>
<div class="J_AsyncDC tb-shop col-sub J_TRegion" data-type="side"></div>
</div>
</div>
<div class="tb-shop J_AsyncDC" data-type="foot" id="ft"></div><div id="copyright"></div>
</div>
</div>
<div data-component-config='{ "cart": "0.0.6","message": "3.4.6","umpp": "1.5.4","mini-login": "6.3.8","tb-ie-updater": "0.0.4","tbar": "2.1.0","tb-footer": "1.1.8","sideba
r": "1.0.10" }' data-tbar='{ "show":true, "miniCart": "2.12.2","paramsBlackList": "_wt,seeyouagain1722","my_activity": "https://market.m.taobao.com/apps/abs/5/38/my12?psId=
58386&amp;pcPsId=58388", "venueUrl": "https://1212.taobao.com?wh_weex=true&amp;data_prefetch=true&amp;wx_navbar_transparent=true", "helpUrl": "https://consumerservice.taoba
o.com/online-help", "validTime":{"startTime": 1512057599, "endTime": 1513094400}, "style": {"name": "171212", "path": "kg/sidebar-style-171212/0.0.5/" }, "page":[],"blackLi
st":[],"navDataId":{"tceSid":1182567,"tceVid":0},"pluginVersion":{ "cart":"0.2.0","history":"0.2.0","redpaper":"0.0.8","gotop":"0.2.5","help":"0.2.1","ww":"0.0.3","pagenav":"0.0.27","myasset":"0.0.9","my1212":"0.0.1","my1111":"0.2.2"}}' id="J_sidebar_config">
</div>
<script>
    Hub = {};
    Hub.config = {
        config: {},
        get: function(key) {
            if (key in this.config) {
                return this.config[key];
            } else {
                return null;
            }
        },
        set: function(key, val) {
            this.config[key] = val;
        }
    };

    Hub.config.set('sku', {
        valCartInfo      : {
            itemId : '690907579222',
            cartUrl: '//cart.taobao.com/cart.htm'
        },
        apiRelateMarket  : '//tui.taobao.com/recommend?appid=16&count=4&itemid=690907579222',
        apiAddCart       : '//cart.taobao.com/add_cart_item.htm?item_id=690907579222',
        apiInsurance     : '',
        wholeSibUrl      : '//detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=690907579222&sellerId=2206570330851&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,activity,fqg,zjys,couponActivity,soldQuantity,page,originalPrice,tradeContract',
        areaLimit        : '',
        bigGroupUrl      : '',
        valPostFee       : '',
        coupon           : {
            couponApi         : '//detailskip.taobao.com/json/activity.htm?itemId=690907579222&sellerId=2206570330851',
            couponWidgetDomain: '//assets.alicdn.com',
            cbUrl             : '/cross.htm?type=weibo'
        },
        valItemInfo      : {

            defSelected: -1,
            skuMap     : {";21241:9999473;1627207:28338;122276097:493262420;":{"price":"1500.00","stock":"2","skuId":"4908202864796","oversold":false},";21241:3873886;1627207:28338;122276097:493262420;":{"price":"1500.00","stock":"2","skuId":"4908202864795","oversold":false}}
            ,propertyMemoMap: {}


        }
    });

    Hub.config.set('desc', {
        dummy       : false,
        apiImgInfo  : '//tds.alicdn.com/json/item_imgs.htm?t=desc/icoss20457689997a024ae5aa9ec431&sid=2206570330851&id=690907579222&s=f9a52e9010c72b0d1f223d630df4ac61&v=2&m=1',
        similarItems: {
            api           : '//tds.alicdn.com/recommended_same_type_items.htm?v=1',
            rstShopId     : '260638490',
            rstItemId     : '690907579222',
            rstdk         : 0,
            rstShopcatlist: ''
        }
    });


    Hub.config.set('async_dc', {
        newDc : true,
        api   : '//hdc1new.taobao.com/asyn.htm?userId=2206570330851&shopId=260638490&pageId=1842749132&v=2014'
    });


    Hub.config.set('support', {
        url : ''
    });

    Hub.config.set('async_sys', {
        api: '//item.taobao.com/asyn.htm?g=sys&v=2'
    });


    Hub.config.set('video', {"videoDuaration":"16","picUrl":"//img.alicdn.com/imgextra/i3/6000000006894/O1CN01lD9eYN20nVGknaKNx_!!6000000006894-0-tmap.jpg_310x310.jpg","videoId":"383191028173","autoplay":"1","videoOwnerId":"2206570330851","videoStatus":"0"});


</script><script>
    g_config.activitySource={"pre":"\/\/img.alicdn.com\/tps\/i1\/TB1o6JsHVXXXXcFXXXXGTSvIXXX-960-80.jpg","start":"\/\/img.alicdn.com\/tps\/i2\/TB1bxJoHVXXXXX5XpXXGTSvIXXX-960-80.jpg"};
</script><script>
    ;(function () {
    var isDaily = !!~location.hostname.indexOf('daily');
    var DAILY_ASSETS_HOST = '//g-assets.daily.taobao.net/';
    var PUBLISH_ASSETS_HOST = '//g.alicdn.com/';
    var DAILY = 'daily', PRE = 'pre', PUB = 'pub';
    var env = location.host.indexOf(DAILY) > -1 ? DAILY : (location.host.indexOf(PRE) > -1 ? PRE : PUB);
    if(location.href.indexOf('env=' + PUB) > -1) env = PUB;
    var unb = 0, result = /tracknick=([^;]+)/.exec(document.cookie);
    if(result) unb = unescape(unescape(result[1])).charCodeAt();
    Components = [];
    function getBase(path) {
        if (typeof path === 'object') {
            path = path[env] || path[PUB];
        }
        var host = isDaily ? DAILY_ASSETS_HOST : PUBLISH_ASSETS_HOST;
        return host + path;
    }
    Config = {
        packages: {
            tbc: {
                base: getBase('tbc/'),
                ignorePackageNameInUri: true
            },
            tb: {
                base: getBase('tb/'),
                ignorePackageNameInUri: true
            },
            kg: {
                base: getBase('kg/'),
                ignorePackageNameInUri: true
            },
            cm: {
                base: getBase('cm/'),
                ignorePackageNameInUri: true
            },
            'sd/data_sufei': {
                base: getBase('sd/data_sufei/1.3.6/sufei'),
                ignorePackageNameInUri: true
            },
            'tb-mod': {
                base: getBase('tb-mod/'),
                ignorePackageNameInUri: true
            }
        },
        modules: {
            datalazyload: {
                alias: ['kg/datalazyload/2.0.2/']
            },
            'gallery/datalazyload/1.0.1/': {
                alias: ['kg/datalazyload/2.0.2/']
            },
            'gallery/datalazyload/1.0/': {
                alias: ['kg/datalazyload/2.0.2/']
            },
            switchable: {
                alias: ['kg/switchable/2.0.0/']
            },
            imagezoom: {
                alias: ['kg/imagezoom/2.0.1/']
            },
            kscroll: {
                alias: ['gallery/kscroll/1.1/']
            },
            rainlib: {
                alias: ['gallery/rainlib/1.0/']
            },
            log: {
                alias: ['tbc/log/']
            },
            sku: {
                alias: ['kg/sku/6.2.0/']
            },
            doctor: {
                alias: ['kg/doctor/0.0.1/']
            },
            shortcuts: {
                alias: ['tbc/shortcuts/0.1.0/']
            },
            slide: {
                alias: ['kg/slide/2.0.2/']
            },
            seckill: {
                alias: ['tb/item-seckill/0.0.7/']
            },
            'address-detail/wlroute': {
                requires: ["node", "io", "xtemplate", "overlay", "event", "address-detail/wlroute.css"]
            },
            'records':{
                alias: ['tb/item-records/0.0.4/']
            },
            'item-detail/index': {
                requires: [
                    'core',
                    'overlay',
                    'xtemplate',
                    'imagezoom',
                    'switchable',
                    'datalazyload',
                    'sku',
                    'log'
                ]
            },
            util: {alias: "kg/kmd-adapter/0.1.5/util"},
            feature: {alias: "kg/kmd-adapter/0.1.5/feature"},
            "event-dom": {alias: "event"},
            "event-custom": {alias: "event"},
            "event-gesture": {alias: "event"}
        }
    };
    define = function (e, a, t) {return KISSY.add(e, a, function (e, a, n, i) {t(a, n, i)})};

    Config.packages["cbase"]={base:getBase("cm/base/0.6.3/"),debug:true,ignorePackageNameInUri:true};
    Config.packages["address-detail"]={base:getBase("ccc/address-detail/2.0.3/"),debug:true,ignorePackageNameInUri:true};
    Config.packages["charity"]={base:getBase("tb/charity/1.0.8/"),debug:true,ignorePackageNameInUri:true};
    Config.packages["wangpu"]={base:getBase("shop/wangpu/1.4.11/"),debug:false,ignorePackageNameInUri:true};
    Config.modules["rate"]={alias:"kg/rate/0.1.5/"};
    Config.modules["header"]={alias:"tbc/header/1.4.8/",requires:["header/index.css"]};
    Config.modules["favorite"]={alias:"tbc/favorite/1.0.8/"};
    Config.modules["contract"]={alias:"kg/contract/0.0.5/"};
    Config.modules["qrcode"]={alias:"kg/item-qrcode/0.0.3/"};
    Config.modules["oversea-service"]={alias:"kg/oversea-detail-service/0.0.1/"};
    Components.push({"path":"kg/anticheat/0.0.1/","init":"Component.init('detail')","precondition":"","name":"anticheat","load":"","retry":0});
    Components.push({"path":"kg/detail-page-pine-module/6.0.12/","init":"new Component({height: KISSY.one('.tb-detail-bd', '#detail').height() - KISSY.one('#J_ShopInfo').height() })","precondition":"document.getElementById('J_ShopInfo') && !g_config.idata.item.enterprise","name":"pine","load":"core","retry":1});
    Components.push({"name":"viewed","path":"kg/detail-viewed-bought-module/6.0.18/","precondition":"document.getElementById('detail-recommend-viewed')","init":"new Component()","load":"lazy","trigger":"scroll:#detail-recommend-viewed","retry":1});
    Components.push({"name":"offline","path":"kg/recommend-offline-module/0.0.9/","precondition":"document.getElementsByClassName('tb-key-off-sale')[0]","init":"new Component();","retry":1});
    Components.push({"name":"charity","path":"//g.alicdn.com/tb/charity/1.0.8/deps.js","precondition":"g_config.hasCharity","init":"KISSY.use('charity/c/detailModule/index', function (S, Charity) { Charity.initView('#J_PublicWelfare', {itemId: g_config.itemId}); })","retry":0});
    Components.push({"name":"tad","path":"kg/detail-item-recommend/0.0.12/","precondition":"g_config.tadInfo","init":"new Component({ data: g_config.tadInfo });","retry":1});
    Components.push({"name":"paimai","path":"kg/pm-sku/0.0.3/index.js","precondition":"g_config.idata.item.auction","init":"Component.start(g_config.DyBase.purl,g_config.itemId)","retry":1});
    Components.push({"name":"size","path":"//g.alicdn.com/tb/mysize/1.0.0/deps.js","precondition":"g_config.idata.item.initSizeJs","init":"KISSY.config({   packages: [{    
 name: 'mysize',     base: '//g.alicdn.com/tb/mysize/1.0.0/',     combine: true,     ignorePackageNameInUri: true,     debug: true   }] }); KISSY.use('mysize/p/showsize/', 
function(S, ShowSize) {   var itemData = g_config.idata.item;   var valItemInfo = Hub.config.get('sku').valItemInfo;   ShowSize(g_config.itemId, g_config.sellerId, valItemI
nfo && valItemInfo.propertyMemoMap, '.J_Prop_measurement', itemData.footType, '.tb-foot-type', itemData.sizeGroupName, itemData.isShowSizeTemplate, itemData.sizeTempId); });","load":"","trigger":"","retry":1});
    Components.push({"name":"qualification","path":"cm/qualified/0.5.0/app-detail/tb-detail","precondition":"g_config.itemQualification","init":"Component.init({result:g_config.itemQualification,link:false});","retry":1});
    Components.push({"name":"pointman","path":"//g.alicdn.com/secdev/pointman/js/index.js#app=taobao","precondition":"!window.attachEvent && Math.random() < 0.011","init":"","load":"lazy","trigger":"time:1000","retry":0});
    Components.push({"name":"caro2o","path":"cbase/p/o2o-service/tb-detail","precondition":"g_config.supportO2OService","init":"","load":"main","trigger":"","retry":0});   
    Components.push({"name":"pureService","path":"cbase/p/pure-service/tb-detail","precondition":"g_config.Electronic","init":"Component.init({itemId : g_config.itemId,serviceData : g_config.Electronic,sellerId:g_config.sellerId});","load":"","trigger":"","retry":0});
    Components.push({"name":"lifemap","path":"//g.alicdn.com/tb/life/2.0.0/config.js","precondition":"g_config.idata.item.isLifeServiceItem","init":"KISSY.use('life/p/service-range-for-detail/',function(S,serviceRangeForDetail){serviceRangeForDetail.init({itemId:g_config.itemId,el:'#J_IframeForLife'});});","load":"","trigger":"","retry":0}); 
    Components.push({"name":"steporder","path":"cbase/p/o2o-steporder/tb-detail","precondition":"g_config.StepOrder","init":"Component.init({itemId : g_config.itemId , StepOrder : g_config.StepOrder });","load":"","trigger":"","retry":0});
    Components.push({"name":"freeBookingCar","path":"//g.alicdn.com/tb/usedcar-booking/0.0.1/config.js","precondition":"g_config.freeBookingCar","init":"USEDCARBOOKING_XCak
e.config({name: 'usedcar-booking',base: '//g.alicdn.com/tb/usedcar-booking/0.0.1/',combine: true});KISSY.use('usedcar-booking/p/popup-booking/', function(S, PopupBooking){ PopupBooking.init(); });","load":"","trigger":"","retry":0});
    Components.push({"name":"item-spu","path":"tb/item-spu/1.0.0/index","precondition":"g_config.spuStandardInfo","init":"Component.init(g_config.spuStandardInfo);","load":"","trigger":"","retry":1});
    Components.push({"name":"fuwubao","path":"//g.alicdn.com/sj/life/2.0.3/config.js","precondition":"g_config.delayInsurance && !g_config.fuwubao","init":"KISSY.use('life/c/service-items/',function(S,serviceItem){serviceItem.init('#J_ServiceItems', g_config.itemId)});","retry":0});
    Components.push({"name":"jiyoujia","path":"//g.alicdn.com/tb-mod/youjia-detail-service/0.0.9/index.js","precondition":"g_config.jiyoujiaPromises","init":"KISSY.use('tb-mod/youjia-detail-service/0.0.9/', function(S, Component){new Component('#J_JiyoujiaPromises', g_config.jiyoujiaPromises);})","load":"","trigger":"","retry":0});
    Components.push({"name":"pine_enterprise","path":"kg/detail-pinus-enterprise-module/6.0.7/","precondition":"(g_config.pinusEnterprise || g_config.idata.item.customHeader) && document.getElementById(\"J_Pinus_Enterprise_Module\")","init":"new Component();","load":"core","retry":1});
    Components.push({"name":"carmodel","path":"kg/carmodel/0.0.2/","precondition":"g_config.cascadeData","init":"Component.init({container: '#J_CascadeData', data: g_config.cascadeData})","load":"","trigger":"","retry":0});
    Components.push({"name":"item-presale","path":"kg/item-presale/0.0.11/","precondition":"g_config.presale","init":"Component.init('#J_TbcPresale', {data:g_config.presale, now:g_config.vdata.sys.now, itemId:g_config.itemId,itemTitle:g_config.idata.item.title});","retry":0});
    Components.push({"name":"linjiahaohuo","path":"kg/linjiahaohuo/0.0.2/","precondition":"document.getElementById('detail-recommend-linjiahaohuo')","init":"Component.init(
{container:'#detail-recommend-linjiahaohuo',itemId:g_config.itemId,sellerId:g_config.sellerId})","load":"lazy","trigger":"scroll:#detail-recommend-linjiahaohuo","retry":1});
    Components.push({"name":"cuntao-coupon","path":"kg/cuntao-coupon-detail/0.1.4/","precondition":"g_config.idata.item.cuntaoItem","init":"new Component({$target:'#J_cuntaoCoupon'})","retry":0});
    Components.push({"name":"cuntao-cycle","path":"kg/cuntao-cycle-detail/0.0.2/","precondition":"g_config.cuntaoCycleItem","init":"new Component({$target:'#J_cuntaoCycle'})","load":"","trigger":"","retry":1});
    Components.push({"name":"sp-services","path":"cm/detail-services-component/0.3.0/","precondition":"document.getElementById('J_SpServices')","init":"Component.init('#J_SpServices')","retry":0});
    Components.push({"name":"item-huichi","path":"kg/detail-huichi-icon/0.0.6/","precondition":"g_config.huichi","init":"new Component({data:g_config.huichi,node:'#J_Huichi'})","load":"lazy","trigger":"scroll:#J_Huichi"});
    Components.push({"name":"cun-packsale-detail","path":"kg/cun-packsale-detail/0.0.6/","precondition":"g_config.cuntaoPackageTrade","init":"new Component({$target:'.tb-meta'})"});
    Components.push({"name":"service","path":"//g.alicdn.com/sj/life/3.0.2/config.js","precondition":"g_config.fuwubao && g_config.delayInsurance","init":"KISSY.use('life/c/service-items/',function(S,serviceItem){serviceItem.init('#J_ServiceItems', g_config.itemId)});"});
    Components.push({"name":"cuntao-goods-tags","path":"kg/cuntao-goods-tags/0.0.2/","precondition":"g_config.cuntao2Item || g_config.cuntaoAgriItem","init":"new Component({$target:'#J_Title'})"});
})();

</script>
<script charset="utf-8" src="//g.alicdn.com/??kissy/k/1.4.14/seed-min.js,sd/sufei/0.2.4/app/common/sufei-kissy.js,mtb/lib-promise/3.1.1/polyfillB.js,mtb/lib-mtop/2.4.2/mtop.js,mtb/videox/0.3.55/videox-pc.js"></script>
<script src="//g.alicdn.com/??kg/kmd-adapter/0.1.5/index.js,kg/kmd-adapter/0.1.5/util.js,kg/global-util/1.0.7/index-min.js,tb/tracker/index.js"></script>
<script>
window.g_config = window.g_config || {};
window.g_config.region = true;
window.g_config.footer = false;
</script>
<style>
#J_SiteNav {
  z-index: 100000001;
}
body #ariaToptoolbar {
    z-index: 100099999;
}
body .mouseten {
    z-index: 100099999;
}
body #accscreen {
    z-index: 100050000;
}
</style>
<script charset="UTF-8" src="//o.alicdn.com/tbhome/tbnav/index.js"></script>
<script>KISSY.config({combine:true, modules:{'flash':{alias:['gallery/flash/1.0/']}}});KISSY.use('kg/global-util/1.0.7/');</script>
<script charset="utf-8" src="//g.alicdn.com/??tb/item-detail/8.0.39/platform-min.js"></script>
</body>
</html>
'''

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the <h3> tag with class 'tb-main-title' and get the value of data-title attribute
    title = Translator().translate(soup.find('h3', class_='tb-main-title')['data-title'], src=constants.CHINESE, dest=constants.VIETNAMESE).text

    script_tags = soup.find_all("script")
    for script_tag in script_tags:
        script_content = script_tag.string
        if script_content and "Hub.config.set" in script_content:
            start_index = script_content.find("wholeSibUrl      : '")
            end_index = script_content.find("tradeContract',")
            json_content = script_content[start_index + 20: end_index]
            detail_link_value = "https:" + json_content

    product = detailValueV2(detail_link_value, title)

    return product

def detailValueV2(linkDetail: str, title : str):
    if linkDetail == None or linkDetail == "":
        return "Empty link"
    if title == None or title == "":
        return "Empty name"
    translator = Translator()
    # product_list = []
    # headers = {
    #     'Cookie': 't=ec0d5bd680cef4c43c9f71708db31058; cna=BRxOHd8VWAICAXGhLjZWD5TR; xlly_s=1; sgcookie=E100H0swvfyYsdVvyTSCrnObIsrV9Aq5T474B8w3cwP5nWHOe6gtbUcYZOtKadjZUZn5FaAW%2BQ1uJQLhLtsuUfTrufcHNomxvIPXmNQua6gPTPE%3D; uc3=vt3=F8dCsGCl3JWCOZIAnLM%3D&id2=UUpgQEvyiTEr4C708g%3D%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D&nk2=F5RDLjqWCLCCNe6Q0ac%3D; lgc=tb627551502528; uc4=id4=0%40U2gqz6QY%2B2LU45CVgCnTHhyjjD3pXce2&nk4=0%40FY4I7WSY2SzxeSCD9wJSplBYHJHaEX%2BF0g%3D%3D; tracknick=tb627551502528; _cc_=WqG3DMC9EA%3D%3D; thw=xx; mt=ci=0_1; _uetsid=2e532be02f4f11ee80918f9d985d2979; _uetvid=dc870040ea5911ed8305a55f0f12c1b7; _m_h5_tk=bffc85d673ab2f3d0eebe9f130993d22_1690891184157; _m_h5_tk_enc=10d0b322cedd523f3f588213614f9e04; hng=VN%7Czh-CN%7CVNM%7C704; _gid=GA1.2.1343417350.1690881464; _ga=GA1.1.658097477.1690881463; _ga_YFVFB9JLVB=GS1.1.1690881463.1.0.1690881469.0.0.0; _ga_JBTWV3NHSY=GS1.1.1690881463.1.0.1690881469.54.0.0; cookie2=1c358ce26fd4234017e383ab667ef88d; _tb_token_=f60ee6eeeb3fe; tfstk=dEwBfWDMPeYQ2aHskBsa1qKLCcD7Oy6VF3i8mupe2vHdF0U45bpPtvlSFP3aL2rEpTi8uPG8z4rex544DpyFtYJSKYDRuZWV3MqnEYBC-c7VkXYd0C-O3tr3xHod0lBVrtfd4GGRnpx5Pl76Bd9ACFkQHiQ5PRiOxqEBJpobBDGikkeBnO5v3qs8BQtsiLisuGs6ZQfuLqHO.; l=fBIQOzNINiq0KRtBBO5Churza77O2COb8sPzaNbMiIEGa6Th1elM8NC61q3pRdtjQT5Y1etyzs0aOdhw5Ja38xOe7pP-OC0eQKp28eM3N7AN.; isg=BGhow2fRmMKnVLTcoTZoExvVOVZ6kcybJYC5NSKc4OPWfQnnyqPpKsX_dQ2NzYRz; x5sec=7b22617365727665723b32223a226137316262343934343964303833653439366131306266303238643831333839434b667a703659474550666873386175362b3461476738794d6a45324d6a41354d544d314d7a67774f7a4969436d4e6863484e736157526c646a49776b4b48466e76762f2f2f2f2f41554144227d',
    #     'Referer': 'https://item.taobao.com/item.htm?id=690907579222&ns=1&abbucket=12#detail',
    #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    #     'Accept-Encoding': 'gzip, deflate, br',
    #     'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    #     'Cache-Control': 'max-age=0',
    #     'Sec-Ch-Ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    #     'Sec-Ch-Ua-Mobile': '?0',
    #     'Sec-Ch-Ua-Platform': '"Windows"',
    #     'Sec-Fetch-Dest': 'document',
    #     'Sec-Fetch-Mode': 'navigate',
    #     'Sec-Fetch-Site': 'same-origin',
    #     'Upgrade-Insecure-Requests': '1',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    # }
    # url = linkDetail
    # response = requests.get(url, headers=headers)
    # if response.status_code != 200:
    #     return "Failed"
    # data = response.json()
    data = {
         'code': 200,
         'data': {'category_id': 217309,
                  'comment_count': None,
                  'currency': 'CNY',
                  'delivery_info': {'area_from': ['上海市'],
                                    'area_id': '',
                                    'postage': '0'},
                  'extra': 'False',
                  'item_id': 726085758711,
                  'main_imgs': [
                      'https://gd4.alicdn.com/imgextra/i4/2215542721611/O1CN01S1Y1fY1Nlsukv6PFc_!!2215542721611.jpg',
                      'https://gd3.alicdn.com/imgextra/i3/2215542721611/O1CN01GSYG6i1NlsupoYJOe_!!2215542721611.jpg',
                      'https://gd3.alicdn.com/imgextra/i3/2215542721611/O1CN01zlOh721NlsuitvfgA_!!2215542721611.jpg',
                      'https://gd2.alicdn.com/imgextra/i2/2215542721611/O1CN01L9tICh1NlsupoqAO3_!!2215542721611.jpg',
                      'https://gd2.alicdn.com/imgextra/i2/2215542721611/O1CN019MUetm1NlsuoGFRGm_!!2215542721611.jpg'],
                  'price_info': {'origin_price': '300.0', 'price': '300.0'},
                  'product_props': [{'狗狗品种': '比熊'},
                                    {'动物性别': '公 母'},
                                    {'毛长': '中毛(如雪纳瑞/萨摩耶等)'},
                                    {'颜色分类': '白色'},
                                    {'狗狗种类': '家庭犬'},
                                    {'血统信息': '有血统证书'},
                                    {'免疫驱虫': '已做完'},
                                    {'宠物体型': '玩具犬(成年体重<4kg，肩高<25cm)'},
                                    {'级别': 'S参赛级'},
                                    {'宠物年龄': '幼年犬(45日龄-12月龄)'},
                                    {'卖家资质分类': '宠物店'}],
                  'product_url': 'https://item.taobao.com/item.htm?id=726085758711',
                  'root_category_id': None,
                  'shop_info': {'followers': None,
                                'good_rate_percentage': None,
                                'is_tmall': False,
                                'seller_id': 2215542721611,
                                'shop_id': 498428785,
                                'shop_logo': '',
                                'shop_name': '萌新宠物馆',
                                'shop_rate': [{'score': 4.99609,
                                               'title': '宝贝描述',
                                               'type': 'desc'},
                                              {'score': 4.99609,
                                               'title': '卖家服务',
                                               'type': 'serv'},
                                              {'score': 4.99609,
                                               'title': '物流服务',
                                               'type': 'post'}],
                                'shop_start_time': None,
                                'shop_url': 'https://shop498428785.taobao.com',
                                'wangwang': 'https://amos.alicdn.com/getcid.aw?groupid=0&s=1&Im5SKL&charset=utf-8&uid=%E4%B8%8A%E6%B5%B7%E5%AE%A0%E7%89%A9%E5%9F%BA%E5%9C%B097&site=cntaobao&kJYNcf'},
                  'sku_props': [{'pid': '21241',
                                 'prop_name': '动物性别',
                                 'values': [{'imageUrl': None,
                                             'name': '母',
                                             'vid': '9999473'},
                                            {'imageUrl': None,
                                             'name': '公',
                                             'vid': '3873886'}]},
                                {'pid': '1627207',
                                 'prop_name': '颜色分类',
                                 'values': [{'imageUrl': None,
                                             'name': '白色',
                                             'vid': '28320'}]},
                                {'pid': '122276097',
                                 'prop_name': '宠物年龄',
                                 'values': [{'imageUrl': None,
                                             'name': '幼年犬(45日龄-12月龄)',
                                             'vid': '97077986'}]}],
                  'skus': [{'origin_price': '1500.0',
                            'props_ids': '21241:9999473;1627207:28320;122276097:97077986',
                            'props_names': '动物性别:母;颜色分类:白色;宠物年龄:幼年犬(45日龄-12月龄)',
                            'sale_price': '300.0',
                            'skuid': '5209138662206',
                            'stock': 200,
                            'sub_price': None,
                            'sub_price_type': 'discounted price'},
                           {'origin_price': '1500.0',
                            'props_ids': '21241:3873886;1627207:28320;122276097:97077986',
                            'props_names': '动物性别:公;颜色分类:白色;宠物年龄:幼年犬(45日龄-12月龄)',
                            'sale_price': '300.0',
                            'skuid': '5209138662207',
                            'stock': 200,
                            'sub_price': None,
                            'sub_price_type': 'discounted price'}],
                  'title': '纯种比熊幼犬长不大不掉毛飞耳法国比熊犬小型犬茶杯犬活体宠物狗',
                  'video_url': 'http://cloud.video.taobao.com/play/u/p/1/e/6/t/1/419427855174.mp4'},
         'msg': 'success'
    }

    # Extract relevant data from the JSON response
    product_url = data["data"]["product_url"]
    main_imgs = data["data"]["main_imgs"]
    product_props = data["data"].get("product_props", [])
    sku_props = data["data"].get("sku_props", [])
    skus = data["data"].get("skus", [])

    # Translate the elements in product_props list
    translated_product_props = [translate_text(prop, constants.VIETNAMESE) for prop in product_props]

    # Translate the elements in sku_props list
    translated_sku_props = [translate_text(prop, constants.VIETNAMESE) for prop in sku_props]

    translated_skus = []

    for sku in skus:
        translated_sku = sku.copy()  # Create a copy of the original sku
        if "props_names" in sku:
            props_names = sku["props_names"]
            translated_props = []
            props_list = props_names.split(';')
            for prop in props_list:
                translated_prop = translate_text(prop, constants.VIETNAMESE)
                translated_props.append(translated_prop)
            translated_sku["props_names"] = ';'.join(translated_props)
        translated_skus.append(translated_sku)

    product_dto = ProductDetailDto.ProductDto(title, product_url, main_imgs, translated_product_props, translated_sku_props, translated_skus)

    return product_dto
