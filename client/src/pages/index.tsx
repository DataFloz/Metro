import useAxios from "axios-hooks";
import { Grid, Tabs, Title } from '@mantine/core';
import PipelinesTable from '@/components/pipelines-table'
import { PipelineList } from '@/models/pipeline-list';
import ConnectorsTable from '@/components/connectors-table';
import { useEffect } from 'react';
import { useDataContext } from '@/context/context';
import CreateTopics from '@/components/create-all-topics';
import PipelinesGraph from '@/components/pipelines-graph';
import RolloutMetro from "@/components/rollout-metro";


export default function Home() {
  const [{ data, loading, error }] = useAxios<PipelineList>({
    url: "/api/pipelines",
  });
  const dataContext = useDataContext()
  useEffect(() => {
    if (data) {
      dataContext?.updateConfig(data)
    }

  }, [data])

  return (
    <>
      <Title>Pipelines-some name</Title>
      { 
        data ? 
          <><Grid grow gutter="lg">
              <Grid.Col span={8}>
              <Tabs defaultValue="graph">
                <Tabs.List>
                  <Tabs.Tab value="table">Table</Tabs.Tab>
                  <Tabs.Tab value="graph">Graph</Tabs.Tab>
                </Tabs.List>

                <Tabs.Panel value="table" pt="xs">
                  <PipelinesTable
                    pipelines={data.pipelines}
                  ></PipelinesTable>
                </Tabs.Panel>

                <Tabs.Panel value="graph" pt="xs">
                  <PipelinesGraph pipelines={data.pipelines}></PipelinesGraph>
                </Tabs.Panel>
              </Tabs>
              </Grid.Col>
              <Grid.Col span={3} offset={1}>
                <ConnectorsTable
                  connectors={data.connectors}
                ></ConnectorsTable>
              </Grid.Col>
              <Grid m={15}>
                <Grid.Col span={1} offset={3}>
                  <CreateTopics pipelines={data.pipelines} kafkaConnector={data.connectors[0]}></CreateTopics>
                </Grid.Col>
                <Grid.Col span={1} offset={5}>
                  <RolloutMetro></RolloutMetro>
                </Grid.Col>
              </Grid>
          </Grid>
          </>
        : 
          <></>
      }
    </>
  )
}
