import { KafkaConnector } from "@/models/connector";
import { Pipeline } from "@/models/pipeline";
import { Kafka, KafkaMessage, PartitionOffset } from "kafkajs";

export const createTopics = async (connector: KafkaConnector, pipelines: Pipeline[]) => {
    // Create the client with the broker list
    const kafka = new Kafka({
        clientId: 'test-client',
        brokers: [...connector.brokers.split(',')],
    });

    const admin = kafka.admin();
    const topics = Array.from(new Set(pipelines.map((p) => p.input.topic)));
    try {
        console.log('start to deleting topics');
        await admin.deleteTopics({ topics: topics });
    } catch {
        console.log('failed to delete topics');
    }

    try {
        console.log('start to creating topics');
        await admin.createTopics({
            topics: topics.map((x) => ({ topic: x })),
            waitForLeaders: false,
        });
    } catch {
        console.log('failed to create topics');
    }
}

export const produceTest = async (connector: KafkaConnector, pipeline: Pipeline, message: string) => {
    // Create the client with the broker list
    const kafka = new Kafka({
        clientId: 'test-client',
        brokers: [...connector.brokers.split(',')],
    });

    const producer = kafka.producer();

    await producer.connect();
    await producer.send({
        topic: pipeline.input.topic,
        messages: [{ key: 'test-key', value: message }],
    });
}

interface IMessage {
    timestamp: string;
    value: string | undefined;
}

export const getMessages = async (connector: KafkaConnector, pipeline: Pipeline): Promise<IMessage[]> => {
    const kafka = new Kafka({
        clientId: 'test-client',
        brokers: [...connector.brokers.split(',')],
    });

    console.log('start get messages');
    const promise = new Promise<IMessage[]>(async (resolve, reject) => {
        const consumer = kafka.consumer({ groupId: 'reader' });
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
                    const messages: IMessage[] = [];
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

                    await consumer.disconnect();
                    resolve(messages);
                },
            })
            .catch(async (err) => {
                await consumer.disconnect();
                reject(err)
            });
    });

    return await promise;
};

export const getTopicMetadata = async (connector: KafkaConnector, pipeline: Pipeline) => {
    const kafka = new Kafka({
        clientId: 'test-client',
        brokers: [...connector.brokers.split(',')],
    });

    console.log('start get metadata');

    const admin = kafka.admin();
    const topicOffsets = await admin.fetchTopicOffsets(pipeline.input.topic);
    
    const promise = new Promise<{ msg: KafkaMessage, topicOffsets: (PartitionOffset & {
        high: string;
        low: string;
    })[] }>(async (resolve, reject) => {
        const consumer = kafka.consumer({ groupId: 'reader' });
        await consumer.connect();
        await consumer.subscribe({
            topics: [pipeline.output.topic],
            fromBeginning: true,
        });

        consumer
            .run({
                eachBatchAutoResolve: false,
                autoCommit: false,
                eachMessage: async ({ topic, partition, message }) => {
                    console.log(message)
                    await consumer.disconnect();
                    resolve({ msg: message, topicOffsets: topicOffsets });
                }
            })
            .catch(async (err) => {
                await consumer.disconnect();
                reject(err)
            });

        consumer.seek({ topic: pipeline.input.topic, partition: topicOffsets[0].partition, offset: topicOffsets[0].offset })
    });

    return await promise;
};
