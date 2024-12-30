# MLflow-on-AWS-Setup

## Overview

This repository provides a step-by-step guide and example code for setting up **MLflow** on an AWS EC2 instance with S3 as the artifact storage. The repository includes an example script that demonstrates the use of MLflow for tracking experiments.

---

## Table of Contents
1. [Setup Guide](#setup-guide)
   - [AWS Configuration](#aws-configuration)
   - [EC2 Machine Setup](#ec2-machine-setup)
   - [Running MLflow Server](#running-mlflow-server)
2. [Example Code](#example-code)
3. [Requirements](#requirements)
4. [Usage](#usage)
5. [License](#license)

---

## Setup Guide

### AWS Configuration

1. **Login to AWS Console**:
   - Navigate to the AWS Management Console.

2. **Create IAM User**:
   - Create an IAM user with **AdministratorAccess** permissions.
   - Save the credentials for later use.

3. **Configure AWS CLI**:
   - Install AWS CLI locally and run the following command:
     ```bash
     aws configure
     ```
   - Provide the IAM credentials, region, and output format when prompted.

4. **Create S3 Bucket**:
   - Create an S3 bucket to store MLflow artifacts.

5. **Create EC2 Machine**:
   - Launch an EC2 instance (Ubuntu 20.04 preferred).
   - Add a security group allowing traffic on port **5000**.

---

### EC2 Machine Setup

1. SSH into your EC2 instance:
   ```bash
   ssh -i <your-key.pem> ubuntu@<EC2_PUBLIC_IP>
   ```

2. Run the following commands to set up the environment:
   ```bash
   sudo apt update
   sudo apt install -y python3-pip pipenv virtualenv
   ```

3. Create a directory for the project:
   ```bash
   mkdir mlflow
   cd mlflow
   ```

4. Install required Python packages:
   ```bash
   pipenv install mlflow awscli boto3
   pipenv shell
   ```

5. Configure AWS credentials:
   ```bash
   aws configure
   ```

---

### Running MLflow Server

1. Start the MLflow server:
   ```bash
   mlflow server -h 0.0.0.0 --default-artifact-root s3://<your-s3-bucket> --port 5000
   ```

2. Access the MLflow UI:
   - Open a browser and navigate to `http://<EC2_PUBLIC_IP>:5000`.

3. Set the MLflow tracking URI in your local environment:
   ```bash
   export MLFLOW_TRACKING_URI=http://<EC2_PUBLIC_IP>:5000
   ```

---

## Example Code

The `app.py` script demonstrates the use of MLflow for tracking an ElasticNet regression model. It includes the following features:
- Logging hyperparameters (`alpha`, `l1_ratio`)
- Tracking metrics (RMSE, MAE, R2 score)
- Storing the trained model as an artifact

To run the script locally:
```bash
python app.py
```

---

## Requirements

- Python 3.x
- AWS CLI
- MLflow
- Scikit-learn

Install the Python dependencies using:
```bash
pip install -r requirements.txt
```

---

## Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/MLflow-on-AWS-Setup.git
   cd MLflow-on-AWS-Setup
   ```

2. Follow the [Setup Guide](#setup-guide) to configure your environment.

3. Run the `app.py` script to log experiments and view results in the MLflow UI.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
