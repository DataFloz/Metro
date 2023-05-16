class PipelineInfrastructureRunner:
    '''Abstract class for the pipeline infrastructure details'''
    def __init__(self):
        pass

    def as_dict(self):
        ''' Abstract function for convert config to dict'''
        return self.__dict__
