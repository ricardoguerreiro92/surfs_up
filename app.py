#dependencies
import datetime as dt
import sqlite3
from venv import create
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify, request

#create engine
engine = create_engine('sqlite:///hawaii.sqlite')
#reflecting database
Base = automap_base()
Base.prepare(engine, reflect=True)

#saving reference to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

#create session link from python to db
session = Session(engine)

#setup flask app
app = Flask(__name__)

#Main route from flask app
@app.route("/")
def welcome():
    print("Welcome page has been accessed...")
    return(
        '''Welcome to the Climate Analysis API</br>
        Available Routes</br>
        <a href = 'http://127.0.0.1:5000/api/v1.0/precipitation'>Precipitation V1.0</a href></br>
        <a href = 'http://127.0.0.1:5000/api/v1.0/stations'>Stations V1.0</a href></br>
        <a href = 'http://127.0.0.1:5000/api/v1.0/tobs'>Time of Observation Error (TOBs) V1.0</a href></br>
        /api/v1.0/temp/start_date(yyyy-mm-dd)/end_date(yyyy-mm-dd)</br>
        ''')

#Precipitation route from flask app    
@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year = dt.date(2017,8,23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    print("Precipitation page has been accessed...")
    return jsonify(precip)

#Station route from flask app
@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    print("Stations page accessed...")
    return jsonify(stations=stations)

#TOBS route from flask app
@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017,8,23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
            filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    print("TOBS page accessed...")
    return jsonify(temps=temps)

#Start/end date routes for min,max,avg temps from flask app
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    #Determine start and end date
    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps = temps)
    
    #Calculate min,avg,max temps
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
            filter(Measurement.date <= end).all()
    
    temps = list(np.ravel(results))
    
    print("Start/End route has been accessed...")
    return jsonify(temps=temps)
    