import pandas as pd
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output, State
from scipy.spatial import KDTree
import plotly.io as pio

# Load data
input_csv_path = '/home/bigboiubu/fresh_data/walkability/boston_walkability_data.csv'
df = pd.read_csv(input_csv_path)

# Extract the specified columns
data = df[['CBSA_POP', 'NatWalkInd', 'Shape_Length', 'Shape_Area']]

# Prepare KDTree for nearest neighbor search
tree = KDTree(data[['CBSA_POP', 'Shape_Length', 'Shape_Area']])

# Initialize the Dash app
app = Dash(__name__)

# Define the CSS styles
app.layout = html.Div(style={'font-family': 'Arial, sans-serif', 'margin': '0 auto', 'max-width': '800px', 'padding': '20px'}, children=[
    html.H1('Interactive Walkability Analysis', style={'text-align': 'center', 'color': '#2c3e50'}),
    dcc.Graph(id='donut-chart'),
    dcc.Download(id="download-chart"),

    html.Div([
        html.Label('Population in location', id='label-CBSA_POP', style={'font-weight': 'bold', 'color': '#2c3e50'}),
        dcc.Slider(id='CBSA_POP-slider', 
                   min=data['CBSA_POP'].min(), 
                   max=data['CBSA_POP'].max(), 
                   value=data['CBSA_POP'].mean(), 
                   step=1, 
                   marks={int(i): str(int(i)) for i in range(int(data['CBSA_POP'].min()), int(data['CBSA_POP'].max()), int((data['CBSA_POP'].max() - data['CBSA_POP'].min()) / 10))},
                   tooltip={"placement": "bottom", "always_visible": True}),
        html.Div(id='CBSA_POP-value', style={'margin-top': '10px', 'color': '#34495e'})
    ], style={'margin-bottom': '30px'}),
    
    html.Div([
        html.Label('Length of area', id='label-Shape_Length', style={'font-weight': 'bold', 'color': '#2c3e50'}),
        dcc.Slider(id='Shape_Length-slider', 
                   min=data['Shape_Length'].min(), 
                   max=data['Shape_Length'].max(), 
                   value=data['Shape_Length'].mean(), 
                   step=0.1, 
                   marks={round(i, 2): str(round(i, 2)) for i in range(int(data['Shape_Length'].min()), int(data['Shape_Length'].max()), int((data['Shape_Length'].max() - data['Shape_Length'].min()) / 10))},
                   tooltip={"placement": "bottom", "always_visible": True}),
        html.Div(id='Shape_Length-value', style={'margin-top': '10px', 'color': '#34495e'})
    ], style={'margin-bottom': '30px'}),
    
    html.Div([
        html.Label('Area of location', id='label-Shape_Area', style={'font-weight': 'bold', 'color': '#2c3e50'}),
        dcc.Slider(id='Shape_Area-slider', 
                   min=data['Shape_Area'].min(), 
                   max=data['Shape_Area'].max(), 
                   value=data['Shape_Area'].mean(), 
                   step=0.1, 
                   marks={round(i, 2): str(round(i, 2)) for i in range(int(data['Shape_Area'].min()), int(data['Shape_Area'].max()), int((data['Shape_Area'].max() - data['Shape_Area'].min()) / 10))},
                   tooltip={"placement": "bottom", "always_visible": True}),
        html.Div(id='Shape_Area-value', style={'margin-top': '10px', 'color': '#34495e'})
    ], style={'margin-bottom': '30px'}),
    
    html.Div([
        html.Label('National Walkability Index (higher means more walkable):', style={'font-weight': 'bold', 'color': '#2c3e50'}),
        html.Div(id='NatWalkInd-value', style={'margin-top': '10px', 'color': '#34495e'})
    ]),
    html.Button("Download Chart", id="btn-download", n_clicks=0)
])

@app.callback(
    [Output('donut-chart', 'figure'),
     Output('CBSA_POP-slider', 'value'),
     Output('Shape_Length-slider', 'value'),
     Output('Shape_Area-slider', 'value'),
     Output('NatWalkInd-value', 'children'),
     Output('download-chart', 'data')],
    [Input('CBSA_POP-slider', 'value'),
     Input('Shape_Length-slider', 'value'),
     Input('Shape_Area-slider', 'value'),
     Input('btn-download', 'n_clicks')],
    [State('CBSA_POP-slider', 'value'),
     State('Shape_Length-slider', 'value'),
     State('Shape_Area-slider', 'value')]
)
def update_chart(cbsa_pop, shape_length, shape_area, n_clicks, cbsa_pop_state, shape_length_state, shape_area_state):
    # Logic to adjust the sliders based on the relationships (example relationships)
    if cbsa_pop != cbsa_pop_state:
        shape_length = shape_length + (cbsa_pop - cbsa_pop_state) * 0.1
        shape_area = shape_area + (cbsa_pop - cbsa_pop_state) * 0.05
    elif shape_length != shape_length_state:
        cbsa_pop = cbsa_pop + (shape_length - shape_length_state) * 0.5
        shape_area = shape_area + (shape_length - shape_length_state) * 0.2
    elif shape_area != shape_area_state:
        cbsa_pop = cbsa_pop + (shape_area - shape_area_state) * 0.2
        shape_length = shape_length + (shape_area - shape_area_state) * 0.3

    # Ensure values are within range
    cbsa_pop = max(min(cbsa_pop, data['CBSA_POP'].max()), data['CBSA_POP'].min())
    shape_length = max(min(shape_length, data['Shape_Length'].max()), data['Shape_Length'].min())
    shape_area = max(min(shape_area, data['Shape_Area'].max()), data['Shape_Area'].min())

    # Find the nearest neighbor to the selected values
    dist, idx = tree.query([cbsa_pop, shape_length, shape_area])
    nat_walk_ind = data.iloc[idx]['NatWalkInd']

    values = [cbsa_pop, shape_length, shape_area]
    labels = ['CBSA_POP', 'Shape_Length', 'Shape_Area']
    
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
    fig.update_layout(title_text=f'Donut Chart - CBSA_POP: {cbsa_pop}, Shape_Length: {shape_length}, Shape_Area: {shape_area}', 
                      title_font=dict(size=20, color='#2c3e50'), 
                      annotations=[dict(text='Walkability', x=0.5, y=0.5, font_size=20, showarrow=False)],
                      showlegend=True)
    fig.update_traces(marker=dict(colors=['#3498db', '#e74c3c', '#2ecc71'], line=dict(color='#fff', width=2)))

    # Save the figure as an HTML file if the download button is clicked
    download_data = None
    if n_clicks > 0:
        html_file_path = '/path/to/save/donut_chart.html'
        pio.write_html(fig, file=html_file_path, auto_open=False)
        download_data = dcc.send_file(html_file_path)

    return (fig, cbsa_pop, shape_length, shape_area, f'NatWalkInd: {nat_walk_ind}', download_data)

if __name__ == '__main__':
    app.run_server(debug=True)
