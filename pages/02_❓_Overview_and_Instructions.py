import streamlit as st
#import joblib, os

# Data dependencies
#import pandas as pd
#import seaborn as sns
#import matplotlib.pyplot as plt

#from sklearn import metrics

# Extra Imports
#from PIL import Image
#import plotly.express as px

#st.set_page_config(page_title="Overview and Instructions")

st.markdown("# :question: Overview and Instructions")
#st.sidebar.markdown("# Overview and Instructions")

col1, col2, col3 = st.columns((1.8,0.5,1))

col1.markdown("## Overview")
col1.markdown("This streamlit application has been developed in conjunction with the construction of predictive machine learning models to provide an easy interface to make predictions as well as explore the data used to train the various models.")
st.markdown("#")
col1.markdown("### Models used")
col1.markdown("- Logistic Regression Classifier")
col1.markdown("This model is commonly used for binary classification tasks and is well-suited for analyzing the relationship between the input features and the target variable.")

col1.markdown("- Support Vector Classifier")
col1.markdown("SVM is a powerful algorithm for both binary and multi-class classification. It aims to find an optimal hyperplane that maximally separates the data points of different classes. We will apply SVM to classify the tweets into different sentiment categories.")

col1.markdown("- K Nearest Neighbours Classifier")
col1.markdown("KNN is a non-parametric algorithm that classifies data points based on their proximity to the nearest neighbors. By considering the k nearest neighbors, we will build a KNN classifier to predict the sentiment of the tweets.")

col1.markdown("- Random Forest Classifier")
col1.markdown("Details to be added")

col3.info("Instructions", icon="ℹ️")
col3.markdown("Provide instructions for use of different features")