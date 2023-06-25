# Required
import streamlit as st

# Data dependencies
import joblib, os

# Data Manipulation and Visualisation

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

#import plotly.express as px
#import base64

st.set_page_config(page_title="Main_Page" ,layout="wide", initial_sidebar_state="collapsed") #initial_sidebar_state="auto","expanded"

image = Image.open('WolfPackDown.jpg')
st.sidebar.image(image)

st.title(":house_with_garden: Main Page")

#with open('WolfPackDown.jpg', "rb") as f:
#    data = base64.b64encode(f.read()).decode("utf-8")
#
#    st.sidebar.markdown(
#        f"""
#        <div style="display:table;margin-top:62%;margin-left:-4%;">
#            <img src="data:image/png;base64,{data}" width="330" height="330">
#        </div>
#        """,
#        unsafe_allow_html=True,
#    )

raw = pd.read_csv("resources/Training_Data.csv")

col1, col2 = st.columns(2)

col1.subheader("Predict the Sentiment of a Tweet")

model_type = col1.radio("Choose a Model Type", ["Logistic Regression Classifier",
						"Support Vector Classifier", "K Nearest Neighbours" , "Random Forest Classifier"])

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
			
	col2.subheader("Probability of Tweet being in each Sentiment")

	fig = plt.figure(figsize=(10, 7))
			
	ax = sns.barplot(data=df_prob)
			
	for i in ax.containers:
		ax.bar_label(i, padding=2)

	col2.pyplot(fig)
			
	#col2.markdown("The bar chart above displays...")

	st.success("Your tweet has been classfied as: {}".format(class_dict[prediction[0]]))