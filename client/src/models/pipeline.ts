export interface Pipeline{
    name: string;
    input: InputModel;
    output: Output;
    transformation: Transformation;
}

export interface InputModel {
    topic: string    
}

export interface Output {
    topic: string
}

export interface Transformation {
    container_url: string
}