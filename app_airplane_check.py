import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sb
import streamlit as st 
import plotly.express as px 
import altair as alt


def run_airplanecheck_app() :
    df = pd.read_csv('csv/Clean_Dataset.csv' ,index_col=0)
    st.subheader('비행기를 조회 해드립니다.')
    
    st.image('https://img.jjang0u.com/data4/docs/160/202103/23/0c/a393bae8cbf605d1abf6fc8f02d62b38_921200.gif')
    
    departure = st.selectbox( '출발지를 선택하세요' ,df['airline'].unique())
    destination =st.selectbox( '목적지를 선택하세요' ,df['destination_city'].unique())
    seat = st.selectbox( '비행기의 좌석을 선택하세요' ,df['class'].unique())
    stopover = st.selectbox('경유 횟수를 선택하세요' ,['zero' , 'one' ,'two_or_more'])
    departure_time = st.selectbox('출발 시간을 정해주세요',df['departure_time'].unique() )
    arrival_time = st.selectbox
    df2 = (df.loc[ (df['airline'] == departure)&(df['destination_city']==destination)&(df['class']==seat)& (df['stops'] == stopover) &  (df['departure_time']==departure_time)  , ])
    st.dataframe(df2)
    airplane = df2.shape[0]
    st.text('선택하신 조건의 비행기수는 {}대 입니다.'.format(airplane))
    
    st.subheader('낮은 순으로 보기')
    selected_Criteria = st.selectbox('기준을 선택하세요' , ['price' , 'days_left' , 'duration'])             
    st.text('{} 순으로 정렬 하겠습니다.' .format(selected_Criteria))
    st.dataframe(df2.sort_values(selected_Criteria))
    
    st.subheader('높은 순으로 보기')            
    st.text('{} 순으로 정렬 하겠습니다.' .format(selected_Criteria))
    st.dataframe(df2.sort_values(selected_Criteria , ascending=False))
    
    column_menu = df.columns[-3 : ]
    choice_list = st.multiselect('보고싶은 관계를 고르세요' , column_menu)
    if len(choice_list) != 0 :
        df_selected = df[choice_list]
        st.line_chart(df_selected)
        
    
    
    df2 = df.groupby('destination_city')['destination_city'].count()
    fig6 = px.pie(df2,df2.index , df2.values ,title= '출발지별 나라 비율')
    st.plotly_chart(fig6)   