def print_gantt_chart(gantt):
    print("\nGantt Chart:")

    # Top border
    for _ in gantt:
        print("+------", end="")
    print("+")

    # Process IDs
    for pid, _, _ in gantt:
        print(f"|  {pid:<3} ", end="")
    print("|")

    # Bottom border
    for _ in gantt:
        print("+------", end="")
    print("+")

    # Time line
    print(f"{gantt[0][1]:<7}", end="")
    for _, _, end in gantt:
        print(f"{end:<7}", end="")
    print("\n")


def sjf_non_preemptive(processes):
    time = 0
    gantt = []
    completed = []

    total_wt = total_tat = 0
    n = len(processes)

    while processes:
        available = [p for p in processes if p[1] <= time]

        if not available:
            time += 1
            continue

        # Select shortest burst time
        pid, at, bt = min(available, key=lambda x: x[2])
        processes.remove((pid, at, bt))

        start = time
        time += bt
        ct = time

        tat = ct - at
        wt = tat - bt

        total_wt += wt
        total_tat += tat

        gantt.append((pid, start, ct))
        completed.append((pid, at, bt, ct, wt, tat))

    # Print table ONCE
    print("\nSJF Non-Preemptive Scheduling")
    print("PID\tAT\tBT\tCT\tWT\tTAT")
    for p in completed:
        print(f"{p[0]}\t{p[1]}\t{p[2]}\t{p[3]}\t{p[4]}\t{p[5]}")

    print(f"\nAverage Waiting Time = {total_wt / n:.2f}")
    print(f"Average Turnaround Time = {total_tat / n:.2f}")

    print_gantt_chart(gantt)


if __name__ == "__main__":
    n = int(input("Enter number of processes: "))
    processes = []

    for i in range(n):
        at = int(input(f"Arrival Time of P{i+1}: "))
        bt = int(input(f"Burst Time of P{i+1}: "))
        processes.append((f"P{i+1}", at, bt))

    sjf_non_preemptive(processes)
