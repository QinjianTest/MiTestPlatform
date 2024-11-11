# core/views.py
from django.shortcuts import render
import requests
import json
from dotenv import load_dotenv
import os

# 加载 .env 文件中的环境变量
load_dotenv()

def example_view(request):
    base_url = os.getenv('BASE_URL')
    api_path = "/api/v1/customers/signin"
    url = base_url + api_path
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')

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
        response.raise_for_status()  # 检查请求是否成功
        news_data = response.json()  # 获取完整的 JSON 响应

        # 断言 success 字段为 True
        if news_data.get('success') == True:
            assertion_result = "Assertion passed: 'success' is True."
        else:
            assertion_result = "Assertion failed: 'success' is not True."

        news_data_str = json.dumps(news_data, ensure_ascii=False, indent=4)  # 将 JSON 转换为格式化的字符串
    except requests.exceptions.RequestException as e:
        news_data_str = f"Error fetching data: {str(e)}"  # 如果请求失败，返回错误信息
    except AssertionError as e:
        assertion_result = str(e)  # 如果断言失败，返回断言错误信息

    # 将数据传递给模板，包括断言结果
    return render(request, 'core/example.html', {
        'news_data_str': news_data_str,
        'assertion_result': assertion_result
    })
