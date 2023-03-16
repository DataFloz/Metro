from configuration_reader import read_configuration_file


def main():
    print("start build pipelines")
    pipelines_configuration = read_configuration_file()

    print("run each pipeline with its configuration")

main()