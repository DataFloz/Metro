import { Connector, KafkaConnector, RedisConnector } from '@/models/connector';
import { Accordion } from '@mantine/core';

interface TableProps {
    connector: Connector;
}

export default function PipelinesTable({ connector }: TableProps) {
    console.log(connector);

    return (
        <Accordion
            title="Connector"
            variant="filled"
            radius="md"
            chevronPosition="left"
            defaultValue="customization"
        >
            <Accordion.Item value="customization" key={connector.name}>
                <Accordion.Control>Connector</Accordion.Control>
                <Accordion.Panel>
                    {connector.name} ({connector.type}),
                    {connector.type == 'kafka' ?
                        `${(connector as KafkaConnector).brokers} | ${(connector as KafkaConnector).group_id}`
                        : `${(connector as RedisConnector).host} | ${(connector as RedisConnector).port}`
                    }
                </Accordion.Panel>
            </Accordion.Item>
        </Accordion>
    );
}
