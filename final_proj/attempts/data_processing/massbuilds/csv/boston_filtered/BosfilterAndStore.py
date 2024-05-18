import os
import pandas as pd

def load_data(file_path):
    """
    Load data from a CSV file into a pandas DataFrame.
    
    Parameters:
    file_path (str): The path to the CSV file.
    
    Returns:
    pd.DataFrame: The loaded DataFrame, or None if an error occurs.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error loading data from {file_path}: {e}")
        return None

def filter_traffic_related_projects(df):
    """
    Filter the DataFrame to include traffic-related projects and extract relevant columns.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame.
    
    Returns:
    pd.DataFrame: The filtered DataFrame, or None if an error occurs.
    """
    try:
        traffic_related_projects = df[
            (df['traffic_count_data_present'].notnull()) |
            (df['n_transit'].notnull())
        ][['year_compl', 'status', 'traffic_count_data_present', 'n_transit', 'singfamhu', 'smmultifam', 'lgmultifam', 'total_cost', 'ret_sqft', 'ofcmd_sqft', 'indmf_sqft', 'affrd_unit']]
        return traffic_related_projects
    except KeyError as e:
        print(f"Error filtering data: {e}")
        return None

def save_data(df, output_dir, output_file):
    """
    Save the filtered DataFrame to a CSV file in the specified directory.
    
    Parameters:
    df (pd.DataFrame): The DataFrame to save.
    output_dir (str): The directory where the file will be saved.
    output_file (str): The name of the output CSV file.
    """
    try:
        # Create the output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Construct the full output file path
        output_path = os.path.join(output_dir, output_file)
        
        # Save the DataFrame to the CSV file
        df.to_csv(output_path, index=False)
        print(f'Filtered data saved to {output_path}')
    except Exception as e:
        print(f"Error saving data to {output_path}: {e}")

def main():
    """
    Main function to load, filter, and save traffic-related project data.
    """
    # Define the file paths
    file_path = '/home/bigboiubu/repos/CS617-Visualizing-Boston/final_proj/attempts/data_processing/massbuilds/csv/boston_filtered/massbuilds-20240515.csv'
    output_dir = os.path.join(os.path.dirname(file_path), 'processed')
    output_file = 'boston_filtered_traffic_related_projects.csv'

    # Load the data
    df = load_data(file_path)
    
    if df is not None:
        # Filter the traffic-related projects
        traffic_related_projects = filter_traffic_related_projects(df)
        
        if traffic_related_projects is not None:
            # Save the filtered data
            save_data(traffic_related_projects, output_dir, output_file)

if __name__ == "__main__":
    main()
