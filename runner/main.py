from api.router import app
from configuration_reader import read_configuration_file
from pipe_runner import run_pipeline


def main():
    print("runner api is up")

    port = 5000
    if __name__ == '__main__':
        app.run('0.0.0.0', port)

main()