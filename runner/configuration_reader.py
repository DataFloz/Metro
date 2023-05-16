import yaml
from utils.logger import logger
from models.metro_cfg import MetroConfig


CONFIGURATION_FILE = './runner/cfg/metro.yaml'

def read_configuration_file()->MetroConfig:
    '''Read Metro yml configuration file
       Returns:
        class object MetroConfig'''
    metro_config = {}
    with open(CONFIGURATION_FILE, 'r', encoding='utf-8') as stream:
        try:
            configuration_data=yaml.safe_load(stream)
            metro_config = MetroConfig.from_config_dict(configuration_data)
        except yaml.YAMLError as err:
            logger.error(err)

    return metro_config
