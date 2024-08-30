# clustering.py

from .config import get_logger
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score
import matplotlib.pyplot as plt
import joblib
import pandas as pd
import os

# Initialize the logger instance
logger = get_logger(__name__)

def kmeans_clustering(df, n_clusters):
    logger.info(f"Starting KMeans clustering with {n_clusters} clusters.")
    logger.info(f"Data shape: {df.shape}")
    
    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(df)
    df['Cluster'] = kmeans.labels_
    logger.info(f"Clustering completed. Assigned clusters: {df['Cluster'].unique()}")
    
    # Calculate clustering metrics
    silhouette_avg = silhouette_score(df, df['Cluster'])
    davies_bouldin_avg = davies_bouldin_score(df, df['Cluster'])
    calinski_harabasz_avg = calinski_harabasz_score(df, df['Cluster'])
    
    logger.info(f"Silhouette Score for {n_clusters} clusters: {silhouette_avg}")
    logger.info(f"Davies-Bouldin Index for {n_clusters} clusters: {davies_bouldin_avg}")
    logger.info(f"Calinski-Harabasz Index for {n_clusters} clusters: {calinski_harabasz_avg}")
    
    # Ensure the directory exists
    model_path = '../models/kmeans_model.pkl'
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    
    # Save the KMeans model
    joblib.dump(kmeans, model_path)
    logger.info(f"KMeans model saved at {model_path}.")
    
    return df, kmeans

def find_optimal_clusters(df, max_k):
    logger.info(f"Finding optimal clusters in range 1 to {max_k}.")
    
    sse = []
    silhouette_avg = []
    davies_bouldin_avg = []
    calinski_harabasz_avg = []

    for k in range(2, max_k + 1):  # Start from 2 to avoid invalid clustering metrics
        kmeans = KMeans(n_clusters=k, random_state=0).fit(df)
        sse.append(kmeans.inertia_)
        
        silhouette_avg.append(silhouette_score(df, kmeans.labels_))
        davies_bouldin_avg.append(davies_bouldin_score(df, kmeans.labels_))
        calinski_harabasz_avg.append(calinski_harabasz_score(df, kmeans.labels_))
        logger.info(f"Cluster {k}: Silhouette Score={silhouette_avg[-1]}, Davies-Bouldin Index={davies_bouldin_avg[-1]}, Calinski-Harasz Index={calinski_harabasz_avg[-1]}")
    
    plt.figure(figsize=(16, 8))
    
    plt.subplot(2, 2, 1)
    plt.plot(range(2, max_k + 1), sse)
    plt.xlabel('Number of Clusters')
    plt.ylabel('SSE')
    plt.title('Elbow Method')

    plt.subplot(2, 2, 2)
    plt.plot(range(2, max_k + 1), silhouette_avg)
    plt.xlabel('Number of Clusters')
    plt.ylabel('Silhouette Score')
    plt.title('Silhouette Method')

    plt.subplot(2, 2, 3)
    plt.plot(range(2, max_k + 1), davies_bouldin_avg)
    plt.xlabel('Number of Clusters')
    plt.ylabel('Davies-Bouldin Index')
    plt.title('Davies-Bouldin Index')

    plt.subplot(2, 2, 4)
    plt.plot(range(2, max_k + 1), calinski_harabasz_avg)
    plt.xlabel('Number of Clusters')
    plt.ylabel('Calinski-Harabasz Index')
    plt.title('Calinski-Harabasz Index')

    plt.tight_layout()
    
    # Ensure the logs directory exists
    os.makedirs('../logs', exist_ok=True)
    
    plt.savefig(f"../logs/cluster_evaluation_metrics.png")
    logger.info(f"Cluster evaluation metrics plot saved as ../logs/cluster_evaluation_metrics.png.")
    plt.show()
