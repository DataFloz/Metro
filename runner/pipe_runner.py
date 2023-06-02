from typing import List
from models.pipline.pipeline_config import PipelineConfig
from models.connector_cfg import ConnectorConfig
from models.infrastructure_runner.pipeline_infrastructure_runner import PipelineInfrastructureRunner
from models.infrastructure_runner.pipeline_container_runner import PipelineContainerRunner
from models.infrastructure_runner.pipeline_kubernetes_runner import PipelineKubernetesRunner
from pipeline_runner.container_runner import ContainerRunner
from pipeline_runner.kubernetes_runner import KubernetesRunner


def run_pipeline(pipelines: List[PipelineConfig], kafka_connector: ConnectorConfig,
                 pipeline_infrastructure_runner: PipelineInfrastructureRunner):
    ''' Run pipeline
        Args:
            pipelines: array of PipelineConfig object
            kafka_connector: ConnectorConfig object
            pipeline_infrastructure_runner: PipelineInfrastructureRunner object'''
    pipeline_runner = None
    if isinstance(pipeline_infrastructure_runner, PipelineContainerRunner):
        pipeline_runner = ContainerRunner(pipeline_infrastructure_runner)
    elif isinstance(pipeline_infrastructure_runner, PipelineKubernetesRunner):
        pipeline_runner = KubernetesRunner(pipeline_infrastructure_runner)

    for pipeline_config in pipelines:
        pipeline_runner.rollout(pipeline_config, kafka_connector)
