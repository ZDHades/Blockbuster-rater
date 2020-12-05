from flask import current_app as app
from app import create_app, cli, db
from app.blueprints.authentication.models import User
from app.blueprints.movies.models import Rating

app = create_app()
cli.register(app)

@app.shell_context_processor
def shell_context():
    return {'User' : User, 'Rating' : Rating}