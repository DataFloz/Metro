import type { NextApiRequest, NextApiResponse } from 'next'
import axios from 'axios';
import { RUNNER_URL } from '@/config';

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  await axios.get(`${RUNNER_URL}/api/deploy-pipelines`);
  
  res.status(200)
}
