import os
import pandas as pd
from os import path

"""
Original data obtained from https://catalog.data.gov/dataset/walkability-index1
US nation-wide data. Extract relevant data for a specified county from the original CSV file.
Script to obtain all data entries containing the specified FIPS code in the original CSV file.
"""

def find_file_path(file_name, search_dir='.'):
    """
    Recursively search for a file in the given directory.
    
    Parameters:
    file_name (str): The name of the file to find.
    search_dir (str): The directory to search in.
    
    Returns:
    str: The full file path if found, otherwise raises FileNotFoundError.
    """
    for root, dirs, files in os.walk(search_dir):
        if file_name in files:
            return path.join(root, file_name)
    raise FileNotFoundError(f"File not found: {file_name}")

def get_county_name(fips_code):
    """
    Get the county name corresponding to a FIPS code.
    
    Parameters:
    fips_code (int): The FIPS code of the county.
    
    Returns:
    str: The name of the county.
    """
    county_names = {
        1: "Barnstable County", 3: "Berkshire County", 5: "Bristol County", 7: "Dukes County", 
        9: "Essex County", 11: "Franklin County", 13: "Hampden County", 15: "Hampshire County", 
        17: "Middlesex County", 19: "Nantucket County", 21: "Norfolk County", 23: "Plymouth County", 
        25: "Suffolk County", 27: "Worcester County"
    }
    return county_names.get(fips_code, f"Unknown_FIPS_{fips_code}")

def create_directory(directory):
    """
    Create a directory if it does not exist.
    
    Parameters:
    directory (str): The path of the directory to create.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

def filter_and_save_mass_data(mass_data_fp, useful_columns):
    """
    Filter the Massachusetts data to include only the useful columns and save it.
    
    Parameters:
    mass_data_fp (str): The file path to the Massachusetts data.
    useful_columns (list): The list of useful columns to keep.
    
    Returns:
    str: The file path to the filtered data.
    """
    # Load the Massachusetts data
    mass_df = pd.read_csv(mass_data_fp)
    
    # Filter the data to include only the useful columns
    existing_columns = [col for col in useful_columns if col in mass_df.columns]
    missing_columns = [col for col in useful_columns if col not in mass_df.columns]
    
    if missing_columns:
        print(f"Warning: Missing columns in Massachusetts data: {missing_columns}")
    
    filtered_mass_df = mass_df[existing_columns]
    
    # Save the filtered data
    filtered_mass_data_fp = path.join(path.dirname(mass_data_fp), 'filtered_only_mass.csv')
    filtered_mass_df.to_csv(filtered_mass_data_fp, index=False)
    print(f'Filtered Massachusetts data saved to {filtered_mass_data_fp}')
    return filtered_mass_data_fp

def main():
    """
    Main function to extract and filter walkability data for Massachusetts and its counties.
    """
    # Get the directory of the current script
    script_dir = path.dirname(path.abspath(__file__))
    search_directory = path.join(script_dir, 'raw_data')

    # Find the original data file dynamically
    original_file_name = 'EPA_SmartLocationDatabase_V3_Jan_2021_Final.csv'
    try:
        original_df_fp = find_file_path(original_file_name, search_directory)
        original_df = pd.read_csv(original_df_fp)
    except FileNotFoundError as e:
        print(e)
        return

    # Create necessary directories
    base_dir = path.dirname(original_df_fp)
    just_massachusetts_dir = path.join(script_dir, 'processed_data/just_massachusetts')
    create_directory(just_massachusetts_dir)
    
    extracted_dir = path.join(script_dir, 'processed_data/byCounty')
    create_directory(extracted_dir)
    create_directory(path.join(extracted_dir, 'all_inclusive'))
    create_directory(path.join(extracted_dir, 'specificKeywords'))

    '''
    Shrink wave 1 
    Filter and shrink data file to contain only data related to the state of Massachusetts.
    Massachusetts FIPS code is 25
    '''
    mass_df = original_df[original_df['STATEFP'] == 25]
    mass_data_fp = path.join(just_massachusetts_dir, 'only_Mass.csv')
    mass_df.to_csv(mass_data_fp, index=False)
    print(f'\nExtracted all data associated with Massachusetts. Stored to {mass_data_fp}')

    # Useful columns to keep
    useful_columns = [
        'CBSA_Name', 'CBSA_POP', 'CBSA_EMP', 'CBSA_WRK', 'Ac_Total', 'Pct_AO0', 'Pct_AO1', 
        'Pct_AO2p', 'TotEmp', 'D2R_JOBPOP', 'Shape_Length', 'Shape_Area', 'Workers', 'R_LowWageWk',
        'R_MedWageWk', 'R_HiWageWk', 'D2A_EPHHM', 'NatWalkInd'
    ]

    # Filter and save the Massachusetts data using useful columns
    filter_and_save_mass_data(mass_data_fp, useful_columns)

    '''
    Shrink wave 2 
    Narrow down to data related to county.
    Boston is in Suffolk County.
    FIPS code for Suffolk County is 025. In data file, it is listed as 25
    May as well get the other counties too.
    '''
    county_fips_codes = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27]

    for county_fips_code in county_fips_codes:
        county_name = get_county_name(county_fips_code)
        county_df = mass_df[mass_df['COUNTYFP'] == county_fips_code]
        county_data_fp = path.join(extracted_dir, f'all_inclusive/{county_name.replace(" ", "_")}_data.csv')
        county_df.to_csv(county_data_fp, index=False)
        print(f'\nAll {county_name} data can be found in {county_data_fp}')
        
        existing_columns = [col for col in useful_columns if col in county_df.columns]
        missing_columns = [col for col in useful_columns if col not in county_df.columns]
        
        if missing_columns:
            print(f"Warning: Missing columns in {county_name} data: {missing_columns}")
        
        filtered_columns_df = county_df[existing_columns]
        filtered_columns_fp = path.join(extracted_dir, f'specificKeywords/filtered_{county_name.replace(" ", "_")}.csv')
        filtered_columns_df.to_csv(filtered_columns_fp, index=False)
        print(f'Filtered columns for {county_name} saved to {filtered_columns_fp}')

if __name__ == "__main__":
    main()
