import { Kafka } from 'kafkajs'
import type { NextApiRequest, NextApiResponse } from 'next'
import { Pipeline } from '@/models/pipeline';
import { Connector } from '@/models/connector';

const topicsMessagesDictionary: { [key: string]: {timestamp: string; value: string | undefined; }[]} = {}

const getMessages = async (pipeline: Pipeline, connector: Connector) => {
  let messages: { timestamp: string; value: string | undefined; }[] = []

  const kafka = new Kafka({
    clientId: 'test-client',
    brokers: [...connector.brokers.split(',')]
  })

  if(!topicsMessagesDictionary[pipeline.output.topic]){
    topicsMessagesDictionary[pipeline.output.topic] = []
  }

  messages = topicsMessagesDictionary[pipeline.output.topic]

  const consumer = kafka.consumer({ groupId: 'reader' })
  await consumer.connect()
  await consumer.subscribe({ topics: [pipeline.output.topic], fromBeginning: true })
  console.log("retrieve messages!")
  consumer.run({
    autoCommit: false,
    eachMessage: async ({ topic, partition, message }) => {
      console.log({
        topic,
        partition,
        offset: message.offset,
        value: message.value ? message.value.toString() : "null",
      });
      topicsMessagesDictionary[pipeline.output.topic].push({ timestamp: message.timestamp, value: message.value ? message.value.toString() : "null" })
    },
  });

  return messages;
}

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  if (req.method === 'POST') {
    const pipeline = req.body.pipeline as Pipeline
    const connector = req.body.kafkaConnector as Connector

    const messages = await getMessages(pipeline, connector);

    res.status(200).json({ transformedMessages: messages })
  } else {
    res.status(405)
  }
}
