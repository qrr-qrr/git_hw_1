import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from etl import get_data
app = dash.Dash(__name__)
app.layout = html.Div(children=[
    html.H1(children='Дашборд'),
    # Добавьте компоненты вашего дашборда здесь
])
if __name__ == '__main__':
    app.run_server(debug=True)
