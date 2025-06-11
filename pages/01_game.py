import streamlit as st
import plotly.graph_objects as go
import random
import time

# 초기 세션 상태 설정
if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.target = (random.uniform(0, 1), random.uniform(0, 1))
    st.session_state.start_time = None
    st.session_state.game_over = False

st.title("🎯 과녁 클릭 게임")
st.markdown("10초 안에 가능한 많은 과녁을 클릭하세요!")

# 게임 시작 버튼
if st.button("게임 시작" if not st.session_state.start_time else "다시 시작"):
    st.session_state.score = 0
    st.session_state.target = (random.uniform(0, 1), random.uniform(0, 1))
    st.session_state.start_time = time.time()
    st.session_state.game_over = False

# 게임 상태 처리
if st.session_state.start_time and not st.session_state.game_over:
    elapsed = time.time() - st.session_state.start_time
    remaining = max(0, 10 - elapsed)
    st.progress((10 - remaining) / 10)
    st.markdown(f"⏱ 남은 시간: `{remaining:.1f}`초")

    if remaining <= 0:
        st.session_state.game_over = True
        st.success(f"🎉 게임 종료! 최종 점수: `{st.session_state.score}`")

# 과녁 위치
target_x, target_y = st.session_state.target

# Plotly 그래프 그리기
fig = go.Figure()
fig.update_layout(
    width=500,
    height=500,
    xaxis=dict(range=[0, 1], showgrid=False, zeroline=False, visible=False),
    yaxis=dict(range=[0, 1], showgrid=False, zeroline=False, visible=False),
    margin=dict(l=0, r=0, t=0, b=0),
    dragmode=False,
)

# 타겟 (과녁) 그리기
fig.add_shape(
    type="circle",
    x0=target_x - 0.05,
    y0=target_y - 0.05,
    x1=target_x + 0.05,
    y1=target_y + 0.05,
    fillcolor="red",
    line_color="red",
)

fig.update_layout(clickmode="event+select")
click = st.plotly_chart(fig, use_container_width=True)

# 클릭 이벤트 확인
clicked = st.session_state.get("clicked", False)

if not clicked:
    st.session_state.clicked = True

    # 클릭 좌표 수신
    clicked_point = st.experimental_get_query_params().get("clickData")
    if clicked_point:
        cx = float(clicked_point["points"][0]["x"])
        cy = float(clicked_point["points"][0]["y"])

        # 거리 계산
        dist = ((cx - target_x) ** 2 + (cy - target_y) ** 2) ** 0.5
        if dist < 0.05 and not st.session_state.game_over:
            st.session_state.score += 1
            st.session_state.target = (random.uniform(0.05, 0.95), random.uniform(0.05, 0.95))
            st.experimental_rerun()
