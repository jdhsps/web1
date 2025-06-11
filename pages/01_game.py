import streamlit as st
from streamlit_drawable_canvas import st_canvas
import random
import time

# 설정
st.set_page_config(page_title="🎯 과녁 클릭 게임", layout="centered")
st.title("🎯 과녁 클릭 게임")

canvas_width = 500
canvas_height = 500
target_radius = 30

# 초기화
if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.start_time = None
    st.session_state.target_x = random.randint(target_radius, canvas_width - target_radius)
    st.session_state.target_y = random.randint(target_radius, canvas_height - target_radius)
    st.session_state.game_over = False

# 게임 시작
if st.button("게임 시작" if not st.session_state.start_time else "다시 시작"):
    st.session_state.score = 0
    st.session_state.start_time = time.time()
    st.session_state.game_over = False
    st.session_state.target_x = random.randint(target_radius, canvas_width - target_radius)
    st.session_state.target_y = random.randint(target_radius, canvas_height - target_radius)

# 타이머
if st.session_state.start_time and not st.session_state.game_over:
    elapsed = time.time() - st.session_state.start_time
    remaining = max(0, 10 - elapsed)
    st.progress((10 - remaining) / 10)
    st.markdown(f"⏱ 남은 시간: `{remaining:.1f}`초")

    if remaining <= 0:
        st.session_state.game_over = True
        st.success(f"🎉 게임 종료! 최종 점수: `{st.session_state.score}`")

# Canvas로 과녁 그리기
if not st.session_state.game_over:
    canvas_result = st_canvas(
        fill_color="rgba(255, 0, 0, 0.6)",
        stroke_width=0,
        background_color="white",
        height=canvas_height,
        width=canvas_width,
        drawing_mode="point",
        key="canvas",
        update_streamlit=True,
        initial_drawing=[
            {
                "type": "circle",
                "left": st.session_state.target_x - target_radius,
                "top": st.session_state.target_y - target_radius,
                "width": target_radius * 2,
                "height": target_radius * 2,
                "fill": "rgba(255, 0, 0, 0.6)"
            }
        ]
    )

    # 클릭 판정
    if canvas_result.json_data and canvas_result.json_data["objects"]:
        obj = canvas_result.json_data["objects"][-1]
        click_x = obj["left"]
        click_y = obj["top"]

        dist = ((click_x - st.session_state.target_x) ** 2 + (click_y - st.session_state.target_y) ** 2) ** 0.5
        if dist <= target_radius:
            st.session_state.score += 1
            st.session_state.target_x = random.randint(target_radius, canvas_width - target_radius)
            st.session_state.target_y = random.randint(target_radius, canvas_height - target_radius)

    st.markdown(f"🏆 점수: `{st.session_state.score}`")
