# Customer Segmentation Project

## Overview

This project is focused on customer segmentation using various clustering techniques. It includes data preprocessing, clustering, and visualization of results, all wrapped in a modular Python codebase. The project aims to provide actionable insights for businesses by grouping customers based on their behavior and characteristics.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [CI/CD Pipeline](#cicd-pipeline)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Data Preprocessing:** Cleans and prepares raw data for clustering.
- **Clustering:** Implements KMeans and other clustering algorithms to segment customers.
- **Evaluation Metrics:** Uses metrics such as Silhouette Score, Davies-Bouldin Index, and Calinski-Harabasz Index to evaluate the quality of clusters.
- **Visualization:** Generates plots to visualize the clusters and evaluation metrics.
- **Logging:** Provides detailed logging for debugging and process tracking.
- **Docker Integration:** Includes Docker configuration for easy deployment and testing.

## Installation

To run this project locally, follow these steps:

### Prerequisites

- Python 3.8 or higher
- Docker (optional for containerized deployment)
- Git

### Clone the Repository

```bash
git clone https://github.com/artificialvirus/customer_segmentation.git
cd customer_segmentation
```

### Set Up a Virtual Environment
```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### Install Dependencies
```
pip install -r requirements.txt
```

### Usage

Running the Clustering Process
To run the clustering process on your dataset:

Place your dataset in the data/ directory.
Modify the config.yaml file to point to your dataset and adjust any necessary parameters.
Run the clustering script:
```
python src/main.py
```

### Visualizing Results
Results and evaluation metrics will be saved in the logs/ directory. You can visualize them by opening the generated images.

### Docker
To build and run the Docker container:
```
docker build -t customer_segmentation .
docker run -p 5000:5000 customer_segmentation
```

### Project Structure
```
customer_segmentation/
├── data/                     # Data files
├── src/                      # Source code for the project
│   ├── __init__.py
│   ├── main.py               # Main script to run the project
│   ├── config.py             # Configuration settings
│   ├── preprocessing.py      # Data preprocessing module
│   ├── clustering.py         # Clustering module
│   ├── visualization.py      # Visualization module
│   ├── logger.py             # Logging setup
│   ├── dashboard.py          # Dashboard module
│   ├── deployment.py         # Deployment script
│   ├── orchestrator.py       # Orchestration logic
│   └── retraining.py         # Model retraining script
├── notebooks/                # Jupyter notebooks for experimentation
├── tests/                    # Unit tests
│   ├── __init__.py
│   ├── test_clustering.py    # Tests for clustering module
│   ├── test_data_preprocessing.py # Tests for preprocessing module
│   ├── test_visualization.py # Tests for visualization module
│   └── test_dashboard.py     # Tests for dashboard module
├── Dockerfile                # Docker configuration
├── requirements.txt          # Python dependencies
├── .flake8                   # Flake8 configuration file
├── README.md                 # Project README file
└── .github/                  # GitHub Actions for CI/CD
    └── workflows/
        └── ci-cd.yml            # CI/CD Pipeline


```

### Testing
This project uses pytest for testing. To run the tests:
```
pytest
```

### CI/CD Pipeline
This project is integrated with GitHub Actions for continuous integration and continuous deployment (CI/CD). The pipeline includes:

Testing: Runs all unit tests.
Docker Build: Builds the Docker image.
Deployment: Optionally deploys the Docker container.
To trigger the pipeline, simply push to the main branch or open a pull request.

### Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature-name).
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature/your-feature-name).
Open a Pull Request.
Please ensure your code follows the project's coding standards and passes all tests before submitting a PR.

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Contact
For any inquiries or questions, feel free to reach out.
