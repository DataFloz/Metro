import { Table } from '@mantine/core';

interface PipelineRowProp {
    name: string;
    inputTopic: string;
    outputTopic: string;
}

interface TableProps {
    pipelines: PipelineRowProp[];
}

export default function PipelinesTable({pipelines}: TableProps) {
    const rows = pipelines.map((row) => (
        <tr key={row.name}>
            <td>{row.name}</td>
            <td>{row.inputTopic}</td>
            <td>{row.outputTopic}</td>
        </tr>
      ));
  
  return (<Table>
      <thead>
        <tr>
          <th>Pipeline name</th>
          <th>input</th>
          <th>output</th>
        </tr>
      </thead>
      <tbody>{rows}</tbody>
  </Table>)
}
