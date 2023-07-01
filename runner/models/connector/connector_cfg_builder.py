
from models.connector.kafka_connector_cfg import KafkaConnectorConfig

def from_config_dict(connector_dict):
    '''The function responsible to convert the connector config
        Args:
        connector dict
        Returns:
        ConnectorConfig object'''
    connector_config = None

    if connector_dict["type"] == 'kafka': 
        connector_config = KafkaConnectorConfig(name=connector_dict["name"],
                                            brokers=connector_dict["brokers"],
                                            group_id=connector_dict["group_id"])

    return connector_config