from configuration_reader import read_configuration_file
import json
import docker
from datetime import datetime
# from pipeline.bl.transformer_runner import Transformer

def main():
    print("start build pipelines")
    pipelines_configuration = read_configuration_file()

    print('end build pipelines')
main()