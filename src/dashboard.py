# dashboard.py

import os
import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Determine the absolute path of the current file's directory
base_path = os.path.abspath(os.path.dirname(__file__))
# Use the absolute path to load the CSV file
csv_file_path = os.path.join(base_path, '../data/processed_customers.csv')

# Load the data
df = pd.read_csv(csv_file_path)

app = dash.Dash(__name__)

# Create a dropdown for selecting the X and Y axes
app.layout = html.Div(children=[
    html.H1(children='Customer Segmentation Dashboard'),
    
    html.Div([
        html.Label('X-axis:'),
        dcc.Dropdown(
            id='x-axis',
            options=[{'label': col, 'value': col} for col in df.columns if col not in ['Cluster']],
            value='Annual Income (k$)'
        ),
    ]),

    html.Div([
        html.Label('Y-axis:'),
        dcc.Dropdown(
            id='y-axis',
            options=[{'label': col, 'value': col} for col in df.columns if col not in ['Cluster']],
            value='Spending Score (1-100)'
        ),
    ]),

    html.Div([
        html.Label('Cluster Filter:'),
        dcc.Dropdown(
            id='cluster-filter',
            options=[{'label': str(cluster), 'value': cluster} for cluster in sorted(df['Cluster'].unique())],
            multi=True,
            value=[]
        ),
    ]),

    dcc.Graph(id='segmentation-graph'),
])

# Update graph based on user input
@app.callback(
    dash.dependencies.Output('segmentation-graph', 'figure'),
    [
        dash.dependencies.Input('x-axis', 'value'),
        dash.dependencies.Input('y-axis', 'value'),
        dash.dependencies.Input('cluster-filter', 'value')
    ]
)
def update_graph(x_axis, y_axis, selected_clusters, data=df):
    filtered_df = data if not selected_clusters else data[data['Cluster'].isin(selected_clusters)]
    fig = px.scatter(filtered_df, x=x_axis, y=y_axis, color='Cluster', title='Customer Segmentation')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
