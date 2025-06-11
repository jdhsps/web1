import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 시뮬레이션 함수 정의
def simulate_three_body(pos, vel, masses, G=1, dt=0.01, steps=1000):
    n_bodies = 3
    positions = np.zeros((steps, n_bodies, 2))
    velocities = np.copy(vel)
    positions[0] = np.copy(pos)

    for step in range(1, steps):
        acc = np.zeros((n_bodies, 2))
        for i in range(n_bodies):
            for j in range(n_bodies):
                if i != j:
                    r = positions[step-1, j] - positions[step-1, i]
                    distance = np.linalg.norm(r)
                    if distance == 0:
                        continue
                    acc[i] += G * masses[j] * r / distance**3
        velocities += acc * dt
        positions[step] = positions[step-1] + velocities * dt
    return positions

# Streamlit 앱 구성
st.set_page_config(page_title="삼체 시뮬레이션", layout="wide")
st.title("🌌 삼체 문제 2D 시뮬레이션")

# 초기 조건 입력
st.sidebar.header("🛠️ 초기 조건 설정")

mass1 = st.sidebar.slider("질량 1", 0.1, 10.0, 1.0)
mass2 = st.sidebar.slider("질량 2", 0.1, 10.0, 1.0)
mass3 = st.sidebar.slider("질량 3", 0.1, 10.0, 1.0)

masses = np.array([mass1, mass2, mass3])

pos = np.array([
    [-1.0, 0.0],
    [1.0, 0.0],
    [0.0, 0.5]
])

vel = np.array([
    [0.0, 0.3],
    [0.0, -0.3],
    [0.2, 0.0]
])

steps = st.sidebar.slider("시뮬레이션 스텝 수", 100, 5000, 1000)
dt = st.sidebar.slider("시간 간격 (dt)", 0.001, 0.1, 0.01)

if st.button("🚀 Run Simulation"):
    st.info("시뮬레이션 실행 중...")
    trajectory = simulate_three_body(pos, vel, masses, dt=dt, steps=steps)

    # 시각화
    fig, ax = plt.subplots()
    colors = ['red', 'green', 'blue']

    for i in range(3):
        ax.plot(trajectory[:, i, 0], trajectory[:, i, 1], color=colors[i], label=f'천체 {i+1}')
        ax.plot(trajectory[0, i, 0], trajectory[0, i, 1], 'o', color=colors[i])

    ax.set_xlabel("X 위치")
    ax.set_ylabel("Y 위치")
    ax.set_title("삼체 시뮬레이션 궤도")
    ax.legend()
    ax.set_aspect('equal')
    st.pyplot(fig)
else:
    st.write("왼쪽에서 초기 조건을 설정한 후 **[Run Simulation]** 버튼을 눌러주세요.")

