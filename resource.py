from app import db
import json
from model import Actor, Movie


def add_movie_info(data):
    if data:
        new = Movie(data['movie_name'], data['movie_actor_id'], data['rating'], data['createdon'])
        try:
            db.session.add(new)
            db.session.commit()
            return "Movie details added successfully ..."
        except Exception as e:
            db.session.rollback()
            return "Please check input details or duplicate values # " + str(e)


def add_actor_info(data):
    if data:
        new = Actor(data['actorName'])
        try:
            db.session.add(new)
            db.session.commit()
            return "Actor details added successfully ..."
        except Exception as e:
            return e


def get_movies_by_id(data):
    if data['id']:
        try:
            res = {}
            for row in db.session.query(Movie).filter(Movie.id == id).all():
                res[row.id] = row.actorName
            return res
        except Exception as e:
            return e
    else:
        return "Please input ID"


def get_movie_by_actor_id(data):
    if data['id']:
        try:
            res = {}
            id = data['id']
            for row in db.session.query(Movie).filter(Movie.movieActorId == id).all():
                res[row.id] = row.movieName
            return res
        except Exception as e:
            return e
    else:
        return "Please input ID"


def get_actor_by_id(data):
    if data['id']:
        try:
            res = {}
            id = data['id']
            for row in db.session.query(Actor).filter(Actor.id == id).all():
                res[row.id] = row.actorName
            return res
        except Exception as e:
            return e
    else:
        return "Please input ID"


def show_all_movies():
    result = db.session.query(Movie).all()
    res = {}
    for row in result:
        res[row.id] = {'moviename':row.movieName, 'actorId':row.movieActorId, 'created_date':row.createdOn, 'rating':row.rating}
    return res


def show_all_actor():
    result = db.session.query(Actor).all()
    res = {}
    for row in result:
        res[row.id] = row.actorName
    return res