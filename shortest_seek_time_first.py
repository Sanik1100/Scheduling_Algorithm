import matplotlib.pyplot as plt

# ----------------- User Input -----------------
requests = list(map(int, input("Enter disk request queue (space separated): ").split()))
head = int(input("Enter initial head position: "))

# ----------------- SSTF Calculation -----------------
req = requests.copy()
order = [head]
movement = 0
movements_list = []

current = head

print("\nSSTF Execution Order:")
print("From\tTo\tMovement")

while req:
    # Find closest request
    closest = min(req, key=lambda x: abs(x - current))
    move = abs(current - closest)
    movement += move
    movements_list.append(move)
    print(f"{current}\t{closest}\t{move}")
    current = closest
    order.append(closest)
    req.remove(closest)

print("\nTotal Head Movement:", movement)

# ----------------- Graph Plotting -----------------
plt.figure(figsize=(12,6))
plt.plot(order, marker='o', linestyle='-', color='g')

# Annotate movement distances
for i in range(len(order)-1):
    plt.text(i + 0.5, (order[i]+order[i+1])/2, str(movements_list[i]),
             color='red', fontsize=10, ha='center', va='bottom')

plt.title('SSTF Disk Scheduling with Head Movement')
plt.xlabel('Sequence of Requests')
plt.ylabel('Cylinder Number (Head Position)')
plt.xticks(range(len(order)), order)
plt.grid(True)
plt.show()
