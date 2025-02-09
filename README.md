# Heart Attack Prediction Model
![Screenshot 2025-02-09 151238](https://github.com/user-attachments/assets/5ab50867-b139-449d-a602-b76f2a4d2bc6)


## Overview
This repository contains a machine learning project that predicts the likelihood of a heart attack based on a dataset of 170,501 rows and 25 features. The current model achieves an accuracy of 75%, with ongoing improvements through feature engineering and scaling.

## Features
- **Dataset Size**: 170,501 rows and 25 columns.
- **Model Accuracy**: 75%.
- **Techniques Used**:
  - **Feature Engineering**: Enhancing feature selection and transformation.
  - **Scaling**: Standardizing feature values for better model performance.

## Objectives
- Improve the model's accuracy and robustness.
- Optimize feature selection and scaling techniques.
- Provide a user-friendly interface and detailed documentation.

## Installation
To set up the project locally, follow these steps:

```bash
# Clone the repository
git clone https://github.com/your-username/heart-attack-prediction.git

# Navigate to the project directory
cd heart-attack-prediction

# Install dependencies
pip install -r requirements.txt
```

## Usage
To train and test the model, run:

```bash
python train.py
```

To make predictions using the trained model:

```bash
python predict.py --input data/sample_input.csv
```

## Dataset
The dataset contains 170,501 records with 25 features, including patient demographics, medical history, and clinical measurements. Data preprocessing includes handling missing values, feature selection, and scaling.

## Model Details
The model is built using machine learning algorithms, with improvements through feature engineering and scaling techniques. The goal is to enhance prediction accuracy beyond 75%.

## Contributing
We welcome contributions! Feel free to fork the repository and submit pull requests.

## License
This project is licensed under the MIT License.

