import os
import pandas as pd
from os import path

"""
Original data obtained from https://catalog.data.gov/dataset/walkability-index1
US nation-wide data. Extract relevant data for a specified county from the original CSV file.
Script to obtain all data entries containing the specified FIPS code in the original CSV file.
"""

def find_file_path(file_name, search_dir='.'):
    for root, dirs, files in os.walk(search_dir):
        if file_name in files:
            return path.join(root, file_name)
    raise FileNotFoundError(f"File not found: {file_name}")

def get_county_name(fips_code):
    county_names = {
        1: "Barnstable County", 3: "Berkshire County", 5: "Bristol County", 7: "Dukes County", 
        9: "Essex County", 11: "Franklin County", 13: "Hampden County", 15: "Hampshire County", 
        17: "Middlesex County", 19: "Nantucket County", 21: "Norfolk County", 23: "Plymouth County", 
        25: "Suffolk County", 27: "Worcester County"
    }
    return county_names.get(fips_code, f"Unknown_FIPS_{fips_code}")

# Load original data file
search_directory = '.'

# Find the original data file dynamically
original_file_name = 'EPA_SmartLocationDatabase_V3_Jan_2021_Final.csv'
original_df_fp = find_file_path(original_file_name, search_directory)

try:
    original_df = pd.read_csv(original_df_fp)
except FileNotFoundError:
    print(f"File not found: {original_df_fp}")
    exit()

# Print the columns of the original dataframe (optional)
# print(f"\n {original_df.columns} \n")

# Create the directory for extracted files
extracted_dir = path.join(path.dirname(original_df_fp), 'byCounty')
os.makedirs(extracted_dir, exist_ok=True)

# Filter and shrink data file to contain only data related to the state of Massachusetts.
# Massachusetts FIPS code is 25
mass_df = original_df[original_df['STATEFP'] == 25]
mass_data_fp = path.join(extracted_dir, 'only_Mass.csv')
mass_df.to_csv(mass_data_fp, index=False)

# Print the columns of the Massachusetts dataframe (optional)
# print(f"\n {mass_df.columns} \n")

print(f'\nExtracted all data associated with Massachusetts. Stored to {mass_data_fp}')

# List of Massachusetts county FIPS codes
county_fips_codes = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27]

# Iterate over each county FIPS code and process the data
for county_fips_code in county_fips_codes:
    county_name = get_county_name(county_fips_code)
    
    # Narrow down to data related to specified county.
    county_df = mass_df[mass_df['COUNTYFP'] == county_fips_code]
    county_data_fp = path.join(extracted_dir, f'{county_name.replace(" ", "_")}_data.csv')
    county_df.to_csv(county_data_fp, index=False)
    
    # Print the columns of the county dataframe (optional)
    # print(f"\n {county_df.columns} \n")
    
    print(f'All {county_name} data can be found in {county_data_fp}')
    
    # Potentially useful columns from data:
    useful_columns = [
        'CBSA_Name', 'CBSA_POP', 'CBSA_EMP', 'CBSA_WRK', 'Ac_Total', 'Pct_AO0', 'Pct_AO1', 
        'Pct_AO2p', 'TotEmp', 'D2R_JOBPOP', 'Shape_Length', 'Shape_Area', 'Workers', 'R_LowWageWk',
        'R_MedWageWk', 'R_HiWageWk', 'D2A_EPHHM', 'NatWalkInd'
    ]
    
    # Check if all useful columns exist in the dataframe
    existing_columns = [col for col in useful_columns if col in county_df.columns]
    missing_columns = [col for col in useful_columns if col not in county_df.columns]
    
    if missing_columns:
        print(f"Warning: Missing columns in {county_name} data: {missing_columns}")
    
    # Extract useful columns and save to a new file
    filtered_columns_df = county_df[existing_columns]
    filtered_columns_fp = path.join(extracted_dir, f'filtered_{county_name.replace(" ", "_")}.csv')
    filtered_columns_df.to_csv(filtered_columns_fp, index=False)
    print(f'Filtered columns for {county_name} saved to {filtered_columns_fp}\n')
    
    print(filtered_columns_df.describe())
