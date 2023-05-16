class ConnectorConfig:
    '''Class represent the metro configuration'''
    def __init__(self, name, type, brokers, group_id):
        self.name = name
        self.type = type
        self.brokers = brokers
        self.group_id = group_id

    def as_dict(self):
        '''Function for convert config to dict'''
        return self.__dict__

    @classmethod
    def from_config_dict(cls, connector_dict):
        '''The function responsible to convert the connector config
            Args:
            connector dict
            Returns:
            ConnectorConfig object'''
        connector_config = cls(name=connector_dict["name"],
                                       type=connector_dict["type"],
                                       brokers=connector_dict["brokers"],
                                       group_id=connector_dict["group_id"])

        return connector_config