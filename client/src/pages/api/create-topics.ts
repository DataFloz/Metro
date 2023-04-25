import { Kafka } from 'kafkajs'
import type { NextApiRequest, NextApiResponse } from 'next'
import { Pipeline } from '@/models/pipeline';
import { Connector } from '@/models/connector';


export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
    if (req.method === 'POST') {
        const pipelines = req.body.pipelines as Pipeline[]
        const connector = req.body.kafkaConnector as Connector
        
        console.log(connector);

        // Create the client with the broker list
        const kafka = new Kafka({
            clientId: 'test-client',
            brokers: [...connector.brokers.split(',')]
        })

        const admin = kafka.admin()
        const topics = Array.from(new Set(pipelines.map(p => p.input.topic)))
        // await admin.deleteTopics({topics: topics})
        await admin.createTopics({topics: topics.map(x => ({topic: x})), waitForLeaders: false})

        res.status(200).json({result:'succeed'})   
    }else{
        res.status(405)
    }
}
