from models.pipline.transformations.container_transformation_cfg \
    import ContainerTransformationConfig
from models.pipline.transformations.http_transformation_cfg import HttpTransformationCfg
from models.pipline.transformations.pickle_transformation_cfg import PickleTransformationCfg
from models.pipline.transformations.sql_transformation_cfg import SQLTransformationCfg


def from_config_dict(pipeline_dict):
    '''Responsible to convert the transformation config
    Args: 
    pipeline: pipeline dict
    Returns:
    TranformationConfig object'''
    transfomation_type = pipeline_dict["transformation"]["type"]

    if transfomation_type == 'http':
        transformation = HttpTransformationCfg(pipeline_dict["transformation"]["http_url"],
                                            pipeline_dict["transformation"]["headers"],
                                            pipeline_dict["transformation"]["params"])
    elif transfomation_type == 'container':
        transformation = \
                ContainerTransformationConfig(pipeline_dict["transformation"]["container-image"])
    elif transfomation_type == 'sql':
        transformation = SQLTransformationCfg(pipeline_dict["transformation"]["sql_query"])
    elif transfomation_type == 'pickle':
        transformation = PickleTransformationCfg(pipeline_dict["transformation"]["file_name"])
    else:
        raise LookupError(f'transformation type {transfomation_type} is not supported yet!')

    return transformation
