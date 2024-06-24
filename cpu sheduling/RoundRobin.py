

def round_robin(process_list, n, time_quanta):
    t = 0
    gantt = []
    completed = {}
    brust_times = {}

    for process in process_list:
        brust_times[process[2]] = process[1]

    process_list = sorted(process_list, key=lambda x:(x[0], x[2]))

    while process_list != []:
        available = []
        for p in process_list:
            if p[0] <= t:
                available.append(p)
        
        if available == []:
            t += 1
            gantt.append("Idle")
            continue
        else:
            process = available[0]
            process_list.remove(process)
            gantt.append(process[2])
            if process[1] <= time_quanta:
                t += process[1]
                pid = process[2]
                at = process[0]
                bt = brust_times[pid]
                ct = t
                tt = ct - at
                wt = tt - bt
                completed[pid] = [tt, wt]
                continue
            else:
                t += time_quanta
                process[1] -= time_quanta
                process_list.append(process)

    print("Order of completion of process ",gantt)
    print(completed)
    total_tt = 0
    total_wt = 0
    for p in completed:
        total_tt += completed[p][0]
        total_wt += completed[p][1]
    
    print("average turn around time: ", total_tt/n)
    print("average waiting time: ", total_wt/n)

if __name__ == "__main__":
    n = int(input("Enter the no. of process: "))
    time_quanta = int(input("Enter the time quanta: "))
    process_list = []
    for i in range(n):
        print("Enter the arrival time, brust time, process id of process",i+1)
        at = int(input("arrival time: "))
        bt = int(input("brust time: "))
        pid = input("process id: ")
        process_list.append([at, bt, pid])
    
    round_robin(process_list, n, time_quanta)