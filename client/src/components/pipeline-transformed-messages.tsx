import { Table } from '@mantine/core';
import useAxios from 'axios-hooks';
import { Connector } from '@/models/connector';
import { Pipeline } from '@/models/pipeline';

interface IProps {
    pipeline: Pipeline;
    connector: Connector;
}

export default function PipelineTransformMessages({pipeline, connector}: IProps) {
    const [{ data, loading, error }] = useAxios<any>({
        url: '/api/transformed-messages',
        method: 'post',
        data: { 
            pipeline: pipeline,
            kafkaConnector: connector
        }
    });

    return (
        <>
            {data && data.transformedMessages ? (
                <>
                <Table>
                    {data.transformedMessages.map((m: any) => (
                        <tr key={m.timestamp}>
                            <td>{m.timestamp}</td>
                            <td>{m.value}</td>
                        </tr>
                    ))}
                </Table>
                </>
            ) : (
                ''
            )}
        </>
    );
}
