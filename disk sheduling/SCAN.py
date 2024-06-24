import matplotlib.pyplot as plt


def SCAN(arr, head, direction, size, disk_size):
    seek_count = 0
    distance, cur_track = 0, 0
    left = []
    right = []
    seek_sequence = []

    # Appending end values which have to be visited before reversing the direction
    if direction == "left":
        left.append(0)
    elif direction == "right":
        right.append(disk_size - 1)

    for i in range(size):
        if arr[i] < head:
            left.append(arr[i])
        if arr[i] > head:
            right.append(arr[i])

    # Sorting left and right vectors
    left.sort()
    right.sort()

    # Run the while loop two times: one by one scanning right and left of the head
    run = 2
    while run != 0:
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

                # Accessed track is now new head
                head = cur_track

            direction = "left"

        run -= 1

    print("Direction:", direction)
    print("Total number of seek operations =", seek_count)
    print("Seek Sequence is:", seek_sequence)

    # Plotting the seek sequence
    plt.ylim(0, disk_size)
    plt.plot(seek_sequence, marker='o')
    plt.title(f"SCAN Disk Scheduling (Initial direction: {direction})")
    plt.xlabel("Sequence of Requests")
    plt.ylabel("Track Number")
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    total_tracks = int(input("enter the total no. of track : "))
    size = int(input("Enter the no. of  requesting tracks : "))
    print("enter the the requesting tracks:")
    arr = list(map(int, input().split()))
    head = int(input("enter the initial point of head: "))
    direction = input("Enyter the direction (left/right):")
    SCAN(arr, head, direction, size, total_tracks)
