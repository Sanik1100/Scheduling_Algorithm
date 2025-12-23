def print_gantt_chart(gantt):
    print("\nGantt Chart:")

    for _ in gantt:
        print("+------", end="")
    print("+")

    for pid, start, end in gantt:
        print(f"|  {pid:^3} ", end="")
    print("|")

    for _ in gantt:
        print("+------", end="")
    print("+")

    print(f"{gantt[0][1]:<7}", end="")
    for pid, start, end in gantt:
        print(f"{end:<7}", end="")
    print("\n")


def sjf_preemptive(processes):
    time = 0
    remaining = {p[0]: p[2] for p in processes}
    completion = {}
    gantt = []

    print("\nSJF Preemptive Scheduling (SRTF)")

    while True:  # runs until all processes are complete
        # Get all available processes
        available = [
            p for p in processes
            if p[1] <= time and remaining[p[0]] > 0
        ]

        # If no process is left to execute 
        if not available:
            if all(remaining[p[0]] == 0 for p in processes):
                break
            time += 1
            continue

        # Select process with shortest remaining time
        pid, at, bt = min(available, key=lambda x: remaining[x[0]])

        start = time
        remaining[pid] -= 1
        time += 1
        end = time

        # Merge Gantt blocks
        if gantt and gantt[-1][0] == pid:
            gantt[-1] = (pid, gantt[-1][1], end)
        else:
            gantt.append((pid, start, end))

        # If process finished
        if remaining[pid] == 0:
            completion[pid] = time

    
    print("\nPID\tAT\tBT\tCT\tWT\tTAT")

    total_wt = total_tat = 0

    for pid, at, bt in processes:
        ct = completion[pid]
        tat = ct - at
        wt = tat - bt

        total_wt += wt
        total_tat += tat

        print(f"{pid}\t{at}\t{bt}\t{ct}\t{wt}\t{tat}")

    print(f"\nAverage Waiting Time = {total_wt / len(processes):.2f}")
    print(f"Average Turnaround Time = {total_tat / len(processes):.2f}")

    print_gantt_chart(gantt)



if __name__ == "__main__":
    n = int(input("Enter number of processes: "))
    processes = []

    for i in range(n):
        at = int(input(f"Arrival time of P{i+1}: "))
        bt = int(input(f"Burst time of P{i+1}: "))
        processes.append((f"P{i+1}", at, bt))

    sjf_preemptive(processes)
