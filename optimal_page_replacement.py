# OPT (Optimal) Page Replacement Algorithm

reference_string = list(
    map(int, input("Enter reference string (space separated): ").split())
)

frames_count = int(input("Enter number of frames: "))

frames = []
page_faults = 0

print("\nOPT Page Replacement Table")
print("Page\tFrames\t\tStatus")
print("-" * 40)

for i in range(len(reference_string)):
    page = reference_string[i]

    if page in frames:
        status = "Hit"
    else:
        status = "Fault"
        page_faults += 1

        if len(frames) < frames_count:
            frames.append(page)
        else:
            future = reference_string[i + 1:]
            indexes = []

            for f in frames:
                if f in future:
                    indexes.append(future.index(f))
                else:
                    indexes.append(float('inf'))

            frames[indexes.index(max(indexes))] = page

    print(f"{page}\t{frames}\t{status}")

hits = len(reference_string) - page_faults
hit_ratio = hits / len(reference_string)

print("\nTotal Page Faults:", page_faults)
print("Hit Ratio:", round(hit_ratio, 2))
