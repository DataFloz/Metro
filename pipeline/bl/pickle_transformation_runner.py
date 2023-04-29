import ast
import pickle
from utils.logger import logger
from bl.transformer_runner_interface import TransforerRunnerInterface


class PickleTransformer(TransforerRunnerInterface):
    '''Inhierent from TransforerRunnerInterface: responsible for pickle transformation.'''
    def __init__(self, file_name):
        self.file_name = file_name

    def run_logic(self, msg):
        logger.info("run the pickle transformer logic")
        msg_value = msg.value()
        encode_msg_value = msg_value.decode('utf-8')
        message_data = ast.literal_eval(encode_msg_value)

        with open(f"/mnt/configs/{self.file_name}", 'rb') as f:
            model = pickle.load(f)
            message_data["predict"] = model.predict(message_data)

      
        logger.debug("result of logic run: %s", message_data)

        return message_data
