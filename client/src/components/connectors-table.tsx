import { Connector } from '@/models/connector';
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
                <Accordion.Control>Kafka Connector</Accordion.Control>
                <Accordion.Panel>
                    {connector.name}, {connector.brokers} | {connector.group_id}
                </Accordion.Panel>
            </Accordion.Item>
        </Accordion>
    );
}
