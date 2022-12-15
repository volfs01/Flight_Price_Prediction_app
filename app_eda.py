import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sb
import streamlit as st 
import plotly.express as px 

def run_eda_app() :
    df = pd.read_csv('csv/Clean_Dataset.csv' ,index_col=0)
    
    st.subheader('데이터 프레임 확인')
    st.dataframe(df.head(3))
    st.subheader('비행시간,D-day,가격의 통계')
    st.dataframe(df.describe())
    
    column_list = df.columns[[0,2,3,4,5,6,7,8,9,10]]
    st.subheader('컬럼별 히스토리 차트')
    selected_columns = st.selectbox('확인할 컬럼을 선택하세요' ,column_list )
    
    fig1 = plt.figure()
    plt.hist(data=df , x=selected_columns , rwidth=0.8 ,bins=6 )
    st.pyplot(fig1)
    
    
    st.subheader('상관 관계 분석')
    column_list2 = df.columns[[0,2,3,4,5,6,7,8,9,10]]
    selected_columns2 = st.multiselect('확인할 컬럼을 선택하세요' , column_list2)
    
    if len(selected_columns2) > 1 :
        df_corr = df[selected_columns2].corr()
        fig2 = plt.figure()
        sb.heatmap(data=df_corr , annot=True , fmt='.2f' , cmap='coolwarm' , vmin= -1 , vmax=1 , linewidths=0.5 )
        st.pyplot(fig2)
        
        
    df2 = pd.read_csv('csv/df2.csv')
    fig6 = px.pie(df2,'lang' , 'sun' ,title= '출발지별 나라 비율')
    st.plotly_chart(fig6) 
    
    st.dataframe(df2.head(2))  