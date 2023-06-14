import { Connector } from './connector';
import { Pipeline } from './pipeline';

export interface PipelineList {
    name: string;
    pipelines: Pipeline[];
    connectors: Connector[];
}
