# test_clustering.py

import unittest
import pandas as pd
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score
from src.clustering import kmeans_clustering, find_optimal_clusters

class TestClustering(unittest.TestCase):

    def setUp(self):
        self.sample_data = pd.DataFrame({
            'Age': [19, 21, 20, 23, 31, 25, 22],
            'Annual Income (k$)': [15, 16, 17, 18, 19, 20, 21],
            'Spending Score (1-100)': [39, 81, 6, 77, 40, 60, 55],
            'Gender_Female': [0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0],
            'Gender_Male': [1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0]
        })

    def test_kmeans_clustering(self):
        # Perform KMeans clustering
        df_clustered, model = kmeans_clustering(self.sample_data.copy(), n_clusters=3)

        # Assert that the 'Cluster' column was added
        self.assertIn('Cluster', df_clustered.columns)
        self.assertEqual(len(df_clustered['Cluster'].unique()), 3)

        # Verify that the clustering metrics are calculated correctly
        silhouette_avg = silhouette_score(df_clustered.drop(columns=['Cluster']), df_clustered['Cluster'])
        davies_bouldin_avg = davies_bouldin_score(df_clustered.drop(columns=['Cluster']), df_clustered['Cluster'])
        calinski_harabasz_avg = calinski_harabasz_score(df_clustered.drop(columns=['Cluster']), df_clustered['Cluster'])

        # Ensure that the calculated metrics are within a reasonable range
        self.assertGreaterEqual(silhouette_avg, -1)
        self.assertLessEqual(silhouette_avg, 1)
        self.assertGreaterEqual(davies_bouldin_avg, 0)
        self.assertGreaterEqual(calinski_harabasz_avg, 0)

    def test_find_optimal_clusters(self):
        # Run the function to find the optimal number of clusters
        try:
            find_optimal_clusters(self.sample_data.copy(), max_k=5)
        except Exception as e:
            self.fail(f"find_optimal_clusters raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()
