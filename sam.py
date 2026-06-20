import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


#1. Dataset load karna
# 2. Missing values identify karna aur report banana
# 3. Duplicate records identify karna
# 4. Data types validation
# 5. Content Distribution Analysis (Movie vs TV Show)
# 6. Release Year Trends Analysis
# 7. Rating Distribution Analysis
# 8. Pie Chart (Content Type)
# 9. Line Chart (Release Year Trends)
# 10. Histogram (Duration Distribution)
# 11. Box Plot (Ratings Distribution)

st.set_page_config(page_title="Netflix Content Analytics", page_icon="C:\\Users\\DELL\\Downloads\\netflix.png", layout="wide")
st.markdown("<h1 style='text-align:center; color: #60A5FA;'>Netflix Content Analytics Portal</h1>",unsafe_allow_html=True,)
st.markdown("<p style='text-align:center; color: #FACC15;'>Advanced Trends Detection, Content Correlation Study, and Movies/Show Insights</p>",unsafe_allow_html=True,)
st.markdown("---")

uploaded_file = st.file_uploader("Please Upload CSV File",type=["CSV"])
if uploaded_file:
    df=pd.read_csv(uploaded_file)
    st.write(df.isnull().sum())
    st.write("total duplicated raws:",df.duplicated().sum())
    st.write(df[df.duplicated()])
    st.write(df.dtypes)
