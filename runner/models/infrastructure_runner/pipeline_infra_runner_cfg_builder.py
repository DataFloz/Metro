
from models.infrastructure_runner.pipeline_container_runner import PipelineContainerRunner
from models.infrastructure_runner.pipeline_kubernetes_runner import PipelineKubernetesRunner


def from_config_dict(pipeline_infra_runner_dict):
    '''The function responsible to convert the pipeline infrastructure config
       Args:
        pipeline infrastructure dict
       Returns:
        PipelineInfrastructureRunner object'''
    infra = None
    if pipeline_infra_runner_dict["infrustructure_type"]=='container':
        infra = PipelineContainerRunner()
    if pipeline_infra_runner_dict["infrustructure_type"]=='kubernetes':
        infra = PipelineKubernetesRunner(
                        cluster_server=pipeline_infra_runner_dict["cluster_server"],
                        cluster_name=pipeline_infra_runner_dict["cluster_name"],
                        context_name=pipeline_infra_runner_dict["context_name"],
                        context_user=pipeline_infra_runner_dict["context_user"])

    return infra
