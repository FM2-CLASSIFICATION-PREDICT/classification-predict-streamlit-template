import streamlit as st
#import joblib, os
import os

# Data dependencies
import numpy as np
import pandas as pd
#import seaborn as sns
import matplotlib.pyplot as plt

from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

#from sklearn import metrics

# Extra Imports
from PIL import Image
#import plotly.express as px

#from Main_Page import raw

image = Image.open('WolfPackDown.jpg')
st.sidebar.image(image)

script_dir = os.path.dirname(__file__)
full_path = os.path.join(script_dir, '../resources/Training_Data.csv')

raw = pd.read_csv(full_path)

st.title(":chart_with_upwards_trend: Data Insights")
#st.sidebar.markdown("# Data Insights")

col1, col2 = st.columns((1, 1))

col1.subheader("Tweet Term Search")

fig = plt.figure(figsize=(10, 4))

search_term = col1.text_input("Enter a search term:")
include_rt = col1.checkbox("Include Retweets")

if col1.button("Search"):

	if include_rt:
		filtered_df = raw[raw['message'].str.contains(search_term, case=False) & raw['message'].str.contains("RT")]
	else:
		filtered_df = raw[raw['message'].str.contains(search_term, case=False)]
	
	if search_term:
	
		filtered_df = raw[raw['message'].str.contains(search_term, case=False)]
	
		if filtered_df.empty:
			col2.subheader("Search Result")
			col2.markdown("No result for the given search term")
		
		else:
		
			col1.subheader("Sentiment Distribution based on Search Term")

			sentiment_counts = filtered_df['sentiment'].value_counts()

			class_dict = {-1 : "Anti", 0 : "Neutral", 1 : "Pro", 2 : "News"}

			label_list = []

			for val in sentiment_counts.index:

				label_list.append(class_dict[val])

			# Pie Chart

			plt.style.use('default')
			fig, ax = plt.subplots(figsize=(7, 7))
			plt.style.use('default')
			#colors = ['#3ea055','#c093ea', '#81cad6', '#ff8379']

			#color_map = {'1': 'red', '2': 'orange', '3': 'green', '4': 'purple'}
			color_map = {'1': 'green', '2': 'purple', '3': 'orange', '4': 'red'}


			ax.pie(sentiment_counts, labels=label_list, autopct='%2.1f%%', startangle=90, colors=color_map.values(), pctdistance=1.09, labeldistance=None)
			ax.legend()
		
			ax.axis('equal')
			col1.pyplot(fig)
			#col1.dataframe(filtered_df[['sentiment', 'message']])

			# Word Cloud
			col2.markdown("#")
			col2.markdown("#")
			col2.markdown("#")
			col2.markdown("##")
			col2.markdown("##")
			col2.markdown("##")
			col2.markdown("##")
			col2.subheader("Wordcloud of Related Terms")

			stopwords = STOPWORDS

			wordcloud_exclude = ["Climate", "Change", "change" "Global", "Warming", "https", "t", "co", "rt", "amp", "U", "Â", "â", "Ã", "ã"]

			for word in wordcloud_exclude:
				stopwords.add(word)

			stopwords = set(stopwords)
			mask = np.array(Image.open("twitter_mask.png"))
			wordcloud = WordCloud(stopwords=stopwords, background_color="white", max_words=100, mask=mask).generate(' '.join(filtered_df['message']))
			#wordcloud = wordcloud[wordcloud.str.len() <= 2]
			# create twitter image
			#image_colors = ImageColorGenerator(mask)
			fig = plt.figure()
			#plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
			plt.imshow(wordcloud, interpolation="bilinear")
			plt.axis("off")
			# store to file
			#plt.savefig("twitter.png", format="png")
			#plt.show()
			col2.pyplot(fig)