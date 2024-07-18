import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
st.title('Credit Card Fraud Detection ')


@st.cache
def load_data(nrows):
    data = pd.read_csv('fraudTrain.csv', nrows=nrows)
    return data


weekly_data = load_data(15)

st.subheader('DataSet')

with st.sidebar.header('1. Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.markdown('**1.1. Glimpse of dataset**')
    st.write(df)

else:
    st.info('Awaiting for CSV file to be uploaded.')
    if st.button('Press to use Example Dataset'):
        st.write(weekly_data)

if st.sidebar.checkbox("Show data description"):
    st.subheader('Data Description')
    st.write(weekly_data.describe())

if st.sidebar.checkbox("Select columns"):
    selected = st.selectbox("Select Columns", weekly_data.columns.to_list())
    new_df = weekly_data[selected]

    selected2 = st.selectbox("Select Column", weekly_data.columns.to_list())
    new_df2 = weekly_data[selected2]

    bar_chart = px.bar(weekly_data, x=new_df, y=new_df2, color_discrete_sequence=['#F63366'] * len(weekly_data),
                       template='plotly_white')
    st.plotly_chart(bar_chart)

    line_chart = px.line(weekly_data, x=new_df, y=new_df2, color_discrete_sequence=['#F63366'] * len(weekly_data),
                         template='plotly_white')
    st.plotly_chart(line_chart)

image = Image.open("OIP (3).jfif")
ph = st.sidebar.image(image)