# core/login.py
import requests
from dotenv import load_dotenv
import os

# 加载 .env 文件中的环境变量
load_dotenv()

def login(email, password):
    base_url = os.getenv('BASE_URL')
    api_path = "/api/v1/customers/signin"
    url = base_url + api_path

    # 请求头
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'zh-TW,zh;q=0.9,pt-BR;q=0.8,pt;q=0.7,zh-CN;q=0.6,ko-KR;q=0.5,ko;q=0.4,hi-IN;q=0.3,hi;q=0.2,de-DE;q=0.1,de;q=0.1,es-ES;q=0.1,es;q=0.1,vi-VN;q=0.1,vi;q=0.1,th-TH;q=0.1,th;q=0.1,ms-MY;q=0.1,ms;q=0.1,id-ID;q=0.1,id;q=0.1,en-US;q=0.1,en;q=0.1,es-US;q=0.1',
        'Content-Length': '213',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'DeviceId': '',
        'Devicename': 'Chrome V130.0.0.0',
        'Eagleeye-Pappname': '1fb384qlq9c@056ac913dbee099',
        'Eagleeye-Sessionid': 'g5m453ns8nyiO4w8Xt4zeCpys4sy',
        'Eagleeye-Traceid': '1417742317310574596301017ee099',
        'Locale': 'zh-TW',
        'Origin': base_url,
        'Priority': 'u=1, i',
        'Referer': base_url,
        'Remember-Me-Token': '',
        'Sec-CH-UA': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'Sec-CH-UA-Mobile': '?0',
        'Sec-CH-UA-Platform': '"macOS"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Session-Token': '',
        'System': 'web',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'Webdeviceid': 'e41c8ff30647bbc4d862fce31eaed6a8'
    }

    # 请求参数
    data = {
        'email': email,
        'password': password,
        'rememberMe': 'true',
        'mobileNumber': '',
        'smsCode': '',
        'countryCallingCode': '852',
        'source': 'zh_website',
        'loadUrl': 'https%3A%2F%2Fdemo-app.mitrade.com%2F%23%2Faccount',
        'refererUrl': '',
        'ticket': ''
    }

    try:
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()

        # 提取响应头中的 remember-me-token
        remember_me_token = response.headers.get('remember-me-token', 'Token not found')
        return remember_me_token
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
