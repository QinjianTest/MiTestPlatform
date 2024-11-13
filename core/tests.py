# core/tests.py
import requests
from .login import login
import os
from dotenv import load_dotenv

# 加载 .env 文件中的环境变量
load_dotenv()

def watch_lists():
    # 登录并获取 remember-me-token
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')
    remember_me_token = login(email, password)

    if isinstance(remember_me_token, dict) and 'error' in remember_me_token:
        print("Login failed:", remember_me_token['error'])
        return

    # 准备 GET 请求
    base_url = os.getenv('BASE_URL')
    api_path = "/api/v1/customers/watch-lists"
    url = base_url + api_path

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'zh-CN,zh;q=0.9,sk;q=0.8,cs;q=0.7,en-US;q=0.6,en;q=0.5',
        'DeviceId': '',
        'Devicename': 'Chrome V131.0.0.0',
        'Eagleeye-Pappname': '1fb384qlq9c@056ac913dbee099',
        'Eagleeye-Sessionid': 'n4mvI3R3fL3svt2Ier67v1vrjv6j',
        'Eagleeye-Traceid': 'd36b18d617314962006001101ee099',
        'Locale': 'zh-TW',
        'Mode': 'REAL_MONEY',
        'Priority': 'u=1, i',
        'Referer': base_url,
        'Remember-Me-Token': remember_me_token,  # 使用从登录请求中获取的 token
        'Sec-CH-UA': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'Sec-CH-UA-Mobile': '?0',
        'Sec-CH-UA-Platform': '"macOS"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Session-Token': 'f6a686a7-54b9-428d-841c-0527dad20c2a',
        'System': 'web',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'Webdeviceid': 'e41c8ff30647bbc4d862fce31eaed6a8'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        # 解析响应数据
        response_data = response.json()

        # 断言 success 字段为 True
        assert response_data.get('success') == True, "Assertion failed: 'success' is not True"
        print("Assertion passed: 'success' is True.")
        print("Watch lists:", response_data.get('value'))
    except requests.exceptions.RequestException as e:
        print("Request failed:", str(e))
    except AssertionError as e:
        print(str(e))
