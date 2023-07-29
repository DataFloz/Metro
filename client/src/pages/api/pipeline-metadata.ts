import { Consumer, Kafka } from 'kafkajs';
import type { NextApiRequest, NextApiResponse } from 'next';
import { Pipeline } from '@/models/pipeline';
import { Connector } from '@/models/connector';

let consumer: Consumer | null = null;

const getPipelineMetadata = async (pipeline: Pipeline, connector: Connector) => {
    const kafka = new Kafka({
        clientId: 'test-client',
        brokers: [...connector.brokers.split(',')],
    });

    console.log('start get metadata');

    const admin = kafka.admin();
    const topicOffsets = await admin.fetchTopicOffsets(pipeline.input.topic);
    let latestMsgTime = undefined;
    const promise = new Promise(async (resolve, reject) => {
        if (!consumer) {
            consumer = kafka.consumer({ groupId: 'reader' });
            await consumer.connect();
            await consumer.subscribe({
                topics: [pipeline.output.topic],
                fromBeginning: true,
            });

            consumer
                .run({
                    eachBatchAutoResolve: false,
                    autoCommit: false,
                    eachMessage: async ({ topic,partition, message}) => {
                        latestMsgTime = message.timestamp;
                        resolve({msg: message, topicOffsets: topicOffsets});
                    }
                })
                .catch((err) => reject(err));

            consumer.seek({topic: pipeline.input.topic,partition: topicOffsets[0].partition, offset: topicOffsets[0].offset})
        } else {
            resolve(undefined);
        }
    });

    return await promise;
};

export default async function handler(
    req: NextApiRequest,
    res: NextApiResponse
) {
    if (req.method === 'POST') {
        const pipeline = req.body.pipeline as Pipeline;
        const connector = req.body.kafkaConnector as Connector;

        const metadata = await getPipelineMetadata(pipeline, connector);

        if (consumer) {
            console.log('retrived messages');
            await consumer.disconnect();
            consumer = null;
        }

        res.status(200).json({ pipelineMetadata: getPipelineMetadata });
    } else {
        res.status(405);
    }
}
