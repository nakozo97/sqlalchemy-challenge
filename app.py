# 1. Import Dependencies

import numpy as np
import pandas as pd

import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session, Query, create_session
from sqlalchemy import create_engine, func, inspect, desc


# 2. import Flask
from flask import Flask, jsonify, request

#################################################
# 3. Database Setup
#################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite", echo=False)
conn = engine.connect()

# reflect an existing database into a new model
# reflect the tables
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

# Create our session (link) from Python to the DB
Session = Session(engine)

#################################################
# 4. Use Flask to create your routes.

# Create an app, being sure to pass __name__
app = Flask(__name__)

#################################################

# 5. Flask routes
@app.route("/")
def home():
    print("Server received request for 'Available Routes' page...")
    return(

         f"Available Routes:<br/>"
         
         f"/api/v1.0/precipitation<br/>"
         
         f"/api/v1.0/stations<br/>"

         f"/api/v1.0/tobs<br/>"

         f"/api/v1.0/&ltstart&gt<br/>"
        
         f"/api/v1.0/&ltstart&gt/&ltend&gt<br/>"

    )

# 6. Define what to do when a user hits the /about route
@app.route("/about")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page! Please navigate back to Home page."

# Convert the query results to a dictionary using date as the key and prcp as the value.
# Return the JSON representation of your dictionary.

@app.route("/api/v1.0/precipitation")
def precipitation(): 
    print("Server received request for '/api/v1.0/precipitation' page...")
    
    prcp_scores = Session.query(measurement.date, measurement.prcp).\
        filter(measurement.date >= (dt.date(2017,8,23) - dt.timedelta(days=365))).\
        order_by(measurement.date).all()

    all_prcp_scores = list(np.ravel(prcp_scores))
    
    return jsonify(all_prcp_scores)

@app.route("/api/v1.0/stations")
def stations(): 
    print("Server received request for '/api/v1.0/stations' page...")
    
    available_stations = Session.query(measurement.station.distinct()).all()

    all_stations = list(np.ravel(available_stations))
    
    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs(): 
    print("Server received request for '/api/v1.0/tobs' page...")
    
    year_ago = dt.date(2017,8,23) - dt.timedelta(days=365)

    top_active_station = Session.query(measurement.station, func.count(measurement.station)).\
        group_by(measurement.station).\
        order_by(func.count(measurement.station).desc()).first()

    USC00519281_last12_months = Session.query(measurement.station, measurement.tobs, measurement.date).\
        filter(measurement.date >= year_ago).\
        filter(measurement.station == top_active_station[0]).\
        order_by(measurement.date).all()
    
    most_active_station = list(np.ravel(USC00519281_last12_months))
    
    return jsonify(most_active_station)

# When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
# Dynamic URL

@app.route("/api/v1.0/<start>")
def start_only(start): 
    print("Server received request for '/api/v1.0/start' page...")

    tobs_results = Session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).\
        filter(measurement.date >= start).all()

    tobs_results_list = list(np.ravel(tobs_results))

    return jsonify(tobs_results_list)
    
# When given the start and the end date, calculate the TMIN, TAVG, and TMAX 
# for dates between the start and end date inclusive.
# Dynamic URL

@app.route("/api/v1.0/<start>/<end>")
def start_end(start,end): 
    print("Server received request for '/api/v1.0/<start>/<end>' page...")

    multi_tobs_results = Session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).\
        filter(measurement.date >= start).\
        filter(measurement.date <= end).all()

    multi_tobs_results_list = list(np.ravel(multi_tobs_results))

    return jsonify(multi_tobs_results_list)

if __name__ == "__main__":
    app.run(debug=True)
