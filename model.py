from app import db

"""Class definitions"""
class Movie(db.Model):
    """Movie class defines the Movie ORM table"""
    __tablename__ = "Movie"

    id = db.Column('movie_id', db.Integer, primary_key=True)
    movieName = db.Column('movie_name', db.String(50), unique=True, index=True)
    movieActorId = db.Column(db.Integer, db.ForeignKey("Actor.id"))

    actor = db.relationship('Actor', backref='Movie')

    rating = db.Column('rating', db.Integer, unique=True, index=True)
    createdOn = db.Column('registered_on', db.DateTime)

    def __init__(self, movie_name, movie_actor, rating, createdon):
        self.movieName = movie_name
        self.movieActor = movie_actor
        self.rating = rating
        self.createdOn = createdon

class Actor(db.Model):
    """Actor class defines for Actor ORM table """
    __tablename__ = 'Actor'

    id=db.Column('id', db.Integer, primary_key=True)
    actorName = db.Column('actorname', db.String(50))

    def __init__(self, actorName):
        self.actorName = actorName

if __name__ == '__main__':
    db.create_all()
