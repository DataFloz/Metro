import type { NextApiRequest, NextApiResponse } from 'next';
import { Pipeline } from '@/models/pipeline';
import { Connector, KafkaConnector } from '@/models/connector';
import { createTopics } from '@/tools/kafka';

const kafkaHandler = async (connector: KafkaConnector, pipelines: Pipeline[]) => {
    await createTopics(connector, pipelines);
}

const redisHandler = () => {

}

export default async function handler(
    req: NextApiRequest,
    res: NextApiResponse
) {
    if (req.method === 'POST') {
        const pipelines = req.body.pipelines as Pipeline[];
        const connector = req.body.kafkaConnector as Connector;

        console.log(connector);
        if (connector.type === 'kafka') {
            await kafkaHandler(connector as KafkaConnector, pipelines);
        } else if (connector.type === 'redis') {
            redisHandler();
        }


        res.status(200).json({ result: 'succeed' });
    } else {
        res.status(405);
    }
}
