import { Connector } from '@/models/connector';
import { Accordion } from '@mantine/core';

interface TableProps {
    connectors: Connector[];
}

export default function PipelinesTable({ connectors }: TableProps) {
    console.log(connectors);
    const rows = connectors.map((row) => (
        <Accordion.Item value="customization" key={row.name}>
            <Accordion.Control>Kafka Connector</Accordion.Control>
            <Accordion.Panel>
                {row.name}, {row.brokers} | {row.group_id}
            </Accordion.Panel>
        </Accordion.Item>
    ));

    return (
        <Accordion
            title="Connectors"
            variant="filled"
            radius="md"
            chevronPosition="left"
            defaultValue="customization"
        >
            {rows}
        </Accordion>
    );
}
