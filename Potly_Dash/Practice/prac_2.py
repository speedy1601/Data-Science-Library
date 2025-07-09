import plotly.express as px
import pandas as pd
from dash import Dash, html, dcc, callback, Output, Input, dash_table

# Load the iris dataset into Polars
iris:pd.DataFrame = px.data.iris()

app = Dash()

app.layout = html.Div([ 
    html.H1(children = "Iris Data Table", style={'textAlign' : 'center'}),
    
    dcc.Dropdown(
        id = 'flower_name',
        options = iris['species'].unique(),
        value = 'setosa',
        placeholder = 'Flower Name'
    ),
    
    dash_table.DataTable(
    id='output_table',
    data=[],
    style_table={
        'height': '500px',
        'width': '95%',
        'overflowY': 'auto',
        'backgroundColor': '#000',   # pitch-black container
        'margin': 'auto'
    },
    style_header={
        'backgroundColor': '#010',   # very dark green
        'color': '#0f0',             # neon green
        'fontFamily': 'Courier New, monospace',
        'fontWeight': 'bold',
        'border': '1px solid #0f0'
    },
    style_cell={
        'backgroundColor': '#000',
        'color': '#0f0',
        'fontFamily': 'Courier New, monospace',
        'textAlign': 'left',
        'minWidth': '100px',
        'whiteSpace': 'normal'
    },
    style_data_conditional=[
        {
            'if': {'row_index': 'odd'},
            'backgroundColor': '#011'  # subtle striping
        }
    ]
)
])

@callback(
    Output(component_id = 'output_table', component_property = 'data'),
    Input(component_id = 'flower_name', component_property = 'value'),
)
def filter_table(flower_name): # flower_name is the 'value' of Dropdown.
    return ( iris.loc[iris['species'] == flower_name]
            .to_dict(orient = 'records') ) # returns list[dict].

if __name__ == '__main__':
    app.run(debug=True)