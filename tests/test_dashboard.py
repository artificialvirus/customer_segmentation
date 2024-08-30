# test_dashboard.py

import unittest
from unittest.mock import patch
from dash import dcc, html
import plotly.express as px
import pandas as pd
from src.dashboard import app, update_graph

class TestDashboard(unittest.TestCase):

    @patch('src.dashboard.pd.read_csv')
    def test_layout(self, mock_read_csv):
        # Mock the CSV loading process
        mock_read_csv.return_value = pd.DataFrame({
            'Annual Income (k$)': [15, 16, 17, 18, 19],
            'Spending Score (1-100)': [39, 81, 6, 77, 40],
            'Cluster': [0, 1, 1, 0, 1]
        })
        
        # Now the app will use the mock data
        self.assertIsInstance(app.layout, html.Div)
        self.assertEqual(len(app.layout.children), 5)

        # Check if the H1 element is correct
        self.assertEqual(app.layout.children[0].children, 'Customer Segmentation Dashboard')

        # Check if there are Dropdown components in the layout
        dropdown_ids = ['x-axis', 'y-axis', 'cluster-filter']
        for i, dropdown_id in enumerate(dropdown_ids, 1):
            self.assertIsInstance(app.layout.children[i].children[1], dcc.Dropdown)
            self.assertEqual(app.layout.children[i].children[1].id, dropdown_id)

    @patch('src.dashboard.pd.read_csv')
    def test_update_graph(self, mock_read_csv):
        # Mock the CSV loading process
        mock_read_csv.return_value = pd.DataFrame({
            'Annual Income (k$)': [15, 16, 17, 18, 19],
            'Spending Score (1-100)': [39, 81, 6, 77, 40],
            'Cluster': [0, 1, 1, 0, 1]
        })

        mock_data = mock_read_csv.return_value

        # Test callback without cluster filter
        fig = update_graph('Annual Income (k$)', 'Spending Score (1-100)', [], data=mock_data)
        self.assertIsInstance(fig, px.scatter().__class__)
        self.assertEqual(len(fig.data[0].x), 5)  # Should match mock data length

        # Test callback with a cluster filter
        fig = update_graph('Annual Income (k$)', 'Spending Score (1-100)', [1], data=mock_data)
        filtered_df = mock_data[mock_data['Cluster'] == 1]
        self.assertEqual(len(fig.data[0].x), len(filtered_df['Annual Income (k$)']))

    def test_server_runs(self):
        # Test if the Dash app can be instantiated and run (without actually running it)
        app_instance = app.server
        self.assertIsNotNone(app_instance)

if __name__ == '__main__':
    unittest.main()
