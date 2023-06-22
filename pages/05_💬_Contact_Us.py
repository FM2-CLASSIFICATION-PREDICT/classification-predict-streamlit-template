import streamlit as st
#import joblib, os

# Data dependencies
#import pandas as pd
#import seaborn as sns
#import matplotlib.pyplot as plt

#from sklearn import metrics

# Extra Imports
#from PIL import Image
#import plotly.express as px

st.markdown("# :wolf: Contact Us")
#st.sidebar.markdown("# Contributors")

st.markdown("## Wolf Pack Team")

team_list = ["Sias Willemse", "Chesley Rogerson", "Thato Molapisi", "Thabiso Khoza", "Thebe Dikobo", "Boitumelo Mphahlele"]
roles = ["Team Lead", "Data Engineer", "Data Scientist", "Data Scientist", "Domain Expert", "Communications Expert"]

#count = 0

for member in team_list:

	st.markdown(member)#, " ", roles[count])
	#count += 1