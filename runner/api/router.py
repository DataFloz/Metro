import json
from flask import Flask, jsonify
from configuration_reader import read_configuration_file
from pipe_runner import run_pipeline


app = Flask(__name__)

@app.route('/api/pipelines')
def get_pipelines():
    pipelines_configuration = read_configuration_file()
    
    return [json.dumps(pipeline.__dict__, indent=4, default=lambda x: x.__dict__) for pipeline in pipelines_configuration], 200

@app.route('/api/deploy-pipelines')
def deploy_pipelines():
    pipelines_configuration = read_configuration_file()
    
    print("run each pipeline with its configuration")
    for pipeline_config in pipelines_configuration:
        run_pipeline(pipeline_config)

    print('end build and run pipelines')

    return 'succeed depoloy pipelines', 200