import ast
import sqlite3
import pandas as pd
from bl.transformer_runner_interface import TransforerRunnerInterface


class SQLTransformer(TransforerRunnerInterface):
    '''Inhierent from TransforerRunnerInterface: responsible for SQL transformation.'''
    def __init__(self, query):
        self.query = query

    def run_logic(self, msg):
        print(msg)
        msg_value = msg.value()
        print(msg_value)
        encode_msg_value = (msg.value().decode('utf-8'))
        print(encode_msg_value)

        message_data = ast.literal_eval(encode_msg_value)
        print([message_data])

        data_frame = pd.DataFrame.from_dict([message_data])
        conn = sqlite3.connect(":memory:")

        # msg is name the query will always use
        data_frame.to_sql('msg', conn, index=False)

        query_result = pd.read_sql_query(self.query, conn)
        print(query_result)
        return query_result.to_dict(orient="records")
