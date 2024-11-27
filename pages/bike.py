import streamlit as st
import pandas as pd
import time

if "ID" not in st.session_state:
    st.session_state["ID"] = "noname"
    
ID=st.session_state["ID"]
with st.sidebar:
    st.caption(f'{ID}님 접속중')

data = pd.read_csv("공공자전거.csv")
data = data.copy().fillna(0) #결측치제거 none값은 0으로 치환
data['total'] = 5*(data["LCD"]+data["QR"])+6

color = {'QR':'#37db91',
    'LCD':'#ebbb37'}

data['color']=data.copy()["운영방식"].map(color)

data
st.map(data,
       latitude="위도",
       longitude="경도",
       zoom=12,
       size = "total",
       color ="color")
       
