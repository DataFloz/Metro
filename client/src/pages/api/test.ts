import type { NextApiRequest, NextApiResponse } from 'next';
import { Pipeline } from '@/models/pipeline';
import { Connector, KafkaConnector, RedisConnector } from '@/models/connector';
import { produceTest as kafkaHandler } from '@/tools/kafka';
import { produceTest as redisHandler } from '@/tools/redis';

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
        }else if(connector.type === 'redis'){
            await redisHandler(connector as RedisConnector, pipeline, message);
        }

        res.status(200).json({ result: 'succeed' });
    } else {
        res.status(405);
    }
}
