import { Accordion, Input } from '@mantine/core';
import useAxios from 'axios-hooks';
import { Pipeline } from '@/models/pipeline';
import { Connector } from '@/models/connector';

interface IProps {
    pipeline: Pipeline;
    connector: Connector;
}

export default function PipelineMetadata({pipeline, connector}: IProps) {
    const [{ data, loading, error }] = useAxios<any>({
        url: '/api/pipeline-metadata',
        method: 'post',
        data: { pipeline: pipeline,
            kafkaConnector: connector
        }
    });

    const getInputValue = (key: string, value: string) => {
        return (
            <div style={{ width: '20%' }}>
                <Input.Wrapper label={key} maw={320} mx="auto">
                    <Input radius="lg" disabled value={value} />
                </Input.Wrapper>
            </div>
        );
    };

    const iterate = (pipeline: Pipeline) => {
        return Object.entries(pipeline).map(([key, value]) => {
            console.log('key', key);
            switch (key) {
                case 'name':
                    return getInputValue(key, value);
                case 'input':
                    return getInputValue('input topic', value.topic);
                case 'output':
                    return getInputValue('output topic', value.topic);
                case 'transformation':
                    switch (value.type) {
                        case 'container':
                            return getInputValue(
                                'container url',
                                value.container_url
                            );
                        case 'http':
                            return getInputValue('HTTP url', value.http_url);
                        case 'sql':
                            return getInputValue('SQL query', value.sql_query);
                        case 'pickle':
                            return getInputValue(
                                'pickle file name',
                                value.file_name
                            );
                        default:
                            break;
                    }
                default:
                    break;
            }
        });
    };

    return (
        <>
            {pipeline ? (
                <>
                    {iterate(pipeline)}
                    {data && data.pipelineMetadata && (
                        <Accordion
                            title="Connector"
                            variant="filled"
                            radius="md"
                            chevronPosition="left"
                            defaultValue="customization"
                        >
                            <Accordion.Item value="customization" key={connector.name}>
                                <Accordion.Control>Pipeline offsets</Accordion.Control>
                                <Accordion.Panel>
                                    {data.pipelineMetadata.topicOffsets}
                                </Accordion.Panel>
                            </Accordion.Item>
                            <Accordion.Item value="customization" key={connector.name}>
                                <Accordion.Control>last item time</Accordion.Control>
                                <Accordion.Panel>
                                    {data.pipelineMetadata.msg.timestamp}
                                </Accordion.Panel>
                            </Accordion.Item>
                        </Accordion>
                    )}
                </>
            ) : (
                ''
            )}
        </>
    );
}
