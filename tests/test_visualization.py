# test_visualization.py

import unittest
import pandas as pd
from unittest.mock import patch
from src.visualization import plot_distribution, plot_correlation_matrix

class TestVisualization(unittest.TestCase):

    def setUp(self):
        # Set up a small sample dataframe to use in tests
        self.sample_data = pd.DataFrame({
            'Age': [19, 21, 20, 23, 31],
            'Annual Income (k$)': [15, 16, 17, 18, 19],
            'Spending Score (1-100)': [39, 81, 6, 77, 40],
            'Gender_Female': [0.0, 1.0, 1.0, 0.0, 1.0],
            'Gender_Male': [1.0, 0.0, 0.0, 1.0, 0.0]
        })

    @patch('src.visualization.plt.show')
    def test_plot_distribution(self, mock_show):
        # Test the plot_distribution function
        try:
            plot_distribution(self.sample_data, 'Age')
        except Exception as e:
            self.fail(f"plot_distribution raised an exception: {e}")

        # Check if plt.show() was called
        mock_show.assert_called_once()

    @patch('src.visualization.plt.show')
    def test_plot_correlation_matrix(self, mock_show):
        # Test the plot_correlation_matrix function
        try:
            plot_correlation_matrix(self.sample_data)
        except Exception as e:
            self.fail(f"plot_correlation_matrix raised an exception: {e}")

        # Check if plt.show() was called
        mock_show.assert_called_once()

if __name__ == '__main__':
    unittest.main()
