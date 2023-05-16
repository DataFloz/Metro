from models.infrastructure_runner.pipeline_infrastructure_runner import PipelineInfrastructureRunner


class PipelineContainerRunner(PipelineInfrastructureRunner):
    def __init__(self):
        self.infrustructure_type = 'container'
