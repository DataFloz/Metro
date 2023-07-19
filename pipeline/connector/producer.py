from utils.logger import logger

class AbstractProducer():
    '''Class responsible of producing and creating prooducer.'''
    def __init__(self, configuration: dict):
        pass


    def produced_callback(self, err, msg):
        '''Callback after produce
            Args:
                err: if the produce failed
                msg: the msg that produced'''
        if err is not None:
            logger.error("Failed to deliver message: %s:%s", str(msg), str(err))
        else:
            logger.error("Message produced: %s", str(msg))

    def produce(self, values):
        '''Function produce msg
            Args:
                values: the values that will be produce'''
        pass
