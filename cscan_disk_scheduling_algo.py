import matplotlib.pyplot as plt

# ----------------- User Input -----------------
requests = list(map(int, input("Enter disk request queue (space separated): ").split()))
head = int(input("Enter initial head position: "))
disk_size = int(input("Enter maximum disk size (e.g., 199): "))

# ----------------- C-SCAN Calculation -----------------
req = sorted(requests)
order = [head]
movement = 0
movements_list = []

current = head

# Requests greater than current
up = [r for r in req if r >= current]
# Requests less than current (to be serviced after jump)
down = [r for r in req if r < current]

print("\nC-SCAN Execution Order:")
print("From\tTo\tMovement")

# Move up first
for r in up:
    move = abs(current - r)
    movement += move
    movements_list.append(move)
    print(f"{current}\t{r}\t{move}")
    order.append(r)
    current = r

# Jump to beginning if there are requests in the lower part
if down:
    # Move to end first if not already at end
    if current != disk_size - 1:
        move = abs(current - (disk_size - 1))
        movement += move
        movements_list.append(move)
        current = disk_size - 1
        order.append(current)  # optional: include end in graph

    # Jump to beginning (0)
    move = abs(current - 0)
    movement += move
    movements_list.append(move)
    current = 0
    order.append(current)  # optional: include start in graph

    # Service remaining requests
    for r in down:
        move = abs(current - r)
        movement += move
        movements_list.append(move)
        print(f"{current}\t{r}\t{move}")
        order.append(r)
        current = r

print("\nTotal Head Movement:", movement)

# ----------------- Graph Plotting -----------------
plt.figure(figsize=(12,6))
plt.plot(order, marker='o', linestyle='-', color='orange')

# Annotate movement distances
for i in range(len(order)-1):
    plt.text(i + 0.5, (order[i]+order[i+1])/2, str(movements_list[i]),
             color='red', fontsize=10, ha='center', va='bottom')

plt.title('C-SCAN Disk Scheduling with Head Movement')
plt.xlabel('Sequence of Requests')
plt.ylabel('Cylinder Number (Head Position)')
plt.xticks(range(len(order)), order)
plt.grid(True)
plt.show()
