import json

import numpy as np
import pandas as pd

import plotly
import plotly.graph_objs as go
import plotly.plotly as py

from flask import Flask, render_template
from queries import *

app = Flask(__name__)

@app.route('/')
def index():    
    return render_template("index.html")


@app.route('/teams')
def teams():

    rows = get_teams()
    
    return render_template("list_teams.html",rows = rows)

@app.route('/showLineChart')
def line():
    count = 500
    xScale = np.linspace(0, 100, count)
    yScale = np.random.randn(count)
 
    # Create a trace
    trace = go.Scatter(
        x = xScale,
        y = yScale
    )
 
    data = [trace]
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('charts.html', graphJSON=graphJSON)

@app.route('/showMultiChart')
def multiLine():
    count = 500
    xScale = np.linspace(0, 100, count)
    y0_scale = np.random.randn(count)
    y1_scale = np.random.randn(count)
    y2_scale = np.random.randn(count)
 
    # Create traces
    trace0 = go.Scatter(
        x = xScale,
        y = y0_scale
    )
    trace1 = go.Scatter(
        x = xScale,
        y = y1_scale
    )
    trace2 = go.Scatter(
        x = xScale,
        y = y2_scale
    )
    data = [trace0, trace1, trace2]
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('charts.html',
                           graphJSON=graphJSON)

@app.route('/test')
def test():
    rows = get_teams()
    df = pd.DataFrame( [[ij for ij in i] for i in rows] )
    df.rename(columns={0: 'ID', 1: 'Name', 2: 'Nickname', 3: 'Squad', 4:'Average Age',5:'Number of Foreigners', 6:'Total Market Value', 7:'Average Market Value'}, inplace=True)
    df = df.sort_values(['Total Market Value'], ascending=[1])
 
    # Create a trace
    trace = go.Scatter(
        x=df['Total Market Value'],
        y=df['Average Market Value'],
        text=df['Name'],
        mode='markers'
    )

    data = [trace]
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('charts.html', graphJSON=graphJSON)


if __name__ == '__main__':  
    print('starting Flask app', app.name)  
    app.run(debug=True)