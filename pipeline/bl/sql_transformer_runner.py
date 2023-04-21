import sqlite3
import pandas as pd
from bl.transformer_runner_interface import TransforerRunnerInterface


class SQLTransformer(TransforerRunnerInterface):
    def __init__(self, query):
        self.query = query

    def run_logic(self, msg):
        data_frame = pd.DataFrame.from_dict(msg)
        conn = sqlite3.connect(":memory:")

        # msg is name the query will always use
        data_frame.to_sql('msg', conn, index=False)

        query_result = pd.read_sql_query(self.query, conn)

        return query_result
