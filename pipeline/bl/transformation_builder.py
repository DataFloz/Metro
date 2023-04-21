import os
import ast
from bl.http_transformer_runner import HttpTransformer
from bl.container_transformer_runner import ContainerTransformer

def build_transformation():
    transformation = ast.literal_eval(os.environ.get('transformation'))
    transformation_type = transformation['type']

    if transformation_type == 'http':
        transformation = HttpTransformer(transformation['http_url'])
    elif transformation_type == 'container':
        transformation = ContainerTransformer(transformation['container_url'])
    else:
        raise Exception(f'transformation type {transformation_type} is not supported yet!')

    return transformation
