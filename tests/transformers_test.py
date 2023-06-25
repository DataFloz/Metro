import unittest
import sys

sys.path.insert(0, './pipeline')
from pipeline.bl.sql_transformer_runner import SQLTransformer

class TransformerTest(unittest.TestCase):
    def test(self):        
        self.assertTrue(True)
  
    def test_sql(self):
        test_query = '''
            SELECT *, age > 18 as is_adult FROM msg
        '''
        sql_transformer = SQLTransformer(test_query)
        payload = {
            "name": "ofir elarat",
            "age": 20
        }
        expected = {
            "name": "ofir elarat",
            "age": 20,
            "is_adult": True
        }

        real = sql_transformer.run_logic(payload)

        self.assertEqual(real[0].items(), expected.items())
    
if __name__ == '__main__':
    unittest.main()