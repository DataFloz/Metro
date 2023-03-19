from configuration_reader import read_configuration_file
from pipe_runner import run_pipeline

def main():
    print("start build pipelines")
    pipelines_configuration = read_configuration_file()

    print("run each pipeline with its configuration")
    for pipeline_config in pipelines_configuration:
        run_pipeline(pipeline_config)

    print('end build and run pipelines')
main()