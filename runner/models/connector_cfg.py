class ConnectorConfig:
    def __init__(self, name, brokers, group_id):
        self.name = name
        self.brokers = brokers
        self.group_id = group_id

    def as_dict(self):
        return self.__dict__
