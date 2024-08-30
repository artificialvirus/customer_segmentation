# data_preprocessing.py

import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer

def load_data(filepath):
    return pd.read_csv(filepath)

def preprocess_data(df, scale_features=None, encode_features=None):
    # Handle missing values
    imputer = SimpleImputer(strategy='mean')
    df[scale_features] = imputer.fit_transform(df[scale_features])
    
    # Scale features
    if scale_features:
        scaler = StandardScaler()
        df[scale_features] = scaler.fit_transform(df[scale_features])
    
    # Encode categorical variables
    if encode_features:
        encoder = OneHotEncoder()
        encoded_df = pd.DataFrame(encoder.fit_transform(df[encode_features]).toarray(),
                                  columns=encoder.get_feature_names_out(encode_features))
        df = df.drop(encode_features, axis=1)
        df = df.join(encoded_df)
    
    return df

if __name__ == "__main__":
    df = load_data('../data/Mall_Customers.csv')
    df = preprocess_data(df, 
                         scale_features=['Age', 'Annual Income (k$)', 'Spending Score (1-100)'], 
                         encode_features=['Gender'])
    df.to_csv('../data/processed_customers.csv', index=False)
