import { Kafka } from 'kafkajs'
import type { NextApiRequest, NextApiResponse } from 'next'
import { Pipeline } from '@/models/pipeline';
import { Connector } from '@/models/connector';


export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
    if (req.method === 'POST') {
        const pipeline = req.body.pipeline as Pipeline
        const connector = req.body.KafkaConnector as Connector
        const message = req.body.message
        console.log(connector);

        // Create the client with the broker list
        const kafka = new Kafka({
            clientId: 'test-client',
            brokers: [...connector.brokers.split(',')]
        })

        const producer = kafka.producer()

        await producer.connect()
        await producer.send({
            topic: pipeline.input.topic,
            messages: [
                { key: 'key1', value: message },
            ],
        })

        res.status(200).json({result:'succeed'})   
    }else{
        res.status(405)
    }
}
