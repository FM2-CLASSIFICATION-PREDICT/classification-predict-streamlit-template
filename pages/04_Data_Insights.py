import streamlit as st
#import joblib, os
import os

# Data dependencies
import pandas as pd
#import seaborn as sns
import matplotlib.pyplot as plt

#from sklearn import metrics

# Extra Imports
#from PIL import Image
#import plotly.express as px

#from Main_Page import raw

script_dir = os.path.dirname(__file__)
full_path = os.path.join(script_dir, '../resources/Training_Data.csv')

raw = pd.read_csv(full_path)

#st.set_page_config(layout="wide")

st.markdown("# Data Insights")
#st.sidebar.markdown("# Data Insights")

col1, col2 = st.columns((1, 2))

col1.subheader("Count of given search term  in each sentiment")

fig = plt.figure(figsize=(10, 4))

search_term = col1.text_input("Enter a search term:")
include_rt = col1.checkbox("Include Retweets")

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
		
		col1.markdown("### Sentiment Distribution based on Search Term")

		sentiment_counts = filtered_df['sentiment'].value_counts()

		class_dict = {-1 : "Anti", 0 : "Neutral", 1 : "Pro", 2 : "News"}

		label_list = []

		for val in sentiment_counts.index:

			label_list.append(class_dict[val])

		plt.style.use('default')
		fig, ax = plt.subplots(figsize=(8, 8))
		plt.style.use('default')
		#colors = ['#81cad6','#ff8379', '#3ea055', '#c093ea']
		colors = ['#3ea055','#c093ea', '#81cad6', '#ff8379']
		ax.pie(sentiment_counts, labels=label_list, autopct='%2.1f%%', startangle=90, colors=colors, pctdistance=1.09, labeldistance=None)
		ax.legend()
		
		#ax.set_title("Sentiment Distribution based on Search Term")
		
		ax.axis('equal')
		#col1.subheader("Count of Sentiments")
		col1.pyplot(fig)
		col2.dataframe(filtered_df[['sentiment', 'message']])

st.markdown("Some information here")

st.markdown("-1 : Anti")
st.markdown("0 : Neutral")
st.markdown("1 : Pro")
st.markdown("2 : News")