import streamlit as st
import os

# Data dependencies
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Extra Imports
from PIL import Image

#from Main_Page import raw

image = Image.open('WolfPackDown.jpg')
st.sidebar.image(image)

script_dir = os.path.dirname(__file__)
full_path = os.path.join(script_dir, '../resources/Training_Data.csv')

raw = pd.read_csv(full_path)

st.title(":books: Explore the Dataframe")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["All Data", "Anti", "Neutral", "Pro", "News"])

with tab1:
	st.subheader("All Sentiment Tweet Data")
	st.dataframe(raw[['sentiment', 'message']], width=1200, hide_index=True)
	st.table({"Number of Tweets" : len(raw), "Percentage of Dataset" : int((len(raw)/len(raw))*100)})
	
with tab2:
	st.subheader("Anti Sentiment Tweet Data")
	anti = raw[raw["sentiment"]==-1]
	st.dataframe(anti[['sentiment', 'message']], width=1200, hide_index=True)
	
with tab3:
	st.subheader("Neutral Sentiment Tweet Data")
	neutral = raw[raw["sentiment"]==0]
	st.dataframe(neutral[['sentiment', 'message']], width=1200, hide_index=True)
	
with tab4:
	st.subheader("Pro Sentiment Tweet Data")
	pro = raw[raw["sentiment"]==1]
	st.dataframe(pro[['sentiment', 'message']], width=1200, hide_index=True)
	
with tab5:
	st.subheader("All Sentiment Tweet Data")
	news = raw[raw["sentiment"]==2]
	st.dataframe(news[['sentiment', 'message']], width=1200, hide_index=True)




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
