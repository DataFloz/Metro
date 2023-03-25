export interface Pipeline{
    name: string;
    input: Input;
    output: Output;
    transformation: Transformation;
}

export interface Input {
    topic: string    
}

export interface Output {
    topic: string
}

export interface Transformation {
    container_url: string
}