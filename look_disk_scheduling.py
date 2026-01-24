import matplotlib.pyplot as plt

# ----------------- User Input -----------------
requests = list(map(int, input("Enter disk request queue (space separated): ").split()))
head = int(input("Enter initial head position: "))

# ----------------- LOOK Calculation -----------------
req = sorted(requests)
order = [head]
movement = 0
movements_list = []

current = head
direction = 'up'  # move towards higher cylinders first

# Split requests based on current head
up = [r for r in req if r >= current]
down = [r for r in req if r < current][::-1]  # reverse for descending

print("\nLOOK Execution Order:")
print("From\tTo\tMovement")

if direction == 'up':
    # Move up
    for r in up:
        move = abs(current - r)
        movement += move
        movements_list.append(move)
        print(f"{current}\t{r}\t{move}")
        order.append(r)
        current = r
    # Move down if needed
    for r in down:
        move = abs(current - r)
        movement += move
        movements_list.append(move)
        print(f"{current}\t{r}\t{move}")
        order.append(r)
        current = r
else:
    # Move down first
    for r in down:
        move = abs(current - r)
        movement += move
        movements_list.append(move)
        print(f"{current}\t{r}\t{move}")
        order.append(r)
        current = r
    # Move up if needed
    for r in up:
        move = abs(current - r)
        movement += move
        movements_list.append(move)
        print(f"{current}\t{r}\t{move}")
        order.append(r)
        current = r

print("\nTotal Head Movement:", movement)

# ----------------- Graph Plotting -----------------
plt.figure(figsize=(12,6))
plt.plot(order, marker='o', linestyle='-', color='teal')

# Annotate movement distances
for i in range(len(order)-1):
    plt.text(i + 0.5, (order[i]+order[i+1])/2, str(movements_list[i]),
             color='red', fontsize=10, ha='center', va='bottom')

plt.title('LOOK Disk Scheduling with Head Movement')
plt.xlabel('Sequence of Requests')
plt.ylabel('Cylinder Number (Head Position)')
plt.xticks(range(len(order)), order)
plt.grid(True)
plt.show()
