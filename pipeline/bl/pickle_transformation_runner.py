import pickle
from utils.logger import logger
from bl.transformer_runner_interface import TransforerRunnerInterface


class PickleTransformer(TransforerRunnerInterface):
    '''Inhierent from TransforerRunnerInterface: responsible for pickle transformation.'''
    def __init__(self, file_name):
        self.file_name = file_name

    def run_logic(self, msg):
        logger.info("run the pickle transformer logic")

        with open(f"/mnt/configs/{self.file_name}", 'rb') as file:
            model = pickle.load(file)
            msg["predict"] = model.predict(msg)

        logger.debug("result of logic run: %s", msg)

        return msg
