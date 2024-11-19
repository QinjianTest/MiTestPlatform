# core/logic/tests.py
import requests
import csv
import json
import logging
from core.logic.login import login
from core.config.config_loader import BASE_URL, EMAIL, PASSWORD
from core.config.logger_setup import setup_logging

# 初始化日志配置
setup_logging()

def watch_lists(file_path):
    # 从这里开始使用 logging 记录日志
    logging.info("Starting watch_lists test execution")
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            casename = row['casename']
            method = row['method']
            api_path = row['api_path']
            data = json.loads(row['data']) if row['data'] else None
            expected_success = row['expected_success'].lower() == 'true'

            url = BASE_URL + api_path

            # 登录并获取 remember-me-token
            remember_me_token = login(EMAIL, PASSWORD)

            if isinstance(remember_me_token, dict) and 'error' in remember_me_token:
                logging.error(f"Login failed: {remember_me_token['error']}")
                continue

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
                'Referer': BASE_URL,
                'Remember-Me-Token': remember_me_token,
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
                logging.info(f"Executing {method} request for {casename} with URL: {url}")
                if method.upper() == 'GET':
                    response = requests.get(url, headers=headers)
                elif method.upper() == 'POST':
                    response = requests.post(url, headers=headers, data=data)

                response.raise_for_status()

                response_data = response.json()

                # 断言 success 字段
                assert response_data.get('success') == expected_success, \
                    f"Assertion failed for {casename}: expected {expected_success}, got {response_data.get('success')}"
                logging.info(f"Test for {casename} passed.")
            except requests.exceptions.RequestException as e:
                logging.error(f"Request failed for {casename}: {str(e)}")
            except AssertionError as e:
                logging.error(str(e))
