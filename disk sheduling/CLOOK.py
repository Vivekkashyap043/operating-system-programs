import matplotlib.pyplot as plt

# Function to perform C-LOOK on the request array starting from the given head
def CLOOK(arr, head, size, disk_size):
    seek_count = 0
    distance = 0
    cur_track = 0

    left = sorted([i for i in arr if i < head])
    right = sorted([i for i in arr if i > head])

    seek_sequence = []

    # First service the requests on the right side of the head
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
    print("Seek Sequence is", seek_sequence)

    # Plotting the seek sequence
    plt.ylim(0, disk_size)
    plt.plot(seek_sequence, marker='o')
    plt.title("C-LOOK Disk Scheduling")
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
    CLOOK(arr, head, size, total_tracks)