
import plotly.graph_objects as go
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html

# Create sample data
data = {'Fruit': ['Apple', 'Banana', 'Orange', 'Mango'],
        'Quantity': [9, 20, 15, 12]}

# Create bar chart
bar_chart = go.Figure(data=[go.Bar(x=data['Fruit'], y=data['Quantity'])])
scatter_plot = px.scatter(data_frame=data, x='Fruit', y='Quantity')

# Create the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1(children='Dashboard'),
    html.Div(children='''
        Sample bar chart and scatter plot.
    '''),
    dcc.Graph(
        id='bar-chart',
        figure=bar_chart
    ),
    dcc.Graph(
        id='scatter-plot',
        figure=scatter_plot
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)