import matplotlib.pyplot as plt

def SSTF(arr, head, size, total_tracks):
    seek_sequence = [head]
    total, current = 0, head
    while arr:
        close = min(arr, key=lambda x: abs(x - current))
        total += abs(close - current)
        current = close
        seek_sequence.append(close)
        arr.remove(close)
    print('Total seek time', total)
    print('Seek sequence', seek_sequence)

    plt.ylim(0, total_tracks)
    plt.plot(seek_sequence, marker='o')
    plt.title("SSTF Disk Scheduling")
    plt.xlabel("Sequence of Requests")
    plt.ylabel("Track Number")
    plt.show()

if __name__ == '__main__':
    total_tracks = int(input("enter the total no. of track : "))
    size = int(input("Enter the no. of  requesting tracks : "))
    print("enter the the requesting tracks:")
    arr = list(map(int, input().split()))
    head = int(input("enter the initial head position: "))
    SSTF(arr, head, size, total_tracks)