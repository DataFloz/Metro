import docker
import json

from bl.iTransformerRunnerInterface import iTransforerRunnerInterface


class ContainerTransformer(iTransforerRunnerInterface):
    def __init__(self, image_name):
        # print("here we will initiate the transformer with the pipeline config")
        self.image_name = image_name
        pass

    def run_logic(self, msg):
        print("run the specific FAAS logic and return the result")
        client = docker.from_env()
        str = json.dumps(msg)
        str = f"'{msg}'"
        container = client.containers.run(self.image_name,command=f"python main.py {str}", detach=True)
        container.wait()
        result = container.logs().decode('utf-8')
        print(f"res: {container.logs().decode('utf-8')}")

        return result