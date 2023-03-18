from configuration_reader import read_configuration_file
import json
import docker
from datetime import datetime
# from pipeline.bl.transformer_runner import Transformer

def main():
    client = docker.from_env()
    now = datetime.now()
    
    # print("now =", now)

    # dd/mm/YY H:M:S
    dt_string = now.strftime('%F %T.%f')[:-3]
    print("date and time =", dt_string)
    # print("start build pipelines")
    # pipelines_configuration = read_configuration_file()
    client.containers.run("test")

    now = datetime.now()
    
    # print("now =", now)

    # dd/mm/YY H:M:S
    dt_string = now.strftime('%F %T.%f')[:-3]
    print("date and time =", dt_string)

    # for i in pipelines_configuration['pipelines']:
    #     print(i)
    #     # transformer = Transformer()   
    # # print(pipelines_configuration['pipelines'][0]['transformation'])
    # # print("run each pipeline with its configuration")

main()