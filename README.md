# Kitchen Commander
> **Distributed Multi-Agent Kitchen AI** — powered by vision, hierarchy, and hardware.  
> *“Where neural nets meet mise en place.”*

---

## Overview
**Kitchen Commander** is a real-time, multi-agent AI system that simulates and physically controls a coordinated kitchen brigade — inspired by *Overcooked!*  

Each “chef” is a networked **Raspberry Pi + Arduino Pro Micro** unit that acts as a Commis or Porter, while a **Jetson Orin Nano** serves as the **Sous Chef**, handling computer-vision, task-planning, and orchestration.

---

## System Architecture
<img width="286" height="274" alt="image" src="https://github.com/user-attachments/assets/681b2b7c-8171-454f-af8e-4baa430cef6c" />


## AI Hierarchy

Sous Chef       → chooses priorities, allocates resources  
Station Chefs   → plan & schedule kitchen tasks  
Commis/Porters  → physically execute those tasks in the game  

**Strategic Layer: "Sous Chef" Planner - Nvidia Jetson Orin Nano**  
Handles prioritization, computer-vision, order assignment, and role assignment to Station Chefs.

**Operational Layer: "Station Chefs" - Nvidia Jetson Orin Nano (threads)**  
Handles decomposition of orders into tasks and commands tactical agents.

**Tactical Layer: "Commis and Porter" - Raspberry Pi 5**  
Handles pathfinding, task completion and reporting. Translates pathing and routing into direct translation instructions and character actions.

**Physical Layer: "Switch Controllers" - Arduino Pro Micro**  
Direct translation of single instructions and actions into button and controller inputs.

## Communication Protocols

**Sous Chef**  
Inputs: Orders, Blackboard, State Matrix  
Outputs: AssignOrder msg, AssignRole msg, AssignTask msg (as required)   

**Station Chef**  
Inputs: AssignRole, AssignOrder, State Matrix  
Outputs: AssignTask, OrderReport  

**Commis**  
Inputs: AssignTask (Chop, Cook, Plate), State Matrix  
Outputs: TaskReport, Help, Action (Move, Dash, Chop, Pass, Pick Up ...)  

**Porter**  
Inputs: AssignTask (Serve, Fetch, Wash), State Matrix  
Outputs: TaskReport, Help, Action (Move, Dash, Pass, Pick Up, Wash ...)  

---

## Hardware Setup
Component	Quantity	Function  

Jetson Orin Nano (8 GB)	1	CV + Sous Chef Planner  

Raspberry Pi 5	2–4	Agent Nodes (Commis/Porter)  

Arduino Pro Micro (32U4)	2–4	HID controller emulation  

Powered USB Hub	1	Connects Arduinos to Switch Dock  

HDMI Capture Card (USB3)	1	Ingests Switch video feed  

HDMI Splitter	1	Pass-through to display + capture  

Switch Dock	1	Main game host  

---

## Inspiration

Escoffier’s Kitchen Brigade

Overcooked! series

Distributed robotics and Swarm AI

U.S. Marine Corps command structure ⚓

---

##Maintainer

**Maurce Trammell**
zmauricetrammell on GitHub

“Building smarter kitchens, one Pi at a time.”
