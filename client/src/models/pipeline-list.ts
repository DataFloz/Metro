import { KafkaConnector, RedisConnector } from './connector';
import { Pipeline } from './pipeline';

export interface PipelineList {
    name: string;
    pipelines: Pipeline[];
    connector: RedisConnector | KafkaConnector;
}
