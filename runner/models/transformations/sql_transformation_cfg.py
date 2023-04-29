from models.transformations.transformation_cfg import TransformationConfig


class SQLTransformationCfg(TransformationConfig):
    '''Inhierent from TransformationConfig: responsible for SQL transformation config'''
    def __init__(self, sql_query):
        self.sql_query = sql_query
        self.type = 'sql'

    def as_dict(self):
        return {
            'sql_query': self.sql_query,
            'type': self.type
        }
