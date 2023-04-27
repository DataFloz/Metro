import json
import docker
from utils.logger import logger
from bl.transformer_runner_interface import TransforerRunnerInterface


class ContainerTransformer(TransforerRunnerInterface):
    '''Inhierent from TransforerRunnerInterface: responsible for container transformation.'''
    def __init__(self, image_name):
        self.image_name = image_name

    def run_logic(self, msg):
        logger.info("run the container transformer logic")
        client = docker.from_env()
        data_str = json.dumps(msg)
        data_str = f"'{msg}'"
        container = client.containers.run(self.image_name,command=f"python main.py {data_str}",
                                            detach=True)
        container.wait()
        result = container.logs().decode('utf-8')
        logger.debug("res: %s", container.logs().decode('utf-8'))

        return result
