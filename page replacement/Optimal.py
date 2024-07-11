capacity = int(input("Enter the no. of frames in memory : "))
p = int(input("Enter the no. of pages : "))
print("Enter the reference string : ",end="")
ref_str = list(map(int, input().strip().split()))
frames, fault= [], 0
occurance = [None for i in range(capacity)]
for i in range(len(ref_str)):
    if ref_str[i] not in frames:
        if len(frames) < capacity:
            frames.append(ref_str[i])
        else:
            for x in range(len(frames)):
                if frames[x] not in ref_str[i+1:] :
                    frames[x] = ref_str[i]
                    break
                else:
                    occurance[x] = ref_str[i+1:].index(frames[x])
            else:
                frames[occurance.index(max(occurance))] = ref_str[i]
        fault  += 1
        
print("Hit count : ", (p-fault))
print("Fault count : ", fault)
            