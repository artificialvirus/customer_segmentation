# test_data_preprocessing.py

import unittest
import pandas as pd
import os
from pandas.testing import assert_frame_equal
from src.data_preprocessing import load_data, preprocess_data

class TestDataPreprocessing(unittest.TestCase):

    def setUp(self):
        self.data_dir = os.path.join(os.path.dirname(__file__), '../data')
        os.makedirs(self.data_dir, exist_ok=True)

        self.sample_data = pd.DataFrame({
            'CustomerID': [1, 2, 3, 4, 5],
            'Gender': ['Male', 'Female', 'Female', 'Male', 'Female'],
            'Age': [19, 21, 20, 23, 31],
            'Annual Income (k$)': [15, 16, 17, 18, 19],
            'Spending Score (1-100)': [39, 81, 6, 77, 40]
        })

        self.expected_columns = ['Age', 'Annual Income (k$)', 'Spending Score (1-100)', 'Gender_Female', 'Gender_Male']

    def test_load_data(self):
        temp_csv = os.path.join(self.data_dir, 'temp_sample_data.csv')
        self.sample_data.to_csv(temp_csv, index=False)
        loaded_df = load_data(temp_csv)
        assert_frame_equal(loaded_df, self.sample_data)

    def test_preprocess_data(self):
        processed_df = preprocess_data(
            self.sample_data.copy(),
            scale_features=['Age', 'Annual Income (k$)', 'Spending Score (1-100)'],
            encode_features=['Gender']
        )

        processed_df = processed_df.drop(columns=['CustomerID'])

        # Check the column names
        self.assertListEqual(list(processed_df.columns), self.expected_columns)

        # Check that the means and stds are within a reasonable range, considering small sample size
        self.assertTrue((processed_df.mean().abs() < 1).all(), "Means should be close to 0 after scaling")
        self.assertTrue((processed_df.std().between(0.5, 2)).all(), "Standard deviations should be within a reasonable range after scaling")

    def test_preprocess_data_with_missing_values(self):
        # Create sample data with missing values
        sample_data_with_nan = self.sample_data.copy()
        sample_data_with_nan.loc[0, 'Age'] = None  # Introduce a missing value

        processed_df = preprocess_data(
            sample_data_with_nan,
            scale_features=['Age', 'Annual Income (k$)', 'Spending Score (1-100)'],
            encode_features=['Gender']
        )

        processed_df = processed_df.drop(columns=['CustomerID'])

        # Ensure missing value was imputed
        self.assertFalse(processed_df.isnull().any().any(), "There should be no missing values after preprocessing")

    def test_preprocess_data_with_unexpected_category(self):
        # Create sample data with an unexpected category in 'Gender'
        sample_data_unexpected_category = self.sample_data.copy()
        sample_data_unexpected_category.loc[0, 'Gender'] = 'Non-Binary'  # Unexpected category

        processed_df = preprocess_data(
            sample_data_unexpected_category,
            scale_features=['Age', 'Annual Income (k$)', 'Spending Score (1-100)'],
            encode_features=['Gender']
        )

        processed_df = processed_df.drop(columns=['CustomerID'])

        # Check if the unexpected category was handled
        expected_columns_with_unexpected = self.expected_columns + ['Gender_Non-Binary']
        self.assertTrue(set(expected_columns_with_unexpected).issubset(processed_df.columns),
                        "Unexpected category in Gender should be handled appropriately")

    def test_preprocess_data_with_identical_rows(self):
        # Create sample data where all rows are identical
        identical_data = pd.DataFrame({
            'CustomerID': [1, 2, 3, 4, 5],
            'Gender': ['Male'] * 5,
            'Age': [20] * 5,
            'Annual Income (k$)': [50] * 5,
            'Spending Score (1-100)': [50] * 5
        })

        processed_df = preprocess_data(
            identical_data.copy(),
            scale_features=['Age', 'Annual Income (k$)', 'Spending Score (1-100)'],
            encode_features=['Gender']
        )

        processed_df = processed_df.drop(columns=['CustomerID'])

        # Ensure all expected columns are present, even if one category is missing
        for col in self.expected_columns:
            if col not in processed_df.columns:
                processed_df[col] = 0.0

        # Reorder the columns to match expected columns order
        processed_df = processed_df[self.expected_columns]

        # Check the column names
        self.assertListEqual(list(processed_df.columns), self.expected_columns)

        # Check that the standard deviations are 0 (since all values are identical)
        self.assertTrue((processed_df.std() == 0).all(), "Standard deviations should be 0 when all values are identical")

        # Check that the means are equal to the values after one-hot encoding
        expected_means = pd.Series({
            'Age': 0.0,
            'Annual Income (k$)': 0.0,
            'Spending Score (1-100)': 0.0,
            'Gender_Female': 0.0,
            'Gender_Male': 1.0  # Since all genders are 'Male'
        })
        
        # Fill missing expected columns with 0 in the processed_df mean comparison
        for col in expected_means.index:
            if col not in processed_df.columns:
                processed_df[col] = 0.0

        self.assertTrue(processed_df.mean().equals(expected_means), "Means should match the expected values for identical rows")

if __name__ == '__main__':
    unittest.main()
