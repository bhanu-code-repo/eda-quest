# -*- coding: utf-8 -*-

# Import the necessary packages
import os
import sys
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display

# Add the project root directory to the system path
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_dir)

# Import the eda_quest package
from eda_quest.utils import styled_dataframe, display_heading
from eda_quest.eda import display_dataframe, dataframe_summary, handle_missing_values

def demonstrate_display_dataframe():
    """
    Demonstrates the display_dataframe function.

    Parameters:
        None

    Returns:
        None
    """
    # Create a sample DataFrame (replace with your own data)
    data = {'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            'B': ['Apple', 'Banana', 'Cherry', 'Date', 'Fig', 'Grape', 'Honeydew', 'Kiwi', 'Lemon', 'Mango'],
            'C': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]}
    df = pd.DataFrame(data)

    # Display the DataFrame with different settings
    display_dataframe(df, title="Sample DataFrame - Default Settings")

    display_dataframe(df, title="Sample DataFrame - Custom Settings",
                      head_rows=3, sample_rows=3, tail_rows=2)

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

    # Styling for visual aesthetics
    sns.set_style("whitegrid")
    plt.rcParams["figure.figsize"] = (10, 6)

    # Print the EDA results with improved visuals
    for key, value in eda_results.items():
        print(f"\033[1m===== {key} =====\033[0m")
        if isinstance(value, pd.DataFrame):
            # Style DataFrame for better visual aesthetics
            styled_df = styled_dataframe(value)
            display(styled_df)
        elif isinstance(value, dict):
            for subkey, subvalue in value.items():
                if isinstance(subvalue, plt.Axes):
                    subvalue.set_title(subkey)  # Set titles for subplots
                    plt.show()  # Display subplots
        else:
            print(value)
            
def demonstrate_handle_missing_values():
    """
    This function demonstrates how to handle missing values in a DataFrame using different strategies.

    Parameters:
        None

    Returns:
        None
    """
    # Create a sample DataFrame (replace with your own data)
    data = {'A': [1, 2, np.nan, 4, 5],
            'B': [10.1, np.nan, 30.3, 40.4, 50.5],
            'C': ['X', 'Y', 'Z', 'X', 'Y']}
    df = pd.DataFrame(data)

    # Print the original DataFrame
    print("===== Original DataFrame =====")
    styled_df = styled_dataframe(df)
    display(styled_df)

    # Handle missing values using different strategies
    strategies = ['auto', 'fill', 'impute', 'drop']
    for strategy in strategies:
        print(f"===== Handling Missing Values - Strategy: {strategy} =====")
        if strategy != 'fill':
            df_processed = handle_missing_values(df, strategy=strategy)
        else:
            df_processed = handle_missing_values(df, strategy=strategy, default_value=0.0)
        styled_processed_df = styled_dataframe(df_processed)
        display(styled_processed_df)

# Example usage:
if __name__ == '__main__':
    display_heading("Example Usage: Display DataFrame and EDA Summary")
    demonstrate_display_dataframe()
    demonstrate_dataframe_summary()
    
    display_heading("Example Usage: Handle Missing Values")
    demonstrate_handle_missing_values()