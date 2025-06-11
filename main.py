import streamlit as st
import folium
from streamlit_folium import st_folium

# 페이지 설정
st.set_page_config(page_title="스페인 여행 가이드", page_icon="🇪🇸", layout="wide")

# CSS 스타일 적용
st.markdown("""
    <style>
        .banner {
            position: relative;
            background-image: url("https://upload.wikimedia.org/wikipedia/commons/9/9e/Plaza_Mayor_de_Madrid_06.jpg");
            background-size: cover;
            height: 400px;
            color: white;
            text-align: center;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .banner h1 {
            font-size: 4em;
            text-shadow: 2px 2px 4px #000000;
        }
        .section-title {
            font-size: 32px;
            margin-top: 40px;
            color: #d62828;
        }
    </style>
""", unsafe_allow_html=True)

# 배너
st.markdown('<div class="banner"
