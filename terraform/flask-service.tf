resource "aws_ecs_task_definition" "flask-task-definition" {
  container_definitions = jsonencode([
    {
      name      = "${var.project_name}-task-definition"
      image     = var.container_definition
      cpu       = 10
      memory    = 512
      essential = true
      portMappings = [
        {
          containerPort = 80
          hostPort      = 80
        }
      ]
    }
  ])
}

resource "aws_ecs_service" "flask-service" {
  name            = "${var.project_name}-service"
  cluster         = aws_ecs_cluster.main.id
  task_definition = aws_ecs_task_definition.flask-task-definition.arn
  desired_count   = 3
}
