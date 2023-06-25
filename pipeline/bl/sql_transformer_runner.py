import sqlite3
import pandas as pd
from bl.transformer_runner_interface import TransforerRunnerInterface
from utils.logger import logger

class SQLTransformer(TransforerRunnerInterface):
    '''Inhierent from TransforerRunnerInterface: responsible for SQL transformation.'''
    def __init__(self, query):
        self.query = query

    def run_logic(self, msg):
        logger.info("run the SQL transformer logic")

        data_frame = pd.DataFrame.from_dict([msg])
        conn = sqlite3.connect(":memory:")

        # msg is name the query will always use
        data_frame.to_sql('msg', conn, index=False)

        query_result = pd.read_sql_query(self.query, conn)
        logger.debug("result of logic run: %s", query_result)

        return query_result.to_dict(orient="records")
