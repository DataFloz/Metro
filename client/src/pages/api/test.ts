import type { NextApiRequest, NextApiResponse } from 'next';
import { Pipeline } from '@/models/pipeline';
import { Connector, KafkaConnector } from '@/models/connector';
import { produceTest } from '@/tools/kafka';

const kafkaHandler = async (connector: KafkaConnector, pipeline: Pipeline, message: string) => {
    await produceTest(connector, pipeline, message);
}

export default async function handler(
    req: NextApiRequest,
    res: NextApiResponse
) {
    if (req.method === 'POST') {
        const pipeline = req.body.pipeline as Pipeline;
        const connector = req.body.kafkaConnector as Connector;
        const message = req.body.message;
        console.log(connector);

        if (connector.type === 'kafka') {
            await kafkaHandler(connector as KafkaConnector, pipeline, message);
        }

        res.status(200).json({ result: 'succeed' });
    } else {
        res.status(405);
    }
}
