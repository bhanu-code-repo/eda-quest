

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
