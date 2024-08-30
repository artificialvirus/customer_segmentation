# main.py

from data_preprocessing import load_data, preprocess_data
from clustering import find_optimal_clusters, kmeans_clustering
from visualization import plot_distribution, plot_correlation_matrix
from retraining import retrain_model
import pandas as pd
from config import get_logger
import argparse

# Get the logger instance
logger = get_logger(__name__)

def run_preprocessing():
    df = load_data('../data/Mall_Customers.csv')
    df = preprocess_data(df, 
                         scale_features=['Age', 'Annual Income (k$)', 'Spending Score (1-100)'], 
                         encode_features=['Gender'])
    df.to_csv('../data/processed_customers.csv', index=False)
    logger.info("Processed data saved as ../data/processed_customers.csv.")
    return df

def run_visualization(df):
    plot_distribution(df, 'Age')
    plot_distribution(df, 'Annual Income (k$)')
    plot_distribution(df, 'Spending Score (1-100)')
    plot_correlation_matrix(df)
    logger.info("Data visualizations completed.")

def run_clustering(df):
    find_optimal_clusters(df, max_k=10)
    df, model = kmeans_clustering(df, n_clusters=5)
    df.to_csv('../data/clustered_customers.csv', index=False)
    logger.info("Clustered data saved as ../data/clustered_customers.csv.")
    return df, model

def run_retraining():
    retrain_model()
    logger.info("Model retraining completed and data saved.")

def main(steps):
    if 'preprocess' in steps:
        df = run_preprocessing()
    else:
        df = pd.read_csv('../data/processed_customers.csv')

    if 'visualize' in steps:
        run_visualization(df)

    if 'cluster' in steps:
        df, model = run_clustering(df)

    if 'retrain' in steps:
        run_retraining()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--steps', nargs='+', default=['preprocess', 'visualize', 'cluster', 'retrain'],
                        help="Steps to run: preprocess, visualize, cluster, retrain")
    args = parser.parse_args()

    main(args.steps)
