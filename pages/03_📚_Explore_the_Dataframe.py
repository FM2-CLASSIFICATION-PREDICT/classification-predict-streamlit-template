import streamlit as st
import os

# Data dependencies
#import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Extra Imports
from PIL import Image

from collections import Counter
from nltk import ngrams
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
#import string
import seaborn as sns

#from Main_Page import raw

image = Image.open('WolfPackDown.jpg')
st.sidebar.image(image)

script_dir = os.path.dirname(__file__)
full_path = os.path.join(script_dir, '../resources/Training_Data.csv')

raw = pd.read_csv(full_path)

@st.cache_data
def calculate_unigrams(filtered_df):

	combined_text = " ".join(filtered_df["message"])

	# Tokenize the text into individual words
	tokens = word_tokenize(combined_text)

	# Remove stopwords
	stop_words = set(stopwords.words("english"))
	word_exclude = ["https", "rt", "amp"]#, "U", "Â", "â", "Ã", "ã"]"t", "co"
	for word in word_exclude:
		stop_words.add(word)
	
	filtered_tokens = [token.lower() for token in tokens if token.lower() not in stop_words and token.isalnum()]

	# Generate unigrams
	unigrams = Counter(filtered_tokens)

	# Get the top 10 unigrams
	top_unigrams = unigrams.most_common(10)

	return top_unigrams

@st.cache_data
def calculate_bigrams(filtered_df):

	combined_text = " ".join(filtered_df["message"])

	# Tokenize the text into individual words
	tokens = word_tokenize(combined_text)

	# Remove stopwords
	stop_words = set(stopwords.words("english"))
	word_exclude = ["https", "rt", "amp"]#, "U", "Â", "â", "Ã", "ã"]"t", "co"
	for word in word_exclude:
		stop_words.add(word)
	
	filtered_tokens = [token.lower() for token in tokens if token.lower() not in stop_words and token.isalnum()]

	# Generate bigrams
	bigrams = Counter(ngrams(filtered_tokens, 2))

	# Get the top 10 bigrams
	top_bigrams = bigrams.most_common(10)

	return top_bigrams


st.title(":books: Explore the Dataframe")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["All Data", "Anti 🚫", "Neutral ⚖️", "Pro ⭐", "News 📣"])

with tab1:
	
	st.subheader("All Sentiment Tweet Data")
	st.dataframe(raw[['sentiment', 'message']], width=1560, column_config={"sentiment": "Sentiment", "message": "Tweet"}, hide_index=True)

	#col1.table({"Number of Tweets" : len(raw), "Percentage of Dataset" : int((len(raw)/len(raw))*100)})

	col1, col2 = st.columns(2)

	show_uni1 = col1.checkbox("Show Top 10 Unigrams", key="AllTab1")

	if show_uni1:
		
		top_unigrams = calculate_unigrams(raw)

		col1.subheader("Top 10 Unigrams")
		fig, ax = plt.subplots(figsize=(8, 6))
		sns.barplot(y=[keyword[0] for keyword in top_unigrams], x=[keyword[1] for keyword in top_unigrams], ax=ax, orient='h', palette="hls")
		ax.set_xlabel("Count")
		#plt.xticks(rotation=45)
		col1.pyplot(fig)

	show_bi1 = col2.checkbox("Show Top 10 Bigrams", key="AllTab2")

	if show_bi1:
		
		top_bigrams = calculate_bigrams(raw)
		
		col2.subheader("Top 10 Bigrams")
		fig, ax = plt.subplots(figsize=(8, 6))
		#sns.barplot(y=[keyword[0] for keyword in top_bigrams], x=[keyword[1] for keyword in top_bigrams], ax=ax, orient='h', palette="hls")
		sns.barplot(y=[keyword[0][0] + " " + keyword[0][1] for keyword in top_bigrams], x=[keyword[1] for keyword in top_bigrams], ax=ax, orient='h', palette="hls")
		ax.set_xlabel("Count")
		#plt.xticks(rotation=45)
		col2.pyplot(fig)

	
with tab2:
	
	st.subheader("Anti Sentiment Tweet Data")
	anti = raw[raw["sentiment"]==-1]
	st.dataframe(anti[['sentiment', 'message']], width=1560, column_config={"sentiment": "Sentiment", "message": "Tweet"}, hide_index=True)

	col1, col2 = st.columns(2)

	show_uni2 = col1.checkbox("Show Top 10 Unigrams", key="AntiTab1")

	if show_uni2:
		
		top_unigrams = calculate_unigrams(anti)

		col1.subheader("Top 10 Unigrams")
		fig, ax = plt.subplots(figsize=(8, 6))
		sns.barplot(y=[keyword[0] for keyword in top_unigrams], x=[keyword[1] for keyword in top_unigrams], ax=ax, orient='h', palette="hls")
		ax.set_xlabel("Count")
		col1.pyplot(fig)

	show_bi2 = col2.checkbox("Show Top 10 Bigrams", key="AntiTab2")

	if show_bi2:
		
		top_bigrams = calculate_bigrams(anti)
		
		col2.subheader("Top 10 Bigrams")
		fig, ax = plt.subplots(figsize=(8, 6))
		sns.barplot(y=[keyword[0][0] + " " + keyword[0][1] for keyword in top_bigrams], x=[keyword[1] for keyword in top_bigrams], ax=ax, orient='h', palette="hls")
		ax.set_xlabel("Count")
		col2.pyplot(fig)
	
with tab3:
	st.subheader("Neutral Sentiment Tweet Data")
	neutral = raw[raw["sentiment"]==0]
	st.dataframe(neutral[['sentiment', 'message']], width=1560, column_config={"sentiment": "Sentiment", "message": "Tweet"}, hide_index=True)

	col1, col2 = st.columns(2)

	show_uni3 = col1.checkbox("Show Top 10 Unigrams", key="NeutralTab1")

	if show_uni3:
		
		top_unigrams = calculate_unigrams(neutral)

		col1.subheader("Top 10 Unigrams")
		fig, ax = plt.subplots(figsize=(8, 6))
		sns.barplot(y=[keyword[0] for keyword in top_unigrams], x=[keyword[1] for keyword in top_unigrams], ax=ax, orient='h', palette="hls")
		ax.set_xlabel("Count")
		col1.pyplot(fig)

	show_bi3 = col2.checkbox("Show Top 10 Bigrams", key="NeutralTab2")

	if show_bi3:
		
		top_bigrams = calculate_bigrams(neutral)
		
		col2.subheader("Top 10 Bigrams")
		fig, ax = plt.subplots(figsize=(8, 6))
		sns.barplot(y=[keyword[0][0] + " " + keyword[0][1] for keyword in top_bigrams], x=[keyword[1] for keyword in top_bigrams], ax=ax, orient='h', palette="hls")
		ax.set_xlabel("Count")
		col2.pyplot(fig)	
	
with tab4:
	st.subheader("Pro Sentiment Tweet Data")
	pro = raw[raw["sentiment"]==1]
	st.dataframe(pro[['sentiment', 'message']], width=1560, column_config={"sentiment": "Sentiment", "message": "Tweet"}, hide_index=True)

	col1, col2 = st.columns(2)

	show_uni4 = col1.checkbox("Show Top 10 Unigrams", key="ProTab1")

	if show_uni4:
		
		top_unigrams = calculate_unigrams(pro)

		col1.subheader("Top 10 Unigrams")
		fig, ax = plt.subplots(figsize=(8, 6))
		sns.barplot(y=[keyword[0] for keyword in top_unigrams], x=[keyword[1] for keyword in top_unigrams], ax=ax, orient='h', palette="hls")
		ax.set_xlabel("Count")
		col1.pyplot(fig)

	show_bi4 = col2.checkbox("Show Top 10 Bigrams", key="ProTab2")

	if show_bi4:
		
		top_bigrams = calculate_bigrams(pro)
		
		col2.subheader("Top 10 Bigrams")
		fig, ax = plt.subplots(figsize=(8, 6))
		sns.barplot(y=[keyword[0][0] + " " + keyword[0][1] for keyword in top_bigrams], x=[keyword[1] for keyword in top_bigrams], ax=ax, orient='h', palette="hls")
		ax.set_xlabel("Count")
		col2.pyplot(fig)

	
with tab5:
	st.subheader("All Sentiment Tweet Data")
	news = raw[raw["sentiment"]==2]
	st.dataframe(news[['sentiment', 'message']], width=1560, column_config={"sentiment": "Sentiment", "message": "Tweet"}, hide_index=True)

	col1, col2 = st.columns(2)

	show_uni5 = col1.checkbox("Show Top 10 Unigrams", key="NewsTab1")

	if show_uni5:
		
		top_unigrams = calculate_unigrams(news)

		col1.subheader("Top 10 Unigrams")
		fig, ax = plt.subplots(figsize=(8, 6))
		sns.barplot(y=[keyword[0] for keyword in top_unigrams], x=[keyword[1] for keyword in top_unigrams], ax=ax, orient='h', palette="hls")
		ax.set_xlabel("Count")
		col1.pyplot(fig)

	show_bi5 = col2.checkbox("Show Top 10 Bigrams", key="NewsTab2")

	if show_bi5:
		
		top_bigrams = calculate_bigrams(news)
		
		col2.subheader("Top 10 Bigrams")
		fig, ax = plt.subplots(figsize=(8, 6))
		sns.barplot(y=[keyword[0][0] + " " + keyword[0][1] for keyword in top_bigrams], x=[keyword[1] for keyword in top_bigrams], ax=ax, orient='h', palette="hls")
		ax.set_xlabel("Count")
		col2.pyplot(fig)

