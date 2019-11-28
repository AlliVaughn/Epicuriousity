import json
from flask import Flask, render_template,jsonify
import pandas as pd
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
###################################
#DATABASE SETUP
###################################
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/epicuriousity.sqlite"
# db = SQLAlchemy(app)


# reflect an existing database into a new model
# Base = automap_base()
# reflect the tables
# Base.prepare(db.engine, reflect=True)

# Save references to each table
# Samples_Metadata = Base.classes.sample_metadata
# Samples = Base.classes.samples

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