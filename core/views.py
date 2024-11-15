# core/views.py
from django.shortcuts import render
import requests
from dotenv import load_dotenv
import os
from .login import login

# 加载 .env 文件中的环境变量
load_dotenv()

def example_view(request):
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')

    # 调用 login.py 中的 login 函数
    response = login(email, password)

    # 初始化断言结果和响应数据
    assertion_result = "Assertion not performed."
    response_data = {}
    response_status = 'N/A'
    response_text = 'No response'

    # 检查响应
    if isinstance(response, requests.Response):
        response_data = response.json()
        response_status = response.status_code
        response_text = response.text
        # 断言 success 字段为 True
        if response_data.get('success'):
            assertion_result = "Assertion passed: 'success' is True."
        else:
            assertion_result = "Assertion failed: 'success' is not True."
    elif isinstance(response, dict) and 'error' in response:
        assertion_result = "Request failed."
        response_text = response['error']

    # 将数据传递给模板
    return render(request, 'core/example.html', {
        'response_data': response_data,
        'assertion_result': assertion_result,
        'response_status': response_status,
        'response_text': response_text
    })


def get_token(request):
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')

    # 调用 login.py 中的 login 函数
    remember_me_token = login(email, password)

   # 将数据传递给模板
    return render(request, 'core/example.html', {
        'remember_me_token': remember_me_token
    })