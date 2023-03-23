import { Pipeline } from '@/models/pipeline';
import { Table } from '@mantine/core';

interface TableProps {
    pipelines: Pipeline[];
}

export default function PipelinesTable({pipelines}: TableProps) {
    const rows = pipelines.map((row) => (
        <tr key={row.name}>
            <td>{row.name}</td>
            <td>{row.input}</td>
            <td>{row.output}</td>
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
