import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, PillowWriter
from io import BytesIO
from PIL import Image
import os

# --- Disk Scheduling Algorithms ---
def fcfs(requests, head):
    seek_sequence = [head] + requests
    total_seek = sum(abs(seek_sequence[i] - seek_sequence[i + 1]) for i in range(len(seek_sequence) - 1))
    return seek_sequence, total_seek

def sstf(requests, head):
    requests = requests[:]
    seek_sequence = [head]
    total_seek = 0
    while requests:
        closest = min(requests, key=lambda x: abs(x - head))
        total_seek += abs(head - closest)
        seek_sequence.append(closest)
        head = closest
        requests.remove(closest)
    return seek_sequence, total_seek

def scan(requests, head, max_cylinder=200):
    left = sorted([r for r in requests if r < head], reverse=True)
    right = sorted([r for r in requests if r >= head])
    seek_sequence = [head] + right + [max_cylinder - 1] + left
    total_seek = sum(abs(seek_sequence[i] - seek_sequence[i + 1]) for i in range(len(seek_sequence) - 1))
    return seek_sequence, total_seek

def cscan(requests, head, max_cylinder=200):
    left = sorted([r for r in requests if r < head])
    right = sorted([r for r in requests if r >= head])
    seek_sequence = [head] + right + [max_cylinder - 1, 0] + left
    total_seek = sum(abs(seek_sequence[i] - seek_sequence[i + 1]) for i in range(len(seek_sequence) - 1))
    return seek_sequence, total_seek

def look(requests, head):
    left = sorted([r for r in requests if r < head], reverse=True)
    right = sorted([r for r in requests if r >= head])
    seek_sequence = [head] + right + left
    total_seek = sum(abs(seek_sequence[i] - seek_sequence[i + 1]) for i in range(len(seek_sequence) - 1))
    return seek_sequence, total_seek

def clook(requests, head):
    left = sorted([r for r in requests if r < head])
    right = sorted([r for r in requests if r >= head])
    seek_sequence = [head] + right + left
    total_seek = sum(abs(seek_sequence[i] - seek_sequence[i + 1]) for i in range(len(seek_sequence) - 1))
    return seek_sequence, total_seek

# --- Streamlit App Layout ---
st.set_page_config(page_title="Disk Scheduler", layout="wide")
st.title("🧠 Disk Scheduling Simulator")

with st.sidebar:
    st.header("⚙️ Configuration")
    algo = st.selectbox("Select Algorithm", ["FCFS", "SSTF", "SCAN", "CSCAN", "LOOK", "CLOOK"])
    queue_input = st.text_input("Enter request queue (comma separated)", "98,183,37,122,14,124,65,67")
    head = st.number_input("Initial Head Position", value=53)
    simulate = st.button("🚀 Simulate")

# --- Process Input ---
if simulate:
    queue = list(map(int, queue_input.split(",")))

    if algo == "FCFS":
        path, total_seek = fcfs(queue, head)
    elif algo == "SSTF":
        path, total_seek = sstf(queue, head)
    elif algo == "SCAN":
        path, total_seek = scan(queue, head)
    elif algo == "CSCAN":
        path, total_seek = cscan(queue, head)
    elif algo == "LOOK":
        path, total_seek = look(queue, head)
    elif algo == "CLOOK":
        path, total_seek = clook(queue, head)

    # Plotting and animating with matplotlib
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(-1, len(path) + 1)
    ax.set_ylim(min(path) - 10, max(path) + 10)
    ax.set_xlabel('Time Step')
    ax.set_ylabel('Track Number')
    ax.set_title(f"{algo} Disk Scheduling")

    line, = ax.plot([], [], marker='o', color='royalblue', lw=4)

    def init():
        line.set_data([], [])
        return line,

    def animate(i):
        line.set_data(range(i + 1), path[:i + 1])
        return line,

    ani = FuncAnimation(fig, animate, frames=len(path), init_func=init, interval=500, blit=True)

    # Save to a file first
    gif_path = "disk_scheduling_animation.gif"
    writer = PillowWriter(fps=2)  # Define the writer for saving GIFs
    ani.save(gif_path, writer=writer)  # Save the animation to a file

    # Read the saved GIF file and display in Streamlit
    with open(gif_path, "rb") as f:
        st.subheader(f"📊 {algo} Disk Scheduling Result")
        st.image(f.read(), caption="Disk Scheduling Animation")

    # Clean up: remove the GIF file after displaying it
    os.remove(gif_path)

    # Display total seek time
    st.success(f"🎯 Total Seek Time: {total_seek}")