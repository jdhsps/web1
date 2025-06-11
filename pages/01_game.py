import streamlit as st
from streamlit_plotly_events import plotly_events
import plotly.graph_objects as go
import random
import time

# 설정
st.set_page_config(page_title="🎯 과녁 클릭 게임", layout="centered")
st.title("🎯 과녁 클릭 게임")

# 초기 상태 설정
if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.target = (random.uniform(0.1, 0.9), random.uniform(0.1, 0.9))
    st.session_state.start_time = None
    st.session_state.game_over = False

# 게임 시작 버튼
if st.button("게임 시작" if not st.session_state.start_time else "다시 시작"):
    st.session_state.score = 0
    st.session_state.target = (random.uniform(0.1, 0.9), random.uniform(0.1, 0.9))
    st.session_state.start_time = time.time()
    st.session_state.game_over = False

# 타이머
if st.session_state.start_time and not st.session_state.game_over:
    elapsed = time.time() - st.session_state.start_time
    remaining = max(0, 10 - elapsed)
    st.progress((10 - remaining) / 10)
    st.markdown(f"⏱ 남은 시간: `{remaining:.1f}`초")

    if remaining <= 0:
        st.session_state.game_over = True
        st.success(f"🎉 게임 종료! 최종 점수: `{st.session_state.score}`")

# 현재 타겟 좌표
target_x, target_y = st.session_state.target

# Plotly 차트 생성
fig = go.Figure()
fig.update_layout(
    width=500,
    height=500,
    xaxis=dict(range=[0, 1], showgrid=False, zeroline=False, visible=False),
    yaxis=dict(range=[0, 1], showgrid=False, zeroline=False, visible=False),
    margin=dict(l=0, r=0, t=0, b=0),
    dragmode=False,
    clickmode="event+select"
)

# 과녁 그리기
fig.add_shape(
    type="circle",
    x0=target_x - 0.05,
    y0=target_y - 0.05,
    x1=target_x + 0.05,
    y1=target_y + 0.05,
    fillcolor="red",
    line_color="red",
)

# 사용자 클릭 감지
clicked_points = plotly_events(fig, click_event=True, select_event=False)

# 클릭 처리
if clicked_points and not st.session_state.game_over:
    click_x = clicked_points[0]["x"]
    click_y = clicked_points[0]["y"]

    dist = ((click_x - target_x) ** 2 + (click_y - target_y) ** 2) ** 0.5
    if dist <= 0.05:
        st.session_state.score += 1
        st.session_state.target = (random.uniform(0.1, 0.9), random.uniform(0.1, 0.9))
