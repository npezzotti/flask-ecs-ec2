import click

from app import db


def register(app):
    @app.cli.command('init-db')
    def init_db():
        db.create_all()
        click.echo("Initialized database")
    
    @app.cli.command('drop-db')
    def drop_db():
        db.drop_all()
        click.echo("Destroyed database")
