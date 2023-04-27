from utils.logger import logger
from api.router import app

def main():
    ''' The main function is the runner entrypoint. '''
    logger.info("runner api is up")

    port = 5000
    if __name__ == '__main__':
        app.run('0.0.0.0', port)

main()
