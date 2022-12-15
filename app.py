import streamlit as st 


from app_home import run_home_app
from app_eda import run_eda_app
from app_airplane_check import run_airplanecheck_app
from app_location import run_location_app
def main() :
    st.title('비행기 조회 , 가격 예측 앱 ')
    menu = ['Home' , 'EDA' , 'Ml' , '비행기 조회' , '공항 위치 조회' ]
    
    choice = st.sidebar.selectbox('메뉴' , menu)
    
    if choice == 'Home' :
        run_home_app()
    elif choice == 'EDA' :
        run_eda_app()
    elif choice == 'Ml' :
        pass
    elif choice == '비행기 조회' :
        run_airplanecheck_app()
    elif choice == '공항 위치 조회' :
        run_location_app()    


if __name__ == '__main__' :
    main()
