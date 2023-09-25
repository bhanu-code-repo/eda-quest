
# -*- coding: utf-8 -*-

# Import packages
import pandas as pd

def styled_dataframe(df):
    """
    Apply styling to a DataFrame for better visual aesthetics.

    Parameters:
    - df: pd.DataFrame
        The DataFrame to style.

    Returns:
    - pd.DataFrame
        The styled DataFrame.
    """
    styled_df = df.style \
        .set_properties(**{'text-align': 'center'}) \
        .set_table_styles([{
            'selector': 'th',
            'props': [('font-size', '14px')]
        }, {
            'selector': 'td',
            'props': [('font-size', '12px')]
        }]) \
        .background_gradient(cmap='coolwarm', subset=df.select_dtypes('number').columns) \
        .applymap(lambda x: 'background-color: lightgray', subset=pd.IndexSlice[:, df.columns[df.isnull().any()]]) \
    
    return styled_df

def display_heading(heading):
    """
    Display a heading with a border.

    Args:
        heading (str): The heading to be displayed.

    Returns:
        None
    """
    border = '*' * 50
    space = ' ' * 14
    print(f'\n{border}')
    print(f'{space}{heading}')
    print(f'{border}\n')