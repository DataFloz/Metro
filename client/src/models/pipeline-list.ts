import { Pipeline } from "./pipeline";

export interface PipelineList{
    name: string;
    pipelines: Pipeline[]
    connectors: [{
        name: string;
        brokers: string;
        group_id: string;
    }]
}