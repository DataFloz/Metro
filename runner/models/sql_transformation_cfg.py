from models.transformation_cfg import TransformationConfig


class SQLTransformationCfg(TransformationConfig):
    def __init__(self, sql_query):
        self.sql_query = sql_query
        self.type = 'sql'
        
    def as_dict(self):
        return {
            'sql_query': self.sql_query,
            'type': self.type
        }
