from models.connector.connector_cfg import ConnectorConfig

class RedisConnectorConfig(ConnectorConfig):
    '''Class represent the metro configuration'''
    def __init__(self, name, host, port):
        super().__init__(name, 'redis')
        self.host = host
        self.port = port
