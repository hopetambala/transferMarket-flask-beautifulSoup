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

@app.route('/market_value_team_comparison')
def marketValues():
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

    layout = go.Layout(
        title='Total Market Value vs Average Market Value',
        xaxis=dict(type='log', title='Total Market Value' ),
        yaxis=dict(title='Average Market Value' )
    )

    fig = go.Figure(data=[trace], layout=layout)
    #data = [trace]
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('charts.html', graphJSON=graphJSON)


@app.route('/market_value_jersey_comparison')
def marketValuesPlayers():
    rows = get_players()
    df = pd.DataFrame( [[ij for ij in i] for i in rows] )
    df.rename(columns={0: 'ID', 1: 'JerseyNumber', 2: 'Name', 3: 'Position', 4:'Birthday',5:'Nationality', 6:'Team', 7:'Market Value'}, inplace=True)
    #df = df.sort_values(['Market Value'], ascending=[1])
 
    # Create a trace
    trace = go.Scatter(
        x=df['JerseyNumber'],
        y=df['Market Value'],
        text=df['Name'],
        mode='markers'
    )

    layout = go.Layout(
        title='Jersey Number vs Player Market Value',
        xaxis=dict(title='Jersey Number' ),
        yaxis=dict(title='Player Market Value' )
    )

    fig = go.Figure(data=[trace], layout=layout)
    #data = [trace]
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('charts.html', graphJSON=graphJSON)

@app.route('/players_detailed')
def teamsPlot():
    rows = get_players()

    df = pd.DataFrame( [[ij for ij in i] for i in rows] )
    df.rename(columns={0: 'ID', 1: 'JerseyNumber', 2: 'Name', 3: 'Position', 4:'Birthday',5:'Nationality', 6:'Team', 7:'Market Value'}, inplace=True)
    #df = df.sort_values(['Market Value'], ascending=[1])
 
    # Create a trace
    trace = go.Table(
        header=dict(values=list(df.columns),
                    fill = dict(color='#C2D4FF'),
                    align = ['left'] * 5),
        cells=dict(values=[df.ID, df.JerseyNumber, df.Name, df.Position,df.Birthday, df.Nationality, df.Team, df['Market Value']],
                fill = dict(color='#F5F8FF'),
                align = ['left'] * 5)
        )

    layout = go.Layout(
        title='Players in the Top Leagues Around the World Ranked by Value',
    )

    fig =go.Figure(data=[trace],layout=layout)
    #data = [trace]

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('charts.html', graphJSON=graphJSON)


@app.route('/positions')
def positionsBarChart():
    rows = count_player_positions()
    print(rows)

    df = pd.DataFrame( [[ij for ij in i] for i in rows] )
    df.rename(columns={0: 'Position', 1: 'Count of Position', 2: 'Average Market Value for Position'}, inplace=True)
    #df = df.sort_values(['Market Value'], ascending=[1])
 
    # Create a trace
    trace = [
        go.Bar(
            x=df['Position'], # assign x as the dataframe column 'x'
            y=df['Count of Position']
            #hoverlabel=df['Team']
        )
    ]

    layout = go.Layout(
        title='Positions vs Count of Positions for Top 5 leagues in Europe and MLS',
        xaxis=dict(title='Position' ),
        yaxis=dict(title='Count of Positions' )
    )
    

    fig = go.Figure(data=trace, layout=layout)
    #data = trace
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('charts.html', graphJSON=graphJSON)

if __name__ == '__main__':  
    print('starting Flask app', app.name)  
    app.run(debug=True)
