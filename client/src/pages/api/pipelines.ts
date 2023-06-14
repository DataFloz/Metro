import { PipelineList } from './../../models/pipeline-list';
import type { NextApiRequest, NextApiResponse } from 'next';
import axios from 'axios';
import { RUNNER_URL } from '@/config';

export default async function handler(
    req: NextApiRequest,
    res: NextApiResponse<PipelineList>
) {
    const runnerPipelines = await axios.get(`${RUNNER_URL}/api/pipelines`);

    res.status(200).json(runnerPipelines.data);
}
