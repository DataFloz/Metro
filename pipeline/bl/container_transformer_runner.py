import json
import docker

from bl.iTransformerRunnerInterface import iTransforerRunnerInterface


class ContainerTransformer(iTransforerRunnerInterface):
    def __init__(self, image_name):
        # print("here we will initiate the transformer with the pipeline config")
        self.image_name = image_name
        pass

    def run_logic(self, msg):
        print("run the specific FAAS logic and return the result")
        client = docker.from_env()
        data_str = json.dumps(msg)
        data_str = f"'{msg}'"
        container = client.containers.run(self.image_name,command=f"python main.py {data_str}", detach=True)
        container.wait()
        result = container.logs().decode('utf-8')
        print(f"res: {container.logs().decode('utf-8')}")

        return result
