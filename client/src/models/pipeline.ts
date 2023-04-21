export interface Pipeline{
    name: string;
    input: InputModel;
    output: Output;
    transformation: ContainerTransformation | HttpTransormation | SQLTransormation;
}

export interface InputModel {
    topic: string    
}

export interface Output {
    topic: string
}
export type transformationType = 'http' | 'container' | 'sql'

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

export interface SQLTransormation extends transformation {
    sql_query: string;
}