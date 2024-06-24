import matplotlib.pyplot as plt


def CSCAN(arr, head, size, disk_size):
    seek_count = 0
    distance = 0
    cur_track = 0
    left = [0]
    right = [disk_size - 1]
    seek_sequence = []

    for i in range(size):
        if arr[i] < head:
            left.append(arr[i])
        if arr[i] > head:
            right.append(arr[i])

    # Sorting left and right vectors
    left.sort()
    right.sort()

    # First service the requests on the right side of the head
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

    # Once reached the right end, jump to the beginning
    head = 0

    # Adding seek count for head returning from 199 to 0
    seek_count += (disk_size - 1)

    # Now service the requests again which are left
    for i in range(len(left)):
        cur_track = left[i]

        # Appending current track to seek sequence
        seek_sequence.append(cur_track)

        # Calculate absolute distance
        distance = abs(cur_track - head)

        # Increase the total count
        seek_count += distance

        # Accessed track is now the new head
        head = cur_track

    print("Total number of seek operations =", seek_count)
    print("Seek Sequence is:", seek_sequence)

    # Plotting the seek sequence
    plt.ylim(0, disk_size)
    plt.plot(seek_sequence, marker='o')
    plt.title("C-SCAN Disk Scheduling")
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
    CSCAN(arr, head, size, total_tracks)