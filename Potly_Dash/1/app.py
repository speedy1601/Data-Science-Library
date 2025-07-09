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
                              html.Div(id = 'float_containing_div', children = html.Div(id = "floating_div"))
                            ],
                 id = 'table_containing_div'),
    ],
)

if __name__ == '__main__':
    app.run(debug=True, port=3006)

"""
dashApp
|---> firstH1
|---> button1
|---> table_containing_div (relative)
|----------> table1 (relative)
|----------> float_containing_div (absolute and bottom = 0. Hence it will stand on table1)
|------------------> floating_div (absolute and bottom = 0. Hence it will stand on float_containing_div/table1)

So ultimately floating_div standing on table1 where bottom = 0 :
 __________
|  table1  |
|   ____   |
|  |flot|  |
|  |ing |  |
|__|div_|__|  -> The ground of of table1 and floating_div(also float_containing_div) are same.
"""