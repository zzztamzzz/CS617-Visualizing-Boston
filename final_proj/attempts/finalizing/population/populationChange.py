import plotly.graph_objects as go
import pandas as pd

# Load the data
population_change_df = pd.read_csv('/home/bigboiubu/repos/CS617-Visualizing-Boston/final_proj/attempts/attempt7/population/Population_Change.csv')

# Create the bar chart
bar_chart = go.Figure()

bar_chart.add_trace(go.Bar(
    x=population_change_df['date'],
    y=population_change_df['Population'],
    name="Population Change",
    marker=dict(
        color=population_change_df['Population'],
        colorscale='Blues',  # Gradient colors
        showscale=True,
        colorbar=dict(
            title="Population Change",
            titlefont=dict(size=14, color='darkslategray'),
            tickfont=dict(size=12, color='darkslategray')
        )
    ),
    opacity=0.8  # Adjusted opacity for better visibility
))

bar_chart.update_layout(
    title={
        'text': "Boston's Population Change Over The Years",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {
            'size': 26,
            'color': 'darkslategray',
            'family': 'Arial, sans-serif'
        }
    },
    xaxis_title={
        'text': "Year",
        'font': {
            'size': 18,
            'color': 'darkslategray',
            'family': 'Arial, sans-serif'
        }
    },
    yaxis_title={
        'text': "Population Change",
        'font': {
            'size': 18,
            'color': 'darkslategray',
            'family': 'Arial, sans-serif'
        }
    },
    xaxis=dict(
        range=["1950", "2023"],
        tickfont=dict(size=12, color='darkslategray', family='Arial, sans-serif'),
        showgrid=True,
        gridcolor='lightgray',
        zerolinecolor='gray'
    ),
    yaxis=dict(
        tickfont=dict(size=12, color='darkslategray', family='Arial, sans-serif'),
        showgrid=True,
        gridcolor='lightgray',
        zerolinecolor='gray',
        minor=dict(
            showgrid=True,
            gridcolor='lightgray',
            gridwidth=0.5
        )
    ),
    plot_bgcolor='#f9f9f9',  # Subtle background color
    paper_bgcolor='white',
    width=750,  
    height=450,
    margin=dict(l=50, r=50, t=70, b=50),  # Adjust margins
    legend=dict(
        x=0.01,
        y=0.99,
        traceorder='normal',
        font=dict(size=12, color='darkslategray', family='Arial, sans-serif')
    ),
    xaxis_rangeslider=dict(visible=True),  # Enable range slider
    xaxis_rangeselector=dict(  # Add range selector buttons
        buttons=list([
            dict(count=10, label="10y", step="year", stepmode="backward"),
            dict(count=20, label="20y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    ),
    images=[  # Add background image
        dict(
            source="https://www.transparenttextures.com/patterns/asfalt-light.png",
            xref="paper", yref="paper",
            x=0, y=1,
            sizex=1, sizey=1,
            sizing="stretch",
            opacity=0.2,
            layer="below"
        )
    ]
)

# Enhance hover information
bar_chart.update_traces(
    hoverinfo='text',
    hovertext=population_change_df.apply(lambda row: f"<b>Year:</b> {row['date']}<br><b>Population Change:</b> {row['Population']}", axis=1),
    hoverlabel=dict(
        bgcolor='white',
        font_size=14,
        font_family='Arial, sans-serif',
        bordercolor='darkslategray'
    )
)

# Add transitions and animations
bar_chart.update_layout(
    transition=dict(
        duration=500,
        easing='cubic-in-out'
    )
)

# Save the chart as an HTML file
bar_chart.write_html('/home/bigboiubu/repos/CS617-Visualizing-Boston/final_proj/attempts/attempt7/population/population_change_chart.html')

# Print confirmation message
print("Bar chart saved as population_change_chart.html")
