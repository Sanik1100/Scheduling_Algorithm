import matplotlib.pyplot as plt

# ----------------- User Input -----------------
requests = list(map(int, input("Enter disk request queue (space separated): ").split()))
head = int(input("Enter initial head position: "))
disk_size = int(input("Enter maximum disk size (e.g., 199): "))

# ----------------- SCAN Calculation -----------------
req = sorted(requests)
order = [head]
movement = 0
movements_list = []

current = head
direction = 'up'  # Change to 'down' if you want the head to move toward 0 first

# Split requests based on current head
up = [r for r in req if r >= current]
down = [r for r in req if r < current][::-1]  # reverse for descending

if direction == 'up':
    # Move up
    for r in up:
        move = abs(current - r)
        movement += move
        movements_list.append(move)
        print(f"{current}\t{r}\t{move}")
        order.append(r)
        current = r
    # Go to end if there are requests in the opposite direction
    if down:
        move = abs(current - (disk_size - 1))
        movement += move
        movements_list.append(move)
        current = disk_size - 1
        order.append(current)  # optional to include end in graph
        # Move down
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
plt.plot(order, marker='o', linestyle='-', color='purple')

# Annotate movement distances
for i in range(len(order)-1):
    plt.text(i + 0.5, (order[i]+order[i+1])/2, str(movements_list[i]),
             color='red', fontsize=10, ha='center', va='bottom')

plt.title('SCAN Disk Scheduling with Head Movement')
plt.xlabel('Sequence of Requests')
plt.ylabel('Cylinder Number (Head Position)')
plt.xticks(range(len(order)), order)
plt.grid(True)
plt.show()
