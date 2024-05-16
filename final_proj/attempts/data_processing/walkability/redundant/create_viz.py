import plotly.graph_objects as go
import pandas as pd

# Create a mock dataset representing the relationships between different factors
data = pd.DataFrame({
    'source': ['Population', 'Employment', 'Households', 'Vehicles', 'Walkability Index', 'Population', 'Employment'],
    'target': ['Employment', 'Households', 'Vehicles', 'Walkability Index', 'Population', 'Vehicles', 'Walkability Index'],
    'value': [10, 20, 30, 40, 50, 60, 70]
})

# Create a list of unique nodes
nodes = list(set(data['source']).union(set(data['target'])))

# Create indices for the source and target columns
data['source_index'] = data['source'].apply(lambda x: nodes.index(x))
data['target_index'] = data['target'].apply(lambda x: nodes.index(x))

# Create the chord diagram
fig = go.Figure(data=go.Chord(
    matrix=data.pivot_table(index='source_index', columns='target_index', values='value', fill_value=0).values,
    labels=nodes,
    colorscale='Viridis',
    colorbar=dict(title='Values')
))

fig.update_layout(
    title_text='Chord Diagram of Factors Affecting Walkability Index',
    font_size=15
)

fig.show()
