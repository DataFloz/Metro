import docker
class Transformer():
    def __init__(image_url):
        client = docker.from_env()

        client.containers.run(image_url)

        print("here we will initiate the transformer with the pipeline config")

    def run_logic(msg):
        print("run the specific FAAS logic and return the result")
        
        return {}