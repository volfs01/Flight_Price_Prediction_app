import streamlit as st 
import pandas as pd

def run_location_app() :
    st.subheader('공항 위치를 알려드릴게요')
    st.image('https://techmarket.airport.kr:6943/portal/img/01.jpg')
    df = pd.read_csv('csv/location1.csv' , index_col=0)
        
    st.dataframe(df.head(3))
        
    st.map(df,zoom=500) 