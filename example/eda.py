# -*- coding: utf-8 -*-

# Import the necessary packages
import pandas as pd
from eda_quest.eda import dataframe_summary

def demonstrate_dataframe_summary():
    """
    This function demonstrates the process of performing Exploratory Data Analysis (EDA) on a DataFrame.

    Parameters:
        None

    Returns:
        None
    """
    # Create a sample DataFrame (replace with your own data)
    data = {'A': [1, 2, 3, 4, 5],
            'B': [10.1, 20.2, 30.3, 40.4, 50.5],
            'C': ['X', 'Y', 'Z', 'X', 'Y']}
    df = pd.DataFrame(data)

    # Perform basic EDA
    eda_results = dataframe_summary(df)

    # Print the EDA results
    for key, value in eda_results.items():
        print(f"===== {key} =====")
        if isinstance(value, pd.DataFrame):
            print(value)
        elif isinstance(value, dict):
            for subkey, subvalue in value.items():
                subvalue.figure.show()
        else:
            print(value)
            

# Example usage:
if __name__ == '__main__':
    demonstrate_dataframe_summary()