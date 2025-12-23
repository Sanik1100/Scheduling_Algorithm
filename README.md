# 🖥️ CPU Scheduling Algorithms Simulator (Python)

## 📌 Overview
This repository contains a **Python-based simulator** for common **CPU Scheduling Algorithms** used in **Operating Systems**.

Each scheduling algorithm is implemented in a **separate Python file** to ensure:
- Better clarity
- Modular design
- Easy academic evaluation

The simulator calculates:
- **Completion Time (CT)**
- **Turnaround Time (TAT)**
- **Waiting Time (WT)**
- **Gantt Chart** (visual representation of CPU execution)

---

## 📚 Scheduling Algorithms Implemented

- **First Come First Serve (FCFS)**
- **Shortest Job First (SJF)**
  - Non-Preemptive
  - Preemptive (Shortest Remaining Time First – SRTF)
- **Round Robin (RR)**
- **Priority Scheduling**
  - Preemptive / Non-Preemptive (based on implementation)

Each algorithm strictly follows **standard Operating System theory rules**.

---

## 🛠️ Requirements

- **Python 3.x**
- No external libraries required

---

## ▶️ How to Run

1. Open **Terminal / Command Prompt**
2. Navigate to the project directory
3. Run any scheduling algorithm file

### Example:
```bash
python sjf_preemptive.py


## 🧾 Input Format

### Common Inputs
- Number of processes  
- Arrival Time (AT)  
- Burst Time (BT)  

### Additional Inputs
- **Priority** → Only for Priority Scheduling  
- **Time Quantum** → Only for Round Robin  

---

## 🔢 Sample Input


---

## 📊 Sample Output Details

### Process Table

| PID | AT | BT | CT | WT | TAT |
|-----|----|----|----|----|-----|
| P1  | 0  | 5  | 5  | 0  | 5   |
| P2  | 1  | 3  | 8  | 4  | 7   |
| P3  | 2  | 1  | 6  | 3  | 4   |

### Average Times
- **Average Waiting Time:** 2.33  
- **Average Turnaround Time:** 5.33  


---

## 📐 Formulas Used

- **Completion Time (CT):** Time at which a process finishes execution  

- **Turnaround Time (TAT):**  
-** TAT=CT-AT **

---

## ⚙️ Algorithm-Wise Description

### 🔹 First Come First Serve (FCFS)
- Processes are executed in the order they arrive  
- Simple and easy to implement  
- May suffer from the **convoy effect**

### 🔹 Shortest Job First (SJF) Non-Preemptive
- Process with the **shortest burst time** is selected  
- Once a process starts, it **cannot be interrupted**  
- Reduces average waiting time compared to FCFS

### 🔹 Shortest Job First (SJF) Preemptive / SRTF
- Process with the **shortest remaining time** is selected  
- CPU can be **preempted at every time unit**  
- Minimizes **average waiting time**

### 🔹 Round Robin (RR)
- Each process is assigned a **fixed time quantum**  
- CPU switches between processes in a **cyclic order**  
- Suitable for **time-sharing systems**

### 🔹 Priority Scheduling
- CPU is allocated based on **priority**  
- Lower number indicates **higher priority**  
- **Starvation** may occur without aging  

---

## 🎯 Learning Outcomes
- Understand **CPU scheduling concepts** and behavior  
- Learn differences between **preemptive and non-preemptive scheduling**  
- Visualize CPU execution using **Gantt Charts**  
- Apply **Operating System theory** using Python programming

---





   
