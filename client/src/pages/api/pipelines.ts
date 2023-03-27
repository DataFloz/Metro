import { PipelineList } from './../../models/pipeline-list';
import type { NextApiRequest, NextApiResponse } from 'next'
import axios from 'axios';
import { Pipeline } from '@/models/pipeline';

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse<PipelineList>
) {
  const runnerPipelines = await axios.get('http://localhost:5000/api/pipelines');
  
  res.status(200).json(runnerPipelines.data)
}
