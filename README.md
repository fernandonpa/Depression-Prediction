# **Depression Prediction Using Machine Learning**

This repository contains the code and resources for a machine learning project aimed at predicting the risk of depression based on lifestyle and demographic factors. The project uses a publicly available dataset from Kaggle and implements various machine learning models to achieve accurate predictions.

---

## **Table of Contents**

1. [Project Overview](#project-overview)
2. [Dataset](#dataset)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Results](#results)
6. [License](#license)
7. [Contact](#contact)

---

## **Project Overview**

Depression is a significant global health issue, and early detection can greatly improve outcomes. This project uses machine learning to predict the risk of depression based on factors such as age, gender, occupation, sleep duration, dietary habits, and financial stress. The goal is to provide a tool that can help identify individuals at risk of depression and encourage them to seek professional help.

---

## **Dataset**

The dataset used in this project is publicly available on Kaggle:  
[**Mental Health Dataset on Kaggle**](https://www.kaggle.com/datasets/firmanhasibuan1/mental-health-dataset).

### **Dataset Description**

- **Source**: Collected through an anonymous survey conducted between January and June 2023.
- **Size**: Approximately 3,000 records, expanded using advanced deep learning techniques.
- **Features**: Includes both categorical (e.g., gender, profession) and numerical (e.g., age, sleep duration) features.
- **Target Variable**: Binary classification (Depression: Yes/No).

---

## **Installation**

To run this project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/fernandonpa/Depression-Prediction.git
   cd Depression-Prediction
   ```
2. **Set Up a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## **Usage**

1. **Load and Preprocess the Data**

   Run the preprocessing notebook to clean and prepare the dataset

2. **Train the Model**

   Train the machine learning models using the preprocessed data

3. **Evaluate the Model**

   Evaluate the model's performance using metrics such as accuracy, precision, recall, and F1 score

4. **Run the GUI application**

   Use the GUI application to input data and get real-time predictions

   ```bash
   python src/gui.py
   ```

---

## **Results**

The best-performing model in this project is CatBoost, which achieved the following results:

- **Accuracy**: `96.22%` (Working Professionals), `89.04%` (Students)
- **F1 Score**:` 0.97` (Working Professionals), `0.92` (Students)

---

## **License**

This project is licensed under the **MIT License**. See the [LICENSE](https://license/) file for details.

---

## **Contact**

For questions or feedback, feel free to reach out:

- **Name** : `Praneeth Anjana`
- **Email** : [`praneeth.22`](mailto:praneeth.22@cse.mart.ac.lk)

---
