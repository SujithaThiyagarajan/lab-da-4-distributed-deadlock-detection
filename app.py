import streamlit as st
import simpy
import networkx as nx
import matplotlib.pyplot as plt

from simulation import DistributedSystem
from deadlock_detection import detect_deadlock, edge_chasing

st.title("Distributed Deadlock Detection Simulator")

st.sidebar.header("Simulation Controls")
num_processes = st.sidebar.slider("Number of Processes", 3, 10, 5)
num_sites = st.sidebar.slider("Number of Sites", 2, 5, 2)
simulation_time = st.sidebar.slider("Simulation Time", 3, 10, 5)

if st.button("Run Simulation"):

    env = simpy.Environment()
    system = DistributedSystem(env, num_processes, num_sites)

    env.process(system.run())
    env.run(until=simulation_time)

    st.subheader("Process → Site Mapping")
    st.write(system.process_site)

    # Build Graph
    G = nx.DiGraph()
    for p, neighbors in system.wait_graph.items():
        for n in neighbors:
            G.add_edge(p, n)

    st.subheader("Wait-For Graph")
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000)
    st.pyplot(plt)

    st.subheader("Deadlock Detection Results")

    if detect_deadlock(system.wait_graph):
        st.error("Deadlock Detected using DFS!")
    else:
        st.success("No Deadlock (DFS)")

    if edge_chasing(system.wait_graph):
        st.warning("Deadlock Detected using Edge-Chasing!")
    else:
        st.info("No Deadlock (Edge-Chasing)")