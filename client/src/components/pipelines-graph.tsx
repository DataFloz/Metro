import Graph from "react-graph-vis";
import { uuid } from 'uuidv4';
import { Pipeline } from "@/models/pipeline";
import { useEffect, useState } from "react";

interface GraphProps {
  pipelines: Pipeline[];
}

export default function PipelinesGraph({ pipelines }: GraphProps) {
  const [edges, setEdges] = useState<{ from: string; to: string; }[]>([])
  const [nodes, setNodes] = useState<{ id: string; label: string; title: string; }[]>([])
  let [graphKey, setGraphKey] = useState(uuid())



  useEffect(()=>{
    debugger;
    const routes: { from: string; to: string; }[] = []
    pipelines.forEach(p => {
      const nextPipelines = pipelines.filter((x) => x.input.topic == p.output.topic)
      nextPipelines.forEach(x => {
        routes.push( { from: p.name, to: x.name })
      })
    });

    setEdges(routes);
    setNodes(pipelines.map(p => ({id: p.name, label: p.name, title: p.name})))
    setGraphKey(uuid())
  }, [])

  const graph = ({
    nodes: nodes,
    edges: edges
  });

  const options = {
    height: "400px"
  };

  const events = {
    select: function(event: { nodes: any; edges: any; }) {
      var { nodes, edges } = event;
    }
  };
  return (
    <Graph
      key={graphKey}
      graph={graph}
      options={options}
      events={events}
    />
  );
}
