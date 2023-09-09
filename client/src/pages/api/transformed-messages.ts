import type { NextApiRequest, NextApiResponse } from 'next';
import { Pipeline } from '@/models/pipeline';
import { Connector, KafkaConnector } from '@/models/connector';
import { getMessages } from '@/tools/kafka';

const kafkaHandler = async (connector: KafkaConnector, pipeline: Pipeline) => {
  return getMessages(connector, pipeline)
};

export default async function handler(
    req: NextApiRequest,
    res: NextApiResponse
) {
    if (req.method === 'POST') {
        const pipeline = req.body.pipeline as Pipeline;
        const connector = req.body.kafkaConnector as Connector;

        let messages;
        if (connector.type === 'kafka') {
            messages = await kafkaHandler(connector as KafkaConnector, pipeline);
        }

        console.log('retrived messages');

        res.status(200).json({ transformedMessages: messages });
    } else {
        res.status(405);
    }
}
