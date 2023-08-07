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
def detailLink(link:str,linkDetail:str, list:list):
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
        listPriceData= data['data']['originalPrice']
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
    encoded_keyWord = urllib.parse.quote(keyWord, safe='')
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
                json_content = script_content[start_index + 15 : end_index +2]
                try:
                    g_page_config_json = json.loads(json_content)
                    data = g_page_config_json['mods']['itemlist']['data']['auctions']
                    for item in data:
                        print(item)
                        sys.stdout.flush()

                        name = translator.translate(item['raw_title'], src=constants.CHINESE ,dest=constants.VIETNAMESE)
                        link = 'https:' + item['detail_url']
                        if 'click.simba.taobao' in link:
                            print(f"Ignoring item '{name}' as it contains 'click.taobao' link.")
                            continue

                        objectDto = {
                            'id': counter,
                            'name': name.text,
                            'link': link,
                            'price': item['view_price'],
                            'image': 'https:'+item['pic_url'],
                            'shopName': item['shopName'],
                        }
                        counter += 1
                        product_list.append(objectDto)
                        if counter == 6:    #Số sản phẩm cần search -1
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
    try:
        for item in list_data:
            name = item['name']
            link = item['link']
            if "click.taobao" in link:
                print(f"Ignoring item '{name}' as it contains 'click.taobao' link.")
                continue

            if not check_if_record_exists(session, name):
                product = models.SearchProduct(name=name,
                                               price=item['price'],
                                               link=link,
                                               image=item['image'])
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
    try:
        # Calculate the offset based on the page number and items per page
        offset = (page_number - 1) * items_per_page

        # Query the database to get a specific page of data
        data = session.query(models.SearchProduct).limit(items_per_page).offset(offset).all()

        return data
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        session.close()

async def get_detail(detail_link, name):
    global detailLinkValue, listName
    product_list = []
    detailLinkValue = {}
    # headers = {
    #     'Cookie': 't=ec0d5bd680cef4c43c9f71708db31058; cna=BRxOHd8VWAICAXGhLjZWD5TR; xlly_s=1; sgcookie=E100H0swvfyYsdVvyTSCrnObIsrV9Aq5T474B8w3cwP5nWHOe6gtbUcYZOtKadjZUZn5FaAW%2BQ1uJQLhLtsuUfTrufcHNomxvIPXmNQua6gPTPE%3D; uc3=vt3=F8dCsGCl3JWCOZIAnLM%3D&id2=UUpgQEvyiTEr4C708g%3D%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D&nk2=F5RDLjqWCLCCNe6Q0ac%3D; lgc=tb627551502528; uc4=id4=0%40U2gqz6QY%2B2LU45CVgCnTHhyjjD3pXce2&nk4=0%40FY4I7WSY2SzxeSCD9wJSplBYHJHaEX%2BF0g%3D%3D; tracknick=tb627551502528; _cc_=WqG3DMC9EA%3D%3D; thw=xx; mt=ci=0_1; _uetsid=2e532be02f4f11ee80918f9d985d2979; _uetvid=dc870040ea5911ed8305a55f0f12c1b7; _m_h5_tk=bffc85d673ab2f3d0eebe9f130993d22_1690891184157; _m_h5_tk_enc=10d0b322cedd523f3f588213614f9e04; hng=VN%7Czh-CN%7CVNM%7C704; _gid=GA1.2.1343417350.1690881464; _ga=GA1.1.658097477.1690881463; _ga_YFVFB9JLVB=GS1.1.1690881463.1.0.1690881469.0.0.0; _ga_JBTWV3NHSY=GS1.1.1690881463.1.0.1690881469.54.0.0; cookie2=1c358ce26fd4234017e383ab667ef88d; _tb_token_=f60ee6eeeb3fe; tfstk=dEwBfWDMPeYQ2aHskBsa1qKLCcD7Oy6VF3i8mupe2vHdF0U45bpPtvlSFP3aL2rEpTi8uPG8z4rex544DpyFtYJSKYDRuZWV3MqnEYBC-c7VkXYd0C-O3tr3xHod0lBVrtfd4GGRnpx5Pl76Bd9ACFkQHiQ5PRiOxqEBJpobBDGikkeBnO5v3qs8BQtsiLisuGs6ZQfuLqHO.; l=fBIQOzNINiq0KRtBBO5Churza77O2COb8sPzaNbMiIEGa6Th1elM8NC61q3pRdtjQT5Y1etyzs0aOdhw5Ja38xOe7pP-OC0eQKp28eM3N7AN.; isg=BGhow2fRmMKnVLTcoTZoExvVOVZ6kcybJYC5NSKc4OPWfQnnyqPpKsX_dQ2NzYRz; x5sec=7b22617365727665723b32223a226137316262343934343964303833653439366131306266303238643831333839434b667a703659474550666873386175362b3461476738794d6a45324d6a41354d544d314d7a67774f7a4969436d4e6863484e736157526c646a49776b4b48466e76762f2f2f2f2f41554144227d',
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

    headers = {
        'Cookie': 't=ec0d5bd680cef4c43c9f71708db31058; cna=BRxOHd8VWAICAXGhLjZWD5TR; xlly_s=1; sgcookie=E100H0swvfyYsdVvyTSCrnObIsrV9Aq5T474B8w3cwP5nWHOe6gtbUcYZOtKadjZUZn5FaAW%2BQ1uJQLhLtsuUfTrufcHNomxvIPXmNQua6gPTPE%3D; uc3=vt3=F8dCsGCl3JWCOZIAnLM%3D&id2=UUpgQEvyiTEr4C708g%3D%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D&nk2=F5RDLjqWCLCCNe6Q0ac%3D; lgc=tb627551502528; uc4=id4=0%40U2gqz6QY%2B2LU45CVgCnTHhyjjD3pXce2&nk4=0%40FY4I7WSY2SzxeSCD9wJSplBYHJHaEX%2BF0g%3D%3D; tracknick=tb627551502528; _cc_=WqG3DMC9EA%3D%3D; thw=xx; mt=ci=0_1; _uetsid=2e532be02f4f11ee80918f9d985d2979; _uetvid=dc870040ea5911ed8305a55f0f12c1b7; _m_h5_tk=bffc85d673ab2f3d0eebe9f130993d22_1690891184157; _m_h5_tk_enc=10d0b322cedd523f3f588213614f9e04; hng=VN%7Czh-CN%7CVNM%7C704; _gid=GA1.2.1343417350.1690881464; _ga=GA1.1.658097477.1690881463; _ga_YFVFB9JLVB=GS1.1.1690881463.1.0.1690881469.0.0.0; _ga_JBTWV3NHSY=GS1.1.1690881463.1.0.1690881469.54.0.0; cookie2=1c358ce26fd4234017e383ab667ef88d; _tb_token_=f60ee6eeeb3fe; tfstk=dEwBfWDMPeYQ2aHskBsa1qKLCcD7Oy6VF3i8mupe2vHdF0U45bpPtvlSFP3aL2rEpTi8uPG8z4rex544DpyFtYJSKYDRuZWV3MqnEYBC-c7VkXYd0C-O3tr3xHod0lBVrtfd4GGRnpx5Pl76Bd9ACFkQHiQ5PRiOxqEBJpobBDGikkeBnO5v3qs8BQtsiLisuGs6ZQfuLqHO.; l=fBIQOzNINiq0KRtBBO5Churza77O2COb8sPzaNbMiIEGa6Th1elM8NC61q3pRdtjQT5Y1etyzs0aOdhw5Ja38xOe7pP-OC0eQKp28eM3N7AN.; isg=BGhow2fRmMKnVLTcoTZoExvVOVZ6kcybJYC5NSKc4OPWfQnnyqPpKsX_dQ2NzYRz; x5sec=7b22617365727665723b32223a226137316262343934343964303833653439366131306266303238643831333839434b667a703659474550666873386175362b3461476738794d6a45324d6a41354d544d314d7a67774f7a4969436d4e6863484e736157526c646a49776b4b48466e76762f2f2f2f2f41554144227d',
        'Referer': detail_link,
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

    url = detail_link
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as resp:
            content = await resp.text()
            soup = BeautifulSoup(content, 'html.parser')
            script_tags = soup.find_all("script")
            print(soup.find_all("h3", attrs={"data-title": True}))
        for script_tag in script_tags:
            script_content = script_tag.string
            # if script_content and 'g_config' in script_content:
            #     print(script_content.find('g_config'))
    # response = requests.get(url, headers=headers)
    # if response.status_code == 200:
    #     content = response.text
    #     soup = BeautifulSoup(content, "html.parser")
    #     li_elements_with_data_value = soup.find_all("li", attrs={"data-value": True})
    #     script_test = soup.find_all("script")
    #     for script in script_test:
    #         script_script = script.string
    #         if script_script and "window._config" in script_script:
    #             startIndex = script_script.find("url")
    #             endIndex = script_script.find("languageConfigJson")
    #             json_content = script_script[startIndex + 6: endIndex]
    #             print(script_script)
    #             # detailValue(json_content)
    #             # print("Json content: " + script_script)
    #         # if script_script and "window._config" in script_script:
    #         #     print("Url " + script_script[200])
    #
    #     listName = {}
        # for li in li_elements_with_data_value:
        #     data_value = li["data-value"]
        #     value = li.span.text.strip()
        #     listName[data_value] = value
        # script_tags = soup.find_all("script")
        # for script_tag in script_tags:
        #     script_content = script_tag.string
        #     if script_content and "Hub.config.set" in script_content:
        #         start_index = script_content.find("wholeSibUrl      : '")
        #         end_index = script_content.find("tradeContract',")
        #         json_content = script_content[start_index + 20: end_index]
        #         detailLinkValue = "https:" + json_content
    # detailLink(url, detailLinkValue, listName)
    return detail_link

def detailValue (linkDetail: str):
    content = linkDetail[0: 181]
    print("https: " + content)