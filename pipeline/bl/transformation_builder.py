import os
import ast
from bl.http_transformer_runner import HttpTransformer
from bl.container_transformer_runner import ContainerTransformer
from bl.sql_transformer_runner import SQLTransformer
from bl.pickle_transformation_runner import PickleTransformer

def build_transformation():
    """ Create the right transformation object by the env data (factory creator)
        Returns:
           TransforerRunnerInterface abstract object"""
    transformation = ast.literal_eval(os.environ.get('transformation'))
    transformation_type = transformation['type']

    if transformation_type == 'http':
        transformation = HttpTransformer(transformation['http_url'])
    elif transformation_type == 'container':
        transformation = ContainerTransformer(transformation['container_url'])
    elif transformation_type == 'sql':
        transformation = SQLTransformer(transformation['sql_query'])
    elif transformation_type == 'pickle':
        transformation = PickleTransformer(transformation['file_name'])
    else:
        raise LookupError(f'transformation type {transformation_type} is not supported yet!')

    return transformation
