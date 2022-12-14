import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sb
import streamlit as st 

def run_eda_app() :
    df = pd.read_csv('csv/Clean_Dataset.csv' ,index_col=0)
    
    st.subheader('데이터 프레임 확인')
    st.dataframe(df.head(3))
    st.subheader('비행시간,D-day,가격의 통계')
    st.dataframe(df.describe())
    
    column_list = df.columns[ 0 : 8 ]
    st.subheader('컬럼별 히스토리 차트')
    selected_columns = st.selectbox('확인할 컬럼을 선택하세요' ,column_list )
    
    fig1 = plt.figure()
    plt.hist(data=df , x=selected_columns , rwidth=0.8 ,bins=6 )
    st.pyplot(fig1)
    
    st.subheader('상관 관계 분석')
    column_list2 = df.columns[8 : ]
    selected_columns2 = st.multiselect('확인할 컬럼을 선택하세요' , column_list2)
    
    if len(selected_columns2) > 1 :
        df_corr = df[selected_columns2].corr()
        fig2 = plt.figure()
        sb.heatmap(data=df_corr , annot=True , fmt='.2f' , cmap='coolwarm' , vmin= -1 , vmax=1 , linewidths=0.5 )
        st.pyplot(fig2)