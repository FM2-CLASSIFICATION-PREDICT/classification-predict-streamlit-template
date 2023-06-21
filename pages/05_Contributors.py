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

st.markdown("# Contributors")
#st.sidebar.markdown("# Contributors")

st.info("Wolf Pack Team")

team_list = ["Sias Willemse", "Chesley Rogerson", "Thato Molapisi", "Thabiso Khoza", "Thebe Dikobo", "Boitumelo Mphahlele"]
		
for member in team_list:

	st.markdown(member)