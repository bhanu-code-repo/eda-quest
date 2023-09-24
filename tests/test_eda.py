
import unittest
import pandas as pd
import matplotlib.pyplot as plt

from eda_quest.eda import dataframe_summary

class TestDataframeSummary(unittest.TestCase):
    
    def test_empty_dataframe(self):
        """
        Test an empty DataFrame by calling the `dataframe_summary` function and asserting various 
        properties of the resulting summary.

        :param self: The instance of the test class.
        """
        # Test an empty DataFrame
        df = pd.DataFrame({'A': [], 'B': [], 'C': []})
        result = dataframe_summary(df)
        self.assertEqual(result['Summary Statistics'].shape, (0, 0))  # Empty DataFrame
        self.assertIsNone(result['Data Types and Missing Values'])
        self.assertEqual(result['Number of Unique Values'].size, 0)  # No columns
        self.assertEqual(result['Missing Values'].size, 0)  # No columns
        self.assertEqual(result['Number of Duplicates'], 0)
        self.assertEqual(result['Histograms'], {})  # No numeric columns

    def test_numeric_and_non_numeric_columns(self):
        # Test a DataFrame with both numeric and non-numeric columns
        df = pd.DataFrame({
            'A': [1, 2, 3],
            'B': ['a', 'b', 'c'],
            'C': [4.5, 6.7, 8.9]
        })
        result = dataframe_summary(df)
        self.assertTrue(result['Summary Statistics'].equals(df.describe()))
        self.assertIsNone(result['Data Types and Missing Values'])
        self.assertTrue(result['Number of Unique Values'].equals(pd.Series([3, 3, 3], index=df.columns)))
        self.assertTrue(result['Missing Values'].equals(pd.Series([0, 0, 0], index=df.columns)))
        self.assertEqual(result['Number of Duplicates'], 0)
        self.assertEqual(result['Histograms'], {})  # No numeric columns

    def test_dataframe_with_missing_values(self):
        # Test a DataFrame with missing values
        df = pd.DataFrame({
            'A': [1, 2, None],
            'B': ['a', None, 'c'],
            'C': [4.5, 6.7, None]
        })
        result = dataframe_summary(df)
        self.assertTrue(result['Summary Statistics'].equals(df.describe()))
        self.assertIsNone(result['Data Types and Missing Values'])
        self.assertTrue(result['Number of Unique Values'].equals(pd.Series([2, 2, 2], index=df.columns)))
        self.assertTrue(result['Missing Values'].equals(pd.Series([1, 1, 1], index=df.columns)))
        self.assertEqual(result['Number of Duplicates'], 0)
        self.assertEqual(result['Histograms'], {})  # No numeric columns

    def test_dataframe_with_duplicates(self):
        # Test a DataFrame with duplicated rows
        df = pd.DataFrame({
            'A': [1, 2, 3, 3],
            'B': ['a', 'b', 'c', 'c'],
            'C': [4.5, 6.7, 8.9, 8.9]
        })
        result = dataframe_summary(df)
        self.assertTrue(result['Summary Statistics'].equals(df.describe()))
        self.assertIsNone(result['Data Types and Missing Values'])
        self.assertTrue(result['Number of Unique Values'].equals(pd.Series([3, 3, 3], index=df.columns)))
        self.assertTrue(result['Missing Values'].equals(pd.Series([0, 0, 0], index=df.columns)))
        self.assertEqual(result['Number of Duplicates'], 1)
        self.assertEqual(result['Histograms'], {})  # No numeric columns

    def test_dataframe_with_numeric_columns(self):
        # Test a DataFrame with numeric columns
        df = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6],
            'C': [7, 8, 9]
        })
        result = dataframe_summary(df)
        self.assertTrue(result['Summary Statistics'].equals(df.describe()))
        self.assertIsNone(result['Data Types and Missing Values'])
        self.assertTrue(result['Number of Unique Values'].equals(pd.Series([3, 3, 3], index=df.columns)))
        self.assertTrue(result['Missing Values'].equals(pd.Series([0, 0, 0], index=df.columns)))
        self.assertEqual(result['Number of Duplicates'], 0)
        self.assertIsInstance(result['Histograms']['A'], plt.Axes)
        self.assertIsInstance(result['Histograms']['B'], plt.Axes)
        self.assertIsInstance(result['Histograms']['C'], plt.Axes)

    def test_dataframe_with_non_numeric_columns(self):
        # Test a DataFrame with non-numeric columns
        df = pd.DataFrame({
            'A': ['a', 'b', 'c'],
            'B': ['x', 'y', 'z']
        })
        result = dataframe_summary(df)
        self.assertTrue(result['Summary Statistics'].equals(df.describe()))
        self.assertIsNone(result['Data Types and Missing Values'])
        self.assertTrue(result['Number of Unique Values'].equals(pd.Series([3, 3], index=df.columns)))
        self.assertTrue(result['Missing Values'].equals(pd.Series([0, 0], index=df.columns)))
        self.assertEqual(result['Number of Duplicates'], 0)
        self.assertEqual(result['Histograms'], {})  # No numeric columns

    def test_dataframe_with_mixed_data_types(self):
        # Test a DataFrame with mixed data types
        df = pd.DataFrame({
            'A': [1, 2, 3],
            'B': ['a', 'b', 'c'],
            'C': [4.5, 6.7, None]
        })
        result = dataframe_summary(df)
        self.assertTrue(result['Summary Statistics'].equals(df.describe()))
        self.assertIsNone(result['Data Types and Missing Values'])
        self.assertTrue(result['Number of Unique Values'].equals(pd.Series([3, 3, 2], index=df.columns)))
        self.assertTrue(result['Missing Values'].equals(pd.Series([0, 0, 1], index=df.columns)))
        self.assertEqual(result['Number of Duplicates'], 0)
        self.assertEqual(result['Histograms'], {})  # No numeric columns

    def test_dataframe_with_all_missing_values(self):
        # Test a DataFrame with all missing values
        df = pd.DataFrame({
            'A': [None, None, None],
            'B': [None, None, None],
            'C': [None, None, None]
        })
        result = dataframe_summary(df)
        self.assertTrue(result['Summary Statistics'].equals(df.describe()))
        self.assertIsNone(result['Data Types and Missing Values'])
        self.assertTrue(result['Number of Unique Values'].equals(pd.Series([0, 0, 0], index=df.columns)))
        self.assertTrue(result['Missing Values'].equals(pd.Series([3, 3, 3], index=df.columns)))
        self.assertEqual(result['Number of Duplicates'], 0)
        self.assertEqual(result['Histograms'], {})  # No numeric columns

    def test_dataframe_with_one_row(self):
        # Test a DataFrame with one row
        df = pd.DataFrame({
            'A': [1],
            'B': ['a'],
            'C': [4.5]
        })
        result = dataframe_summary(df)
        self.assertTrue(result['Summary Statistics'].equals(df.describe()))
        self.assertIsNone(result['Data Types and Missing Values'])
        self.assertTrue(result['Number of Unique Values'].equals(pd.Series([1, 1, 1], index=df.columns)))
        self.assertTrue(result['Missing Values'].equals(pd.Series([0, 0, 0], index=df.columns)))
        self.assertEqual(result['Number of Duplicates'], 0)
        self.assertEqual(result['Histograms'], {})  # No numeric columns

    def test_dataframe_with_multiple_numeric_columns(self):
        # Test a DataFrame with multiple numeric columns
        df = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6],
            'C': [7, 8, 9],
            'D': [10, 11, 12]
        })
        result = dataframe_summary(df)
        self.assertTrue(result['Summary Statistics'].equals(df.describe()))
        self.assertIsNone(result['Data Types and Missing Values'])
        self.assertTrue(result['Number of Unique Values'].equals(pd.Series([3, 3, 3, 3], index=df.columns)))
        self.assertTrue(result['Missing Values'].equals(pd.Series([0, 0, 0, 0], index=df.columns)))
        self.assertEqual(result['Number of Duplicates'], 0)
        self.assertIsInstance(result['Histograms']['A'], plt.Axes)
        self.assertIsInstance(result['Histograms']['B'], plt.Axes)
        self.assertIsInstance(result['Histograms']['C'], plt.Axes)
        self.assertIsInstance(result['Histograms']['D'], plt.Axes)

# def test_dataframe_summary():
#     """
#     Test the function dataframe_summary().

#     This function tests the functionality of the dataframe_summary() function
#     by using various test cases. It checks the output of the function against
#     the expected results for different scenarios.

#     Parameters:
#     - None

#     Returns:
#     - None
#     """
#     # Test case 1: Empty DataFrame
#     df = pd.DataFrame()
#     result = dataframe_summary(df)
#     assert result == {
#         'Summary Statistics': pd.DataFrame(),
#         'Data Types and Missing Values': None,
#         'Number of Unique Values': pd.Series(),
#         'Missing Values': pd.Series(),
#         'Number of Duplicates': 0,
#         'Histograms': {},
#     }

#     # Test case 2: DataFrame with numeric and non-numeric columns
#     df = pd.DataFrame({
#         'A': [1, 2, 3],
#         'B': ['a', 'b', 'c'],
#         'C': [4.5, 6.7, 8.9]
#     })
#     result = dataframe_summary(df)
#     assert result['Summary Statistics'].equals(df.describe())
#     assert result['Data Types and Missing Values'] is None
#     assert result['Number of Unique Values'].equals(pd.Series([3, 3, 3], index=df.columns))
#     assert result['Missing Values'].equals(pd.Series([0, 0, 0], index=df.columns))
#     assert result['Number of Duplicates'] == 0
#     assert result['Histograms'] == {}

#     # Test case 3: DataFrame with missing values
#     df = pd.DataFrame({
#         'A': [1, 2, None],
#         'B': ['a', None, 'c'],
#         'C': [4.5, 6.7, None]
#     })
#     result = dataframe_summary(df)
#     assert result['Summary Statistics'].equals(df.describe())
#     assert result['Data Types and Missing Values'] is None
#     assert result['Number of Unique Values'].equals(pd.Series([2, 2, 2], index=df.columns))
#     assert result['Missing Values'].equals(pd.Series([1, 1, 1], index=df.columns))
#     assert result['Number of Duplicates'] == 0
#     assert result['Histograms'] == {}

#     # Test case 4: DataFrame with duplicated rows
#     df = pd.DataFrame({
#         'A': [1, 2, 3, 3],
#         'B': ['a', 'b', 'c', 'c'],
#         'C': [4.5, 6.7, 8.9, 8.9]
#     })
#     result = dataframe_summary(df)
#     assert result['Summary Statistics'].equals(df.describe())
#     assert result['Data Types and Missing Values'] is None
#     assert result['Number of Unique Values'].equals(pd.Series([3, 3, 3], index=df.columns))
#     assert result['Missing Values'].equals(pd.Series([0, 0, 0], index=df.columns))
#     assert result['Number of Duplicates'] == 1
#     assert result['Histograms'] == {}

#     # Test case 5: DataFrame with numeric columns
#     df = pd.DataFrame({
#         'A': [1, 2, 3],
#         'B': [4, 5, 6],
#         'C': [7, 8, 9]
#     })
#     result = dataframe_summary(df)
#     assert result['Summary Statistics'].equals(df.describe())
#     assert result['Data Types and Missing Values'] is None
#     assert result['Number of Unique Values'].equals(pd.Series([3, 3, 3], index=df.columns))
#     assert result['Missing Values'].equals(pd.Series([0, 0, 0], index=df.columns))
#     assert result['Number of Duplicates'] == 0
#     assert isinstance(result['Histograms']['A'], plt.Axes)
#     assert isinstance(result['Histograms']['B'], plt.Axes)
#     assert isinstance(result['Histograms']['C'], plt.Axes)

#     # Test case 6: DataFrame with non-numeric columns
#     df = pd.DataFrame({
#         'A': ['a', 'b', 'c'],
#         'B': ['x', 'y', 'z']
#     })
#     result = dataframe_summary(df)
#     assert result['Summary Statistics'].equals(df.describe())
#     assert result['Data Types and Missing Values'] is None
#     assert result['Number of Unique Values'].equals(pd.Series([3, 3], index=df.columns))
#     assert result['Missing Values'].equals(pd.Series([0, 0], index=df.columns))
#     assert result['Number of Duplicates'] == 0
#     assert result['Histograms'] == {}

#     # Test case 7: DataFrame with mixed data types
#     df = pd.DataFrame({
#         'A': [1, 2, 3],
#         'B': ['a', 'b', 'c'],
#         'C': [4.5, 6.7, None]
#     })
#     result = dataframe_summary(df)
#     assert result['Summary Statistics'].equals(df.describe())
#     assert result['Data Types and Missing Values'] is None
#     assert result['Number of Unique Values'].equals(pd.Series([3, 3, 2], index=df.columns))
#     assert result['Missing Values'].equals(pd.Series([0, 0, 1], index=df.columns))
#     assert result['Number of Duplicates'] == 0
#     assert result['Histograms'] == {}

#     # Test case 8: DataFrame with all missing values
#     df = pd.DataFrame({
#         'A': [None, None, None],
#         'B': [None, None, None],
#         'C': [None, None, None]
#     })
#     result = dataframe_summary(df)
#     assert result['Summary Statistics'].equals(df.describe())
#     assert result['Data Types and Missing Values'] is None
#     assert result['Number of Unique Values'].equals(pd.Series([0, 0, 0], index=df.columns))
#     assert result['Missing Values'].equals(pd.Series([3, 3, 3], index=df.columns))
#     assert result['Number of Duplicates'] == 0
#     assert result['Histograms'] == {}

#     # Test case 9: DataFrame with one row
#     df = pd.DataFrame({
#         'A': [1],
#         'B': ['a'],
#         'C': [4.5]
#     })
#     result = dataframe_summary(df)
#     assert result['Summary Statistics'].equals(df.describe())
#     assert result['Data Types and Missing Values'] is None
#     assert result['Number of Unique Values'].equals(pd.Series([1, 1, 1], index=df.columns))
#     assert result['Missing Values'].equals(pd.Series([0, 0, 0], index=df.columns))
#     assert result['Number of Duplicates'] == 0
#     assert result['Histograms'] == {}

#     # Test case 10: DataFrame with multiple numeric columns
#     df = pd.DataFrame({
#         'A': [1, 2, 3],
#         'B': [4, 5, 6],
#         'C': [7, 8, 9],
#         'D': [10, 11, 12]
#     })
#     result = dataframe_summary(df)
#     assert result['Summary Statistics'].equals(df.describe())
#     assert result['Data Types and Missing Values'] is None
#     assert result['Number of Unique Values'].equals(pd.Series([3, 3, 3, 3], index=df.columns))
       
       
if __name__ == '__main__':
    unittest.main()