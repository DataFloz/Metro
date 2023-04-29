from models.transformations.transformation_cfg import TransformationConfig


class HttpTransformationCfg(TransformationConfig):
    '''Inhierent from TransformationConfig: responsible for HTTP transformation config'''
    def __init__(self, http_url, headers={}, params={}):
        self.http_url = http_url
        self.type = 'http'
        self.headers = headers
        self.params = params

    def as_dict(self):
        return {
            'http_url': self.http_url,
            'headers': self.headers,
            'params': self.params,
            'type': self.type
        }
