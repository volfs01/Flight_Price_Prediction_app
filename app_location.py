import streamlit as st 
import pandas as pd

def run_location_app() :
    st.subheader('출발 공항 위치를 알려드릴게요')
    
    df = pd.read_csv('csv/location1.csv')
        
    st.dataframe(df.head(3))
        
    st.map(df,zoom=10) 