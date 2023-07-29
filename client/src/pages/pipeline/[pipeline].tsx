import { useDataContext } from '@/context/context';
import { useRouter } from 'next/router';
import { Button, Drawer, Table } from '@mantine/core';
import { Grid } from '@mantine/core';
import ProduceTest from '@/components/test-message-dialog';
import { useDisclosure } from '@mantine/hooks';
import PipelineTransformMessages from '@/components/pipeline-transformed-messages';
import PipelineMetadata from '@/components/pipeline-metadata';

export default function Home() {
    const router = useRouter();
    const { pipeline } = router.query;
    
    const dataContext = useDataContext();

    const [messagesDrawerOpened, { open, close }] = useDisclosure(false);

    const onOpenMessagesDrawer = async () => {
        open();
    };

    let currentPipeline = dataContext?.config.pipelines.filter(
        (pipe) => pipe.name === pipeline
    )[0];

    return (
        <>
            {currentPipeline ? (
                <>
                    <PipelineMetadata 
                        pipeline={currentPipeline}
                        connector={dataContext!.config.connector} />
                    <Grid m={15}>
                        <Grid.Col span={2}>
                            <ProduceTest
                                pipeline={currentPipeline}
                                kafkaConnector={
                                    dataContext!.config.connector
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
                            <PipelineTransformMessages 
                                pipeline={currentPipeline}
                                connector={dataContext!.config.connector} />
                        </Table>
                    </Drawer>
                </>
            ) : (
                ''
            )}
        </>
    );
}
