from models.connector.connector_cfg import ConnectorConfig

class KafkaConnectorConfig(ConnectorConfig):
    '''Class represent the metro configuration'''
    def __init__(self, name, brokers, group_id):
        super().__init__(name, 'kafka')
        self.brokers = brokers
        self.group_id = group_id
