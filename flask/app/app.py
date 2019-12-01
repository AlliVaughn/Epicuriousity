import numpy as np
import pandas as pd
import json
import sqlalchemy as db
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
from flask import Flask, jsonify, render_template
from sqlalchemy import MetaData

app = Flask(__name__)

# # Path to sqlite
# # database_path = "epi_db.sqlite"

# # Create an engine that can talk to the database
# engine = create_engine(f"sqlite:///data/epi-db.sqlite")
# conn = engine.connect()

# # reflect the tables
# m = MetaData()
# m.reflect(engine)
# epifactor = db.Table('epifactor', m, autoload=True, autoload_with=engine)

# # Select the table to query
# query = db.select([epifactor])
# ResultProxy = conn.execute(query)
# ResultSet = ResultProxy.fetchall()

# # Send quesry results from table to a dataframe
# ResultSet = pd.DataFrame(ResultSet)

# # Drop column "0" and row 0 (not importing index and column names?), resset index to start a 0 and rename columns
# ResultSet.drop([0], inplace=True)
# ResultSet.drop(0, axis=1, inplace=True)
# ResultSet.reset_index(inplace=True)
# ResultSet.rename(columns={1:'Calories', 2:'Fat', 3:'Protein', 4:'Ingredients'}, inplace=True)

# data = [{'name': 'Calories', 'value': ResultSet['Calories'][0]},
#                    {'name': 'Fat', 'value': ResultSet['Fat'][0]},
#                    {'name': 'Protein', 'value': ResultSet['Protein'][0]},
#                    {'name': 'Ingredients', 'value': ResultSet['Ingredients'][0]},
#                    {'name': 'Nothing', 'value': 0.2}] 

@app.route('/')
def index():
   
    return render_template('index2.html')
@app.route('/radar')
def radar():
    df = pd.read_csv('data_1.csv')
    data = df.to_dict(orient='records')
    return render_template('radar.html', data=data)   
@app.route('/radar2') 
def radar2():
    df = pd.read_csv('data_2.csv')
    data = df.to_dict(orient='records')
    return render_template('radar_2.html', data=data)
@app.route('/radar3') 
def radar3():
    df = pd.read_csv('data_3.csv')
    data = df.to_dict(orient='records')
    return render_template('radar_3.html', data=data)   
@app.route('/radar4') 
def radar4():
    df = pd.read_csv('data_4.csv')
    data = df.to_dict(orient='records')
    return render_template('radar_4.html', data=data)         
@app.route('/radar5') 
def radar5():
    df = pd.read_csv('data_5.csv')
    data = df.to_dict(orient='records')
    return render_template('radar_5.html', data=data)    

if __name__ == "__main__":
    app.run(debug=True)