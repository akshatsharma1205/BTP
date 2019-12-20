from app import db
from sqlalchemy.dialects.postgresql import JSON


class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    lon = db.Column(db.String())
    lat = db.Column(db.String())

    def __init__(self, lon, lat):
        self.lon = lon
        self.lat = lat

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id, 
            'lon': self.lon,
            'lat': self.lat
        }
