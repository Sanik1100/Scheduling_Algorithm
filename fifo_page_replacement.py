# FIFO Page Replacement Algorithm (User Input)

reference_string = list(map(int, input("Enter reference string (space separated): ").split()))
frames_count = int(input("Enter number of frames: "))

frames = []
page_faults = 0

print("\nFIFO Page Replacement Table")
print("Page\tFrames\t\tStatus")
print("-" * 40)

for page in reference_string:
    if page in frames:
        status = "Hit"
    else:
        status = "Fault"
        page_faults += 1
        if len(frames) < frames_count:
            frames.append(page)
        else:
            frames.pop(0)      # FIFO removal
            frames.append(page)

    print(f"{page}\t{frames}\t{status}")

hits = len(reference_string) - page_faults
hit_ratio = hits / len(reference_string)

print("\nTotal Page Faults:", page_faults)
print("Hit Ratio:", round(hit_ratio, 2))
