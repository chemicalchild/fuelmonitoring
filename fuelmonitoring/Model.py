from fuelmonitoring import db
from datetime import datetime


class LocationFuelData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    altitude = db.Column(db.Float, nullable=False)
    fuel_level = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, latitude, longitude, altitude, fuel_level):
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.fuel_level = fuel_level
