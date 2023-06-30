import unittest
import sys

sys.path.insert(0, './runner')
from runner.models.metro_cfg import MetroConfig


class ConfigurationConverterTest(unittest.TestCase):
    def test_metro_full(self):
        payload = {
            "name": 'test-config',
            "running_infrastructure": {
                "infrustructure_type": 'container'
            },
            "connector": {
                "name": 'test-kafka-connector',
                "type": 'kafka',
                "brokers": 'kafka:29092',
                "group_id": 'some_group_id'
            },
            "pipelines": [
                {
                    "name": 'test-pipeline',
                    "input": {
                        "type": 'kafka',
                        "topic": 'test-in-topic'
                    },
                    "output": {
                        "type": 'kafka',
                        "topic": 'test-out-topic'
                    },
                    "transformation": {
                        "type": 'sql',
                        "sql_query": 'SELECT *, first_name || " " || last_name as full_name FROM msg'
                    }
                }
            ]
        }

        expected = {
            "name": 'test-config',
            "pipeline_infrastructure_runner": {
                "infrustructure_type": 'container'
            },
            "connector": {
                "name": 'test-kafka-connector',
                "type": 'kafka',
                "brokers": 'kafka:29092',
                "group_id": 'some_group_id'
            },
            "pipelines": [
                {
                    "name": 'test-pipeline',
                    "input": {
                        "topic": 'test-in-topic'
                    },
                    "output": {
                        "topic": 'test-out-topic'
                    },
                    "transformation": {
                        "type": 'sql',
                        "sql_query": 'SELECT *, first_name || " " || last_name as full_name FROM msg'
                    }
                }
            ]
        }

        real = MetroConfig.from_config_dict(payload)

        self.assertEqual(real.as_dict().items(), expected.items())


if __name__ == '__main__':
    unittest.main()
