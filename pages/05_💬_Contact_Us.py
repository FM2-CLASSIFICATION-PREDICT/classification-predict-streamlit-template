import streamlit as st

# Extra Imports
from PIL import Image

image = Image.open('WolfPackDown.jpg')
st.sidebar.image(image)

st.title(":speech_balloon: Contact Us")

col1, col2 = st.columns(2)

col1.subheader("Team Lead")
col1.markdown("Sias Willemse - siaswillemse14@gmail.com")

col1.subheader("Lead Data Engineer")
col1.markdown("Chesley Rogerson - ckrogerson@gmail.com")

col1.subheader("Lead Data Scientist")
col1.markdown("Thato Molapisi - tee.molapisi@gmail.com")

col1.subheader("Data Scientist")
col1.markdown("Thabiso Khoza - thabisogcwabaza@icloud.com")

col1.subheader("Domain Expert")
col1.markdown("Thebe Dikobo - tumelokethebe.d@gmail.com")

col1.subheader("Communications Expert")
col1.markdown("Boitumelo Mphahlele - teeboitumelo@gmail.com")

col2.subheader("In Colloboration with:")
col2.markdown("##")

logo_paths = ["AWS.png", "Comet.JPG", "python.jpg", "streamlit.png"]

logo_width = 100

# Create columns within col2 for the logos
columns = col2.columns(len(logo_paths))

# Display each logo in a column within the collage
for i, logo_path in enumerate(logo_paths):
    with columns[i]:
        st.image(logo_path, width=logo_width)