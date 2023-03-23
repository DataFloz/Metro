import { PipelineList } from './../../models/pipeline-list';
import type { NextApiRequest, NextApiResponse } from 'next'

export default function handler(
  req: NextApiRequest,
  res: NextApiResponse<PipelineList>
) {
  res.status(200).json({ 
                        name: 'John Doe', 
                        pipelines: [{
                          name: 'some pipeline',
                          input: 'some input',
                          output: 'some output'
                        }] 
                      })
}
