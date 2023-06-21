import streamlit as st
import joblib, os

# Data dependencies
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#from sklearn import metrics

# Extra Imports
#from PIL import Image
#import plotly.express as px

st.set_page_config(layout="wide")

default_vectorizer = open("resources/tfidfvect.pkl","rb")
default_vectorizer = joblib.load(default_vectorizer) # loading your vectorizer from the pkl file

raw = pd.read_csv("resources/Training_Data.csv")

st.title("Main page 🎈")
#st.sidebar.markdown("# Main page 🎈")

col1, col2 = st.columns(2)

col1.markdown("## Predict the sentiment of a tweet")
col1.markdown("This will detail the steps to follow")
col1.selectbox("Choose a Classifier", ["Default", "Wolf"])
		# Creating a text box for user input
tweet_text = col1.text_area("Enter Tweet","Type Here")

if col1.button("Classify"):
			
	# Transforming user input with vectorizer
	vect_text = default_vectorizer.transform([tweet_text]).toarray()
			
	# Load your .pkl file with the model of your choice + make predictions
	# Try loading in multiple models to give the user a choice
	predictor = joblib.load(open(os.path.join("resources/Logistic_regression.pkl"),"rb"))
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