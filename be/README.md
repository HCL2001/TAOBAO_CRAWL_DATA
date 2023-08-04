
Change the configurations to suit your system.
Recommended : /www/wwwroot/megasop-crawl-data

****
    www
      |__wwwroot
                |__megasop-crawl-data
                                     |__fe
                                     |__megasop-crawl-data
****

****
    megasop-crawl-data
    |_____api
    |_____crawl
    |_____myenv
    |_____script_database
    |Readme.md
****
https://ibb.co/5YcrVRp

Import script to create database.
### Use Command prompt from: megasop-crawl-data
```bash
python -m venv venv
```
***
### B1 :  cmd from megasop-crawl-data : 
```bash
venv\Scripts\activate
```
```bash
pip install -r requirements.txt
```

### B2 : Start API : 
```bash
cd .\api\ 
```
```bash
uvicorn main:app --reload 
```


- swagger API : http://127.0.0.1:8000/docs#/
***
### API Get_Data:
    - input any keyword. Example :"nuoc hoa nam" or "nước hoa"
    - Reponse : A product list have more info : name , price , brand_name , link
    - Copy link or more link to API Save_Link
***

### API Save_Link :
  - Past link copy from reponse API Get_Data and submit

***

### B3: Start auto crwal after 1 one minutes
```bash
cd .\crawl\crawl\ 
```
```bash
python megasop.py
```

View database