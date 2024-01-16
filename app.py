import streamlit as st
from PIL import Image
import const, utility

st.set_page_config(**const.SET_PAGE_CONFIG)

st.title("ODI SAS 予測プログラム")
st.markdown("---")
col1, col2, col3, col4 = st.columns(4)
with col1:
    diag_list = ["POAG(HTG)", "NTG", "PACG", "OAG", "PE", "Steroid", "uveitis", "PPG", "その他・不明", "normal"]
    with st.container():
        st.write("**診断名**")
        diag_r = st.selectbox("右", diag_list)
        diag_l = st.selectbox("左", diag_list)
with col2:
    with st.container():
        st.write("**年齢**")
        age = st.text_input("","", key="age")
with col3:
    sex = ["男性", "女性"]
    with st.container():
        st.write("**性別**")
        sex = st.selectbox("", sex)
with col4:
    with st.container():
        st.write("**身長**")
        height = st.text_input("","", key="height")
