import streamlit as st
import joblib, os

# Data dependencies
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#from sklearn import metrics

# Extra Imports
from PIL import Image
#import plotly.express as px

st.set_page_config(layout="wide")

#image = Image.open('WolfPackDown.jpg')
#st.sidebar.image(image)

import base64

with open('WolfPackDown.jpg', "rb") as f:
    data = base64.b64encode(f.read()).decode("utf-8")

    st.sidebar.markdown(
        f"""
        <div style="display:table;margin-top:62%;margin-left:-4%;">
            <img src="data:image/png;base64,{data}" width="330" height="330">
        </div>
        """,
        unsafe_allow_html=True,
    )

#default_vectorizer = open("resources/tfidfvect.pkl","rb")
#default_vectorizer = joblib.load(default_vectorizer) # loading your vectorizer from the pkl file

raw = pd.read_csv("resources/Training_Data.csv")

st.title(":house_with_garden: Main page")
#st.sidebar.markdown("# Main page 🎈")

col1, col2 = st.columns(2)

col1.markdown("## Predict the sentiment of a tweet")
col1.markdown("This will detail the steps to follow")
#col1.selectbox("Choose a Classifier", ["Default", "Logistic Regression", "Support Vector Machine", "Random Forest"])
#model_type = col1.radio("Choose a classifier", ["Default", "Logistic Regression Classifier", "Support Vector Classifier", "K Nearest Neighbours" , "Random Forest Classifier"])

model_type = col1.radio("Choose a classifier", ["Logistic Regression Classifier", "Support Vector Classifier", "K Nearest Neighbours" , "Random Forest Classifier"])

#model_type = col1.radio("Choose a classifier", ["Logistic Regression Classifier", "Support Vector Classifier", "K Nearest Neighbours"])

#if model_type == "Default":
#	default_vectorizer = open("resources/tfidfvect.pkl","rb")
#	default_vectorizer = joblib.load(default_vectorizer)
#	predictor = joblib.load(open(os.path.join("resources/Logistic_regression.pkl"),"rb"))

if model_type == "Logistic Regression Classifier":
	default_vectorizer = open("resources/cv_up_logreg.pkl","rb")
	default_vectorizer = joblib.load(default_vectorizer)
	predictor = joblib.load(open(os.path.join("resources/up_logreg_model.pkl"),"rb"))

elif model_type == "Support Vector Classifier":
	default_vectorizer = open("resources/cv_up_svc.pkl","rb")
	default_vectorizer = joblib.load(default_vectorizer)
	predictor = joblib.load(open(os.path.join("resources/up_svc_model.pkl"),"rb"))

elif model_type == "K Nearest Neighbours":
	default_vectorizer = open("resources/cv_up_knn.pkl","rb")
	default_vectorizer = joblib.load(default_vectorizer)
	predictor = joblib.load(open(os.path.join("resources/up_knn_model.pkl"),"rb"))

elif model_type == "Random Forest Classifier":
	default_vectorizer = open("resources/cv_up_rfc.pkl","rb")
	default_vectorizer = joblib.load(default_vectorizer)
	predictor = joblib.load(open(os.path.join("resources/up_rfc_model.pkl"),"rb"))


		# Creating a text box for user input
tweet_text = col1.text_area("Enter Tweet","Type Here")

if col1.button("Classify"):
			
	# Transforming user input with vectorizer
	vect_text = default_vectorizer.transform([tweet_text]).toarray()
			
	# Load your .pkl file with the model of your choice + make predictions
	# Try loading in multiple models to give the user a choice
	#predictor = joblib.load(open(os.path.join("resources/Logistic_regression.pkl"),"rb"))
	prediction = predictor.predict(vect_text)

			# When model has successfully run, will print prediction
			# You can use a dictionary or similar structure to make this output
			# more human interpretable.

	class_dict = {-1 : "Anti", 0 : "Neutral", 1 : "Pro", 2 : "News"}

			#st.success("Text Categorized as: {}".format(prediction))

	probabilities = predictor.predict_proba(vect_text)

	df_prob = pd.DataFrame(probabilities, columns = ['Anti','Neutral','Pro', 'News'])
			
	col2.markdown("## Probability of Tweet being in each Sentiment")

	fig = plt.figure(figsize=(10, 7))
			
	ax = sns.barplot(data=df_prob)
			
	for i in ax.containers:
		ax.bar_label(i, padding=2)

	col2.pyplot(fig)
			
	col2.markdown("The bar chart above displays...")

	st.success("Your tweet has been classfied as: {}".format(class_dict[prediction[0]]))