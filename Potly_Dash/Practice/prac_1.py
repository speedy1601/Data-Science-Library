import plotly.express as px
from dash import Dash, html, dcc, callback, Output, Input, dash_table
import dash_bootstrap_components as dbc
import pandas as pd

iris:pd.DataFrame = px.data.iris(return_type = "pandas")

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([ 
    html.H1(children = "Iris Data table", style = {'textAlign':'center'}),

    dcc.Dropdown(id = 'flower_name',
                 options = iris['species'].unique(),
                 value = 'setosa',
                 placeholder = 'flower name',
    ),

    dash_table.DataTable(id = 'output_table', data = [], row_selectable = 'multi')
])

@callback(
        Output(component_id = 'output_table', component_property = 'data'),
        Input(component_id = 'flower_name', component_property = 'value'),
)
def filter_table(flower_name): # 'value' of Dropdown.
    return ( iris.iloc[(iris['species'] == flower_name).to_numpy(), :4]
            .to_dict(orient = 'records') ) # for pandas --> .to_dict(orient = 'records').

if __name__ == '__main__':
    app.run(debug = True)