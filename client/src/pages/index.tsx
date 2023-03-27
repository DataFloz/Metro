import Head from 'next/head'
import useAxios from "axios-hooks";
import { AppShell, Footer, Header, Title } from '@mantine/core';
import PipelinesTable from '@/components/pipelines-table'
import { Pipeline } from '@/models/pipeline';
import { PipelineList } from '@/models/pipeline-list';


export default function Home() {
  const [{ data, loading, error }] = useAxios<PipelineList>({
    baseURL: "http://localhost:3000",
    url: "/api/pipelines",
  });
  
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
          <PipelinesTable 
            pipelines={data.pipelines}
          ></PipelinesTable>
        : 
          <></>
      }
    </AppShell>
    </>
  )
}
