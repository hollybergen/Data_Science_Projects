#--------------- Import Dependencies --------------#

import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
import datetime as dt
from datetime import datetime

#---------------- Set up Database -----------------#

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)


#------------------ Set up Flask -------------------#

from flask import Flask, jsonify
app = Flask(__name__)


#------------------- Index Route -------------------#

@app.route("/")
def home():
    """List all available api routes."""
    print("Server received request for 'Home' page...")
    return (
    f"List of available routes:<br/>"
    f"/api/v1.0/precipitation<br/>"
    f"/api/v1.0/stations<br/>"
    f"/api/v1.0/tobs<br/>"
    )

#------------------- Flask Routes -------------------#

@app.route("/api/v1.0/precipitation")
def precipitation():
    
    results = session.query(Measurement, Station).filter(Measurement.station == Station.station).all()

    precip_dict = {}

    for r in results:
        (m, s) = r
        precip_dict[m.date] = m.prcp

    return jsonify(precip_dict)
    

@app.route("/api/v1.0/stations")
def stations():
    stations = session.query(Station.name).all()
    return jsonify(stations)


@app.route("/api/v1.0/tobs")
def tobs():

    max_date = session.query(Measurement.date).order_by(Measurement.date.desc()).limit(1).all()[0][0] # ('2017-08-23'), str
    latest_date_dt = datetime.strptime(max_date,'%Y-%m-%d') # datetime.datetime(2017, 8, 23, 0, 0)
    def yr_prior(target_date):
            return datetime(year=target_date.year-1, month=target_date.month, day=target_date.day).strftime('%Y-%m-%d')
    
    station_yr_ago = yr_prior(latest_date_dt) # '2016-08-23', str

    last_12 = session.query(Measurement.date, Measurement.tobs).\
    filter(Measurement.date > f'{station_yr_ago}').\
    filter(Measurement.date < f'{max_date}').\
    order_by(Measurement.date.desc()).all()

    date = []
    tobs = []

    for row in last_12:
        date.append(row[0])
        tobs.append(row[1])

    tobs_dict = dict(zip(date, tobs))

    return jsonify(tobs_dict)


if __name__ == "__main__":
    app.run(debug=True)