import streamlit as st

from PIL import Image

image = Image.open('WolfPackDown.jpg')
st.sidebar.image(image)

st.title(":question: Overview and Instructions")

col1, col2, col3 = st.columns((1.8,0.5,1))

col1.subheader("Overview")
#col1.markdown("This streamlit application has been developed in conjunction with the construction of predictive machine learning models to provide an easy interface to make predictions as well as explore the data used to train the various models.")
col1.markdown("This Streamlit application has been designed to accompany the development of predictive machine learning models. Its purpose is to provide a user-friendly interface for making predictions and exploring the training data used in these models.")

st.markdown("#")

col1.subheader("Models Investigated")

col1.markdown("- Logistic Regression Classifier")
col1.markdown("The logistic regression model is commonly used for binary classification tasks and is well-suited for analyzing the relationship between the input features and the target variable assuming a linear relationship.")

col1.markdown("- Support Vector Classifier")
col1.markdown("Support Vector Machines are powerful algorithms for both binary and multi-class classification. It aims to find an optimal hyperplane that maximally separates the data points of different classes.")

col1.markdown("- K Nearest Neighbours Classifier")
col1.markdown("KNN is a non-parametric algorithm that classifies data points based on their proximity to the nearest neighbors.")

col1.markdown("- Random Forest Classifier")
col1.markdown("A Random Forest Classifier is an ensemble learning method that combines multiple decision trees to make predictions.")

col3.info("How to Use", icon="ℹ️")

# Text Classification
col3.subheader("Text Classification")
col3.markdown("- Navigate to the main page.")
col3.markdown("- Choose a model from the provided options.")
col3.markdown("- Enter a piece of text in the designated input field.")
col3.markdown("- Click the 'Classify' button.")
col3.markdown("- The selected model will be used to classify the entered text and display the predicted classification.")

# Sentiment Filtering
col3.subheader("Sentiment Filtering")
col3.markdown("- Navigate to the 'Explore the Dataframe' page.")
col3.markdown("- Use the tabs to filter the dataframe (e.g. All, Anti, Neutral, Pro, or News).")
col3.markdown("- The displayed dataframe will update to show only the rows that match the selected sentiment.")

# Observations Search
col3.subheader("Observations Search")
col3.markdown("- Navigate to the 'Data Insights' tab.")
col3.markdown("- Enter a search term in the provided search box.")
col3.markdown("- Click the 'Search' button.")
col3.markdown("- All observations from the training data that contain the entered search term will be displayed.")
