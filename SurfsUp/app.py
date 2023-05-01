# Import the dependencies.
import os
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


from flask import Flask, jsonify


#################################################
# Database Setup
#################################################

# 1. Use the SQLAlchemy create_engine() function to connect to your SQLite database.
SQLITE_PATH = os.path.join("Resources", "hawaii.sqlite")
os.chdir(os.path.dirname(os.path.realpath(__file__)))
engine = create_engine(f"sqlite:///{SQLITE_PATH}")

#engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# 2. Use the SQLAlchemy automap_base() function to reflect your tables into classes, and then save references to the classes named station and measurement.
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

# 3. Link Python to the database by creating a SQLAlchemy session.
# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def homepage():
    """List all available api routes."""
    return (
        f"Static Routes:<br/>"
        f"Precipitation for recent year: /api/v1.0/precipitation<br/>"
        f"Stations: /api/v1.0/stations<br/>"
        f"Most active station temperature observations for recent year: /api/v1.0/tobs<br/>"
        f"<br/>Dynamic Routes: <br/>*Start and end dates from 2010-01-01 to 2017-08-23*<br/>"
        f"Temp stats from start date to end of dataset: /api/v1.0/yyyy-mm-dd<br/>"
        f"Temp stats from start date to end date: /api/v1.0/yyyy-mm-dd/yyyy-mm-dd><br/>"
    )

# precipitation route
@app.route('/api/v1.0/precipitation')
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list precipitation date and amount from the last 12 months"""
        # most recent date
    recent_date = session.query(measurement.date).order_by(measurement.date.desc()).first().date

    # date one year ago from most recent date
    one_year_ago = (dt.datetime.strptime(recent_date, '%Y-%m-%d') - dt.timedelta(days=365)).strftime('%Y-%m-%d')

    results = session.query(measurement.date, measurement.prcp).\
        filter(measurement.date >= one_year_ago).all()

    session.close()

    # precipitation dictionary creation
    precipitation_list = []
    for date, prcp in results:
        prcp_dict = {}
        prcp_dict["Date"] = date
        prcp_dict["Precipitation"] = prcp
        precipitation_list.append(prcp_dict)

    return jsonify(precipitation_list)

# stations route
@app.route('/api/v1.0/stations')
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of the stations id, name, latitude, longitude and elevation"""
    # sel = [station.station,station.name,station.latitude,station.longitude,station.elevation]
    results = session.query(station.station, station.name, station.latitude, station.longitude, station.elevation).all()

    session.close()

    stations_list = list(np.ravel(results))

    return jsonify(stations_list)

# tobs route
@app.route('/api/v1.0/tobs')
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of temperature observations for the previous year for the most active station"""
    # most recent date
    recent_date = session.query(measurement.date).order_by(measurement.date.desc()).first().date

    # date one year ago from most recent date
    one_year_ago = (dt.datetime.strptime(recent_date, '%Y-%m-%d') - dt.timedelta(days=365)).strftime('%Y-%m-%d')

    # most active station
    most_active_station = session.query(measurement.station).group_by(measurement.station).\
    order_by(func.count().desc()).first().station
    
    # last 12 months of temperature observation data for most active station
    observation_12_month = session.query(measurement.date, measurement.tobs).\
    filter_by(station = most_active_station).\
    filter(measurement.date >= one_year_ago).all()

    session.close()

    tobs_list = []
    for date, tobs in observation_12_month:
        tobs_dict = {}
        tobs_dict["Date"] = date
        tobs_dict["Tobs"] = tobs
        tobs_list.append(tobs_dict)

    return jsonify(tobs_list)

# date start route
@app.route('/api/v1.0/<start>')
def start_date(start):

    # Create our session (link) from Python to the DB
    session = Session(engine)

    results = session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).\
        filter(measurement.date >= start).all()
    
    session.close()

    start_list = []
    for min, avg, max in results:
        tobs_dict = {}
        tobs_dict["TMIN"] = min
        tobs_dict["TAVG"] = avg
        tobs_dict["TMAX"] = max
        start_list.append(tobs_dict)

    return jsonify(start_list)

# date end route
@app.route('/api/v1.0/<start>/<end>')
def start_end(start, end):

    # Create our session (link) from Python to the DB
    session = Session(engine)

    results = session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).\
        filter(measurement.date >= start).filter(measurement.date <= end).all()
    
    session.close()

    start_end_list = []
    for min, avg, max in results:
        tobs_dict = {}
        tobs_dict["TMIN"] = min
        tobs_dict["TAVG"] = avg
        tobs_dict["TMAX"] = max
        start_end_list.append(tobs_dict)

    return jsonify(start_end_list)
    
session.close()

if __name__ == '__main__':
    app.run(debug=True)