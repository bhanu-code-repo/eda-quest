
# Import the necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt


def bar_plots(
    dataframe, 
    categorical_columns=None, 
    hue=None, 
    subplot_height=3, 
    subplot_width=4, 
    plots_per_row=2
) -> None:
    """
    Generates bar charts for categorical columns in a DataFrame.

    Parameters:
        dataframe (pandas.DataFrame): The DataFrame containing the data.
        categorical_columns (list, optional): List of categorical columns to plot. If None, all categorical columns will be plotted. Defaults to None.
        hue (str, optional): The column in the DataFrame to use for color encoding. Defaults to None.
        subplot_height (int, optional): The height of each subplot in inches. Defaults to 3.
        subplot_width (int, optional): The width of each subplot in inches. Defaults to 4.
        plots_per_row (int, optional): The number of subplots to display in each row. Defaults to 2.

    Returns:
        None
    """
    # If categorical_columns is None, get categorical columns from the DataFrame
    if categorical_columns is None:
        categorical_columns = dataframe.select_dtypes(include=['object']).columns.tolist()

    # Calculate the number of rows needed for the subplots
    num_rows = len(categorical_columns) // plots_per_row + (len(categorical_columns) % plots_per_row > 0)

    # Calculate the total figure height based on the number of rows and subplot height
    fig_height = num_rows * subplot_height

    # Create subplots with the specified height and width
    fig, axes = plt.subplots(nrows=num_rows, ncols=plots_per_row, 
                             figsize=(subplot_width * plots_per_row, fig_height), squeeze=False)

    # Loop through each categorical column and create a bar chart
    for i, col in enumerate(categorical_columns):
        row = i // plots_per_row  # Calculate the row index
        col_num = i % plots_per_row  # Calculate the column index

        # Plot bar chart
        if hue:
            sns.countplot(data=dataframe, x=col, hue=hue, ax=axes[row, col_num])
        else:
            sns.countplot(data=dataframe, x=col, ax=axes[row, col_num])
        axes[row, col_num].set_title(f'Bar Chart: {col}')
        axes[row, col_num].set_xlabel(col)
        axes[row, col_num].set_ylabel('Count')

    # Remove empty subplots if the number of plots is odd
    if len(categorical_columns) % plots_per_row != 0:
        for j in range(len(categorical_columns) % plots_per_row, plots_per_row):
            fig.delaxes(axes[num_rows - 1, j])

    plt.tight_layout()
    plt.legend(loc='best')
    plt.show()
    

def histogram_plots(
    dataframe, 
    numeric_columns=None, 
    kde=False, 
    subplot_height=2, 
    subplot_width=4, 
    plots_per_row=2
) -> None:
    """
    Generate histogram plots for numeric columns in a given DataFrame.

    Parameters:
        dataframe (pandas.DataFrame): The DataFrame containing the data.
        numeric_columns (list, optional): The list of numeric columns to create histograms for. If None, all numeric columns in the DataFrame will be used. Defaults to None.
        kde (bool, optional): Whether to include a kernel density estimate in the histogram. Defaults to False.
        subplot_height (int, optional): The height of each subplot in inches. Defaults to 2.
        subplot_width (int, optional): The width of each subplot in inches. Defaults to 4.
        plots_per_row (int, optional): The number of plots to display per row. Defaults to 2.

    Returns:
        None
    """
    # If numeric_columns is None, get the numeric columns in the DataFrame
    if numeric_columns is None:
        numeric_columns = dataframe.select_dtypes(include=[np.number]).columns

    # Calculate summary statistics for numeric columns
    summary_stats = dataframe[numeric_columns].describe()

    # Calculate the number of rows needed for the subplots
    num_rows = len(numeric_columns) // plots_per_row + (len(numeric_columns) % plots_per_row > 0)

    # Calculate the total figure height based on the number of rows and subplot height
    fig_height = num_rows * (subplot_height + 2)  # Add extra height for summary statistics

    # Create subplots with the specified height and width
    fig, axes = plt.subplots(nrows=num_rows, ncols=plots_per_row, figsize=(subplot_width * plots_per_row, fig_height), squeeze=False)

    # Loop through each numeric column and create a histogram with or without KDE
    for i, col in enumerate(numeric_columns):
        row = i // plots_per_row  # Calculate the row index
        col_num = i % plots_per_row  # Calculate the column index
        
        # Plot histogram with optional KDE
        sns.histplot(data=dataframe, x=col, kde=kde, ax=axes[row, col_num])
        axes[row, col_num].set_title(f'Histogram: {col}')
        axes[row, col_num].set_xlabel(col)
        if kde:
            axes[row, col_num].set_ylabel('Density')
        else:
            axes[row, col_num].set_ylabel('Count')
        
        # Display summary statistics as text
        summary_text = summary_stats[col].to_string(index=False)
        axes[row, col_num].annotate(summary_text, xy=(0.7, 0.85), xycoords='axes fraction')

    # Remove empty subplots if the number of plots is odd
    if len(numeric_columns) % plots_per_row != 0:
        for j in range(len(numeric_columns) % plots_per_row, plots_per_row):
            fig.delaxes(axes[num_rows - 1, j])

    plt.tight_layout()
    plt.show()
    
    
def count_plots(
    dataframe, 
    categorical_columns=None, 
    subplot_height=3, 
    subplot_width=4, 
    plots_per_row=2
) -> None:
    """
    Generate a count plot for each categorical column in the given DataFrame.
    
    Parameters:
        dataframe (pandas.DataFrame): The DataFrame containing the data.
        categorical_columns (List[str], optional): The list of categorical columns to plot. 
                                                   If None, all categorical columns in the DataFrame 
                                                   will be used. Defaults to None.
        subplot_height (int, optional): The height of each subplot. Defaults to 3.
        subplot_width (int, optional): The width of each subplot. Defaults to 4.
        plots_per_row (int, optional): The number of plots per row. Defaults to 2.
    
    Returns:
        None
    """
    # If categorical_columns is None, get the categorical columns in the DataFrame
    if categorical_columns is None:
        categorical_columns = dataframe.select_dtypes(include=['object']).columns.tolist()

    # Calculate the number of rows needed for the subplots
    num_rows = len(categorical_columns) // plots_per_row + (len(categorical_columns) % plots_per_row > 0)

    # Calculate the total figure height based on the number of rows and subplot height
    fig_height = num_rows * subplot_height

    # Create subplots with the specified height and width
    fig, axes = plt.subplots(nrows=num_rows, ncols=plots_per_row, figsize=(subplot_width * plots_per_row, fig_height), squeeze=False)

    # Loop through each categorical column and create a count plot
    for i, col in enumerate(categorical_columns):
        row = i // plots_per_row  # Calculate the row index
        col_num = i % plots_per_row  # Calculate the column index

        # Plot count plot
        sns.countplot(data=dataframe, x=col, ax=axes[row, col_num])
        axes[row, col_num].set_title(f'Count Plot: {col}')
        axes[row, col_num].set_xlabel(col)
        axes[row, col_num].set_ylabel('Count')

    # Remove empty subplots if the number of plots is odd
    if len(categorical_columns) % plots_per_row != 0:
        for j in range(len(categorical_columns) % plots_per_row, plots_per_row):
            fig.delaxes(axes[num_rows - 1, j])

    plt.tight_layout()
    plt.show()
    
def scatter_plots(
    dataframe, 
    target_column,
    numeric_columns=None,
    hue=None, 
    subplot_height=3, 
    subplot_width=6, 
    plots_per_row=2
) -> None:
    """
    Create scatter plots for numeric columns in a dataframe against a target column.
    
    Args:
        dataframe (pd.DataFrame): The dataframe containing the data.
        target_column (str): The name of the target column.
        numeric_columns (List[str]): Optional. The list of numeric columns to create scatter plots for.
                                     If None, all numeric columns excluding the target column will be used.
        hue (str): Optional. The name of the column used for color encoding.
        subplot_height (int): Optional. The height of each subplot in inches.
        subplot_width (int): Optional. The width of each subplot in inches.
        plots_per_row (int): Optional. The number of plots per row.
        
    Returns:
        None
    """
    # If numeric_columns is None, get the numeric columns in the DataFrame excluding the target column
    if numeric_columns is None:
        numeric_columns = [col for col in dataframe.columns if col != target_column 
                           and np.issubdtype(dataframe[col].dtype, np.number)]

    # Calculate the number of rows needed for the subplots
    num_rows = len(numeric_columns) // plots_per_row + (len(numeric_columns) % plots_per_row > 0)

    # Calculate the total figure height based on the number of rows and subplot height
    fig_height = num_rows * subplot_height

    # Create subplots with the specified height and width
    fig, axes = plt.subplots(nrows=num_rows, ncols=plots_per_row, 
                             figsize=(subplot_width * plots_per_row, fig_height), squeeze=False)

    # Loop through each numeric column and create a scatter plot with the target
    for i, col in enumerate(numeric_columns):
        row = i // plots_per_row  # Calculate the row index
        col_num = i % plots_per_row  # Calculate the column index
        if hue:
            sns.scatterplot(data=dataframe, x=col, y=target_column, hue=hue, ax=axes[row, col_num])
        else:
            sns.scatterplot(data=dataframe, x=col, y=target_column, ax=axes[row, col_num])
        axes[row, col_num].set_title(f'Scatter Plot: {col} vs. {target_column}')
        axes[row, col_num].set_xlabel(col)
        axes[row, col_num].set_ylabel(target_column)

    # Remove empty subplots if the number of plots is odd
    if len(numeric_columns) % plots_per_row != 0:
        for j in range(len(numeric_columns) % plots_per_row, plots_per_row):
            fig.delaxes(axes[num_rows - 1, j])

    plt.tight_layout()
    plt.show()
    
def box_plots(
    dataframe, 
    numeric_columns=None, 
    subplot_height=3, 
    subplot_width=10, 
    plots_per_row=2
) -> None:
    """
    Generates a set of box plots for numeric columns in a given DataFrame.

    Parameters:
    - dataframe: The DataFrame containing the data for the box plots.
    - numeric_columns: A list of column names containing numeric data. If None, all numeric columns in the DataFrame will be used.
    - subplot_height: The height of each subplot in inches. Default is 3.
    - subplot_width: The width of each subplot in inches. Default is 10.
    - plots_per_row: The number of box plots to display per row. Default is 2.

    Returns:
    None
    """
    # If numeric_columns is None, get the numeric columns in the DataFrame
    if numeric_columns is None:
        numeric_columns = dataframe.select_dtypes(include=[np.number]).columns

    # Calculate the number of rows needed for the subplots
    num_rows = len(numeric_columns) // plots_per_row + (len(numeric_columns) % plots_per_row)

    # Calculate the total figure height based on the number of rows and subplot height
    fig_height = num_rows * subplot_height

    # Calculate the number of columns based on the specified plots_per_row
    num_cols = min(plots_per_row, len(numeric_columns))

    # Create subplots with the specified height and width
    fig, axes = plt.subplots(nrows=num_rows, ncols=num_cols, figsize=(subplot_width * num_cols, fig_height))

    # Loop through each numeric column and create a box plot
    for i, col in enumerate(numeric_columns):
        row = i // num_cols  # Calculate the row index
        col_num = i % num_cols  # Calculate the column index
        sns.boxplot(data=dataframe, x=col, ax=axes[row, col_num])
        axes[row, col_num].set_title(f'Box Plot of {col}')
        axes[row, col_num].set_xlabel(col)

    # Remove empty subplots if the number of plots is odd
    if len(numeric_columns) % num_cols != 0:
        for j in range(len(numeric_columns) % num_cols, num_cols):
            fig.delaxes(axes[num_rows - 1, j])

    plt.tight_layout()
    plt.show()