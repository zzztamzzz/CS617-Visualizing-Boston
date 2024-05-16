import pandas as pd
import plotly.express as px

# Load the data
file_path = '/home/bigboiubu/repos/CS617-Visualizing-Boston/final_proj/attempts/data_processing/walkability/just_massachusetts/filtered_only_mass.csv'
df = pd.read_csv(file_path)

# Rename columns
column_rename_map = {
    'CBSA_Name': 'Area',
    'CBSA_POP': 'Population',
    'CBSA_EMP': 'Total Employment',
    'CBSA_WRK': 'Workers in the area',
    'Ac_Total': 'Total area (acres)',
    'Pct_AO0': 'No car owners',
    'Pct_AO1': 'One car owner',
    'Pct_AO2p': '2 or more cars',
    'TotEmp': 'Total people employed',
    'D2R_JOBPOP': 'Job to population ratio',
    'Shape_Length': 'Length of the geographic shape',
    'Shape_Area': 'Area of the geographic shape',
    'R_LowWageWk': 'Low wage workers',
    'R_MedWageWk': 'Medium wage workers',
    'R_HiWageWk': 'High wage workers',
    'D2A_EPHHM': 'Employment per household metric',
    'NatWalkInd': 'National Walkability Index'
}
df.rename(columns=column_rename_map, inplace=True)

# Create output directory path
output_directory = '/home/bigboiubu/repos/CS617-Visualizing-Boston/final_proj/attempts/data_processing/walkability/plots/mass'

# Heatmap: Correlation Matrix
# Exclude non-numeric columns
numeric_df = df.select_dtypes(include='number')
correlation_matrix = numeric_df.corr()

# Create the heatmap with a diverging color scale
heatmap = px.imshow(
    correlation_matrix,
    text_auto=True,
    title='Correlation Matrix',
    color_continuous_scale='RdBu',  # Use a diverging color scale
    labels={'color': 'Correlation Coefficient'}
)

# Update layout for better visualization
heatmap.update_layout(
    title={
        'text': 'Correlation Matrix',
        'y': 0.95,  # Position title above the heatmap
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    xaxis_title='Variables',
    yaxis_title='Variables',
    font=dict(size=12),
    margin=dict(l=50, r=50, b=50, t=100)  # Adjust top margin to make space for the title
)

# Save the heatmap to an HTML file
heatmap_html_path = f'{output_directory}/correlation_matrix.html'
heatmap.write_html(heatmap_html_path)
print(f'Heatmap (Correlation Matrix) saved to: {heatmap_html_path}')