frame = int(input("Enter the no. of frame in main memory : "))
pages = int(input("Enter the no. of pages : "))
print("Enter the reference string : ",end="")
ref_str = list(map(int, input().split()))
memory = [None]*frame
hit, fault, del_pointer = 0, 0 , 0
for i in range(len(ref_str)):
    if ref_str[i] in memory:
        hit += 1
    else:
        memory[del_pointer] = ref_str[i]
        del_pointer += 1
        if del_pointer ==frame:
            del_pointer = 0
        fault += 1
        
print("Hit count : ", hit)
print("Fault count : ", fault)