# visualization.py

import seaborn as sns
import matplotlib.pyplot as plt

def plot_distribution(df, column):
    sns.histplot(df[column], kde=True)
    plt.title(f'{column} Distribution')
    plt.show()

def plot_correlation_matrix(df):
    corr = df.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()
