

def sjf(process_list, n):
    t = 0
    gantt = []
    completed = {}
    brust_times = {}

    for process in process_list:
        brust_times[process[2]] = process[0]

    while process_list != []:
        available = []
        for p in process_list:
            if p[1] <= t:
                available.append(p)
        
        if available == []:
            t += 1
            gantt.append("Idle")
            continue
        else:
            available = sorted(available, key=lambda x:(x[0], x[1]))
            process = available[0]
            process_list.remove(process)
            available.pop(0)
            process[0] -= 1
            t += 1
            gantt.append(process[2])
            if process[0] == 0:
                pid = process[2]
                at = process[1]
                bt = brust_times[pid]
                ct = t
                tt = ct - at
                wt = tt - bt
                completed[pid] = [tt, wt]
            else:
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
    process_list = []
    for i in range(n):
        print("Enter the brust time, arrival time, process id of process",i+1)
        bt = int(input("brust time: "))
        at = int(input("arrival time: "))
        pid = input("process id: ")
        process_list.append([bt, at, pid])
    
    sjf(process_list, n)