import matplotlib.pyplot as plt

# ----------------- User Input -----------------
requests = list(map(int, input("Enter disk request queue (space separated): ").split()))
head = int(input("Enter initial head position: "))

# ----------------- C-LOOK Calculation -----------------
req = sorted(requests)
order = [head]
movement = 0
movements_list = []

current = head

# Requests in ascending order
up = [r for r in req if r >= current]
down = [r for r in req if r < current]

print("\nC-LOOK Execution Order:")
print("From\tTo\tMovement")

# Move up first
for r in up:
    move = abs(current - r)
    movement += move
    movements_list.append(move)
    print(f"{current}\t{r}\t{move}")
    order.append(r)
    current = r

# Jump to the first request (smallest) if there are remaining requests
if down:
    move = abs(current - down[0])
    movement += move
    movements_list.append(move)
    print(f"{current}\t{down[0]}\t{move}")
    order.append(down[0])
    current = down[0]

    # Service remaining requests in ascending order
    for r in down[1:]:
        move = abs(current - r)
        movement += move
        movements_list.append(move)
        print(f"{current}\t{r}\t{move}")
        order.append(r)
        current = r

print("\nTotal Head Movement:", movement)

# ----------------- Graph Plotting -----------------
plt.figure(figsize=(12,6))
plt.plot(order, marker='o', linestyle='-', color='magenta')

# Annotate movement distances
for i in range(len(order)-1):
    plt.text(i + 0.5, (order[i]+order[i+1])/2, str(movements_list[i]),
             color='red', fontsize=10, ha='center', va='bottom')

plt.title('C-LOOK Disk Scheduling with Head Movement')
plt.xlabel('Sequence of Requests')
plt.ylabel('Cylinder Number (Head Position)')
plt.xticks(range(len(order)), order)
plt.grid(True)
plt.show()
