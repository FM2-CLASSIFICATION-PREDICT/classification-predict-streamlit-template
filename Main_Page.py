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

st.set_page_config(page_title="Main_Page" ,layout="wide", initial_sidebar_state="auto") #initial_sidebar_state="auto","expanded"

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

col1.subheader("Predict Tweet Sentiment")

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

	probabilities = predictor.predict_proba(vect_text)

	df_prob = pd.DataFrame(probabilities, columns = ['Anti','Neutral','Pro', 'News'])
			
	#col2.subheader("Probability of Tweet being in each Sentiment")
	col2.subheader("Sentiment Probability Distribution")

	#col2.markdown(
    #"""
    #<div style="text-align: center;">
    #    <h2 style="font-size: 24px;">Probability of Tweet being in each Sentiment</h2>
    #</div>
    #""",
    #unsafe_allow_html=True)

	fig = plt.figure(figsize=(10, 7))

	color_map = {'Anti': 'red', 'Neutral': 'orange', 'Pro': 'green', 'News': 'purple'}

	ax = sns.barplot(data=df_prob, palette=color_map.values())
			
	for i in ax.containers:
		ax.bar_label(i, padding=2)

	col2.pyplot(fig)
			
	col1.markdown("#")

	st.markdown(
    """
    <style>
        .positive-label {
            background-color: green;
            color: white;
            padding: 10px;
            border-radius: 5px;
	    	font-size: 24px;
        }
        .negative-label {
            background-color: red;
            color: white;
            padding: 10px;
            border-radius: 5px;
	    	font-size: 24px;
        }
        .neutral-label {
            background-color: orange;
            color: white;
            padding: 10px;
            border-radius: 5px;
	    	font-size: 24px;
        }
		.news-label {
            background-color: purple;
            color: white;
            padding: 10px;
            border-radius: 5px;
	    	font-size: 24px;
        }
    </style>
    """,
    unsafe_allow_html=True)

	if class_dict[prediction[0]] == "Pro":
		#col1.success(" This tweet is pro climate change ⭐")
		st.markdown("""
		<div style="text-align: center;">
    <span class="positive-label">This tweet is Pro Climate Change ⭐</span>
    </div>
    """,
    unsafe_allow_html=True)
	elif class_dict[prediction[0]] == "Neutral":
		#col1.success(" This tweet is neutral towards climate change ⚖️")
		st.markdown("""
		<div style="text-align: center;">
    <span class="neutral-label">This tweet is neutral towards climate change ⚖️</span>
    </div>
    """,
    unsafe_allow_html=True)
	elif class_dict[prediction[0]] == "Anti":
		#col1.success(" This tweet is anti climate change 🚫")
		st.markdown("""
		<div style="text-align: center;">
    <span class="negative-label">This tweet is Anti Climate Change 🚫</span>
    </div>
    """,
    unsafe_allow_html=True)
	elif class_dict[prediction[0]] == "News":
		#col1.success(" This tweet is from a news vendor 📣")
		st.markdown("""
		<div style="text-align: center;">
    <span class="news-label">This tweet is from a news vendor 📣</span>
    </div>
    """,
    unsafe_allow_html=True)

	#col1.success(" This tweet is {} climate change 😄".format(class_dict[prediction[0]]))

	#st.balloons()