# MiTestPlatform

MiTestPlatform：Django测试平台

## 迭代更新
*工作间隙更新*
1. 2024-11-7 环境与架构搭建
2. 2024-11-8 接口示例

## 安装与运行

1. 克隆项目代码：

   ```bash
   git clone xxx
   cd MiTestPlatform
   ```
2. 创建虚拟环境并激活
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # 对于 Windows 使用 .venv\Scripts\activate
    ```
3. 安装项目依赖
    ```bash
   pip install -r requirements.txt
    ```
4. 运行 Django 开发服务器
    ```bash
    python manage.py runserver 8766
    ```
5. 访问
    ```bash
    http://127.0.0.1:8766/
    ```  

## 配置
1. 配置文件在根目录的config.yml文件，可以使用config.yml.bak参考配置，执行不同环境命令参考
    ```bash
   ENV=production python run_test.py
   ```
2. 日志配置放在core/logger_setup.py里面，日志生成在根目录的/logs，查询日志通过UUID定位
3. 用例放在cases/test_cases.csv里面