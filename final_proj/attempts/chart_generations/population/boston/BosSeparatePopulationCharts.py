import pandas as pd
import plotly.graph_objects as go

# Load data from CSV files
annual_change_path = '/home/bigboiubu/repos/CS617-Visualizing-Boston/final_proj/attempts/data_processing/population/boston/polished/Boston_Annual_Change.csv'
population_change_path = '/home/bigboiubu/repos/CS617-Visualizing-Boston/final_proj/attempts/data_processing/population/boston/polished/Boston_Population_Change.csv'

annual_change_df = pd.read_csv(annual_change_path)
population_change_df = pd.read_csv(population_change_path)

# Ensure column names are stripped of leading/trailing spaces
annual_change_df.columns = annual_change_df.columns.str.strip()
population_change_df.columns = population_change_df.columns.str.strip()

# Define custom colors
bar_color = 'rgb(56, 108, 176)'
line_color = 'rgb(255, 127, 0)'
background_color = 'rgb(240, 240, 240)'
grid_color = 'rgb(200, 200, 200)'

# Create bar chart for population count
bar_chart = go.Figure([go.Bar(
    x=population_change_df['date'], 
    y=population_change_df['Population'], 
    marker_color=bar_color,
    hoverinfo='x+y',
    text=population_change_df['Population'],
    textposition='outside'
)])
bar_chart.update_layout(
    title='Population Count Over the Years',
    xaxis_title='Year',
    yaxis_title='Population',
    plot_bgcolor=background_color,
    paper_bgcolor=background_color,
    font=dict(color='black'),
    xaxis=dict(showgrid=True, gridcolor=grid_color),
    yaxis=dict(showgrid=True, gridcolor=grid_color)
)

# Save bar chart as HTML
bar_chart.write_html('/home/bigboiubu/repos/CS617-Visualizing-Boston/final_proj/attempts/chart_generations/population/boston/charts/boston_population_bar_chart.html')

# Create line chart for percentage change in population
line_chart = go.Figure([go.Scatter(
    x=annual_change_df['date'], 
    y=annual_change_df['Annual Change'], 
    mode='lines+markers', 
    line=dict(color=line_color),
    marker=dict(size=8),
    hoverinfo='x+y',
    text=annual_change_df['Annual Change']
)])
line_chart.update_layout(
    title='Percentage Change in Population Over the Years',
    xaxis_title='Year',
    yaxis_title='Percentage Change',
    plot_bgcolor=background_color,
    paper_bgcolor=background_color,
    font=dict(color='black'),
    xaxis=dict(showgrid=True, gridcolor=grid_color),
    yaxis=dict(showgrid=True, gridcolor=grid_color)
)

# Save line chart as HTML
chart_storage_fp = '/home/bigboiubu/repos/CS617-Visualizing-Boston/final_proj/attempts/chart_generations/population/boston/charts/boston_population_line_chart.html'
line_chart.write_html(chart_storage_fp)
print(f'Go check them out: /home/bigboiubu/repos/CS617-Visualizing-Boston/final_proj/attempts/chart_generations/population/boston/charts/')
