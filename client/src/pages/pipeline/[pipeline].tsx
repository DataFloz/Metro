import { useDataContext } from '@/context/context';
import { useRouter } from 'next/router';
import { Pipeline } from '../../models/pipeline';
import { Button, Drawer, Input, Table } from '@mantine/core';
import { Grid } from '@mantine/core';
import ProduceTest from '@/components/test-message-dialog';
import { useDisclosure } from '@mantine/hooks';
import axios from 'axios';
import { useState } from 'react';

export default function Home() {
    const router = useRouter();
    const { pipeline } = router.query;
    const [messagesDrawerOpened, { open, close }] = useDisclosure(false);
    const [messages, setMessages] = useState([]);

    const onOpenMessagesDrawer = async () => {
        let currentPipeline = dataContext?.config.pipelines.filter(
            (pipe) => pipe.name === pipeline
        )[0];
        const results = await axios.post('/api/transformed-messages', {
            pipeline: currentPipeline,
            kafkaConnector: dataContext!.config.connectors[0],
        });
        setMessages(results.data.transformedMessages);
        open();
    };

    const getInputValue = (key: string, value: string) => {
        return (
            <div style={{ width: '20%' }}>
                <Input.Wrapper label={key} maw={320} mx="auto">
                    <Input radius="lg" disabled value={value} />
                </Input.Wrapper>
            </div>
        );
    };
    const dataContext = useDataContext();
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

    let currentPipeline = dataContext?.config.pipelines.filter(
        (pipe) => pipe.name === pipeline
    )[0];
    return (
        <>
            {currentPipeline ? (
                <>
                    {iterate(currentPipeline)}
                    <Grid m={15}>
                        <Grid.Col span={2}>
                            <ProduceTest
                                pipeline={currentPipeline}
                                kafkaConnector={
                                    dataContext!.config.connectors[0]
                                }
                            ></ProduceTest>
                        </Grid.Col>
                        <Grid.Col span={2}>
                            <Button onClick={onOpenMessagesDrawer}>
                                Show transfomed messages
                            </Button>
                        </Grid.Col>
                    </Grid>
                    <Drawer
                        opened={messagesDrawerOpened}
                        onClose={close}
                        title="Transformed messages"
                    >
                        <Table>
                            {messages.map((m: any) => (
                                <tr key={m.timestamp}>
                                    <td>{m.timestamp}</td>
                                    <td>{m.value}</td>
                                </tr>
                            ))}
                        </Table>
                    </Drawer>
                </>
            ) : (
                ''
            )}
        </>
    );
}
