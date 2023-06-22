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

#st.set_page_config(page_title="Overview and Instructions")

st.markdown("# :question: Overview and Instructions")
#st.sidebar.markdown("# Overview and Instructions")

col1, col2, col3 = st.columns(3)

col1.markdown("## Overview")
col1.markdown("This streamlit application has been developed in conjunction with the construction of predictive machine learning models to provide an easy interface to make predictions as well as explore the data used to train the various models.")
st.markdown("#")
col3.info("Instructions", icon="ℹ️")
col3.markdown("Provide instructions for use of different features")