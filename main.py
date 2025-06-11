import streamlit as st
import folium
from streamlit_folium import st_folium

# 여행지 데이터 정의
destinations = {
    "바르셀로나": {
        "location": [41.3851, 2.1734],
        "description": "가우디의 도시! 사그라다 파밀리아 성당, 구엘 공원 등 유명한 건축물로 가득한 도시입니다.",
    },
    "마드리드": {
        "location": [40.4168, -3.7038],
        "description": "스페인의 수도. 프라도 미술관, 왕궁 등 문화와 역사가 풍부한 도시입니다.",
    },
    "세비야": {
        "location": [37.3891, -5.9845],
        "description": "안달루시아 지방의 중심. 플라멩코와 알카사르 궁전으로 유명합니다.",
    },
    "그라나다": {
        "location": [37.1773, -3.5986],
        "description": "알함브라 궁전으로 유명한 아름다운 산악 도시입니다.",
    },
    "산 세바스티안": {
        "location": [43.3183, -1.9812],
        "description": "해변과 미식으로 유명한 바스크 지방의 진주입니다.",
    },
}

# Streamlit 앱 구성
st.title("🇪🇸 스페인 여행 가이드")
st.markdown("스페인의 주요 관광지를 지도와 함께 알아보세요!")

# 지도 만들기 (중심은 스페인 중심부로)
map_center = [40.0, -3.7]
m = folium.Map(location=map_center, zoom_start=6)

# 지도에 마커 추가
for city, info in destinations.items():
    folium.Marker(
        location=info["location"],
        popup=f"<b>{city}</b><br>{info['description']}",
        tooltip=city,
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(m)

# Folium 지도를 Streamlit에 표시
st_data = st_folium(m, width=700, height=500)

# 선택한 도시 정보 출력
if st_data and st_data.get("last_object_clicked_tooltip"):
    selected_city = st_data["last_object_clicked_tooltip"]
    st.subheader(f"📍 {selected_city}")
    st.write(destinations[selected_city]["description"])
