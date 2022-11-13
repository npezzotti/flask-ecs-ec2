resource "aws_cloudwatch_log_group" "main" {
  name = "${var.project_name}-log-group"
}

resource "aws_ecs_cluster" "main" {
  name = "${var.project_name}-cluster"
}