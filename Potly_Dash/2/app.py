import plotly.express as px
import pandas as pd
from dash import Dash, html, dcc, callback, Output, Input, dash_table

# Load the iris dataset into dataframe.
iris:pd.DataFrame = px.data.iris()

app = Dash()

app.layout = html.Div(
    id = 'dashApp',

    children = [
        html.H1(id = 'firstH1', children = "Iris Data Table"),

        html.Button(id = 'button1', children = "button1"),

        html.Div(children = [ dash_table.DataTable(id = 'table1', data = iris.to_dict(orient = 'records')),
                              html.Div(id = "floating_div"),
                            ],
                 id = 'table_and_floatingDiv'),
    ],
)

if __name__ == '__main__':
    app.run(debug=True, port=3007)