
def calculate_need(allocated, max_required, n):
    need = {}
    for pid in allocated:
        allocate = allocated[pid]
        required = max_required[pid]
        need_value = []
        for i in range(n):
            need_value.append(required[i] - allocate[i])
        need[pid] = need_value
    return need

    

def bankers(allocated, max_required, available, n, p):
    need = calculate_need(allocated, max_required, n)
    not_processed = 0
    safe_sequence = []
    processes = []
    for pid in allocated:
        processes.append(pid)

    while not_processed < p and len(safe_sequence)!=p:
        pid = processes.pop(0)

        if available >= need[pid]:
            safe_sequence.append(pid)
            not_processed = 0
            for i in range(n):
                available[i] += allocated[pid][i]
        else:
            processes.append(pid)
            not_processed += 1
    
    if len(safe_sequence) != p:
        print("No safe sequence possible")
    else:
        print("Safe sequence is: ", end="")
        print(*safe_sequence,sep="->")
        print("Avaiable matrix: ", available)




if __name__ == "__main__":
    n = int(input("Enter the total no. resources: "))
    p = int(input("Enter the no. of process: "))
    allocated = {}
    max_required = {}
    for i in range(p):
        pid = "p"+str(i+1)
        print("Enter the allocated matrix for "+pid)
        allocate = list(map(int, input().split()))
        allocated[pid] = allocate
    for i in range(p):
        pid = "p"+str(i+1)
        print("Enter the Max required matrix for "+pid)
        max_req = list(map(int, input().split()))
        max_required[pid] = max_req
    print("Enter the available matrix:")
    available = list(map(int, input().split()))
    bankers(allocated, max_required, available, n, p)
        
