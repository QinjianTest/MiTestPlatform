# config_loader.py
# 切换环境配置
import yaml
import os

def load_config(env_name):
    with open('config.yml', 'r') as file:
        config = yaml.safe_load(file)
        return config['environments'].get(env_name)

# 获取当前环境变量，默认为 development
current_env = os.getenv('ENV', 'development')
environment_config = load_config(current_env)

BASE_URL = environment_config['BASE_URL']
EMAIL = environment_config['EMAIL']
PASSWORD = environment_config['PASSWORD']
