import { Pipeline } from '@/models/pipeline';
import { Table } from '@mantine/core';

interface TableProps {
    pipelines: Pipeline[];
}

export default function PipelinesTable({pipelines}: TableProps) {
    console.log(pipelines)
    const rows = pipelines.map((row) => (
        <tr key={row.name}>
            <td>{row.name}</td>
            <td>{row.input.topic}</td>
            <td>{row.output.topic}</td>
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
