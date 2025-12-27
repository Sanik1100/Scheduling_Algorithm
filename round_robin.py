from collections import deque

# Input
n = int(input("Enter number of processes: "))

processes = []
for i in range(n):
    at = int(input(f"Arrival time of P{i+1}: "))
    bt = int(input(f"Burst time of P{i+1}: "))
    processes.append({
        "pid": f"P{i+1}",
        "at": at,
        "bt": bt,
        "rt": bt,   # remaining time
        "ct": 0
    })

time_quantum = int(input("Enter time quantum: "))

# Sort by arrival time
processes.sort(key=lambda x: x["at"])

time = 0
queue = deque()
gantt_chart = []
index = 0
completed = 0

print("\nRound Robin Scheduling\n")

while completed < n:

    # Add processes that have arrived
    while index < n and processes[index]["at"] <= time:
        queue.append(processes[index])
        index += 1

    if not queue:
        time += 1
        continue

    current = queue.popleft()
    exec_time = min(time_quantum, current["rt"])

    gantt_chart.append((current["pid"], time, time + exec_time))

    time += exec_time
    current["rt"] -= exec_time

    # Add newly arrived processes during execution
    while index < n and processes[index]["at"] <= time:
        queue.append(processes[index])
        index += 1

    if current["rt"] > 0:
        queue.append(current)
    else:
        current["ct"] = time
        completed += 1

# Calculate TAT and WT
total_tat = 0
total_wt = 0

print("PID\tAT\tBT\tCT\tTAT\tWT")
for p in processes:
    tat = p["ct"] - p["at"]
    wt = tat - p["bt"]
    total_tat += tat
    total_wt += wt
    print(f"{p['pid']}\t{p['at']}\t{p['bt']}\t{p['ct']}\t{tat}\t{wt}")

print(f"\nAverage Turnaround Time = {total_tat / n:.2f}")
print(f"Average Waiting Time = {total_wt / n:.2f}")

# Gantt Chart
print("\nGantt Chart:")
for g in gantt_chart:
    print(f"| {g[0]} ", end="")
print("|")

for g in gantt_chart:
    print(f"{g[1]:<4}", end="")
print(time)
