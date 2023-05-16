from models.infrastructure_runner.pipeline_infrastructure_runner import PipelineInfrastructureRunner


class PipelineKubernetesRunner(PipelineInfrastructureRunner):
    def __init__(self):
        self.infrustructure_type = 'kubernetes'
