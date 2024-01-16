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
    sex_list = ["男性", "女性"]
    with st.container():
        st.write("**性別**")
        sex = st.selectbox("", sex_list)
with col4:
    with st.container():
        st.write("**身長**")
        height = st.text_input("","", key="height")
st.markdown("---")
col5, col6, col7, col8 = st.columns(4)
with col5:
    with st.container():
        st.write("**体重**")
        weight = st.text_input("","", key="weight")
with col6:
    ht_list = ["あり", "なし"]
    with st.container():
        st.write("**高血圧**")
        ht = st.selectbox("", ht_list, key="ht")
with col7:
    apnea_list = ["あり", "なし", "不明"]
    with st.container():
        st.write("**家族からの無呼吸の指摘**")
        apnea = st.selectbox("", apnea_list, key="apnea")
with col8:
    snore_list = ["あり", "なし", "不明"]
    with st.container():
        st.write("**家族からのいびきの指摘**")
        snore = st.selectbox("", snore_list, key="snore")

st.markdown("---")
st.write("以下は左右少なくとも1眼は全ての値を入力してください")
col9, col10, col11, col12 = st.columns(4)
with col9:
    with st.container():
        st.write("**眼軸長**")
        al_r = st.text_input("右", "", key="al_r")
        al_l = st.text_input("左", "", key="al_l")
    with st.container():
        st.write("**レフ値**")
        st.write("右")
        ref_r1, ref_r2 = st.columns(2)
        with ref_r1:
            ref_r_s = st.text_input("S", "", key="reg_r_s")
        with ref_r2:
            ref_r_c = st.text_input("C", "", key="reg_r_c")
        st.write("左")
        ref_l1, ref_l2 = st.columns(2)
        with ref_l1:
            ref_l_s = st.text_input("S", "", key="ref_l_s")
        with ref_l2:
            ref_l_c = st.text_input("C", "", key="ref_l_c")
with col10:
    eye_drops_list = [0,1,2,3,4,5,6]
    with st.container():
        st.write("**点眼薬の成分数**")
        eye_drops_list_r = st.selectbox("右", eye_drops_list, key="eye_drops_list_r")
        eye_drops_list_l = st.selectbox("右", eye_drops_list, key="eye_drops_list_l")
with col11:
    st.write("**中心下方TD値**")
    st.write("右")
    td_col_r1, td_col_r2, td_col_r3 = st.columns(3)
    with td_col_r1:
        td_r1 = st.text_input("","",key="td_r1")
    with td_col_r2:
        td_r2 = st.text_input("","",key="td_r2")
    with td_col_r3:
        td_r3 = st.text_input("","",key="td_r3")
    st.write("TD値については下記赤枠内をご記入ください")
    img = Image.open("./images/td_description_r.png")
    st.image(img)
with col12:
    st.write("**中心下方TD値**")
    st.write("左")
    td_col_l1, td_col_l2, td_col_l3 = st.columns(3)
    with td_col_l1:
        td_l1 = st.text_input("","",key="td_l1")
    with td_col_l2:
        td_l2 = st.text_input("","",key="td_l2")
    with td_col_l3:
        td_l3 = st.text_input("","",key="td_l3")
    st.write("TD値については下記赤枠内をご記入ください")
    #img = Image.open("./images/td_description_l.png")
    st.image("./images/td_description_l.png")
st.markdown("---")
if st.button("予測"):
    print("tapped")
