capacity = int(input("Enter the no. of frames in memory : "))
p = int(input("Enter the no. of pages : "))
print("Enter the reference string : ",end="")
s = list(map(int, input().strip().split()))
f, fault= [], 0
occurance = [None for i in range(capacity)]
for i in range(len(s)):
    if s[i] not in f:
        if len(f) < capacity:
            f.append(s[i])
        else:
            for x in range(len(f)):
                if f[x] not in s[i+1:] :
                    f[x] = s[i]
                    break
                else:
                    occurance[x] = s[i+1:].index(f[x])
            else:
                f[occurance.index(max(occurance))] = s[i]
        fault  += 1
        
print("Hit count : ", (p-fault))
print("Fault count : ", fault)
            