import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load the data into a pandas DataFrame
file_path = '/home/bigboiubu/repos/CS617-Visualizing-Boston/final_proj/attempts/finalizing/massbuilds/csv/boston_filtered/massbuilds-20240512.csv'
df = pd.read_csv(file_path)

# Filter the data to include only completed projects
completed_projects = df[df['status'] == 'completed']

# Extract relevant columns
traffic_related_projects = completed_projects[['year_compl', 'traffic_count_data_present', 'n_transit']]

# Filter projects that have traffic-related data
traffic_related_projects = traffic_related_projects[
    (traffic_related_projects['traffic_count_data_present'].notnull()) |
    (traffic_related_projects['n_transit'].notnull())
]

# Count the number of traffic-related projects completed each year
traffic_projects_by_year = traffic_related_projects.groupby('year_compl').size().reset_index(name='count')

# Create the bar plot with enhancements
fig = px.bar(traffic_projects_by_year, x='year_compl', y='count',
             labels={'year_compl': 'Year of Completion', 'count': 'Number of Traffic-related Projects'},
             title='Number of Traffic-related Renovation Projects Completed Over the Years')

# Enhance the visual appearance
fig.update_traces(marker_color='dodgerblue', marker_line_color='black', marker_line_width=1.5)
fig.update_layout(
    title={'text': 'Number of Traffic-related Renovation Projects Completed Over the Years', 'x': 0.5, 'xanchor': 'center'},
    xaxis_title='Year of Completion',
    yaxis_title='Number of Traffic-related Projects',
    plot_bgcolor='white',
    yaxis=dict(
        showgrid=True,
        gridcolor='lightgray',
        zerolinecolor='lightgray',
    ),
    xaxis=dict(
        showgrid=True,
        gridcolor='lightgray',
        zerolinecolor='lightgray',
    ),
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="black"
    ),
    hovermode="x unified",
    hoverlabel=dict(
        bgcolor="white",
        font_size=14,
        font_family="Arial"
    )
)

# Add annotations for the highest and lowest points
max_count = traffic_projects_by_year['count'].max()
min_count = traffic_projects_by_year['count'].min()
max_year = traffic_projects_by_year[traffic_projects_by_year['count'] == max_count]['year_compl'].values[0]
min_year = traffic_projects_by_year[traffic_projects_by_year['count'] == min_count]['year_compl'].values[0]

fig.add_annotation(x=max_year, y=max_count,
                   text=f"Highest: {max_count}",
                   showarrow=True,
                   arrowhead=2,
                   arrowsize=1,
                   arrowwidth=2,
                   arrowcolor="green",
                   ax=0,
                   ay=-40)

fig.add_annotation(x=min_year, y=min_count,
                   text=f"Lowest: {min_count}",
                   showarrow=True,
                   arrowhead=2,
                   arrowsize=1,
                   arrowwidth=2,
                   arrowcolor="red",
                   ax=0,
                   ay=40)

# Add a trend line
fig.add_trace(go.Scatter(
    x=traffic_projects_by_year['year_compl'],
    y=traffic_projects_by_year['count'],
    mode='lines',
    name='Trend Line',
    line=dict(color='firebrick', width=2)
))

# Add interactivity: buttons to filter data by year ranges
fig.update_layout(
    updatemenus=[
        dict(
            buttons=list([
                dict(
                    args=[{"xaxis.range": [2010, 2015]}],
                    label="2010-2015",
                    method="relayout"
                ),
                dict(
                    args=[{"xaxis.range": [2015, 2020]}],
                    label="2015-2020",
                    method="relayout"
                ),
                dict(
                    args=[{"xaxis.range": [2020, 2025]}],
                    label="2020-2025",
                    method="relayout"
                ),
                dict(
                    args=[{"xaxis.autorange": True}],
                    label="All Years",
                    method="relayout"
                )
            ]),
            direction="down",
            showactive=True
        )
    ]
)

# Add a range slider
fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=5, label="5Y", step="year", stepmode="backward"),
                dict(count=10, label="10Y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(visible=True),
        type="linear"
    )
)

# Save the plot to an HTML file
html_file = '/home/bigboiubu/repos/CS617-Visualizing-Boston/final_proj/attempts/finalizing/massbuilds/csv/boston_filtered/traffic_projects_plot.html'
fig.write_html(html_file)

print(f'Plot saved to {html_file}')
