# -*- coding: utf-8 -*-

# Import the necessary libraries
import re
from IPython.display import display
from eda_quest.utils import styled_dataframe

def display_dataframe(df, title="DataFrame Preview", head_rows=5, sample_rows=5, tail_rows=5):
    """
    Display the head, sample, and tail of a DataFrame with good visual aesthetics.

    Parameters:
    - df: pd.DataFrame
        The DataFrame to display.
    - title: str, optional
        Title to display above the DataFrame. Default is "DataFrame Preview".
    - head_rows: int, optional
        Number of rows to display from the head of the DataFrame. Default is 5.
    - sample_rows: int, optional
        Number of random rows to display as a sample from the DataFrame. Default is 5.
    - tail_rows: int, optional
        Number of rows to display from the tail of the DataFrame. Default is 5.

    Returns:
    - None
    """
    print(f"\033[1m{title}\033[0m")
    
    # Display the head of the DataFrame
    styled_dataframe(df.head(head_rows))
    
    # Display a random sample from the DataFrame
    if sample_rows > 0:
        sample_df = df.sample(min(sample_rows, len(df)))
        print("\n\033[1mSample Data\033[0m")
        styled_dataframe(sample_df)
    
    # Display the tail of the DataFrame
    styled_dataframe(df.tail(tail_rows))

def dataframe_summary(df):
    """
    Perform basic exploratory data analysis (EDA) on a Pandas DataFrame.

    Parameters:
    df (DataFrame): The DataFrame to analyze.

    Returns:
    dict: A dictionary containing various EDA statistics and information.
    """
    # Summary statistics
    summary_stats = df.describe()

    # Data types and missing values
    data_info = df.info()

    # Number of unique values in each column
    num_unique = df.nunique()

    # Check for missing values
    missing_values = df.isnull().sum()

    # Check for duplicated rows
    num_duplicates = df.duplicated().sum()

    # Basic histogram for numeric columns
    numeric_columns = df.select_dtypes(include=['number'])
    histograms = {}
    for column in numeric_columns.columns:
        histograms[column] = df[column].plot(kind='hist', title=column)
    
    # Create a dictionary to store the EDA results
    eda_results = {
        'Summary Statistics': summary_stats,
        'Data Types and Missing Values': data_info,
        'Number of Unique Values': num_unique,
        'Missing Values': missing_values,
        'Number of Duplicates': num_duplicates,
        'Histograms': histograms,
    }

    return eda_results


def visualize_missing_data(df, height=None, width=None, heatmap=True, cmap='YlGnBu'):
    """
    Visualize missing data in a DataFrame, inspect categorical features, and provide insights.

    Parameters:
    - df: pd.DataFrame
        The DataFrame to analyze.
    - height: int, optional
        The height of the figure for the heatmap. Default is None.
    - width: int, optional
        The width of the figure for the heatmap. Default is None.
    - heatmap: bool, optional
        Whether to display a heatmap of missing data. Default is True.

    Returns:
    - None
    """
    # Check for missing values
    missing_data = df.isnull()
    total_missing = missing_data.sum()
    percent_missing = (missing_data.sum() / len(df)) * 100

    # Create a summary DataFrame
    missing_info = pd.DataFrame({'Total Missing': total_missing, 'Percent Missing': percent_missing})
    missing_info = missing_info[missing_info['Total Missing'] > 0].sort_values(by='Percent Missing', ascending=False)

    # Display missing data info
    print("\033[1mMissing Data Information\033[0m")
    display(missing_info)

    # Analyze categorical features
    categorical_features = df.select_dtypes(include=['object']).columns.tolist()
    if categorical_features:
        print("\n\033[1mCategorical Feature Analysis\033[0m")
        for feature in categorical_features:
            unique_values = df[feature].unique()
            print(f"\n\033[1mFeature: {feature}\033[0m")
            print(f"Number of Unique Values: {len(unique_values)}")
            print("Unique Values:", unique_values)
            
            # Check for special characters in categorical data
            special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', ';', ':', "'", '"', '<', '>', ',', '.', '?', '/', '~', '`']
            has_special_characters = any(df[feature].str.contains('|'.join(map(re.escape, special_characters)), na=False))
            if has_special_characters:
                print("\n\033[1mSpecial Characters Detected!\033[0m")
                print("Recommendation: Consider removing or replacing special characters.")
            else:
                print("\n\033[1mNo Special Characters Detected\033[0m")
                
            # Check for consistent binary values
            if len(unique_values) == 2:
                print("\n\033[1mBinary feature detected\033[0m.")
                print("Recommendation: Check if binary values are consistent (e.g., 'Yes'/'No', 'True'/'False').")
            else:
                print("\n\033[1mNo binary feature detected\033[0m.")
                
            # Check cardinality and provide recommendations
            if len(unique_values) < 10:
                print("\n\033[1mLow cardinality feature detected\033[0m.")
                print("Recommendation: Check for consistency and consider one-hot encoding.")
            else:
                print("\n\033[1mHigh cardinality feature detected\033[0m.")
                print("Recommendation: Review and possibly reduce cardinality through grouping or feature engineering.")
            
            # Check for inconsistent capitalization
            unique_values_lower = [value.lower() for value in unique_values if isinstance(value, str)]
            unique_values_lower_set = set(unique_values_lower)
            if len(unique_values_lower_set) != len(unique_values):
                print("Inconsistent Capitalization Detected!")
                print("Recommendation: Standardize capitalization (e.g., convert all values to lowercase).")

            # Check for redundant or similar categories
            def is_similar(value1, value2):
                return value1.lower().replace(" ", "") == value2.lower().replace(" ", "")

            similar_categories = []
            for i, value1 in enumerate(unique_values):
                for j, value2 in enumerate(unique_values):
                    if i != j and is_similar(str(value1), str(value2)):
                        similar_categories.append((value1, value2))
            if similar_categories:
                print("Redundant or Similar Categories Detected!")
                print("Recommendation: Consolidate similar categories into a single category.")
                print("Similar Category Pairs:")
                for pair in similar_categories:
                    print(pair)
               
    # Check numerical features for non-numeric entries
    numerical_features = df.select_dtypes(include=['number']).columns.tolist()
    if numerical_features:
        print("\n\033[1mNumerical Feature Analysis\033[0m")
        for feature in numerical_features:
            if df[feature].apply(lambda x: isinstance(x, (int, float))).all():
                print(f"\n\033[1mFeature: {feature}\033[0m")
                print("All entries are numeric.")
            else:
                print(f"\n\033[1mFeature: {feature}\033[0m")
                print("Non-numeric entries detected.")
                print("Recommendation: Check and clean non-numeric entries if necessary.")
                
    # Create and display a heatmap
    if heatmap:
        if height and width:
            plt.figure(figsize=(width, height))
        elif height:
            plt.figure(figsize=(6, height))
        elif width:
            plt.figure(figsize=(width, 6))
        else:
            plt.figure()
        sns.heatmap(missing_data, cbar=False, cmap=cmap)
        plt.title('Missing Data Heatmap', fontsize=12)
        plt.xlabel('Columns')
        plt.ylabel('Rows')
        plt.show()


def handle_missing_values(df, strategy='auto', default_value=None, threshold=5, row_threshold=None, column_threshold=None):
    """
    Handle missing values in a DataFrame using different strategies.

    Parameters:
    - df: pd.DataFrame
        The DataFrame to perform missing value treatment on.
    - strategy: str, optional
        The missing value handling strategy. Options: 'auto', 'fill', 'impute', 'drop'.
        Default is 'auto'.
    - default_value: any, optional
        The default value to fill missing values with when strategy is 'fill'.
        Default is None.
    - threshold: int, optional
        The threshold difference between mean and median for choosing the imputation method (mean or median).
        Default is 5.
    - row_threshold: int, optional
        Maximum number of missing values allowed in a row before dropping it (for 'auto' and 'drop' strategies).
        Default is None (no row dropping).
    - column_threshold: int, optional
        Maximum number of missing values allowed in a column before dropping it (for 'auto' and 'drop' strategies).
        Default is None (no column dropping).

    Returns:
    - pd.DataFrame
        The DataFrame with missing values handled based on the specified strategy.
    """
    df_processed = df.copy()

    # Automatically identify numeric and categorical columns
    numeric_columns = df.select_dtypes(include=['number']).columns
    categorical_columns = df.select_dtypes(exclude=['number']).columns
    
    if strategy == 'auto':
        for column in numeric_columns:
            if df[column].isnull().sum() > 0:
                if abs(df[column].mean() - df[column].median()) <= threshold:
                    df_processed[column].fillna(df[column].mean(), inplace=True)
                else:
                    df_processed[column].fillna(df[column].median(), inplace=True)
        
        for column in categorical_columns:
            if df[column].isnull().sum() > 0:
                df_processed[column].fillna(df[column].mode()[0], inplace=True)  # Fill with mode for categorical columns
    
    elif strategy == 'fill' and default_value is not None:
        df_processed.fillna(default_value, inplace=True)
    
    elif strategy == 'impute':
        for column in numeric_columns:
            if df[column].isnull().sum() > 0:
                if abs(df[column].mean() - df[column].median()) <= threshold:
                    df_processed[column].fillna(df[column].mean(), inplace=True)
                else:
                    df_processed[column].fillna(df[column].median(), inplace=True)
        
        for column in categorical_columns:
            if df[column].isnull().sum() > 0:
                df_processed[column].fillna(df[column].mode()[0], inplace=True)
                
    elif strategy == 'drop':
        if row_threshold is not None and column_threshold is not None:
            # Scenario 1: Drop rows and columns based on both row_threshold and column_threshold

            # Calculate the total number of missing values in each row and column
            row_missing_counts = df_processed.isnull().sum(axis=1)
            column_missing_counts = df_processed.isnull().sum(axis=0)

            # Drop rows exceeding the row_threshold
            rows_to_drop = row_missing_counts[row_missing_counts >= row_threshold].index
            df_processed.drop(index=rows_to_drop, inplace=True)

            # Drop columns exceeding the column_threshold
            columns_to_drop = column_missing_counts[column_missing_counts >= column_threshold].index
            df_processed.drop(columns=columns_to_drop, inplace=True)

        elif row_threshold is not None:
            # Scenario 2: Drop rows based on row_threshold

            # Calculate the total number of missing values in each row
            row_missing_counts = df_processed.isnull().sum(axis=1)

            # Drop rows exceeding the row_threshold
            rows_to_drop = row_missing_counts[row_missing_counts >= row_threshold].index
            df_processed.drop(index=rows_to_drop, inplace=True)

        elif column_threshold is not None:
            # Scenario 3: Drop columns based on column_threshold

            # Calculate the total number of missing values in each column
            column_missing_counts = df_processed.isnull().sum(axis=0)

            # Drop columns exceeding the column_threshold
            columns_to_drop = column_missing_counts[column_missing_counts >= column_threshold].index
            df_processed.drop(columns=columns_to_drop, inplace=True)

        else:
            # Scenario 4: Drop all rows with any missing values (default behavior)

            df_processed.dropna(axis=0, inplace=True)

    return df_processed