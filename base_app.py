"""

    Simple Streamlit webserver application for serving developed classification
	models.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within this directory for guidance on how to use this script
    correctly.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend the functionality of this script
	as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st
import joblib, os

# Data dependencies
import pandas as pd

# Extra Imports
from PIL import Image
#import plotly.express as px

# Vectorizers
default_vectorizer = open("resources/tfidfvect.pkl","rb")
default_vectorizer = joblib.load(default_vectorizer) # loading your vectorizer from the pkl file

# For when multiple models are loaded
#wolf_vectorizer = open("resources/tfidfvect.pkl","rb")
#wolf_vectorizer = joblib.load(wolf_vectorizer)

# Load your raw data
#raw = pd.read_csv("resources/train.csv")
raw = pd.read_csv("resources/Training_Data.csv")

# The main function where we will build the actual app
def main():
	"""Tweet Classifier App with Streamlit """

	# Creates a main title and subheader on your page -
	# these are static across all pages
	st.title("Tweet Classifier")
	st.subheader("Climate change tweet classification")
	st.markdown("#")

	# Creating sidebar with selection box -
	# you can create multiple pages this way
	options = ["Overview and Instructions", "Make a Prediction", "Explore the Data", "Contributors"]
	selection = st.sidebar.selectbox("Choose Option", options)

	#Building Overview page
	if selection == "Overview and Instructions":
	
		st.info("Overview")
		st.markdown("Description of scope and utility of application")
		st.markdown("#")
		st.info("Instructions", icon="ℹ️")
		st.markdown("Provide instructions for use of different features")

	# Building prediction page
	if selection == "Make a Prediction":
		
		st.info("Make a Prediction")
		# Creating a text box for user input
		tweet_text = st.text_area("Enter Tweet","Type Here")

		if st.button("Classify"):
			# Transforming user input with vectorizer
			vect_text = default_vectorizer.transform([tweet_text]).toarray()
			# Load your .pkl file with the model of your choice + make predictions
			# Try loading in multiple models to give the user a choice
			predictor = joblib.load(open(os.path.join("resources/Logistic_regression.pkl"),"rb"))
			prediction = predictor.predict(vect_text)

			# When model has successfully run, will print prediction
			# You can use a dictionary or similar structure to make this output
			# more human interpretable.
			st.success("Text Categorized as: {}".format(prediction))

	# Building information page
	if selection == "Explore the Data":

		st.subheader("Count of Sentiments in Training Data")

		sentiment_count = raw["sentiment"].value_counts()
		st.bar_chart(sentiment_count)

		st.subheader("Raw Training Data")
		graph_selection = st.sidebar.selectbox("Select a Sentiment", ["All", "-1", "0", "1", "2"])

		if graph_selection == "All":

			#st.markdown("## All Tweets")

			st.info("All Tweets")

			st.write(raw[['sentiment', 'message']])

			st.table({"Number of Tweets" : len(raw), "Percentage of Dataset" : int((len(raw)/len(raw))*100)})

		if graph_selection == "-1":

			st.info("Anti Climate Change Tweets")

			anti = raw[raw["sentiment"]==-1]

			st.write(anti[["sentiment", "message"]])

			st.table({"Number of Tweets" : len(anti), "Percentage of Dataset" : int((len(anti)/len(raw))*100)})

		if graph_selection == "0":
			
			st.info("Neutral to Climate Change Tweets")

			neut = raw[raw["sentiment"]==0]

			st.write(neut[["sentiment", "message"]])

			st.table({"Number of Tweets" : int(len(neut)), "Percentage of Dataset" : int((len(neut)/len(raw))*100)})

		if graph_selection == "1":
			
			st.info("Pro Climate Change Tweets")
			
			pro = raw[raw["sentiment"]==1]

			st.write(pro[["sentiment", "message"]])

			st.table({"Number of Tweets" : len(pro), "Percentage of Dataset" : int((len(pro)/len(raw))*100)})

		if graph_selection == "2":
			
			st.info("News Climate Change Tweets")
			
			news = raw[raw["sentiment"]==2]

			st.write(news[["sentiment", "message"]])

			st.table({"Number of Tweets" : len(news), "Percentage of Dataset" : int((len(news)/len(raw))*100)})	

		st.subheader("Data Description")
		# You can read a markdown file from supporting resources folder
		#st.markdown("Some information here")

		st.markdown("-1 : Anti")
		st.markdown("0 : Neutral")
		st.markdown("1 : Pro")
		st.markdown("2 : News")

		#st.subheader("Raw Twitter data and label")
		#if st.checkbox('Show raw data'): # data is hidden if box is unchecked
			#st.write(raw[['sentiment', 'message']]) # will write the df to the page

	# Building Contributors Page
	if selection == "Contributors":
		
		st.info("Wolf Pack Team")

		team_list = ["Sias Willemse", "Chesley Rogerson", "Thato Molapisi", "Thabiso Khoza", "Thebe Dikobo", "Boitumelo Mphahlele"]
		
		for member in team_list:

			st.markdown(member)

		#df = raw.groupby("sentiment")#.count().reset_index().rename(columns={"Item_Name": "Count"})

		#fig = px.bar(df, x="sentiment", y="Count", color="sentiment", text="Count")

		#fig = px.bar(itemcrosstab, barmode="group", text_auto=True)

		

# Required to let Streamlit instantiate our web app.  
if __name__ == '__main__':
	main()
