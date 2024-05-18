import os
import shutil

directories_to_delete = [
    "/home/bigboiubu/repos/CS617-Visualizing-Boston/final_proj/attempts/data_processing/massbuilds/csv/boston_filtered/processed",
    "/home/bigboiubu/repos/CS617-Visualizing-Boston/final_proj/attempts/data_processing/massbuilds/csv/massachusetts/processed",
    "/home/bigboiubu/repos/CS617-Visualizing-Boston/final_proj/attempts/data_processing/population/boston/polished",
    "/home/bigboiubu/repos/CS617-Visualizing-Boston/final_proj/attempts/data_processing/population/massachusetts/polished",
    "/home/bigboiubu/repos/CS617-Visualizing-Boston/final_proj/attempts/data_processing/walkability/processed_data",
    "/home/bigboiubu/repos/CS617-Visualizing-Boston/final_proj/attempts/data_processing/walkability/plots"
]

def delete_directories(directory_list):
    for directory in directory_list:
        try:
            if os.path.exists(directory):
                shutil.rmtree(directory)
                print(f"Successfully deleted directory and its contents: {directory}")
            else:
                print(f"Directory does not exist: {directory}")
        except Exception as e:
            print(f"Error deleting directory {directory}: {e}")

delete_directories(directories_to_delete)
