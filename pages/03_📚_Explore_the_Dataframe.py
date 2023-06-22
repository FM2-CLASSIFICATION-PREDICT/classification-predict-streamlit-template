import streamlit as st
#import joblib, os
import os

# Data dependencies
import numpy as np
import pandas as pd
#import seaborn as sns
import matplotlib.pyplot as plt

#from sklearn import metrics

# Extra Imports
from PIL import Image
#from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

#import plotly.express as px

#from Main_Page import raw

image = Image.open('WolfPackDown.jpg')
st.sidebar.image(image)

script_dir = os.path.dirname(__file__)
full_path = os.path.join(script_dir, '../resources/Training_Data.csv')

raw = pd.read_csv(full_path)

#st.set_page_config(layout="wide")

st.title(":books: Explore the Dataframe")
#st.sidebar.markdown("# Explore the Dataframe")

#st.subheader("Raw Training Data")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["All Data", "Anti", "Neutral", "Pro", "News"])

with tab1:
	#col1, col2 = st.columns(2)
	#with col1:
	st.header("All Sentiment Tweet Data")
	st.dataframe(raw[['sentiment', 'message']], width=1200, hide_index=True)
	#with col2:
		# Generate a word cloud image
		
		#raw['message'] = raw['message'].str.lower()

		#stopwords = STOPWORDS

		#wordcloud_exclude = ["Climate", "Change", "change" "Global", "Warming", "https", "t", "co", "rt", "amp", "U", "Â", "â", "Ã", "ã"]

		#for word in wordcloud_exclude:
		#	stopwords.add(word)

		#stopwords = set(stopwords)
		#mask = np.array(Image.open("twitter_mask.png"))
		#wordcloud = WordCloud(stopwords=stopwords, background_color="white", max_words=100, mask=mask).generate(' '.join(raw['message']))
		#wordcloud = wordcloud[wordcloud.str.len() <= 2]
		# create twitter image
		#image_colors = ImageColorGenerator(mask)
		#fig = plt.figure()
		#plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
		#plt.imshow(wordcloud, interpolation="bilinear")
		#plt.axis("off")
		# store to file
		#plt.savefig("twitter.png", format="png")
		#plt.show()
		#st.pyplot(fig)
	
	
with tab2:
	#col1, col2 = st.columns(2)
	#with col1:
	st.header("Anti Sentiment Tweet Data")
	anti = raw[raw["sentiment"]==-1]
	st.dataframe(anti[['sentiment', 'message']], width=1200, hide_index=True)
	#with col2:
		# Generate a word cloud image
		#stopwords = set(STOPWORDS)
		#mask = np.array(Image.open("twitter_mask.png"))
		#wordcloud = WordCloud(stopwords=stopwords, background_color="white", max_words=100, mask=mask).generate(' '.join(anti['message']))
		# create twitter image
		#fig = plt.figure()
		#plt.imshow(wordcloud, interpolation="bilinear")
		#plt.axis("off")
		# store to file
		#plt.savefig("twitter.png", format="png")
		#plt.show()
		#st.pyplot(fig)

	#col1.header("Anti Sentiment Tweet Data")
	#anti = raw[raw["sentiment"]==-1]
	#col1.write(anti[["sentiment", "message"]])
	
with tab3:
	#col1, col2 = st.columns(2)
	#with col1:
	st.header("Neutral Sentiment Tweet Data")
	neutral = raw[raw["sentiment"]==0]
	st.dataframe(neutral[['sentiment', 'message']], width=1200, hide_index=True)
	#with col2:
		# Generate a word cloud image
		#stopwords = set(STOPWORDS)
		#mask = np.array(Image.open("twitter_mask.png"))
		#wordcloud = WordCloud(stopwords=stopwords, background_color="white", max_words=100, mask=mask).generate(' '.join(neutral['message']))
		# create twitter image
		#fig = plt.figure()
		#plt.imshow(wordcloud, interpolation="bilinear")
		#plt.axis("off")
		# store to file
		#plt.savefig("twitter.png", format="png")
		#plt.show()
		#st.pyplot(fig)

	#col1.header("Neutral Sentiment Tweet Data")
	#neutral = raw[raw["sentiment"]==0]
	#col1.write(neutral[["sentiment", "message"]])
	
with tab4:
	#col1, col2 = st.columns(2)
	#with col1:
	st.header("Pro Sentiment Tweet Data")
	pro = raw[raw["sentiment"]==1]
	st.dataframe(pro[['sentiment', 'message']], width=1200, hide_index=True)
	#with col2:

		# Generate a word cloud image
		#stopwords = set(STOPWORDS)
		#mask = np.array(Image.open("twitter_mask.png"))
		#wordcloud = WordCloud(stopwords=stopwords, background_color="white", max_words=100, mask=mask).generate(' '.join(pro['message']))
		# create twitter image
		#fig = plt.figure()
		#plt.imshow(wordcloud, interpolation="bilinear")
		#plt.axis("off")
		# store to file
		#plt.savefig("twitter.png", format="png")
		#plt.show()
		#st.pyplot(fig)

	#col1.header("Pro Sentiment Tweet Data")
	#pro = raw[raw["sentiment"]==1]
	#col1.write(pro[["sentiment", "message"]])
	
with tab5:
	#col1, col2 = st.columns(2)
	#with col1:
	st.header("All Sentiment Tweet Data")
	news = raw[raw["sentiment"]==2]
	st.dataframe(news[['sentiment', 'message']], width=1200, hide_index=True)
	#with col2:
		# Generate a word cloud image
		#stopwords = set(STOPWORDS)
		#mask = np.array(Image.open("twitter_mask.png"))
		#wordcloud = WordCloud(stopwords=stopwords, background_color="white", max_words=100, mask=mask).generate(' '.join(news['message']))
		# create twitter image
		#fig = plt.figure()
		#plt.imshow(wordcloud, interpolation="bilinear")
		#plt.axis("off")
		# store to file
		#plt.savefig("twitter.png", format="png")
		#plt.show()
		#st.pyplot(fig)

	#col1.header("News Sentiment Tweet Data")
	#news = raw[raw["sentiment"]==2]
	#col1.write(news[["sentiment", "message"]])




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
