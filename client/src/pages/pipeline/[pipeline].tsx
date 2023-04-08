import { useDataContext } from "@/context/context";
import { useRouter } from "next/router";
import { useEffect } from "react";
import { Pipeline, InputModel } from "../../models/pipeline";
import { Input } from '@mantine/core';

export default function Home() {
  const router = useRouter();
  const { pipeline } = router.query;

  const dataContext = useDataContext();
  const iterate = (pipeline: Pipeline) => {
    Object.values(pipeline).filter((value) => {
       if (typeof value === 'string') {
        return (
          <div>
            <Input radius="xl" value={value} />
          </div>
        )}
    })
    // for (let key in pipeline ) {
    //   console.log('key', key)
    //   console.log('type', typeof key)

    //   if (pipeline[key] instanceof InputModel)
    //   { console.log('yes')}
    // }
  }
  useEffect(() => {
    console.log(dataContext?.config);
  }, [dataContext]);
  let currentPipeline = dataContext?.config.pipelines.filter(
    (pipe) => pipe.name === pipeline
  )[0];
  iterate(currentPipeline!)
  return (
    <>
      <div>{pipeline}</div>

      {/* {Object.keys(currentPipeline!).forEach((key) => {
        console.log('key', key)
        console.log('type', typeof key)
        // console.log("key", currentPipeline[key as keyof Pipeline]);
      })} */}

      <div>{dataContext?.config.name}</div>
    </>
  );
}
