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
            background-image: url("https://a.travel-assets.com/findyours-php/viewfinder/images/res70/348000/348698-Madrid.jpg");
            background-position: center -60px;
            background-size: cover;
            height: 600px;
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
st.markdown('<div class="banner"><h1>🇪🇸 스페인 여행 가이드</h1></div>', unsafe_allow_html=True)

# 섹션 1: 스페인 소개
st.markdown('<h2 class="section-title">🇪🇸 스페인은 어떤 나라일까요?</h2>', unsafe_allow_html=True)
st.markdown("""
스페인은 남유럽의 아름다운 나라로, 다양한 문화와 역사, 음식, 해변, 건축물이 조화를 이루고 있어요.  
고대 로마 유적, 이슬람 문화, 가우디의 독창적인 건축물까지, 매 도시마다 색다른 매력을 느낄 수 있습니다.  
- 수도: **마드리드**
- 사용 언어: **스페인어**
- 통화: **유로 (€)**  
- 여행하기 좋은 시기: **4~6월, 9~10월**
""")

# 도시 정보
destinations = {
    "바르셀로나": {
        "location": [41.3851, 2.1734],
        "description": "🎨 가우디의 도시! 사그라다 파밀리아, 구엘 공원, 해변, 쇼핑까지 다양하게 즐길 수 있어요.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/e/ef/Sagrada_Familia_01.jpg"
    },
    "마드리드": {
        "location": [40.4168, -3.7038],
        "description": "🎭 스페인의 수도! 왕궁, 프라도 미술관, 활기찬 도심과 음식의 천국.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/9/9e/Palacio_Real_de_Madrid.jpg"
    },
    "세비야": {
        "location": [37.3891, -5.9845],
        "description": "💃 안달루시아의 열정! 플라멩코, 스페인 광장, 이슬람 건축의 향기.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/6/6d/Plaza_de_España_Sevilla_01.jpg"
    },
    "그라나다": {
        "location": [37.1773, -3.5986],
        "description": "🏯 알함브라 궁전이 있는 신비로운 도시, 산과 함께하는 중세의 느낌.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/5/57/Alhambra_Granada_Andalucia_Spain.jpg"
    },
    "산 세바스티안": {
        "location": [43.3183, -1.9812],
        "description": "🍽️ 미식 천국! 아름다운 바닷가와 고급 타파스 레스토랑으로 유명해요.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/6/66/San_Sebastian_-_La_Concha_Bay.jpg"
    },
}

# 섹션 2: 지도
st.markdown('<h2 class="section-title">🗺️ 주요 도시 지도</h2>', unsafe_allow_html=True)

m = folium.Map(location=[40.0, -3.7], zoom_start=6, tiles="cartodb positron")

for city, data in destinations.items():
    folium.Marker(
        location=data["location"],
        tooltip=city,
        popup=f"<b>{city}</b><br>{data['description']}",
        icon=folium.Icon(color="orange", icon="info-sign")
    ).add_to(m)

st_data = st_folium(m, width=1000, height=500)

# 섹션 3: 도시 상세 정보
if st_data and st_data.get("last_object_clicked_tooltip"):
    selected = st_data["last_object_clicked_tooltip"]
    info = destinations[selected]

    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(info["image"], use_column_width=True)
    with col2:
        st.markdown(f"### 📍 {selected}")
        st.markdown(info["description"])
else:
    st.info("지도의 마커를 클릭해 여행지 정보를 확인해 보세요!")

# 섹션 4: 추천 여행 일정
st.markdown('<h2 class="section-title">📆 추천 여행 일정</h2>', unsafe_allow_html=True)
st.markdown("""
**5일 추천 루트**  
- Day 1: 마드리드 도착 – 왕궁 & 그란비아 거리 산책  
- Day 2: 마드리드 – 프라도 미술관 → 세비야로 이동  
- Day 3: 세비야 관광 – 스페인 광장, 알카사르  
- Day 4: 그라나다 – 알함브라 궁전  
- Day 5: 바르셀로나 – 사그라다 파밀리아, 고딕 지구  

**맛집 & 특산물**  
- 바르셀로나: 해산물 빠에야  
- 세비야: 살모레호(토마토 스프)  
- 마드리드: 츄로스 & 핫초콜릿  
- 산 세바스티안: 피크소스 핀초스(타파스)
""")

# 섹션 5: 스페인 음식
st.markdown('<h2 class="section-title">🍷 스페인에서 꼭 먹어봐야 할 음식</h2>', unsafe_allow_html=True)
st.markdown("""
- **빠에야(Paella)**: 해산물 혹은 고기를 넣고 샤프란으로 향을 낸 밥 요리  
- **하몽(Jamón)**: 이베리코 돼지 다리를 건조시켜 만든 생햄  
- **핀초스(Pintxos)**: 바스크 지방식 타파스, 빵 위에 올린 한입 요리  
- **상그리아(Sangria)**: 와인과 과일을 섞은 달콤한 술  
""")

# 푸터
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 14px; color: gray;'>Made with ❤️ by Streamlit | Designed for Spain Travelers 2025</p>", unsafe_allow_html=True)
