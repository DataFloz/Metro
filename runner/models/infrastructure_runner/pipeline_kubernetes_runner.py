from models.infrastructure_runner.pipeline_infrastructure_runner import PipelineInfrastructureRunner


class PipelineKubernetesRunner(PipelineInfrastructureRunner):
    def __init__(self, cluster_server, cluster_name, context_name, context_user):
        self.infrustructure_type = 'kubernetes'
        self.cluster_server = cluster_server
        self.cluster_name = cluster_name
        self.context_name = context_name
        self.context_user = context_user
