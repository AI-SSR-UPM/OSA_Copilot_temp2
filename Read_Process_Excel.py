import pandas as pd

def read_excel_file(file_path):
    """
    Reads an Excel file and returns a DataFrame.

    Parameters:
    file_path (str): The path to the Excel file.

    Returns:
    pd.DataFrame: The data from the Excel file as a DataFrame.
    """
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        print(f"An error occurred: {e}")
        return None