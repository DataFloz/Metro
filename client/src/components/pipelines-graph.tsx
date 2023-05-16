import Graph from "react-graph-vis";
import { uuid } from 'uuidv4';
import { Pipeline } from "@/models/pipeline";
import { useEffect, useState } from "react";
import { useRouter } from "next/router";

interface GraphProps {
  pipelines: Pipeline[];
}

export default function PipelinesGraph({ pipelines }: GraphProps) {
  const [edges, setEdges] = useState<any[]>([])
  const [nodes, setNodes] = useState<{ id: string; label: string; title: string; }[]>([])
  let [graphKey, setGraphKey] = useState(uuid())
  const { push } = useRouter();

  useEffect(() => {
    const routes: any[] = []
    pipelines.forEach(p => {
      const nextPipelines = pipelines.filter((x) => x.input.topic == p.output.topic)
      nextPipelines.forEach(x => {
        routes.push({
          from: p.name, to: x.name
        })
      })
    });

    setEdges(routes);
    setNodes(pipelines.map(p => ({ id: p.name, label: p.name, title: p.name, group: p.transformation.type })))
    setGraphKey(uuid())
  }, [])

  const graph = ({
    nodes: nodes,
    edges: edges
  });

  const options = {
    height: "400px",
    physics: {
      enabled: true,
      hierarchicalRepulsion: {
        avoidOverlap: 3,
      },
    },
    layout: {
      hierarchical: {
        direction: "LR",
        sortMethod: "directed",
      },
    },
    nodes: {
      shape: "dot",
      size: 15,
    },
    edges: {
      smooth: {
        type: "continuous",
      },
      arrows: { to: true },
    },
  };

  const events = {
    select: function (event: { nodes: any; edges: any; }) {
      const { nodes, edges } = event;
      if (nodes && nodes.length)
        push(`/pipeline/${nodes[0]}`)
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
