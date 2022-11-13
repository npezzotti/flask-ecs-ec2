variable "project_name" {
    description = "Name of project"
    default = "flask-ecs-ec2"
}

variable "region" {
    description = "AWS region" 
    default = "us-east-1"
}

variable "container_image" {
    description = "Container Image"
    default = "092505501776.dkr.ecr.us-east-1.amazonaws.com/flask-app"
}