import plotly.graph_objects as go
import pandas as pd

# Load the data
annual_change_df = pd.read_csv('/home/bigboiubu/repos/CS617-Visualizing-Boston/final_proj/attempts/attempt7/population/Annual_Change.csv')

# Create the line chart
line_chart = go.Figure()

# Add custom hover text
hover_text = [
    f"Year: {date}<br>Annual Change: {change:.2f}%" 
    for date, change in zip(annual_change_df['date'], annual_change_df['Annual Change'])
]

line_chart.add_trace(go.Scatter(
    x=annual_change_df['date'],
    y=annual_change_df['Annual Change'],
    mode='lines+markers',
    name="Annual Change",
    line=dict(color='royalblue', width=2, dash='dashdot'),
    marker=dict(color='red', size=8, symbol='diamond', line=dict(width=1, color='black')),
    text=hover_text,
    hoverinfo='text'
))

line_chart.update_layout(
    title=dict(
        text="Boston's Population Change Percentage",
        x=0.5,
        xanchor='center',
        font=dict(size=24, color='darkblue', family='Arial, sans-serif')
    ),
    xaxis=dict(
        title="Year",
        titlefont=dict(size=18, color='darkblue', family='Arial, sans-serif'),
        tickfont=dict(size=14, color='darkblue', family='Arial, sans-serif'),
        range=["1950", "2023"],
        showgrid=True,
        gridcolor='lightgrey',
        zeroline=True,
        zerolinecolor='grey',
        showline=True,
        linewidth=2,
        linecolor='black',
        mirror=True,
        rangeselector=dict(
            buttons=list([
                dict(count=10, label="10y", step="year", stepmode="backward"),
                dict(count=20, label="20y", step="year", stepmode="backward"),
                dict(count=30, label="30y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        )
    ),
    yaxis=dict(
        title="Annual Change",
        titlefont=dict(size=18, color='darkblue', family='Arial, sans-serif'),
        tickfont=dict(size=14, color='darkblue', family='Arial, sans-serif'),
        showgrid=True,
        gridcolor='lightgrey',
        zeroline=True,
        zerolinecolor='grey',
        showline=True,
        linewidth=2,
        linecolor='black',
        mirror=True
    ),
    plot_bgcolor='white',
    paper_bgcolor='lightgrey',
    width=750,  
    height=550,  
    margin=dict(l=60, r=60, t=80, b=60),
    legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01,
        font=dict(size=14, color='darkblue')
    ),
    hovermode='x unified',
    hoverlabel=dict(
        bgcolor="white",
        font_size=14,
        font_family="Arial, sans-serif"
    ),
)

# Add annotation if the year 2000 exists in the dataset
if '2000' in annual_change_df['date'].values:
    annotation_y_value = annual_change_df.loc[annual_change_df['date'] == '2000', 'Annual Change'].values[0]
    line_chart.add_annotation(
        x='2000',
        y=annotation_y_value,
        xref="x",
        yref="y",
        text="Significant change",
        showarrow=True,
        arrowhead=2,
        ax=0,
        ay=-40
    )

# Save the chart as an HTML file
line_chart.write_html('/home/bigboiubu/repos/CS617-Visualizing-Boston/final_proj/attempts/attempt7/population/annual_change_chart.html')

# Print confirmation message
print("Line chart saved as annual_change_chart.html")
