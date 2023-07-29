import { useDataContext } from '@/context/context';
import { useRouter } from 'next/router';
import { Button, Drawer, Table } from '@mantine/core';
import { Grid } from '@mantine/core';
import ProduceTest from '@/components/test-message-dialog';
import { useDisclosure } from '@mantine/hooks';
import PipelineTransformMessages from '@/components/pipeline-transformed-messages';
import PipelineMetadata from '@/components/pipeline-metadata';
import { useEffect, useState } from 'react';
import axios from 'axios';
import { PipelineList } from '@/models/pipeline-list';
import { Pipeline } from '@/models/pipeline';
import { Connector } from '@/models/connector';

export default function Home() {
    const router = useRouter();
    const { pipeline } = router.query;
    
    const dataContext = useDataContext();

    const [currentPipeline, setCurrentPipeline] = useState<Pipeline | undefined>(undefined);
    const [connector, setConnector] = useState<Connector | undefined>(undefined);

    const [messagesDrawerOpened, { open, close }] = useDisclosure(false);

    const onOpenMessagesDrawer = async () => {
        open();
    };

    const getPipelineDataFromServer = async () => {
        const resultPipelineData = await axios.get<PipelineList>(`/api/pipelines?pipeline=${pipeline}`)
        setCurrentPipeline(resultPipelineData.data.pipelines[0]);
        setConnector(resultPipelineData.data.connector);
    }
    
    useEffect(() => {
        const incomingPipeline = dataContext?.config.pipelines.filter(
            (pipe) => pipe.name === pipeline
        )[0];
        if(incomingPipeline){
            setCurrentPipeline(incomingPipeline);
            setConnector(dataContext!.config.connector);
        }
        else if(pipeline) {
            getPipelineDataFromServer();
        }
    }, [pipeline])


    return (
        <>
            {currentPipeline && connector ? (
                <>
                    <PipelineMetadata 
                        pipeline={currentPipeline}
                        connector={connector} />
                    <Grid m={15}>
                        <Grid.Col span={2}>
                            <ProduceTest
                                pipeline={currentPipeline}
                                kafkaConnector={connector}
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
                            <PipelineTransformMessages 
                                pipeline={currentPipeline}
                                connector={connector} />
                        </Table>
                    </Drawer>
                </>
            ) : (
                ''
            )}
        </>
    );
}
