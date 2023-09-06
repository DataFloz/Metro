
from models.connector.kafka_connector_cfg import KafkaConnectorConfig
from models.connector.redis_connector_cfg import RedisConnectorConfig


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
    elif connector_dict["type"] == 'redis':
        connector_config = RedisConnectorConfig(name=connector_dict["name"],
                                                host=connector_dict["host"],
                                                port=connector_dict["port"])
    return connector_config
