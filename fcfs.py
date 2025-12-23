def print_gantt_chart(gantt):
    print("\nGantt Chart:")

    for _ in gantt:
        print("+------", end="")
    print("+")

    for pid, start, end in gantt:
        print(f"|  {pid}  ", end="")
    print("|")

    for _ in gantt:
        print("+------", end="")
    print("+")

    print(f"{gantt[0][1]:<7}", end="")
    for pid, start, end in gantt:
        print(f"{end:<7}", end="")
    print("\n")


def fcfs(processes):
    time = 0
    gantt = []

    print("\nFCFS Scheduling")
    print("PID\tAT\tBT\tCT\tWT\tTAT")

    total_wt = total_tat = 0

    for pid, at, bt in processes:
        if time < at:
            time = at

        start = time
        time += bt
        ct = time

        tat = ct - at
        wt = tat - bt

        total_wt += wt
        total_tat += tat

        gantt.append((pid, start, ct))

        print(f"{pid}\t{at}\t{bt}\t{ct}\t{wt}\t{tat}")

    print(f"\nAverage Waiting Time = {total_wt / len(processes):.2f}")
    print(f"Average Turnaround Time = {total_tat / len(processes):.2f}")

    print_gantt_chart(gantt)


if __name__ == "__main__":
    n = int(input("Enter number of processes: "))
    processes = []

    for i in range(n):
        at = int(input(f"Arrival Time of P{i+1}: "))
        bt = int(input(f"Burst Time of P{i+1}: "))
        processes.append((f"P{i+1}", at, bt))

    processes.sort(key=lambda x: x[1])
    fcfs(processes)
