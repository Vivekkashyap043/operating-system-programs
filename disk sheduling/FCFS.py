import matplotlib.pyplot as plt

def FCFS(arr, head, size, total_tracks):

    arr.insert(0, head)
    seek_count = 0
    distance, cur_track = 0, 0

    for i in range(size):
        cur_track = arr[i]
        distance = abs(cur_track - head)
        seek_count += distance
        head = cur_track

    print("Total number of seek operations = ", seek_count)
    print("Seek Sequence is", arr)

    plt.ylim(0, total_tracks)
    plt.plot(arr, marker='o')
    plt.title("FCFS Disk Scheduling")
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
    FCFS(arr, head, size, total_tracks)
