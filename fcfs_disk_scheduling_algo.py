import matplotlib.pyplot as plt

# ----------------- User Input -----------------
requests = list(map(int, input("Enter disk request queue (space separated): ").split()))
head = int(input("Enter initial head position: "))

# ----------------- FCFS Calculation -----------------
order = [head] + requests
movement = 0
movements_list = []  # Store individual movements

print("\nFCFS Execution Order:")
print("From\tTo\tMovement")
for i in range(len(order)-1):
    move = abs(order[i+1] - order[i])
    movement += move
    movements_list.append(move)
    print(f"{order[i]}\t{order[i+1]}\t{move}")

print("\nTotal Head Movement:", movement)

# ----------------- Graph Plotting -----------------
plt.figure(figsize=(12,6))
plt.plot(order, marker='o', linestyle='-', color='b')

# Annotate movement distances
for i in range(len(order)-1):
    plt.text(i + 0.5, (order[i]+order[i+1])/2, str(movements_list[i]),
             color='red', fontsize=10, ha='center', va='bottom')

plt.title('FCFS Disk Scheduling with Head Movement')
plt.xlabel('Sequence of Requests')
plt.ylabel('Cylinder Number (Head Position)')
plt.xticks(range(len(order)), order)
plt.grid(True)
plt.show()
