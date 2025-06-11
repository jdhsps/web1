import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# -------------------------------
# 시뮬레이션 함수 정의
# -------------------------------
def simulate_three_body_3d(pos, vel, masses, G=1.0, dt=0.01, steps=1000):
    n_bodies = 3
    positions = np.zeros((steps, n_bodies, 3))
    velocities = np.copy(vel)
    positions[0] = np.copy(pos)

    for step in range(1, steps):
        acc = np.zeros((n_bodies, 3))
        for i in range(n_bodies):
            for j in range(n_bodies):
                if i != j:
                    r = positions[step - 1, j] - positions[step - 1, i]
                    dist = np.linalg.norm(r)
                    if dist == 0:
                        continue
                    acc[i] += G * masses[j] * r / dist**3
        velocities += acc * dt
        positions[step] = positions[step - 1] + velocities * dt
    return positions

# -------------------------------
# Streamlit UI 구성
# -------------------------------
st.set_page_config(page_title="🌌 삼체 시뮬레이션 3D", layout="wide")
st.title("🌌 삼체 문제 3D 시뮬레이션")

st.sidebar.header("🛠️ 초기 조건")

# 초기 질량 설정
mass1 = st.sidebar.slider("질량 1", 0.1, 10.0, 1.0)
mass2 = st.sidebar.slider("질량 2", 0.1, 10.0, 1.0)
mass3 = st.sidebar.slider("질량 3", 0.1, 10.0, 1.0)
masses = np.array([mass1, mass2, mass3])

# 시뮬레이션 파라미터
steps = st.sidebar.slider("시뮬레이션 스텝 수", 500, 5000, 2000, step=100)
dt = st.sidebar.slider("시간 간격 (dt)", 0.001, 0.1, 0.01)

# 초기 위치 및 속도 설정
initial_positions = np.array([
    [1.0, 0.0, 0.0],
    [-1.0, 0.0, 0.0],
    [0.0, 1.0, 0.0]
])

initial_velocities = np.array([
    [0.0, 0.1, 0.2],
    [0.0, -0.1, -0.2],
    [0.1, 0.0, 0.0]
])

if st.button("🚀 시뮬레이션 실행"):
    st.info("시뮬레이션 중... 잠시만 기다려주세요.")
    traj = simulate_three_body_3d(initial_positions, initial_velocities, masses, dt=dt, steps=steps)

    # -------------------------------
    # 시각화 (3D 궤도 그래프)
    # -------------------------------
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    colors = ['red', 'green', 'blue']

    for i in range(3):
        ax.plot(traj[:, i, 0], traj[:, i, 1], traj[:, i, 2], color=colors[i], label=f'천체 {i+1}')
        ax.scatter(traj[0, i, 0], traj[0, i, 1], traj[0, i, 2], color=colors[i], marker='o')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title("삼체 궤도 시뮬레이션 (3D)")
    ax.legend()
    ax.view_init(elev=30, azim=45)  # 3D 시점 설정
    st.pyplot(fig)

else:
    st.write("왼쪽 사이드바에서 초기 조건을 설정하고 **[시뮬레이션 실행]** 버튼을 눌러보세요.")
