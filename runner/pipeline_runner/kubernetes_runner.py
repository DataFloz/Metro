from kubernetes import client, config
from pipeline_runner.abstract_runner import AbstractRunner
from models.connector_cfg import ConnectorConfig
from models.pipline.pipeline_config import PipelineConfig

# Define the Kubernetes configuration.
kubeconfig = {
    "apiVersion": "v1",
    "clusters": [
        {
            "cluster": {
                "server": "https://my-kubernetes-cluster.example.com",
                "certificate-authority-data": "<CA_CERT_DATA>",
            },
            "name": "my-kubernetes-cluster",
        }
    ],
    "contexts": [
        {
            "context": {
                "cluster": "my-kubernetes-cluster",
                "user": "my-user",
            },
            "name": "my-context",
        }
    ],
    "users": [
        {
            "name": "my-user",
            "user": {
                "client-certificate-data": "<CLIENT_CERT_DATA>",
                "client-key-data": "<CLIENT_KEY_DATA>",
            },
        }
    ],
    "current-context": "my-context",
}

class KubernetesRunner(AbstractRunner):
    def __init__(self):
        super().__init__()
        # Load the Kubernetes configuration.
        # config.load_kube_config(config_dict=kubeconfig)
        config.load_kube_config()
        self.api = client.CoreV1Api()

    def rollout(self, pipeline_configuration: PipelineConfig, kafka_connector: ConnectorConfig):
        # create a container with environment variables
        container = client.V1Container(
            name="my-container",
            image="my-image:latest",
            image_pull_policy="Never",
            env=[
                client.V1EnvVar(name="MY_ENV_VAR", value="my value"),
            ]
        )

        # create a pod spec with the container
        pod_spec = client.V1PodSpec(containers=[container])

        # create the pod object
        pod = client.V1Pod(
            metadata=client.V1ObjectMeta(name="my-pod"),
            spec=pod_spec
        )

        # create the pod using the Kubernetes API
        self.api.create_namespaced_pod(namespace="default", body=pod)
