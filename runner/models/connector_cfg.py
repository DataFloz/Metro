class ConnectorConfig:
    def __init__(self, name, type, brokers, group_id):
        self.name = name
        self.type = type
        self.brokers = brokers
        self.group_id = group_id

    def as_dict(self):
        return self.__dict__
