from flask import Flask, jsonify
from utils.logger import logger
from configuration_reader import read_configuration_file
from pipe_runner import run_pipeline

app = Flask(__name__)

@app.route('/api/pipelines')
def get_pipelines():
    '''Route for getting the metro configuration as json.'''
    metro_configuration = read_configuration_file()

    return jsonify(metro_configuration.as_dict())

@app.route('/api/deploy-pipelines')
def deploy_pipelines():
    '''Route for rollout the current metro configuration.'''
    pipelines_configuration = read_configuration_file()

    logger.info("run each pipeline with its configuration")
    kafka_connector = pipelines_configuration.connector
    run_pipeline(pipelines_configuration.pipelines, kafka_connector, pipelines_configuration.pipeline_infrastructure_runner)

    logger.info('end build and run pipelines')

    return 'succeed depoloy pipelines', 200
