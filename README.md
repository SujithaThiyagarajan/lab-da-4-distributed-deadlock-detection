# Distributed Deadlock Detection Simulator using Wait-For Graph

## Objective
The objective of this project is to design and implement a Distributed Deadlock Detection System using the Wait-For Graph (WFG) model. The system simulates multiple processes distributed across different sites and detects deadlocks using Cycle Detection (DFS) and a Probe-Based Edge-Chasing Algorithm.

---

## Problem Statement
In distributed systems, multiple processes compete for shared resources located across different sites. Improper resource allocation can lead to a situation where processes wait indefinitely for each other, resulting in a deadlock.

Since distributed systems lack a global view, detecting deadlocks becomes challenging. This project simulates such an environment and applies detection techniques to identify deadlocks.

---

## Key Concepts
- Distributed Systems  
- Deadlock Detection  
- Wait-For Graph (WFG)  
- Cycle Detection (DFS)  
- Edge-Chasing Algorithm  

---

## System Design

### Process and Site Model
- N processes (P1, P2, ..., Pn)  
- Multiple sites (S1, S2, ...)  
- Processes request resources held by others  

### Wait-For Graph (WFG)
- Nodes represent processes  
- Edge Pi → Pj means Pi is waiting for Pj  
- Cycle in graph ⇒ Deadlock  

### Deadlock Detection Methods
**1. DFS Cycle Detection**
- Detects cycles using depth-first search  

**2. Edge-Chasing Algorithm**
- Uses probe messages (initiator, sender, receiver)  
- Deadlock detected when probe returns to initiator  

---

## Tools and Technologies
- Python  
- SimPy  
- Streamlit  
- NetworkX  
- Matplotlib  

---

## Implementation
- SimPy used for simulation  
- Random resource requests generate WFG  
- Graph updated dynamically  
- Deadlock detection using DFS and edge-chasing  
- Visualization using NetworkX  

---

## Features
- Multi-process simulation  
- Distributed site representation  
- Dynamic Wait-For Graph  
- Dual detection methods  
- Graph visualization  
- Interactive UI  

---

## Output
- Process-to-site mapping  
- Wait-For Graph visualization  
- Deadlock detection result  

---

## How to Run

```bash
pip install -r requirements.txt
streamlit run app.py

