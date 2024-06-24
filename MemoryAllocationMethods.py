import random

def best_fit(blocks, processes):
    allocation = [-1] * len(processes)
    for i in range(len(processes)):
        best_idx = -1
        for j in range(len(blocks)):
            if blocks[j] >= processes[i]:
                if (best_idx == -1 or blocks[j] < blocks[best_idx]) and j not in allocation:
                    best_idx = j
        if best_idx != -1:
            allocation[i] = best_idx
    return allocation

def worst_fit(blocks, processes):
    allocation = [-1] * len(processes)
    for i in range(len(processes)):
        worst_idx = -1
        for j in range(len(blocks)):
            if blocks[j] >= processes[i]:
                if (worst_idx == -1 or blocks[j] > blocks[worst_idx]) and j not in allocation:
                    worst_idx = j
        if worst_idx != -1:
            allocation[i] = worst_idx
    return allocation

def first_fit(blocks, processes):
    allocation = [-1] * len(processes)
    for i in range(len(processes)):
        for j in range(len(blocks)):
            if blocks[j] >= processes[i] and j not in allocation:
                allocation[i] = j
                break
    return allocation

def main():
    num_blocks = int(input("Enter the number of blocks: "))
    num_processes = int(input("Enter the number of processes: "))
    block_sizes = [random.randint(10, 500) for _ in range(num_blocks)]
    process_sizes = [int(input(f"Enter size of process {i+1}: ")) for i in range(num_processes)]
    algorithm = input("Enter memory allocation algorithm (best/worst/first): ")
    if algorithm == "best":
        allocation = best_fit(block_sizes, process_sizes)
    elif algorithm == "worst":
        allocation = worst_fit(block_sizes, process_sizes)
    elif algorithm == "first":
        allocation = first_fit(block_sizes, process_sizes)
    else:
        print("Invalid algorithm type.")
        return

    print("\nMemory Allocation:")
    print("Block sizes : ",block_sizes)
    for i in range(len(process_sizes)):
        if allocation[i] != -1:
            print(f"Process {i+1} allocated to Block {allocation[i]+1}")
        else:
            print(f"Process {i+1} cannot be allocated")

if __name__ == "__main__":
    main()
