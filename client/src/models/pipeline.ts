export interface Pipeline{
    name: string;
    input: InputModel;
    output: Output;
    transformation: ContainerTransformation | HttpTransormation;
}

export interface InputModel {
    topic: string    
}

export interface Output {
    topic: string
}
export type transformationType = 'http' | 'container'

export interface transformation {
    type: transformationType
}
export interface ContainerTransformation extends transformation {   
    container_url: string
}

export interface HttpTransormation extends transformation {
    http_url: string;
    headers?: [];
    params?: [];
}