export interface Connector {
    name: string;
    type: 'kafka' | 'redis';
    brokers?: string;
    group_id?: string;
    host?: string;
    port?: number
}
