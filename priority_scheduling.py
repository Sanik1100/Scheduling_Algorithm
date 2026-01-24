# Preemptive Priority Scheduling Algorithm

n = int(input("Enter number of processes: "))

processes = []

for i in range(n):
    at = int(input(f"Arrival time of P{i+1}: "))
    bt = int(input(f"Burst time of P{i+1}: "))
    pr = int(input(f"Priority of P{i+1} (lower number = higher priority): "))
    processes.append({
        "pid": f"P{i+1}",
        "at": at,
        "bt": bt,
        "rt": bt,        # Remaining Time
        "priority": pr,
        "ct": 0
    })

time = 0
completed = 0
prev_process = None
gantt_chart = []

print("\nPreemptive Priority Scheduling\n")

while completed < n:
    idx = -1
    highest_priority = float('inf')

    for i in range(n):
        if processes[i]["at"] <= time and processes[i]["rt"] > 0:
            if processes[i]["priority"] < highest_priority:
                highest_priority = processes[i]["priority"]
                idx = i
            elif processes[i]["priority"] == highest_priority:
                if processes[i]["at"] < processes[idx]["at"]:
                    idx = i

    if idx == -1:
        time += 1
        continue

    current_pid = processes[idx]["pid"]

    if prev_process != current_pid:
        gantt_chart.append([current_pid, time])
        prev_process = current_pid

    processes[idx]["rt"] -= 1
    time += 1

    if processes[idx]["rt"] == 0:
        processes[idx]["ct"] = time
        completed += 1

# Calculations
total_tat = 0
total_wt = 0

print("PID\tAT\tBT\tPR\tCT\tTAT\tWT")
for p in processes:
    tat = p["ct"] - p["at"]
    wt = tat - p["bt"]
    total_tat += tat
    total_wt += wt
    print(f"{p['pid']}\t{p['at']}\t{p['bt']}\t{p['priority']}\t{p['ct']}\t{tat}\t{wt}")

print(f"\nAverage Turnaround Time = {total_tat / n:.2f}")
print(f"Average Waiting Time = {total_wt / n:.2f}")

# Gantt Chart Output
print("\nGantt Chart:")
for g in gantt_chart:
    print(f"| {g[0]} ", end="")
print("|")

for g in gantt_chart:
    print(f"{g[1]:<4}", end="")
print(time)
