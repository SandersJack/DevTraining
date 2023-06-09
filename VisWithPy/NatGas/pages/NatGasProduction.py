# Author: Jack Sanders
# Created: 13/04/23

import pandas as pd
import dash
from dash import Dash, dcc, html, Input, Output, callback

dash.register_page(__name__)

data = (
    pd.read_csv("dataSets/NG_PROD_SUM_A_EPG0_FGW_MMCF_M.csv")
    .assign(Date=lambda data: pd.to_datetime(data["Date"], format="%d/%m/%Y"))
    .sort_values(by="Date")
)

data_price = (
    pd.read_csv("dataSets/NG_PRI_SUM_DCU_NUS_M.csv")
    .assign(Date=lambda data: pd.to_datetime(data["Date"], format="%d/%m/%Y"))
    .sort_values(by="Date")
)

data_export = (
    pd.read_csv("dataSets/NG_MOVE_EXPC_S1_M.csv")
    .assign(Date=lambda data: pd.to_datetime(data["Date"], format="%d/%m/%Y"))
    .sort_values(by="Date")
)

can_data_prod = (
    pd.read_csv("dataSets/canada-production.csv")
    .assign(Date=lambda data: pd.to_datetime(data["Date"], format="%m/%d/%Y"))
    .sort_values(by="Date")
)

can_data_export = (
    pd.read_csv("dataSets/canada-import-export.csv")
    .assign(Date=lambda data: pd.to_datetime(data["Date"], format="%d/%m/%Y"))
    .sort_values(by="Date")
)

can_data_LNG_export = (
    pd.read_csv("dataSets/canada-LNG-exports.csv")
    .assign(Date=lambda data: pd.to_datetime(data["Date"], format="%d/%m/%Y"))
    .sort_values(by="Date")
)

can_data_LNG_export = can_data_LNG_export.loc[(can_data_LNG_export['Flow'] == "Exports") & (can_data_LNG_export['Terminal'] == "Total")]
can_data_export = can_data_export.loc[(can_data_export['Flow'] == "Exports") & (can_data_export['Region'] == "Total")]

world_data = (
    pd.read_csv("dataSets/world-data.csv")
    .assign(Date=lambda data: pd.to_datetime(data["Date"], format="%Y"))
    .sort_values(by="Date")
)

country_list = []
countries = [] #["United States", "Canada"]

for col in world_data.columns:
    if "exports" in col:
        countries.append(col[25:-8])
        country_list.append(col[25:-8])
        
countries.sort()

ex_style = [
    {
       "href": (
            "https://fonts.googleapis.com/css2?"
            "family=Lato:wght@400;700&display=swap"
        ),
        "rel": "stylesheet", 
    }
]

#app = Dash(__name__,external_stylesheets=ex_style)
#app.title = "Natural Gas Analytics"

layout = html.Div(
    children=[
        html.Div(
            children=[
                html.H1(
                    children="Production Data",
                    className="sub-header-title"
                ),
            ],
            className="header",
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(children="Country", className="menu-title"),
                        dcc.Dropdown(
                            id="country-filter",
                            options=[
                                {'label': html.Span( [
                                    html.Img(src="/assets/imgs/flagicons_py/{}.png".format(_country), height=20,width=20),
                                    html.Span(_country,style={'font-size': 15, 'padding-left': 10}),
                                ],
                                ), 'value': _country}
                                for _country in countries
                                ],
                            value="World", 
                            clearable=False, 
                            className="dropdown",
                        ),
                    ]
                ),
                html.Div(
                    children=[
                        html.Div(
                            children='Date Range', className='menu-title'
                        ),
                        dcc.DatePickerRange(
                            id='date-range',
                            min_date_allowed=data['Date'].min().date(),
                            max_date_allowed=data['Date'].max().date(),
                            start_date=data['Date'].min().date(),
                            end_date=data['Date'].max().date(),
                        ),
                    ]
                ),
            ],
            className="menu"
        ), 
        html.Div(
            children=[
                html.Div(
                    children = dcc.Graph(
                        id="Withdrawl-chart", 
                        config={"displayModeBar":False},
                    ),
                    className = "card",
                ),
            ],
            className="wrapper",
        ),
        html.Div(
            children=[
                html.Div(
                    children = dcc.Graph(
                        id="Export-chart", 
                        config={"displayModeBar":False},
                    ),
                    className = "card",
                ),
            ],
            className="wrapper",
        ),
        html.Div(
            children=[
                html.Div(
                    children = dcc.Graph(
                        id="Price-chart", 
                        config={"displayModeBar":False},
                    ),
                    className = "card",
                ),
            ],
            className="wrapper",
        ),
    ]
)

@callback(
    Output('Withdrawl-chart', 'figure'),
    Output('Export-chart', 'figure'),
    Output('Price-chart', 'figure'),
    Input('country-filter', 'value'),
    Input("date-range", "start_date"),
    Input("date-range", "end_date"),
)

def update_charts(_country,start_date, end_date):
    
    if(_country == "United States"):
        
        fdata = data.query(
        "Date >= @start_date and Date <= @end_date"
        )
        
        fdata_export = data_export.query(
        "Date >= @start_date and Date <= @end_date"
        )
        
        fdata_price = data_price.query(
        "Date >= @start_date and Date <= @end_date"
        )
        
        full_chart_fig = {
            "data": [
                {
                    "x": fdata["Date"],
                    "y": fdata["U.S. Natural Gas Gross Withdrawals (MMcf)"],
                    "type": "lines", 
                    "hovertemplate": "%{x:%m-%Y}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "text": "Natural Gas Gross Withdrawals",
                    "x": 0.05,
                    "xanchor": "left",
                },
                "xaxis": {"title": "Date","fixedrange": True},
                "yaxis": {"title": "Gas Gross Withdrawals [MMcf]", "fixedrange": True},
                "colorway": ["#87CEEB"],
            },
        }
        
        export_chart_fig = {
            "data": [
                {
                    "x": fdata_export["Date"],
                    "y": fdata_export["Liquefied U.S. Natural Gas Exports (MMcf)"],
                    "type": "lines", 
                    "name": "Liquefied Exports",
                    "hovertemplate": "%{x:%m-%Y}<extra></extra>",
                },
                {
                    "x": fdata_export["Date"],
                    "y": fdata_export["U.S. Natural Gas Pipeline Exports (MMcf)"],
                    "type": "lines", 
                    "name": "Pipeline Exports",
                    "hovertemplate": "%{x:%m-%Y}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "text": "Natural Gas Exports",
                    "x": 0.05,
                    "xanchor": "left",
                },
                "xaxis": {"title": "Date","fixedrange": True},
                "yaxis": {"title": "Gas Gross Withdrawals [MMcf]", "fixedrange": True},
                "colorway": ["#A020F0","#71797E"],
            },
        }
        
        price_chart_fig = {
            "data": [
                {
                    "x": fdata_price["Date"],
                    "y": fdata_price["Price of Liquefied U.S. Natural Gas Exports (Dollars per Thousand Cubic Feet)"],
                    "type": "lines", 
                    "name": "Liquefied Exports",
                    "hovertemplate": "%{x:%m-%Y}<extra></extra>",
                },
                {
                    "x": fdata_price["Date"],
                    "y": fdata_price["Price of U.S. Natural Gas Pipeline Exports (Dollars per Thousand Cubic Feet)"],
                    "type": "lines", 
                    "name": "Pipeline Exports",
                    "hovertemplate": "%{x:%m-%Y}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "text": "Natural Gas Price",
                    "x": 0.05,
                    "xanchor": "left",
                },
                "xaxis": {"title": "Date","fixedrange": True},
                "yaxis": {"title": "Natural Gas Price [$/kCF]", "fixedrange": True},
                "colorway": ["#A020F0","#71797E"],
            },
        }
    
    elif(_country == "Canada"):
        
        fcan_data_prod = can_data_prod.query(
        "Date >= @start_date and Date <= @end_date"
        )
        
        fcan_data_export = can_data_export.query(
        "Date >= @start_date and Date <= @end_date"
        )
        
        fcan_data_LNG_export = can_data_LNG_export.query(
        "Date >= @start_date and Date <= @end_date"
        )
        
        
        full_chart_fig = {
            "data": [
                {
                    "x": fcan_data_prod["Date"],
                    "y": fcan_data_prod["Total (mmcf/d)"]*30.437,
                    "type": "lines", 
                    "hovertemplate": "%{x:%m-%Y}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "text": "Natural Gas Gross Withdrawals",
                    "x": 0.05,
                    "xanchor": "left",
                },
                "xaxis": {"title": "Date","fixedrange": True},
                "yaxis": {"title": "Gas Gross Withdrawals [MMcf]", "fixedrange": True},
                "colorway": ["#87CEEB"],
            },
        }
        
        export_chart_fig = {
            "data": [
                {
                    "x": fcan_data_export["Date"],
                    "y": fcan_data_export["Volume (MCF)"],
                    "type": "lines", 
                    "name": "Exports",
                    "hovertemplate": "%{x:%m-%Y}<extra></extra>",
                },
                {
                    "x": fcan_data_LNG_export["Date"],
                    "y": fcan_data_LNG_export["Volume (MCF)"],
                    "type": "lines", 
                    "name": "LNG Exports",
                    "hovertemplate": "%{x:%m-%Y}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "text": "Natural Gas Exports",
                    "x": 0.05,
                    "xanchor": "left",
                },
                "xaxis": {"title": "Date","fixedrange": True},
                "yaxis": {"title": "Gas Gross Withdrawals [Mcf]", "fixedrange": True},
                "colorway": ["#A020F0","#71797E"],
            },
        }
        
        price_chart_fig = {
            "data": [
                {
                    "x": fcan_data_export["Date"],
                    "y": fcan_data_export["Price (US$/kCF)"],
                    "type": "lines", 
                    "name": "Exports",
                    "hovertemplate": "%{x:%m-%Y}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "text": "Natural Gas Price",
                    "x": 0.05,
                    "xanchor": "left",
                },
                "xaxis": {"title": "Date","fixedrange": True},
                "yaxis": {"title": "Natural Gas Price [$/kCF]", "fixedrange": True},
                "colorway": ["#A020F0","#71797E"],
            },
        }
        
    else:
        
        fworld_data = world_data.query(
        "Date >= @start_date and Date <= @end_date"
        )
        
        prod_name = "Dry natural gas production, {}, Annual".format(_country)
        export_name = "Dry natural gas exports, {}, Annual".format(_country)
        
        full_chart_fig = {
            "data": [
                {
                    "x": fworld_data["Date"],
                    "y": fworld_data[prod_name],
                    "type": "lines", 
                    "hovertemplate": "%{x:%m-%Y}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "text": "Natural Gas Gross Withdrawals",
                    "x": 0.05,
                    "xanchor": "left",
                },
                "xaxis": {"title": "Date","fixedrange": True},
                "yaxis": {"title": "Gas Gross Withdrawals [Bcf]", "fixedrange": True},
                "colorway": ["#87CEEB"],
            },
        }
        
        export_chart_fig = {
            "data": [
                {
                    "x": fworld_data["Date"],
                    "y": fworld_data[export_name],
                    "type": "lines", 
                    "name": "Exports",
                    "hovertemplate": "%{x:%m-%Y}<extra></extra>",
                },
            ],
            "layout": {
                "title": {
                    "text": "Natural Gas Exports",
                    "x": 0.05,
                    "xanchor": "left",
                },
                "xaxis": {"title": "Date","fixedrange": True},
                "yaxis": {"title": "Gas Annul Exports [Bcf]", "fixedrange": True},
                "colorway": ["#A020F0","#71797E"],
            },
        }
        
        price_chart_fig = {
            "data": [
            ],
            "layout": {
                "title": {
                    "text": "Natural Gas Price",
                    "x": 0.05,
                    "xanchor": "left",
                },
                "xaxis": {"title": "Date","fixedrange": True},
                "yaxis": {"title": "Natural Gas Price [$/kCF]", "fixedrange": True},
                "colorway": ["#A020F0","#71797E"],
            },
        }

    
    return full_chart_fig,export_chart_fig, price_chart_fig

#if __name__ == "__main__":
#    app.run_server(host= '0.0.0.0',debug=True)