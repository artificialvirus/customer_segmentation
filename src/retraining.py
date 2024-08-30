# retraining.py

from apscheduler.schedulers.blocking import BlockingScheduler
import pandas as pd
from data_preprocessing import preprocess_data
from clustering import kmeans_clustering
from config import get_logger

# Get the logger instance
logger = get_logger(__name__)

def retrain_model():
    df = pd.read_csv('../data/Mall_Customers.csv')
    df = preprocess_data(df, 
                         scale_features=['Age', 'Annual Income (k$)', 'Spending Score (1-100)'], 
                         encode_features=['Gender'])
    df, model = kmeans_clustering(df, n_clusters=5)
    df.to_csv('../data/processed_customers.csv', index=False)
    logger.info("Model retrained and saved the updated processed data.")

if __name__ == "__main__":
    scheduler = BlockingScheduler()
    scheduler.add_job(retrain_model, 'interval', days=30)
    logger.info("Retraining job scheduled to run every 30 days.")
    scheduler.start()
