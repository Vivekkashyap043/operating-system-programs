import random

n=int(input('Enter Memory Size:'))
fr_size=int(input('Enter Frame Size:'))
no_of_frames=n//fr_size
frames=[random.randint(0,1) for _ in range(no_of_frames)]
no_process = int(input("Enter no. of processes: "))
process_pages = []
for i in range(no_process):
    no_pages = int(input(f"Enter no. of pages of process {i+1}: "))
    process_pages.append(no_pages)

for p in range(no_process):
    print("Process - "+str(p+1))
    for page in range(process_pages[p]):
        free_all = [i for i,frame in enumerate(frames) if frame == 0]
        if len(free_all) > 0:
            idx = free_all.pop(0)
            frames[idx] = 1
            print("Page-"+str(page+1)+" in frame "+str(idx))
        else:
            print("Page-"+str(page+1)+" not allocated")
        
