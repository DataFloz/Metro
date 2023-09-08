export interface Connector {
    name: string;
    type: 'kafka' | 'redis';
}

export interface KafkaConnector extends Connector {
    brokers: string;
    group_id: string;
}

export interface RedisConnector extends Connector {
    host: string;
    port: number
}