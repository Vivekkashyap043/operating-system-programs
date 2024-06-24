import matplotlib.pyplot as plt

def LOOK(arr, head, direction, total_tracks):
    print('Direction:', direction)
    seek_count = 0
    distance = 0
    cur_track = 0

    left = sorted([i for i in arr if i < head])
    right = sorted([i for i in arr if i > head])

    seek_sequence = []
    seek_sequence.append(head)

    run = 2
    while run:
        if direction == "left":
            for i in range(len(left) - 1, -1, -1):
                cur_track = left[i]

                # Appending current track to seek sequence
                seek_sequence.append(cur_track)

                # Calculate absolute distance
                distance = abs(cur_track - head)

                # Increase the total count
                seek_count += distance

                # Accessed track is now the new head
                head = cur_track

            # After finishing left, reverse direction
            direction = "right"

        elif direction == "right":
            for i in range(len(right)):
                cur_track = right[i]

                # Appending current track to seek sequence
                seek_sequence.append(cur_track)

                # Calculate absolute distance
                distance = abs(cur_track - head)

                # Increase the total count
                seek_count += distance

                # Accessed track is now the new head
                head = cur_track

            # After finishing right, reverse direction
            direction = "left"

        run -= 1

    print("Total number of seek operations =", seek_count)
    print("Seek Sequence is:", *seek_sequence)

    # Plotting the seek sequence
    plt.figure(figsize=(10, 5))
    plt.ylim(0, total_tracks)
    plt.plot(seek_sequence, marker='o')
    plt.title(f"LOOK Disk Scheduling (Initial direction: {direction})")
    plt.xlabel("Sequence of Requests")
    plt.ylabel("Track Number")
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    total_tracks = int(input("Enter the total number of tracks: "))
    size = int(input("Enter the number of requesting tracks: "))
    print("Enter the requesting tracks:")
    arr = list(map(int, input().split()))
    head = int(input("Enter the initial position of the head: "))
    direction = input("Enter the direction (left/right): ")
    LOOK(arr, head, direction, total_tracks)
