# 🌾 Crop Yield Prediction (End-to-End ML Project)

# 🔗 App Link: https://crop-yielding-v7bxlprefmbdffngnajdjq.streamlit.app/

## 📌 Project Overview

This project is an End-to-End Machine Learning application that predicts crop yield based on environmental and agricultural factors.

It covers the complete ML lifecycle:

📂 Data preprocessing – Cleaning and preparing historical crop data
⚙️ Feature encoding – One-hot encoding for categorical features (Area, Crop Item)
🤖 Model training – Pre-trained regression model for crop yield prediction
💾 Model persistence – Saved and loaded using Pickle
🖥️ Interactive frontend – Streamlit UI for user input and predictions

## 🚀 Features

🧠 Predicts crop yield (hg/ha) based on user inputs

⚡ Real-time prediction via a Streamlit web app

🔍 Handles categorical and numerical features automatically

🖥️ Clean, user-friendly UI for easy input and result visualization

## 🛠️ Tech Stack

Python 🐍

Scikit-learn → Regression model & preprocessing

Streamlit → Web app frontend

NumPy / Pandas → Data processing

Pickle → Model saving & loading

## 📂 Project Structure
Crop_Yield_App/
├── app.py
├── crop_yield_model_full.pkl
├── data.csv
├── requirements.txt
└── README.md

## ⚙️ Installation & Setup

Install dependencies

pip install -r requirements.txt


## Run the Streamlit app

streamlit run app.py


## 📊 Model Performance

Algorithm: Regression Model (trained on historical crop data)

Evaluation Metrics:

✅ R²: 0.90

✅ RMSE: 27,000 hg/ha

⚠️ Note: Predictions may be higher than actual values if inputs are outside training data ranges or encoding mismatches occur.
