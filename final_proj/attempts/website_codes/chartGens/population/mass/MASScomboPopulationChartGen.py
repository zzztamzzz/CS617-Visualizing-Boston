
'''
combo of both
'''
import pandas as pd
import plotly.graph_objects as go

# Load data from CSV files
annual_change_path = '/home/bigboiubu/repos/CS617-Visualizing-Boston/final_proj/attempts/data_processing/population/massachusetts/polished/Massachusetts_Annual_Change_State.csv'
population_change_path = '/home/bigboiubu/repos/CS617-Visualizing-Boston/final_proj/attempts/data_processing/population/massachusetts/polished/Massachusetts_Population_Change_State.csv'

annual_change_df = pd.read_csv(annual_change_path)
population_change_df = pd.read_csv(population_change_path)

# Ensure column names are stripped of leading/trailing spaces
annual_change_df.columns = annual_change_df.columns.str.strip()
population_change_df.columns = population_change_df.columns.str.strip()

# Define custom colors
bar_color = 'rgb(34, 139, 34)'  # Forest Green
line_color = 'rgb(255, 69, 0)'  # Red-Orange
background_color = 'rgb(245, 245, 245)'  # White Smoke
grid_color = 'rgb(220, 220, 220)'  # Gainsboro

# Create combination chart
fig = go.Figure()

# Add bar chart for population count
fig.add_trace(go.Bar(
    x=population_change_df['date'],
    y=population_change_df['Population'],
    name='Population',
    marker_color=bar_color,
    hoverinfo='x+y',
    text=population_change_df['Population'],
    textposition='outside',
    yaxis='y'
))

# Add line chart for percentage change in population
fig.add_trace(go.Scatter(
    x=annual_change_df['date'],
    y=annual_change_df['Annual Change'],
    name='Annual Change',
    mode='lines+markers',
    line=dict(color=line_color),
    marker=dict(size=8),
    hoverinfo='x+y',
    text=annual_change_df['Annual Change'],
    yaxis='y2'
))

# Update layout for the combination chart
fig.update_layout(
    title='Population Count and Annual Change Over the Years',
    xaxis=dict(
        title='Year',
        showgrid=True,
        gridcolor=grid_color
    ),
    yaxis=dict(
        title='Population',
        showgrid=True,
        gridcolor=grid_color
    ),
    yaxis2=dict(
        title='Annual Change (%)',
        overlaying='y',
        side='right',
        showgrid=False,
    ),
    plot_bgcolor=background_color,
    paper_bgcolor=background_color,
    font=dict(color='black'),
    legend=dict(x=0.1, y=1.1, orientation='h')
)

# Save the combination chart as HTML
chart_location = '/home/bigboiubu/repos/CS617-Visualizing-Boston/final_proj/attempts/website_codes/chartGens/population/mass/mass_population_combination_chart.html'
fig.write_html(chart_location)
print(f'Look at this BEAUT {chart_location}')
