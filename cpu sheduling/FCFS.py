
def fcfs(process_list, n):
    t = 0
    gantt = []
    completed = {}
    process_list = sorted(process_list, key=lambda x: (x[0], x[2]))

    while process_list != []:
        if process_list[0][0] > t:
            gantt.append("Idle")
            t += 1
            continue
        else:
            process = process_list.pop(0)
            gantt.append(process[2])
            t += process[1]
            pid = process[2]
            ct = t
            tt = ct - process[0]
            wt = tt - process[1]
            completed[pid] = [tt, wt]
    
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
        print("Enter the arrival time, brust time, process id of process",i+1)
        at = int(input("arrival time: "))
        bt = int(input("brust time: "))
        pid = input("process id: ")
        process_list.append([at, bt, pid])
    
    fcfs(process_list, n)