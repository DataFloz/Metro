import type { NextApiRequest, NextApiResponse } from 'next';
import { Pipeline } from '@/models/pipeline';
import { Connector, KafkaConnector } from '@/models/connector';
import { getTopicMetadata } from '@/tools/kafka';

const kafkaHandler = async (connector: KafkaConnector, pipeline: Pipeline) => {
    return getTopicMetadata(connector, pipeline);
};

export default async function handler(
    req: NextApiRequest,
    res: NextApiResponse
) {
    if (req.method === 'POST') {
        const pipeline = req.body.pipeline as Pipeline;
        const connector = req.body.kafkaConnector as Connector;

        let metadata;
        if (connector.type === 'kafka') {
            metadata = await kafkaHandler(connector as KafkaConnector, pipeline);
        }

        console.log('retrived messages');

        res.status(200).json({ pipelineMetadata: metadata });
    } else {
        res.status(405);
    }
}
