import streamlit as st
import os

# Data dependencies
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Extra Imports
from PIL import Image

from collections import Counter
from nltk import ngrams
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import seaborn as sns

#from Main_Page import raw

image = Image.open('WolfPackDown.jpg')
st.sidebar.image(image)

script_dir = os.path.dirname(__file__)
full_path = os.path.join(script_dir, '../resources/Training_Data.csv')

raw = pd.read_csv(full_path)

#def calculate_top_keywords(filtered_df):
#
#	combined_text = " ".join(filtered_df["message"])

	# Tokenize the text into individual words
#	tokens = word_tokenize(combined_text)

	# Remove stopwords
#	stop_words = set(stopwords.words("english"))
#	word_exclude = ["https", "rt", "amp"]#, "U", "Â", "â", "Ã", "ã"]"t", "co"
#	for word in word_exclude:
#		stop_words.add(word)
	
#	filtered_tokens = [token.lower() for token in tokens if token.lower() not in stop_words and token.isalnum()]

	# Generate unigrams and bigrams
#	unigrams = Counter(filtered_tokens)
#	bigrams = Counter(ngrams(filtered_tokens, 2))

	# Get the top 10 unigrams and bigrams
#	top_unigrams = unigrams.most_common(10)
#	top_bigrams = bigrams.most_common(10)

#	top_bigrams_formatted = [(f"{bigram[0][0]} {bigram[0][1]}", bigram[1]) for bigram in top_bigrams]

#	return top_unigrams, top_bigrams_formatted

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

	# Generate unigrams and bigrams
	unigrams = Counter(filtered_tokens)
	#bigrams = Counter(ngrams(filtered_tokens, 2))

	# Get the top 10 unigrams and bigrams
	top_unigrams = unigrams.most_common(10)
	#top_bigrams = bigrams.most_common(10)

	#top_bigrams_formatted = [(f"{bigram[0][0]} {bigram[0][1]}", bigram[1]) for bigram in top_bigrams]

	return top_unigrams #, top_bigrams_formatted

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

	# Generate unigrams and bigrams
	#unigrams = Counter(filtered_tokens)
	bigrams = Counter(ngrams(filtered_tokens, 2))

	# Get the top 10 unigrams and bigrams
	#top_unigrams = unigrams.most_common(10)
	top_bigrams = bigrams.most_common(10)

	#top_bigrams_formatted = [(f"{bigram[0][0]} {bigram[0][1]}", bigram[1]) for bigram in top_bigrams]

	return top_bigrams #top_unigrams, top_bigrams_formatted


st.title(":books: Explore the Dataframe")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["All Data", "Anti", "Neutral", "Pro", "News"])

with tab1:
	
	st.subheader("All Sentiment Tweet Data")
	st.dataframe(raw[['sentiment', 'message']], width=1560, hide_index=True)

	#col1.table({"Number of Tweets" : len(raw), "Percentage of Dataset" : int((len(raw)/len(raw))*100)})

	#col2.header("Top Unigrams")
	#for unigram, count in top_unigrams:
	#	col2.write(f"{unigram}: {count}")

	#col2.header("Top Bigrams")
	#for bigram, count in top_bigrams:
	#	col2.write(f"{' '.join(bigram)}: {count}")

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


	#top_unigrams, top_bigrams = calculate_top_keywords(raw)

	#show_uni = col1.checkbox("Show Top 10 Unigrams", key="AllTab1")

	#if show_uni:
	#	col1.subheader("Top 10 Unigrams")
	#	fig, ax = plt.subplots(figsize=(8, 6))
	#	sns.barplot(y=[keyword[0] for keyword in top_unigrams], x=[keyword[1] for keyword in top_unigrams], ax=ax, orient='h', palette="hls")
	#	ax.set_xlabel("Count")
	#	#plt.xticks(rotation=45)
	#	col1.pyplot(fig)

	#show_bi = col2.checkbox("Show Top 10 Bigrams", key="AllTab2")

	#if show_bi:
	#	col2.subheader("Top 10 Bigrams")
	#	fig, ax = plt.subplots(figsize=(8, 6))
	#	sns.barplot(y=[keyword[0] for keyword in top_bigrams], x=[keyword[1] for keyword in top_bigrams], ax=ax, orient='h', palette="hls")
	#	ax.set_xlabel("Count")
	#	#plt.xticks(rotation=45)
	#	col2.pyplot(fig)
	
with tab2:
	
	st.subheader("Anti Sentiment Tweet Data")
	anti = raw[raw["sentiment"]==-1]
	st.dataframe(anti[['sentiment', 'message']], width=1560, hide_index=True)

	col1, col2 = st.columns(2)

	#top_unigrams, top_bigrams = calculate_top_keywords(raw)

	show_uni2 = col1.checkbox("Show Top 10 Unigrams", key="AntiTab1")

	if show_uni2:
		
		top_unigrams = calculate_unigrams(anti)

		col1.subheader("Top 10 Unigrams")
		fig, ax = plt.subplots(figsize=(8, 6))
		sns.barplot(y=[keyword[0] for keyword in top_unigrams], x=[keyword[1] for keyword in top_unigrams], ax=ax, orient='h', palette="hls")
		ax.set_xlabel("Count")
		#plt.xticks(rotation=45)
		col1.pyplot(fig)

	show_bi2 = col2.checkbox("Show Top 10 Bigrams", key="AntiTab2")

	if show_bi2:
		
		top_bigrams = calculate_bigrams(anti)
		
		col2.subheader("Top 10 Bigrams")
		fig, ax = plt.subplots(figsize=(8, 6))
		#sns.barplot(y=[keyword[0] for keyword in top_bigrams], x=[keyword[1] for keyword in top_bigrams], ax=ax, orient='h', palette="hls")
		sns.barplot(y=[keyword[0][0] + " " + keyword[0][1] for keyword in top_bigrams], x=[keyword[1] for keyword in top_bigrams], ax=ax, orient='h', palette="hls")
		ax.set_xlabel("Count")
		#plt.xticks(rotation=45)
		col2.pyplot(fig)
	
with tab3:
	st.subheader("Neutral Sentiment Tweet Data")
	neutral = raw[raw["sentiment"]==0]
	st.dataframe(neutral[['sentiment', 'message']], width=1560, hide_index=True)

	#top_unigrams, top_bigrams = calculate_top_keywords(neutral)

	#st.header("Top Unigrams")
	#for unigram, count in top_unigrams:
	#	st.write(f"{unigram}: {count}")

	#st.header("Top Bigrams")
	#for bigram, count in top_bigrams:
	#	st.write(f"{' '.join(bigram)}: {count}")
	
with tab4:
	st.subheader("Pro Sentiment Tweet Data")
	pro = raw[raw["sentiment"]==1]
	st.dataframe(pro[['sentiment', 'message']], width=1560, hide_index=True)

	#top_unigrams, top_bigrams = calculate_top_keywords(pro)

	#st.header("Top Unigrams")
	#for unigram, count in top_unigrams:
	#	st.write(f"{unigram}: {count}")

	#st.header("Top Bigrams")
	#for bigram, count in top_bigrams:
	#	st.write(f"{' '.join(bigram)}: {count}")
	
with tab5:
	st.subheader("All Sentiment Tweet Data")
	news = raw[raw["sentiment"]==2]
	st.dataframe(news[['sentiment', 'message']], width=1560, hide_index=True)

	#top_unigrams, top_bigrams = calculate_top_keywords(news)

	#st.header("Top Unigrams")
	#for unigram, count in top_unigrams:
	#	st.write(f"{unigram}: {count}")

	#st.header("Top Bigrams")
	#for bigram, count in top_bigrams:
	#	st.write(f"{' '.join(bigram)}: {count}")


#graph_selection = st.selectbox("Select a Sentiment", ["All", "-1", "0", "1", "2"])

#if graph_selection == "All":

	#st.markdown("## All Tweets")

#	st.info("All Tweets")

#	st.write(raw[['sentiment', 'message']])

#	st.table({"Number of Tweets" : len(raw), "Percentage of Dataset" : int((len(raw)/len(raw))*100)})

#if graph_selection == "-1":

#	st.info("Anti Climate Change Tweets")

#	anti = raw[raw["sentiment"]==-1]

#	st.write(anti[["sentiment", "message"]])

#	st.table({"Number of Tweets" : len(anti), "Percentage of Dataset" : int((len(anti)/len(raw))*100)})

#if graph_selection == "0":
			
#	st.info("Neutral to Climate Change Tweets")

#	neut = raw[raw["sentiment"]==0]

#	st.write(neut[["sentiment", "message"]])

#	st.table({"Number of Tweets" : int(len(neut)), "Percentage of Dataset" : int((len(neut)/len(raw))*100)})

#if graph_selection == "1":
			
#	st.info("Pro Climate Change Tweets")
			
#	pro = raw[raw["sentiment"]==1]

#	st.write(pro[["sentiment", "message"]])

#	st.table({"Number of Tweets" : len(pro), "Percentage of Dataset" : int((len(pro)/len(raw))*100)})

#if graph_selection == "2":
			
#	st.info("News Climate Change Tweets")
			
#	news = raw[raw["sentiment"]==2]

#	st.write(news[["sentiment", "message"]])

#	st.table({"Number of Tweets" : len(news), "Percentage of Dataset" : int((len(news)/len(raw))*100)})
