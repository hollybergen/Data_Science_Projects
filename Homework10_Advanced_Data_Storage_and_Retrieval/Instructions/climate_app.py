#--------------- Import Dependencies --------------#

import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

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
    
    results = session.query(Measurement, Station).filter(Measurement.station == Station.station).limit(10).all()

    precip_dict = {}

    for r in results:
        (m, s) = r
        precip_dict[m.date] = m.prcp

    return jsonify(precip_dict)
    

if __name__ == "__main__":
    app.run(debug=True)