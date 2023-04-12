# Author: Jack Sanders
# Created: 12/04/23

import pandas as pd
from dash import Dash, dcc, html

data = (
    pd.read_csv("avocado.csv")
    .query("type == 'conventional' and region == 'Albany'")
    .assign(Date=lambda data: pd.to_datetime(data["Date"], format="%Y-%m-%d"))
    .sort_values(by="Date")
)

ex_style = [
    {
       "href": (
            "https://fonts.googleapis.com/css2?"
            "family=Lato:wght@400;700&display=swap"
        ),
        "rel": "stylesheet", 
    }
]

app = Dash(__name__,external_stylesheets=ex_style)
app.title = "Avocado Analytics: Understand Your Avocados!"

app.layout = html.Div(
    children = [
        html.Div(
            children=[
                html.P(children="🥑", className="header-emoji"),
                html.H1(
                    children="Avocado Analytics", 
                    className="header-title"),
                html.P(
                    children=(
                        "To Analyze the behavior of avocado prices and the number"
                        " of avocados sold in the US between 2015 and 2018"
                    ),
                    className="header-description",
                ),
            ],
            className="header",
        ),
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="price-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                            {
                                "x": data["Date"],
                                "y": data["AveragePrice"],
                                "type": "lines",
                                "hovertemplate": (
                                    "$%{y:.2f}<extra></extra>"
                                )
                            },
                        ],
                        "layout": {
                            "title": {
                                "text": "Average Price of Avocados",
                                "x": 0.05,
                                "xanchor": "left",
                            },
                            "xaxis": {"fixedragon": True}, 
                            "yaxis": {
                                "tickprefix": "S", 
                                "fixedrange": True,
                            },
                            "colorway": ['#17b89'],
                        },
                    },
                ),
                className="card",
            ),
            html.Div(
                    children=dcc.Graph(
                        id="volume-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                "x": data["Date"],
                                "y": data["Date"],
                                "type": "lines",
                                }
                            ],
                            "layout": {
                                "title": {
                                    "text" : "Avocados Sold",
                                    "x": 0.05,
                                    "xanchor":"left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {"fixedrange": True},
                                "colorway": ["#E12D39"],
                            },
                        },
                    ),
                    className="card",
                ),
            ],
            className="wrapper",
        ),
    ]  
)

if __name__ == "__main__":
    app.run_server(debug=True)