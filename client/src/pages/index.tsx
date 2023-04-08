import Head from 'next/head'
import useAxios from "axios-hooks";
import { AppShell, Footer, Grid, Header, Title } from '@mantine/core';
import PipelinesTable from '@/components/pipelines-table'
import { PipelineList } from '@/models/pipeline-list';
import ConnectorsTable from '@/components/connectors-table';
import ProduceTest from '@/components/test-message-dialog';
import { useEffect } from 'react';
import { useDataContext } from '@/context/context';
import CreateTopics from '@/components/create-all-topics';


export default function Home() {
  const [{ data, loading, error }] = useAxios<PipelineList>({
    baseURL: "http://localhost:3000",
    url: "/api/pipelines",
  });
  const dataContext = useDataContext()
  useEffect(() => {
    if (data) {
      console.log('daaaaata', data)
      dataContext?.updateConfig(data)
    }

  }, [data])

  useEffect(() => {
    console.log('dataContext.config', dataContext?.config)
  }, [dataContext?.config])
  return (
    <>
      <Head>
        <title>DataFloz</title>
        <meta name="description" content="Generated by create next app" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <AppShell
          padding="md"
          header={<Header height={60} p="xs">DataFloz</Header>}
          footer={
            <Footer height={60} p="md">
              Application footer
            </Footer>
          }
          styles={(theme) => ({
            main: { backgroundColor: theme.colorScheme === 'dark' ? theme.colors.dark[8] : theme.colors.gray[0] },
        })}
      >
      <Title>Pipelines-some name</Title>
      { 
        data ? 
          <><Grid grow gutter="lg">
              <Grid.Col span={8}>
                <PipelinesTable
                  pipelines={data.pipelines}
                ></PipelinesTable>
              </Grid.Col>
              <Grid.Col span={3} offset={1}>
                <ConnectorsTable
                  connectors={data.connectors}
                ></ConnectorsTable>
              </Grid.Col>
              <Grid>
                <Grid.Col span={2} offset={2}>
                  <ProduceTest pipeline={data.pipelines[0]} kafkaConnector={data.connectors[0]}></ProduceTest>
                </Grid.Col>
                <Grid.Col span={2} offset={5}>
                  <CreateTopics pipelines={data.pipelines} kafkaConnector={data.connectors[0]}></CreateTopics>
                </Grid.Col>
              </Grid>
          </Grid>
          </>
        : 
          <></>
      }
    </AppShell>
    </>
  )
}
