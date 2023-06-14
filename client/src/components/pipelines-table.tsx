import { Pipeline } from '@/models/pipeline';
import { Table } from '@mantine/core';
import Link from 'next/link';

interface TableProps {
    pipelines: Pipeline[];
}

export default function PipelinesTable({ pipelines }: TableProps) {
    const rows = pipelines.map((row) => (
        <tr key={row.name}>
            <td>
                <Link href={`/pipeline/${encodeURIComponent(row.name)}`}>
                    {row.name}
                </Link>
            </td>

            <td>{row.input.topic}</td>
            <td>{row.output.topic}</td>
        </tr>
    ));

    return (
        <Table>
            <thead>
                <tr>
                    <th>Pipeline name</th>
                    <th>input</th>
                    <th>output</th>
                </tr>
            </thead>
            <tbody>{rows}</tbody>
        </Table>
    );
}
