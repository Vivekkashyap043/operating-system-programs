
def priority(process_list, n):
    t = 0
    completed = {}
    gantt = []

    while process_list != []:
        available = []
        for p in process_list:
            if p[2] <= t:
                available.append(p)
        
        if available == []:
            t += 1
            gantt.append("Idle")
            continue
        else:
            available = sorted(available, key=lambda x:(x[0], x[2]))
            process = available[0]
            pid = process[3]
            at = process[2]
            bt = process[1]
            t += bt
            ct = t
            tt = ct - at
            wt = tt - bt
            gantt.append(pid)
            completed[pid] = [tt, wt]
            process_list.remove(process)

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
        print("Enter the priority, brust time, arrival time, process id of process",i+1)
        p = int(input("priority: "))
        bt = int(input("brust time: "))
        at = int(input("arrival time: "))
        pid = input("process id: ")
        process_list.append([p, bt, at, pid])
    
    priority(process_list, n)