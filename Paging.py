msize = int(input("Enter the memory size: "))
psize = int(input("Enter the page size: "))
nopages = msize // psize
print("The number of pages available in memory are:", nopages)
np = int(input("Enter the number of processes: "))
pages = [0] * (nopages + 1)
process = [0] * (np + 1)
k = 1
j = 0 # Define j here
for i in range(np):
    x = int(input(f"Enter number of pages required for P[{i + 1}]: "))
    process[k] = j + 1
    k += 1
 
    if j + x <= nopages:
        print(f"Enter page table for P[{i + 1}]:")
        for _ in range(x):
            p = int(input())
            j += 1
            pages[j] = p
    else:
        print("Memory is Full")
        break

print("Logical Address to find Physical Address")
pno, pageno, offset = map(int, input("Enter process number, page number, and offset: ").split())
paddress = pages[process[pno] + pageno - 1] * psize + offset
print("The physical address is:", paddress)
