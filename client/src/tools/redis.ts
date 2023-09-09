import redis from 'redis';
import { RedisConnector } from "@/models/connector";
import { Pipeline } from "@/models/pipeline";

export const produceTest = async (connector: RedisConnector, pipeline: Pipeline, message: string) => {
    const redisClient = redis.createClient({
        url: `redis://${connector.host}:${connector.port}/0`
    })
    await redisClient.publish(pipeline.input.topic, message);
}