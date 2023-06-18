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
import joblib,os

# Data dependencies
import pandas as pd

# Vectorizer
news_vectorizer = open("resources/tfidfvect.pkl","rb")
tweet_cv = joblib.load(news_vectorizer) # loading your vectorizer from the pkl file

# Load your raw data
#raw = pd.read_csv("resources/train.csv")
raw = pd.read_csv("resources/Training_Data.csv")

# The main function where we will build the actual app
def main():
	"""Tweet Classifier App with Streamlit """

	# Creates a main title and subheader on your page -
	# these are static across all pages
	#st.title("Tweet Classifier")


	# Creating sidebar with selection box -
	# you can create multiple pages this way
	options = ["Overview and Instructions", "Make a Prediction", "Explore the Data", "Contributors"]
	selection = st.sidebar.selectbox("Choose Option", options)

	if selection == "Overview and Instructions":
		
		st.info("# Tweet Classifier")
		st.subheader("Climate change tweet classification")
		st.markdown("#")
		
		st.info("Overview")
		st.markdown("Description of scope and utility of application")
		st.markdown("#")
		st.info("Instructions", icon="ℹ️")
		st.markdown("Provide instructions for use of features")

	# Building out the predication page
	if selection == "Make a Prediction":
		
		st.info("# Tweet Classifier")
		#st.subheader("Climate change tweet classification")
		st.markdown("#")
		
		st.info("Prediction with ML Models")
		# Creating a text box for user input
		tweet_text = st.text_area("Enter Text","Type Here")

		if st.button("Classify"):
			# Transforming user input with vectorizer
			vect_text = tweet_cv.transform([tweet_text]).toarray()
			# Load your .pkl file with the model of your choice + make predictions
			# Try loading in multiple models to give the user a choice
			predictor = joblib.load(open(os.path.join("resources/Logistic_regression.pkl"),"rb"))
			prediction = predictor.predict(vect_text)

			# When model has successfully run, will print prediction
			# You can use a dictionary or similar structure to make this output
			# more human interpretable.
			st.success("Text Categorized as: {}".format(prediction))

	# Building out the "Information" page
	if selection == "Explore the Data":
		
		st.info("# Tweet Classifier")
		#st.subheader("Climate change tweet classification")
		st.markdown("#")
		
		st.info("General Information")
		# You can read a markdown file from supporting resources folder
		st.markdown("Some information here")

		st.subheader("Raw Twitter data and label")
		if st.checkbox('Show raw data'): # data is hidden if box is unchecked
			st.write(raw[['sentiment', 'message']]) # will write the df to the page

	if selection == "Contributors":
		
		st.info("# Tweet Classifier")
		#st.subheader("Climate change tweet classification")
		st.markdown("#")
		
		st.info("Team")

		team_list = ["Sias Willemse", "Chesley Rogerson", "Thato Molapisi", "Thabiso Khoza", "Thebe Dikobo", "Boitumelo Mphahlele"]
		
		for member in team_list:

			st.markdown(member)

# Required to let Streamlit instantiate our web app.  
if __name__ == '__main__':
	main()
