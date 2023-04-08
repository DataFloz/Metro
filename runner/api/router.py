import json
from flask import Flask, Response, jsonify, request
from configuration_reader import read_configuration_file
from pipe_runner import run_pipeline


app = Flask(__name__)

@app.route('/api/pipelines')
def get_pipelines():
    metro_configuration = read_configuration_file()
    
    return jsonify(metro_configuration.as_dict())

@app.route('/api/pipeline_by_name/')
def get_pipeline_by_name():
    metro_configuration = read_configuration_file()
    name1 = request.args.get('name')
    # print(f'name: {name}')
    jsoned =jsonify(metro_configuration.as_dict())
    # input_dict = json.loads(jsoned)
    input_dict = jsoned
    print('whgat')
    print(str(input_dict))
    # print(input_dict['pipelines'])
    output_dict = [x for x in input_dict["pipelines"] if x['name'] == name1]

    connectos = jsoned['connectors']
    name = jsoned['name']
    result = {'connectors': connectos, 'name': name, 'pipelines': output_dict }
    output_json = json.dumps(result)

    return result


@app.route('/api/deploy-pipelines')
def deploy_pipelines():
    pipelines_configuration = read_configuration_file()
    
    print("run each pipeline with its configuration")
    kafka_connector = next((connector for connector in
                             pipelines_configuration.connectors if connector.type == 'kafka'), None)
    for pipeline_config in pipelines_configuration.pipelines:
        run_pipeline(pipeline_config, kafka_connector)

    print('end build and run pipelines')

    return 'succeed depoloy pipelines', 200
