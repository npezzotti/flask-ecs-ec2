from app import create_app, cli

application = create_app()
cli.register(application)
