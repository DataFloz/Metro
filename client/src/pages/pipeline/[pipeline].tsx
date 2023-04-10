import { useDataContext } from "@/context/context";
import { useRouter } from "next/router";
import { Pipeline } from "../../models/pipeline";
import { Input } from "@mantine/core";
import { Grid } from '@mantine/core';
import ProduceTest from "@/components/test-message-dialog";

export default function Home() {
  const router = useRouter();
  const { pipeline } = router.query;

  const getInputValue = (key:string, value: string) => {
    return (
      <div style={{ width: "20%" }}>
      <Input.Wrapper
        label={key}
        maw={320}
        mx="auto"
      >
        <Input radius="lg" disabled value={value} />
      </Input.Wrapper>
    </div>

    )
  }
  const dataContext = useDataContext();
  const iterate = (pipeline: Pipeline) => {
    return Object.entries(pipeline).map(([key, value]) => {
      console.log('key', key)
      switch (key) { 
        case 'name': 
          return getInputValue(key, value)
        case 'input':
          return getInputValue('input topic', value.topic)
        case 'output':
          return getInputValue('output topic', value.topic)
        case 'transformation':
          switch (value.type) {
            case 'container':
              return getInputValue('container url', value.container_url)
            case 'http':
              return getInputValue('http url', value.http_url)
            default:
              break;
          }
        default: break
      }      
    });
  };
  
  let currentPipeline = dataContext?.config.pipelines.filter(
    (pipe) => pipe.name === pipeline
  )[0];
  return (
    <>
      {currentPipeline ? 
        <>
          {iterate(currentPipeline)}
          <Grid m={15}>
            <ProduceTest pipeline={currentPipeline} kafkaConnector={dataContext!.config.connectors[0]}></ProduceTest>
          </Grid>
        </> : ""}
    </>
  );
}
