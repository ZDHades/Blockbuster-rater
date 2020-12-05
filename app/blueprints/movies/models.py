from app import db

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie = db.Column(db.String)
    thumbs_up = db.Column(db.Boolean, default=False)
    thumbs_down = db.Column(db.Boolean, default=False)

