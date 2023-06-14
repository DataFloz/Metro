import { Consumer, Kafka } from 'kafkajs';
import type { NextApiRequest, NextApiResponse } from 'next';
import { Pipeline } from '@/models/pipeline';
import { Connector } from '@/models/connector';

let consumer: Consumer | null = null;

const getMessages = async (pipeline: Pipeline, connector: Connector) => {
    const kafka = new Kafka({
        clientId: 'test-client',
        brokers: [...connector.brokers.split(',')],
    });

    console.log('start get messages');
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
                    eachBatch: async ({ batch, resolveOffset, heartbeat }) => {
                        const messages: {
                            timestamp: string;
                            value: string | undefined;
                        }[] = [];
                        for (let message of batch.messages) {
                            console.log({
                                value: message.value
                                    ? message.value.toString()
                                    : 'null',
                                partition: batch.partition,
                                offset: message.offset,
                                timestamp: message.timestamp,
                            });
                            messages.push({
                                timestamp: message.timestamp,
                                value: message.value
                                    ? message.value.toString()
                                    : 'null',
                            });
                        }

                        resolve(messages);
                    },
                })
                .catch((err) => reject(err));
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

        const messages = await getMessages(pipeline, connector);

        if (consumer) {
            console.log('retrived messages');
            await consumer.disconnect();
            consumer = null;
        }

        res.status(200).json({ transformedMessages: messages });
    } else {
        res.status(405);
    }
}
